---
type: second-opinion-reconciliation
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
second_opinion_model: codex
---

# Second Opinion Reconciliation (Gate 8.4)

The codex second opinion ran independently on the research questions only — it did not see
my findings, sources, or synthesis. Its dossier is at
`research/ai-coding-productivity-second-opinion/`; its summary is saved as
`review/second-opinion-codex.md`.

## Agreement (raises confidence)

The second opinion **independently converges on the same headline findings**:

1. **The broad claim is not supported for experienced devs on familiar codebases.** ✅
   agreement. Both runs anchor on METR early-2025 (+19% slower) and note the late-2025
   update retires/casts doubt on the current number.
2. **Gains concentrate in well-specified, implementation-heavy, often greenfield/junior
   work.** ✅ agreement. Both cite Peng 55.8% and Cui/Demirer's heterogeneity.
3. **Self-reported vs. measured divergence is the key finding.** ✅ agreement. Both cite
   METR's 24/20/-19 perception gap and NAV IT's perceived-vs-commit divergence.
4. **Non-speed effects (defects, stability, maintenance, comprehension) skew negative or
   mixed.** ✅ agreement.
5. **The current 2026 agentic-tool effect for the user's exact condition is unmeasured /
   blocked.** ✅ agreement.

This independent convergence on the central claims — especially the measured-vs-self-reported
divergence and the recency caveat — **raises confidence** in those conclusions. Two
different models from different lineages (pi:glm-5.2 researching, codex second-opining)
arrived at the same answer from separate searches.

## Disagreement / coverage failure (the valuable part)

The second opinion found **three sources I missed**, one of which is a *counterpoint* that
balances my non-speed section:

1. **Xu et al. (arXiv 2510.10165, Oct 2025)** — "AI-Assisted Programming Decreases the
   Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance
   Burden." This is **directly on the user's condition** (experienced devs) and reports a
   negative effect via maintenance burden. This strengthens my Q3/Q5. **Coverage failure
   on my part — I should have found it.** Now added: [[sources/xu-maintenance-burden-2025]].
2. **Sawada et al. (arXiv 2605.06464, May 2026)** — "To What Extent Does Agent-generated
   Code Require Maintenance?" Finds agent-generated files received **less** frequent
   maintenance than human-authored files. This is a **counterpoint** to my uniformly
   negative non-speed framing. My synthesis over-stated the negative direction by omitting
   it. **Coverage failure — now added:** [[sources/sawada-agent-maintenance-2026]].
3. **Song et al. (arXiv 2410.02091, Oct 2024)** — Copilot in collaborative OSS: +5.9%
   project contributions but +8% coordination time. Relevant to the review-burden /
   coordination axis (G-H4). Not added as a full source note (the second opinion already
   captures it; I cite it via the second-opinion dossier to avoid duplication), but
   recorded here as evidence the coordination-burden gap has a partial source.

The second opinion also found the Uplevel vendor study (41% more bugs) — corroborating the
defect axis; I treat it as vendor commentary corroborating GitClear/DORA rather than a
new primary note.

## What I changed in response

- Added Xu et al. and Sawada et al. as source notes in my dossier.
- Updated `evidence.md` Q5 to include both — and **explicitly include the Sawada
  counterpoint** so the non-speed section is no longer one-sided.
- Updated `synthesis.md` Q5 to reflect the balanced direction (non-speed effects skew
  negative *but not unanimously* — maintenance burden evidence is mixed).
- Recorded this as a coverage failure in `log.md`. The second opinion found two
  decision-relevant sources my discovery missed; that is the clearest signal that my
  discovery was too narrow, and exactly the failure the second-opinion gate exists to
  catch. Per Gate 8.4, disagreement is a new gap — now resolved by adding the sources.

## Disagreements that are not errors

The second opinion's framing of METR as "High for studied setting, medium for
generalization" is slightly more generous than mine (I cap METR's current-answer value
lower because of the tool-era mismatch). This is a calibration judgment, not a factual
dispute; both are defensible. I keep my more conservative framing because METR themselves
retired the early-2025 number.

## Net effect on the dossier

The second opinion **did not overturn any finding**. It **strengthened the central claims
by independent convergence** and **corrected a coverage failure** on the non-speed axis
(Xu, Sawada). The dossier is more balanced and better-evidenced after reconciliation. The
honest answer is unchanged: the broad claim is not supported for the user's condition; the
current state is unmeasured; self-report is unreliable; non-speed effects are a real and
mixed (not uniformly negative) risk; measure it yourself.