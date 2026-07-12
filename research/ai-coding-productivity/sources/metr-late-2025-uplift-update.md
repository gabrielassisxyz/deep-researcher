---
type: source
source_type: official
title: "We are Changing our Developer Productivity Experiment Design (Late-2025 update)"
publisher: "METR"
url: "https://metr.org/blog/2026-02-24-uplift-update/"
author: "Joel Becker, Nate Rush, Tom Cunningham, David Rein, Khalid Mahamud"
published: 2026-02-24
accessed: 2026-07-12
confidence: high
used_for: [recency, measured-speedup, selection-effects, experienced-developers]
independence: independent
---

# METR Late-2025 Uplift Update

Continuation of the early-2025 RCT with late-2025 AI tools (Claude Code, Codex, etc.).

## Setup

- 57 developers (10 original + 47 new), 143 repos, 800+ tasks.
- New devs from more diverse repos incl. smaller, greenerfield, less mature.
- Paid $50/hr (down from $150/hr — a confound).
- Aug 2025 onward.

## Key results

- Original-dev subset: estimated **18% speedup** (CI -38% to +9%) — i.e. sign flipped
  vs. early-2025, but wide CI includes both slowdown and speedup.
- New-dev subset: estimated **4% speedup** (CI -15% to +9%).
- Early-2025 by comparison: +19% time (slowdown), CI +2% to +39%.

## Why METR does NOT trust these numbers

Selection effects now severe:
1. Developers increasingly refuse to participate rather than work without AI
   → systematically missing the most AI-optimistic devs.
2. 30–50% of devs admit not submitting tasks they didn't want to do without AI
   → systematically missing high-uplift tasks.
3. Lower pay ($50/hr) likely worsened selection.
4. Some devs run multiple agents concurrently → time reports unreliable.
5. Task-substitution: devs choose different tasks when agentic AI is available.

METR's qualitative belief from interviews: devs are probably more sped-up now than in
early-2025, but the experiment can only provide "very weak evidence" of the size.

## Implication for the dossier

- The early-2025 "19% slower" result is NOT the current state. It may have narrowed or
  reversed.
- But the *measurement infrastructure* for the current state has broken down: selection
  effects make RCTs of this design increasingly unreliable as AI adoption saturates.
- This is itself a meta-finding: **as AI becomes more valuable, it becomes harder to
  measure the value experimentally**, because no one will consent to the control condition.

## Claim typing

- Fact (update published, methods described): high.
- Performance (late-2025 effect size): LOW confidence in the specific number — METR
  themselves say it's unreliable. Direction (less slowdown than early-2025) is medium.