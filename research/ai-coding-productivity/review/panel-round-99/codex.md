---
type: external-review
reviewer: codex
round: 99
status: complete
verdict: needs-fixes
---

# Review — codex — Round 99

## Findings

| ID | Severity | Target | Finding | Why it matters | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| F1 | major | decision-guide.md:61 | The proposed local experiment asks for "30 real tasks" total, then says "minimum n=20 tasks per condition" and optionally compares autocomplete vs agentic tools. Those instructions cannot all be true at once: two randomized conditions need at least 40 tasks for n=20 per arm, and adding tool-class comparisons increases the needed task count again. | The dossier correctly says the local experiment is the only way to answer the fit question for Gabriel. If the experiment design is internally inconsistent, the main recommendation can produce an underpowered or misinterpreted result. | Rework the experiment section into one explicit design: e.g. 40 tasks minimum for AI-allowed vs AI-disallowed, 60 preferred; if comparing autocomplete vs agentic, run separate randomized blocks or state the larger required sample. |
| F2 | major | review/second-opinion-reconciliation.md:52 | The reconciliation identifies Song et al. as a source relevant to the review-burden / coordination axis, with +8% coordination time, but it is not added as a source note and `open-questions.md` still says no primary measured review-burden study surfaced. The saved `review/second-opinion-codex.md` summary also does not preserve Song's details, so "cite it via the second-opinion dossier" is not auditable. | G-H4 is a high-impact gap. Either Song is relevant measured evidence and the gap is not fully blocked as written, or Song is only adjacent coordination evidence and should be explicitly ruled out. Leaving it half-integrated weakens the gap-closure audit trail. | Add a `sources/song-copilot-oss-coordination.md` note and update `evidence.md` / `open-questions.md`, or explicitly classify Song as coordination-not-review and remove the claim that it is cited via the second-opinion dossier. |
| F3 | minor | README.md:46 | Some audit counters remain stale after Round 3: README still says `sources/` has 9 source notes and the audit ledger has 19 queries / 9 sources, while `log.md` final termination says 20 queries, 14 scrapes, and 11 sources. `methodology.md:13` also still says 19 queries across 2 rounds. | The research workflow treats the search ledger as proof that discovery happened. Conflicting counters make a later audit harder, even though the final `log.md` appears to have the better count. | Reconcile README and methodology counters to the final log: 3 rounds, 20 queries, 14 scrapes, 11 kept sources, and the current rejected-source count. |
| F4 | minor | README.md:60 | The source-tier list labels Tier 1 as "Independent RCT / peer-reviewed" but includes the Anthropic skill-formation study there, then lists the same study again under vendor RCTs. The body correctly caps Anthropic at medium, but the tier heading is misleading. | Source independence is central to the dossier's confidence calibration. A vendor RCT appearing under an "independent" tier can confuse readers skimming the overview. | Put Anthropic only under the vendor RCT tier, or rename the first tier so it does not imply Anthropic is independent. |

## False-Positive Risks

F2 is the one with the most judgment involved. Song measures coordination time and code discussions, not necessarily code-review effort/time. If the dossier wants G-H4 to mean only reviewer effort, Song can be excluded; the fix still needs to say that explicitly because the reconciliation currently calls it relevant to that axis.

F3 and F4 are bookkeeping / overview issues. They do not overturn the synthesis, but they matter because this workflow is intentionally audit-heavy.

## What The Dossier Got Right

The core answer is much better calibrated than the earlier round: it leads with the recency correction, treats the current agentic-tool effect as unmeasured, caps vendor performance claims, and names the user-specific fit question as web-unanswerable.

The search ledger is real enough to audit: it records failed and hijacked searches, rejected candidates, review-triggered Round 3 work, second-opinion coverage failures, and an explicit final termination. The source notes are generally substantive rather than stubs, and the decision guide does not pretend the web can settle Gabriel's own productivity.
