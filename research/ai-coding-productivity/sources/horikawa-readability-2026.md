---
type: source
source_type: paper
title: "Do AI Agents Really Improve Code Readability?"
publisher: "arXiv / MSR '26 (Mining Software Repositories)"
url: "https://arxiv.org/abs/2603.13723"
author: "Kyogo Horikawa, Kosei Horikawa, Yutaro Kashiwa, Hidetake Uwano, Hajimu Iida"
published: 2026-03-14
accessed: 2026-07-12
confidence: medium
used_for: [non-speed-effects, maintainability, code-quality-metrics, agentic-tools]
independence: independent
---

# Horikawa et al. — AI Agent Refactoring & Code Readability

Independent academic study, accepted at MSR '26. Peer-reviewed venue. Adds causal-ish
evidence on the maintainability axis for *agentic* (not autocomplete) AI.

## Setup

- Mined the AIDev dataset for commits with readability-related keywords.
- 403 commits analyzed before/after on quantitative readability + maintainability metrics
  (Maintainability Index, Cyclomatic Complexity).

## Key results

- AI agents primarily targeted logic complexity (42.4%) and documentation (24.2%), not
  surface-level naming/formatting.
- **Contrary to expectations, readability-focused commits often DEGRADED quality
  metrics:**
  - Maintainability Index decreased in **56.1%** of commits.
  - Cyclomatic Complexity increased in **42.7%** of commits.

## Why this matters

- This is agentic-tool-era evidence (not 2022 Copilot autocomplete) that AI "refactoring"
  can *worsen* the maintainability metrics it claims to improve.
- Caveats: metric-based (MI/CC are imperfect proxies); "readability-related keywords"
  selection may miss non-keyworded refactors; no human-judgment readability assessment.
- Corroborates GitClear's cloning/decline-in-refactoring finding and DORA's stability
  finding from a different angle (commit-level metric analysis vs org-level survey).

## Claim typing

- Fact (study exists, dataset described): high.
- Performance (AI-agent refactoring frequently degrades maintainability metrics):
  medium — independent, peer-reviewed venue, but proxy metrics and selection on keywords.