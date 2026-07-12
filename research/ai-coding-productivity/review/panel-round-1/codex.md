---
type: external-review
reviewer: codex
round: 1
status: complete
verdict: needs-fixes
---

# Review — codex — Round 1

## Findings

| ID | Severity | Target | Finding | Why it matters | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| F1 | major | research-contract.md:136 | The contract enables a Codex second opinion, but the dossier contains no `review/second-opinion-codex.md` and no reconciliation file; only `review/codex-second-opinion-stdout.log` exists. | Gate 8.4 is designed to catch omitted sources and disagreements. Without a saved second-opinion report and reconciliation, the dossier can terminate as `Done` while skipping a configured omission check. | Save the second-opinion result as a Markdown artifact, add `review/second-opinion-reconciliation.md`, and send any disagreements or newly found studies back through Gate 5/6; if the run failed, mark it `blocked` in `log.md` and README. |
| F2 | major | research-contract.md:90 | The contract says each major measured/controlled study gets a `papers/` note, and expected artifacts include `papers/*.md`, but the dossier has no `papers/` directory. | The primary unit of analysis is studies. Keeping them only as `sources/` notes may be acceptable, but the finished dossier does not satisfy its own declared artifact contract. | Either create `papers/` notes for the major studies with the required fields, or revise the contract to say study notes are intentionally represented by `sources/*.md` and ensure those notes meet the study-note depth requirements. |
| F3 | major | open-questions.md:25 | High-impact gap G-H2 is marked `BLOCKED (partially mitigated)`, and `log.md:141` repeats `BLOCKED, partially mitigated`. | The workflow only allows high-impact gaps to terminate as `resolved` or `blocked`. The modifier is not as bad as `partially resolved`, but it weakens the terminal-state invariant and makes consensus/audit parsing ambiguous. | Split the statement: mark the causal long-run maintainability gap simply `blocked`, then add a separate note that Horikawa mitigates the directional-evidence gap but does not resolve causality. |
| F4 | major | decision-guide.md:24 | The condition matrix says experienced developers on unfamiliar codebases are `Likely positive`, citing only METR caveats and no direct RCT, while the synthesis says novel/unfamiliar work has no significant speedup and worse comprehension. | This is a decision-facing recommendation that overstates thin and partly contrary evidence. It could lead the user to treat unfamiliar-codebase work as supported when the dossier's own evidence does not support that. | Change the speed effect to `Unknown / mixed` and distinguish exploration assistance from measured productivity; cite Anthropic as a caution, not support for likely positive speedup. |
| F5 | major | evidence.md:100 | Claim 4.1 is typed as `Fit/methodology` with `Confidence: high`. | Gate 4.5 says fit claims cannot exceed low from web evidence. If this is not a fit claim, the typing is wrong; if it is a fit claim, the confidence is wrong. | Reclassify it as a methodology/inference claim, or downgrade the fit component to low and keep any methodological observation separately calibrated. |
| F6 | major | synthesis.md:192 | The confidence summary marks the task-type gradient and junior-benefit heterogeneity as `High`, while the evidence ledger rates the same claims `medium-high` and notes vendor/mixed-independence and underpowered senior subgroups. | The final confidence summary is what readers will use. It currently outruns the dossier's own claim-level calibration. | Downgrade these two summary claims to `Medium` or explicitly justify why multiple independent sources clear the high-confidence bar despite vendor and subgroup caveats. |
| F7 | minor | log.md:22 | The search ledger counts are internally inconsistent: Round 1 says `11 searches; 8 scrapes` but lists 12 queries and 11 scrape bullets; Round 2 says `3 searches, 1 scrape` but lists queries 13-19. | The ledger is the proof that discovery happened. Count mismatches do not invalidate the evidence, but they make the audit trail look less reliable than it should. | Normalize the query/scrape counts in `log.md`, `README.md`, and `methodology.md`; make the frontmatter `sources_rejected` count match the termination summary. |

## False-Positive Risks

F1 may be a timing artifact if the second-opinion process is still running while this review panel is being assembled. If so, the fix is still to mark the artifact as pending/blocked rather than letting the dossier read as complete.

F2 may be intentional if the author decided that `sources/*.md` would serve as study notes. The problem is not the folder name by itself; it is the mismatch with the contract.

F3 is a wording/audit-state concern, not evidence that the gap was ignored. The blocking reason is present.

## What The Dossier Got Right

The core synthesis is source-backed and skeptical in the right places: it does not treat the 55.8% Copilot study as generally applicable, it gives METR's recency caveat real weight, and it names the user-specific fit question as unanswerable without a local experiment. The source notes I checked generally support the cited headline claims, especially for METR, Cui/Demirer, DORA, Anthropic, and NAV IT.
