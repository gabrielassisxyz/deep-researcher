---
type: research
slug: ai-coding-productivity
topic: "Do AI coding agents actually make experienced developers faster?"
status: draft
created: 2026-07-12
updated: 2026-07-12
freshness_requirement: "AI tooling changes fast; evidence stale within ~6 months. METR's early-2025 result is already superseded by their Feb 2026 update."
confidence: medium
source_count: 11
tags: [ai-coding, developer-productivity, rct, experienced-developers, measured-vs-self-reported]
---

# Do AI coding agents actually make experienced developers faster?

## What this dossier answers

Whether AI coding agents produce a **real, measured** productivity gain for **experienced
developers** in **codebases they already know** — the user's exact working condition —
and the conditions under which the gain is supported vs. not. The user explicitly did
not provide candidate studies; all evidence was discovered by search.

## The headline (one paragraph — corrected for recency)

**The honest answer is a trajectory, not a number.** The only clean RCT on the user's
exact condition — experienced developers on codebases they know well — found that
early-2025 AI tools (Cursor + Claude 3.5/3.7) made them **19% slower** (METR, now
*retired by its authors*). METR's late-2025 follow-up with agentic tools point-estimates an
**18% speedup** but is **uninterpretable** due to selection effects (developers refusing
to work without AI). **The current state for the user's condition is unmeasured.** What
survives the recency correction: (1) the popular "55.8% faster" is a vendor lab figure on
the wrong population and task type; field RCTs show positive effects **concentrated in
juniors**, with small/non-significant effects for seniors; (2) **the predicted key
finding is real and robust — self-reported speedup diverges from measured speedup by ~40
percentage points**, and the divergence flows to the system level (individuals feel
faster while organizational delivery gets slightly worse); (3) **non-speed effects
(maintainability, stability, comprehension, long-term skill) skew negative and are
better-evidenced than the speed effects.** The recommendation that survives is "measure
it yourself" — strengthened, not weakened, by the recency correction.

## Map of notes

- **Decision & framing**: [[intake.md]], [[research-contract.md]]
- **Answer**: [[synthesis.md]] (with mandatory "what the web cannot settle" section),
  [[decision-guide.md]] (condition matrix + the local self-experiment to run)
- **Evidence**: [[evidence.md]] (claim-level ledger), `sources/` (9 source notes)
- **Method**: [[methodology.md]] (source tiers, metric interpretation, claim typing)
- **Gaps**: [[open-questions.md]] — all 4 high-impact gaps `blocked` with reasons; the fit
  question is structurally unanswerable from web evidence
- **Audit**: [[log.md]] — full search ledger (19 queries, 7 hijacked, 2 fruitless), 9
  sources kept, 8+ rejected with reasons

## Sources kept (11)

**9 from my own discovery + 2 added via the codex second opinion (Gate 8.4)
reconciliation** (Xu et al. and Sawada et al. — the second opinion found decision-relevant
sources my discovery missed; recorded as coverage failures in `log.md` and
`review/second-opinion-reconciliation.md`).

Tier 1 (independent RCT):
- [[sources/metr-early-2025-rct]] — the only RCT on experienced+familiar devs. +19% (slower),
  early-2025, **now retired by its authors.**
- [[sources/anthropic-skill-formation-rct]] — vendor RCT (see Tier 3); novel task, no
  speedup, −17% comprehension.

Tier 2 (independent peer-reviewed, observational/commit-mining — NOT RCTs):
- [[sources/nav-it-longitudinal-study]] — HICSS-59, observational (not RCT). No activity
  change after Copilot.
- [[sources/horikawa-readability-2026]] — MSR '26, commit-mining. AI refactoring degrades
  maintainability metrics in 56% of commits.
- [[sources/beyond-the-commit-bny-mellon]] — ICSE SEIP, 2,989 devs, mixed-methods.
  Conflicting perspectives; long-term costs undercounted (Round 3).
- [[sources/gao-survey-bugs-ai-code]] — systematic review of bugs in AI-generated code
  (Round 3).
