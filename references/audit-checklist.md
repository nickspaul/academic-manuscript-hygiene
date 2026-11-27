# Academic Manuscript Hygiene Checklist (EN & ZH)

Quick reference of common manuscript defects and their clean academic replacements.

## 1. Internal Jargon & Opaque Codes
| Avoid | Replace with | Why |
|---|---|---|
| `Exp-2`, `Run-A`, `Dev-Set` | `Synth-Bench`, `Real-Eval`, `Held-Out Split` | Unexplained internal project IDs |
| `Frozen checkpoints`, `frozen archive` | `Offline-trained policies`, `evaluated without retraining` | Sounds like an external or unfair baseline |
| `ON`, `Variant-B`, `16s`, `45p`, `6t/20i` | `Shielded Policy`, `Lagrangian Variant`, `16 seeds`, `45 params`, `6 agents` | Internal script flags / ambiguous shorthand |
| `修复精确...`, `审计基准` | `精确分段...`, `离线参照基准` | Revision-history / bug-fix residue |
| `verify_solver.py` | `exhaustive trajectory enumeration` | Local code filenames do not belong in prose |
| `1 s SLA`, `BF exact` | `1 s limit`, `brute-force exact` | Undefined corporate/code jargon |

## 2. Defensive & QA-Log Language
| Avoid | Replace with |
|---|---|
| `confirming lower error does not stem from exploiting...` | `Including a terminal residual penalty preserves these gains...` |
| `should be viewed as X rather than Y` | `acts as X` (state positively what it is) |
| `without claiming a statistically tested difference` | `overlapping CIs indicate comparable performance` |
| `untouched calendar days` / `未触碰自然日` | `held-out calendar days` / `独立留出自然日` |
| `zero failed seeds`, `zero infeasibilities and zero fallbacks` | `all runs converged reliably`, `all evaluated steps remained feasible` |
| `applied zero-shot without test-set tuning` | `evaluated directly` / `transfers zero-shot` |

## 3. Code Leakage in Prose
| Avoid in Main Text | Replace with (Keep Exact Flags in Appendix) |
|---|---|
| `presolve=False`, `mip_rel_gap=0.0` | `solved to zero optimality gap with presolve disabled` |
| `OMP_NUM_THREADS=1`, `CUDA_VISIBLE_DEVICES=0` | `single-threaded CPU execution`, `single GPU evaluation` |
| `\texttt{EvalStep}`, `\texttt{refill\_obs}(s_t)` | `\textsc{OnlineDispatch}`, $\mathbb{I}_{\mathrm{refill}}(s_t)$ |

## 4. Tone, Typography, Signs & Bilingual Hygiene
| Category | Avoid | Replace with |
|---|---|---|
| Sports/informal verbs | `beats`, `edges out`, `holds an edge`, `wins 45/45`, `run dry` | `outperforms`, `slightly outperforms`, `performs better`, `lower error in 45 of 45`, `are depleted` |
| AI clichés | `leverage`, `delineate`, `delve`, `paramount`, `pivotal`, `Taken together`, `reconcile` | `use`, `identify` / `clarify`, `central`, `together`, `combine` |
| Invented / mismatched terms | `unfloored`, `exact-capped`, `UTC-local`, `per arm` | `base model`, `exact piecewise-capped`, `local time`, `per variant` |
| Double parentheses | `Method (1.0) (38.0)`, `Method (1.0)'s` | `Method 1.0 (38.0)`, `the ... of Method 1.0` |
| Sign mismatch | `increases by +13.4 (-23.2%)` | `increases by +13.4 (+30.2%; a 23.2% reduction when enabled)` |
| ZH/EN mixing | `Core cont.`, `Part A/B`, `vs.`, `Feb. 4`, `局/回合`混用 | `核心指标`, `上半部分/下半部分`, `对比`, `2 月 4 日`, 统一量词 |
