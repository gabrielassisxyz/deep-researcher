---
type: source
source_type: paper
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
publisher: "METR (arXiv preprint)"
url: "https://arxiv.org/abs/2507.09089"
author: "Joel Becker, Nate Rush, Elizabeth Barnes, David Rein"
published: 2025-07-12
accessed: 2026-07-12
confidence: high
used_for: [measured-speedup, experienced-developers, familiar-codebase, perception-vs-measured, task-type]
independence: independent
---

# METR Early-2025 RCT

Independent nonprofit (METR). RCT, not vendor-funded. The single most decision-relevant
study for this dossier's exact question.

## Setup

- 16 experienced open-source developers, avg 5 years experience on their studied repos.
- 246 real tasks (bug fixes, features, refactors) from mature, high-quality OSS repos
  (avg 22k+ stars, 1M+ LOC). Tasks avg 2 hours.
- Randomized per-task: AI-allowed vs AI-disallowed (within-subject).
- AI-allowed: developers' choice, primarily **Cursor Pro + Claude 3.5/3.7 Sonnet**
  (frontier at the time).
- Paid $150/hr. Screen-recorded. Self-reported implementation time.
- Period: Feb–June 2025.

## Key results

- **Measured: AI-allowed tasks took 19% LONGER** (CI +2% to +39%). AI slowed them down.
- **Forecast (before): developers predicted AI would make them 24% faster.**
- **Self-report (after): developers still believed AI made them 20% faster.**
- ~40 percentage-point gap between perceived and measured effect.
- Also contradicted expert forecasts: economists predicted 39% shorter, ML experts 38% shorter.
- Robust across estimators, outcome measures, subsets. 20 candidate explanations
  investigated; 5 plausible contributors, artifacts largely ruled out.

## METR's own caveats (Table 2 of paper)

- Do NOT claim this generalizes to most developers or to other settings.
- Do NOT claim AI won't speed up this exact setting in the near future.
- Do NOT claim there's no better way to use these tools (e.g. repo-specific finetuning,
  heavier agent scaffolding).
- Plausible AI helps less-experienced devs or devs in unfamiliar codebases — not tested here.

## Critical recency note

METR's own blog now displays a warning: **"These results are out of date."** They released a
Feb 2026 continuation ([[sources/metr-late-2025-uplift-update]]) showing the slowdown
narrowed and possibly reversed, though selection effects make the late-2025 data unreliable.
The early-2025 result is historically valid but should not be read as the current state.

## Claim typing

- Fact (study exists, methods described): high.
- Performance (experienced devs slower in this setting, early-2025): high — independent RCT.
- Fit (does this mean *I* am slower): low — not generalizable to the user's setting.