- [[sources/xu-maintenance-burden-2025]] — AI shifts maintenance burden onto experienced
  devs; aggregate gains from peripheral devs. **Found by second opinion.**
- [[sources/sawada-agent-maintenance-2026]] — COUNTERPOINT: agent-generated files received
  less frequent maintenance. **Found by second opinion.**

Tier 3 (independent field RCT, mixed independence):
- [[sources/cui-demirer-mit-copilot-field-experiments]] — 4,867 devs, 3 firms. +26%
  throughput; senior effect small/ns. Confidence capped medium.

Tier 4 (vendor RCT, capped medium):
- [[sources/github-copilot-55-percent-study]] — lab, single greenfield task, −55.8% time,
  pooled mixed-experience sample (NOT a junior-subgroup estimate).
- [[sources/anthropic-skill-formation-rct]] — listed under Tier 1 above for its
  independence-of-publication honesty, but it is a vendor RCT; confidence capped medium.

Tier 5 (independent observational / survey):
- [[sources/dora-2024-report]] — AI adoption ↔ −7.2% delivery stability; self-report
  positive.
- [[sources/gitclear-code-quality-2025]] — cloned code up, refactoring down (figures
  verified on public landing page; methodology email-gated).

Tier 6 (self-report survey, explicitly distrusted by its authors):
- [[sources/metr-2026-self-report-survey]] — 1.4–2x value self-report; METR says don't
  trust the magnitude.

Plus the critical recency update:
- [[sources/metr-late-2025-uplift-update]] — METR's late-2025 data point-estimates a
  speedup but is unreliable due to selection. The early-2025 result is *historically*
  valid but *not* the current state.

## Key caveats (read before acting on this)

1. **Recency is the single most important caveat.** METR's +19% (slower) is early-2025
   (Cursor + Claude 3.5/3.7, chat/autocomplete). METR's own Feb 2026 update retires that
   number; their late-2025 follow-up with agentic tools point-estimates an 18% speedup but
   is uninterpretable due to selection effects. **The current state for the user's
   condition is unmeasured.** The synthesis and decision guide lead with this trajectory,
   not with the retired number.
2. **METR matches the user on population + familiarity, mismatches on tool generation.**
   METR's arm was early-2025 chat/autocomplete; the user is a daily agentic (Claude Code)
   user. METR names "heavier agent scaffolding" as an untested condition. Weight METR as
   high evidentiary value for the *question*, limited for the *current answer*.
3. **Single RCT for the user's condition**: METR is the only study on experienced +
   familiar. Don't over-rely on the exact +19%; the *direction* (small/negative for
   experienced+familiar in early 2025) is corroborated by Cui/Demirer's underpowered
   senior subgroup, and the late-2025 direction may have flipped.
4. **Non-speed effects are correlational**: DORA, GitClear, Horikawa, BNY Mellon show
   consistent negative direction but not causation.
5. **Vendor studies capped at medium** per Gate 4.5: Peng et al. and Anthropic cannot
   support a high-confidence performance claim.
6. **The fit question is unanswerable from the web.** The decision guide specifies the
   30-task self-experiment that would answer it for the user.

## External review status

- **Second opinion (codex)**: ran independently; result + reconciliation in `review/`.
- **Review panel (agy, codex, claude:opus)**: ran, 1 loop. **1 of 3 reviewers blocked
  (agy could not be invoked).** 2/2 active reviewers returned `needs-fixes`; consensus
  computed in `review/panel-round-1/consensus.md`; all consensus findings fixed in
  `review/panel-round-1/fixes.md`. Do not report the panel's verdict as unanimous — one
  reviewer failed to run.

## How to audit this dossier

- Start at [[log.md]] — every query is logged including the failures. If a source
  appears nowhere in the ledger, it was assumed, not discovered.
- Check [[evidence.md]] — every claim has a source and a confidence typed per Gate 4.5
  (fact / performance / fit).
- Check [[open-questions.md]] — no high-impact gap is left in `partially resolved`.
- Check [[synthesis.md]] §"What the web cannot settle" — the fit question is named, not
  quietly answered.