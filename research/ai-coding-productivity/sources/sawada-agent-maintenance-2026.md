---
type: source
source_type: paper
title: "To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study"
publisher: "arXiv"
url: "https://arxiv.org/abs/2605.06464"
author: "Shota Sawada, Tatsuya Shirai, Yutaro Kashiwa, Ken'ichi Yamaguchi, Hiroshi Iwata, Hajimu Iida"
published: 2026-05-07
accessed: 2026-07-12
confidence: medium
used_for: [agentic-code, maintenance, counterpoint, non-speed-effects]
independence: independent
---

# Sawada et al. — Agent-Generated Code Maintenance (a counterpoint)

**Found by the codex second opinion (Gate 8.4); added to this dossier after
reconciliation.** This is the **counterpoint** that balances the otherwise uniformly
negative non-speed section. Independent arXiv empirical study.

## Key findings (per second-opinion capture)

- Empirical study of agent-generated pull requests and their subsequent maintenance.
- **Agent-generated files received *less* frequent maintenance than human-authored files.**
- I.e. "AI always increases maintenance burden" is NOT settled — this study finds the
  opposite signal for agentic-code maintenance frequency.

## Why this matters (and why it's in the dossier despite cutting against the main thread)

- Per Gate 8.4, the second opinion's job is to surface what I missed — including evidence
  that complicates my conclusion. Omitting this would leave the non-speed section
  one-sided.
- This does NOT overturn the negative non-speed direction (DORA, GitClear, Horikawa, Xu,
  Anthropic, BNY Mellon all point the other way), but it means the maintenance axis is
  **mixed**, not unanimous. The synthesis has been updated to reflect this.
- Caveat: arXiv preprint; "maintenance frequency" is a proxy for maintenance burden (less
  maintenance could mean better code OR could mean deferred/hidden issues). Confidence
  medium.

## Claim typing

- Fact (study exists): high.
- Performance (agent-generated files required less frequent maintenance in this study):
  medium — independent, but proxy metric and preprint.