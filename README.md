# academic-manuscript-hygiene

An Agent Skill for auditing and polishing English and Chinese scientific manuscripts (`.tex`, `.md`, tables, figures, cover letters, and submission packages) before peer review.

## What It Checks

1. **Cold-Reader Self-Containment & Semantic Naming** — Replaces opaque internal dataset/run codes, script filenames, and shorthand with self-explanatory names, and ensures every acronym and symbol is defined on first use.
2. **Evidence Pruning** — Eliminates table–figure duplication, folds giant $p$-value matrices into prose alongside effect sizes, and keeps only primary operating modes in main tables.
3. **Anti-Defensive Phrasing** — Removes preemptive reviewer-anticipation language (`does not stem from exploiting...`, `zero failed seeds`, references to reviewers/referees) in favor of positive, bounded scientific reporting.
4. **Code-to-Prose Separation** — Keeps solver/training API flags (`presolve=False`, `OMP_NUM_THREADS`, `CUDA_VISIBLE_DEVICES`) and `snake_case` code identifiers out of main prose, reserving exact solver details for the Appendix.
5. **Humanizer, Register, Sign & Bilingual Hygiene** — Flags AI template vocabulary (`delve`, `leverage`, `pivotal`, `paramount`), informal/sports verbs (`beats`, `edges out`), duplicate parenthetical acronyms, sign mismatches, and unlocalized English fragments in Chinese drafts.
6. **Automated Audit Script & Visual QA** — Includes `scripts/check_manuscript_hygiene.py` (with repeatable `--extra-pattern` flags for project-specific legacy codes) and `references/audit-checklist.md`.

## Installation

### Antigravity / Workspace Skill
```bash
git clone https://github.com/nickspaul/academic-manuscript-hygiene.git .agents/skills/academic-manuscript-hygiene
```

### Universal Skills CLI (`npx skills`)
```bash
npx skills add nickspaul/academic-manuscript-hygiene
```

### Claude Code / Codex
```bash
git clone https://github.com/nickspaul/academic-manuscript-hygiene.git ~/.claude/skills/academic-manuscript-hygiene
```

## Automated Hygiene Script Usage

```bash
python scripts/check_manuscript_hygiene.py manuscript.tex manuscript_zh.tex manuscript.pdf
```

To flag project-specific internal codes or legacy terms during an audit:

```bash
python scripts/check_manuscript_hygiene.py manuscript.tex \
  --extra-pattern "\b(Exp-2|Run-A|OldMethod)\b"
```

*(Inspecting `.pdf` files requires `pymupdf`; `.tex`, `.md`, and `.txt` files run with Python standard library only.)*

---

## 中文简介

面向中英文科研论文投稿前的规范化自检与润色 Skill，重点排查：内部实验代号与代码标识混入正文、图与表内容重复、防御性/预设审稿人话术、AI 模板高频词、符号正负号不一致以及中文稿件中的中英夹杂，并附带可直接执行的 CLI 检查脚本 `scripts/check_manuscript_hygiene.py` 与对照清单 `references/audit-checklist.md`。
