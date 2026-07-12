---
type: open-questions
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, gaps]
---

# Open Questions

## High-Impact Gaps

| Gap | Impact | Status | Resolution Evidence |
| --- | --- | --- | --- |
| Whether controlled evidence exists specifically for experienced developers on real work in familiar existing codebases. | high | resolved | METR early-2025 RCT directly studies this setting and finds a slowdown. METR late-2025 update says current effects are likely different but not cleanly estimated. See [[sources/metr-early-2025-rct]] and [[sources/metr-late-2025-uplift-update]]. |
| Whether self-reported speedup diverges materially from measured speedup. | high | resolved | METR shows forecast/post-hoc speedup beliefs diverging from measured slowdown; NAV case study finds perceived productivity has negligible correlation with commit metrics. See [[sources/metr-early-2025-rct]] and [[sources/stray-nav-copilot-longitudinal]]. |
| Whether non-speed costs offset measured speed gains. | high | resolved | Evidence shows possible impacts on delivery stability, bugs, duplication, comprehension, coordination, and expert review burden. See [[sources/dora-2024-ai-impact]], [[sources/uplevel-copilot-quantitative-study]], [[sources/gitclear-code-quality-2025]], [[sources/anthropic-skill-formation-rct]], [[sources/xu-maintenance-burden-2025]], and [[sources/song-copilot-collaborative-oss]]. |
| Whether current 2026 autonomous coding agents make experienced developers faster in familiar codebases. | high | blocked | METR's late-2025 update says current tools likely improve speed relative to early 2025 but the available task-level experiment is biased and unreliable. No clean independent 2026 RCT for the exact setting was found. See [[sources/metr-late-2025-uplift-update]]. |

## Medium-Impact Gaps

| Gap | Impact | Status | Resolution Evidence |
| --- | --- | --- | --- |
| How current agentic coding tools differ from Copilot-style assistant evidence. | medium | blocked | Current agentic tools make measurement harder because developers run agents concurrently and choose different task types. Evidence exists, but not enough to quantify a stable speedup. See [[sources/metr-late-2025-uplift-update]] and [[sources/sawada-agent-maintenance-2026]]. |
| Whether peer-reviewed evidence exists for experienced developers in familiar codebases. | medium | blocked | Search found preprints, field reports, and vendor/industry reports, but no peer-reviewed controlled trial that cleanly matches experienced developers doing familiar-codebase work. |

## Not Answerable From The Web

The expected productivity gain for a specific experienced developer or team in its own familiar codebase is a fit claim. Web research can identify plausible conditions and risks, but a local evaluation is required.

Concrete local evaluation:

- Select 20 to 40 real tasks from the team's normal backlog, stratified by boilerplate, bug fix, refactor, feature, ambiguous investigation, and review-heavy change.
- Randomize at the task level or developer-week level between AI-allowed and AI-disallowed conditions.
- Require baseline tests or acceptance checks before starting each task.
- Measure wall-clock implementation time, active human time, agent waiting time, review cycles, defects found before merge, defects after merge, PR size, and follow-up rework within two to four weeks.
- Collect self-reported expected speedup before the task and perceived speedup after the task, then compare to measured outcomes.
- Analyze experienced developers separately from junior developers and familiar repositories separately from unfamiliar ones.
