---
name: academic-manuscript-hygiene
description: >-
  Audit and polish English or Chinese scientific manuscripts, tables, figures, and
  submission packages for cold-reader clarity, semantic naming, evidence pruning,
  anti-defensive phrasing, code-to-prose separation, and AI-cliche removal. Use when
  reviewing or rewriting a manuscript before submission so an unfamiliar reader can
  understand every term and symbol cleanly.
---

# Academic Manuscript Hygiene and Clarity Audit

Apply this workflow when auditing or restructuring a research manuscript (`.tex`, `.md`,
tables, figure scripts, cover letters, or bilingual Chinese/English drafts) before
submission.

## Procedure

### 1. Enforce Cold-Reader Self-Containment and Semantic Naming
Assume the reader has zero knowledge of your codebase, earlier project iterations, or
internal experiment logs.
- Replace internal dataset, run, or variant codes (`Exp-2`, `Run-A`, `v4`, `ON`, `16s`)
  with self-explanatory semantic names (`Synth-Bench`, `Real-Eval`, `Constrained RL`).
- Never refer to your own prior baselines as "frozen checkpoints", "frozen archive", or
  "repaired/fixed" versions. State cleanly that baselines were trained offline on
  synthetic scenarios and evaluated without test-time retraining.
- Define every acronym and symbol on first use in prose, abstracts, and tables (e.g.,
  algorithm family, objective terms, action-space dimension $M$, weighting parameters).
- Remove local script filenames (`eval_script.py`), internal seed blocks, and engineering
  SLA shorthand (`1 s SLA` -> `1 s limit`, `BF exact` -> `brute-force exact`) from figures,
  captions, and main text.

### 2. Prune Redundant Evidence and Eliminate Table-Figure Duplication
Keep the shortest sufficient evidence chain in the main text:
- Never duplicate an identical dataset across both a full table and a multi-panel figure;
  keep the visual display and summarize non-plotted bounds in 1--2 sentences.
- Fold large pairwise $p$-value matrices into the Results prose alongside effect sizes.
- Standardize around primary operating modes (e.g., base model + validation-selected
  guardrail) and move stray sensitivity rows or redundant ablations out of main tables.

### 3. Remove Defensive and Reviewer-Anticipation Phrasing
Write as an objective scientific report, never as a preemptive rebuttal:
- Never mention reviewers, referees, or defending against objections in the manuscript.
- Eliminate defensive "rather than" disclaimers (`should be viewed as X rather than Y`,
  `does not stem from exploiting...`, `without claiming a statistically tested difference`)
  and replace them with positive, bounded statements of what the experiment measures.
- Eliminate QA-log phrases (`zero failed seeds`, `zero infeasibilities and zero fallbacks`,
  `untouched test days`, `without test-set tuning` stacked onto `zero-shot`). Use standard
  terminology (`held-out days`, `all evaluated steps remained feasible`).

### 4. Separate Prose from Code and API Identifiers
Keep implementation flags out of the main narrative, algorithm blocks, and figures:
- Replace API flags (`presolve=False`, `mip_rel_gap=0.0`, `OMP_NUM_THREADS=1`,
  `CUDA_VISIBLE_DEVICES`) and snake_case identifiers (`eval_step`, `refill_flag`) in
  prose with clean mathematical or engineering descriptions (`solved to zero optimality gap
  with presolve disabled`, `single-threaded CPU execution`, $\mathbb{I}_{\mathrm{refill}}(s_t)$).
- Document exact solver and training flags once in the Appendix / Methods provenance table.

### 5. Apply Humanizer, Register, Sign, and Bilingual Hygiene
- Remove prose em-dashes (`---` / `—`), AI clichés (`leverage`, `delineate`,
  `reconcile`, `pivotal`, `paramount`, `delve`, `seamlessly`, `Taken together`), and
  sports/marketing verbs (`beats`, `edges out`, `holds an edge`, `wins 10/10`, `delivers`,
  `run dry`). Use neutral verbs (`outperforms`, `reduces error relative to`, `achieves`).
- Eliminate invented compound adjectives (`unfloored`, `exact-capped`, `UTC-local`) and
  domain-mismatched terms (`per arm` -> `per variant` / `per method`).
- Avoid adjacent double parentheses such as `Method (1.0) (38.0)` or `Method (1.0)'s`;
  write `Method 1.0 (38.0)`.
- Verify sign consistency whenever reporting percentage deltas alongside absolute deltas
  (`+13.4` increase must pair with `+30.2%`, never with the reverse reduction sign).
- In Chinese manuscripts, purge half-translated table headers (`Core cont.`, `Elig. viol.`),
  English sub-headers (`Part A/B`, `vs.`, `Feb.`), and inconsistent measure words.

### 6. Run Automated Checks and Visual Inspection
1. Consult [audit-checklist.md](./references/audit-checklist.md) for quick bad-vs-good
   patterns.
2. Run [check_manuscript_hygiene.py](./scripts/check_manuscript_hygiene.py) on all `.tex`
   files and compiled `.pdf` outputs, passing any project-specific legacy codes with
   `--extra-pattern`:
   ```bash
   python scripts/check_manuscript_hygiene.py manuscript.tex manuscript_zh.tex manuscript.pdf --extra-pattern "\b(Exp-2|Run-A)\b"
   ```
3. Visually inspect rendered Page 1 and every figure PNG to verify zero clipping, overlaps,
   or unreadable abbreviations.
