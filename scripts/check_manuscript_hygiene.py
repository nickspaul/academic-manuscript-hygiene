"""Audit academic manuscripts (.tex, .md, .txt, .pdf) for internal jargon, defensive
phrasing, code/API leakage, AI cliches, typographic issues, and bilingual mixing.

Usage:
  python check_manuscript_hygiene.py file1.tex file2.pdf [--extra-pattern REGEX ...]
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

RULES: list[tuple[str, str, str, bool]] = [
    # (category, regex_pattern, message, check_zh_only)
    ("INTERNAL_JARGON", r"\bfrozen\b|冻结", "Avoid 'frozen' baseline phrasing; describe offline training and zero-shot evaluation.", False),
    ("INTERNAL_JARGON", r"\b[a-zA-Z0-9_-]+\.py\b", "Local script filename detected in manuscript text.", False),
    ("INTERNAL_JARGON", r"\bSLA\b|\bBF exact\b", "Undefined shorthand or engineering jargon detected.", False),
    ("INTERNAL_JARGON", r"\b\d+t/\d+i\b", "Abbreviated team/instance shorthand; write out in full.", False),
    ("DEFENSIVE", r"\b(reviewer|referee)s?\b|审稿人", "Do not reference reviewers/referees in manuscript prose.", False),
    ("DEFENSIVE", r"does not stem from exploiting|without claiming a statistically", "Defensive reviewer-anticipation phrasing detected.", False),
    ("DEFENSIVE", r"\buntouched\b|未触碰|zero failed seeds", "Use objective scientific terminology instead of QA-log phrasing.", False),
    ("AI_CLICHE_TONE", r"\b(delve|tapestry|pivotal|paramount|seamlessly|leverages?|delineat(e|es|ing))\b", "AI template vocabulary detected; prefer plain academic verbs.", False),
    ("AI_CLICHE_TONE", r"\b(beats|edges out|holds an edge|run dry)\b", "Informal or sports-commentary phrasing detected.", False),
    ("INVENTED_TERM", r"\b(unfloored|exact-capped|UTC-local)\b", "Non-standard compound term detected.", False),
    ("TYPOGRAPHY", r"(\([A-Z]{2,8}\)).*\1", "Duplicate parenthetical acronym in the same line.", False),
    ("CODE_IN_PROSE", r"presolve\s*=\s*(False|True)|mip_rel_gap\s*=|OMP_NUM_THREADS|CUDA_VISIBLE_DEVICES|batch_size\s*=|learning_rate\s*=", "Solver/training API flag in prose (keep implementation flags in Appendix).", False),
    ("ZH_MIXING", r"\b(Part A|Part B|vs\.)\b", "Unlocalized English fragment in Chinese manuscript/table.", True),
]


def extract_lines(path: Path) -> list[tuple[str, str]]:
    """Return list of (location_label, text_line)."""
    if path.suffix.lower() == ".pdf":
        try:
            import fitz  # PyMuPDF
        except ImportError as exc:
            raise SystemExit(
                f"[ERROR] PyMuPDF ('fitz') is required to inspect PDF files such as {path.name}. "
                "Install it with: pip install pymupdf"
            ) from exc
        doc = fitz.open(path)
        out = []
        for idx, page in enumerate(doc, 1):
            for ln in page.get_text().splitlines():
                out.append((f"p.{idx}", ln))
        doc.close()
        return out
    lines = path.read_text(encoding="utf-8").splitlines()
    return [(f"L{idx}", ln) for idx, ln in enumerate(lines, 1)]


def is_zh_document(path: Path, lines: list[tuple[str, str]]) -> bool:
    if "_zh" in path.stem.lower():
        return True
    cjk_count = sum(len(re.findall(r"[\u4e00-\u9fff]", ln)) for _, ln in lines)
    return cjk_count >= 50


def audit_file(path: Path, extra_rules: list[tuple[str, str, str, bool]]) -> list[str]:
    lines = extract_lines(path)
    is_zh = is_zh_document(path, lines)
    is_pdf = path.suffix.lower() == ".pdf"
    findings: list[str] = []
    in_appendix = False
    in_refs = False
    rules = RULES + extra_rules

    for loc, line in lines:
        if path.suffix.lower() in {".tex", ".cls"} and line.lstrip().startswith("%"):
            continue
        if re.search(r"\\appendix\b", line) or (is_pdf and re.match(r"^Appendix\s+[A-Z]\b", line.strip())):
            in_appendix = True
        if re.search(r"\\begin\{thebibliography\}", line) or line.strip() in {"References", "参考文献"}:
            in_refs = True
        for cat, pat, msg, zh_only in rules:
            if zh_only and (not is_zh or in_refs):
                continue
            if cat == "CODE_IN_PROSE" and in_appendix:
                continue
            if re.search(pat, line):
                snippet = line.strip()[:100]
                findings.append(f"[{cat}] {path.name}:{loc}: {msg} -> {snippet}")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check academic manuscript hygiene.")
    parser.add_argument("files", nargs="+", type=Path, help="Manuscript files (.tex, .md, .txt, .pdf)")
    parser.add_argument(
        "--extra-pattern",
        action="append",
        default=[],
        metavar="REGEX",
        help="Additional project-specific regex pattern to flag (repeatable).",
    )
    args = parser.parse_args(argv)

    extra_rules = [
        ("CUSTOM_PATTERN", pat, f"Matched custom legacy pattern: {pat}", False)
        for pat in args.extra_pattern
    ]

    all_findings: list[str] = []
    for p in args.files:
        if not p.exists():
            print(f"[ERROR] File not found: {p}", file=sys.stderr)
            return 2
        all_findings.extend(audit_file(p, extra_rules))

    if all_findings:
        for item in all_findings:
            print(item)
        print(f"\n[FAIL] {len(all_findings)} hygiene issue(s) found.")
        return 1

    print(f"[OK] Checked {len(args.files)} file(s): 0 hygiene issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
