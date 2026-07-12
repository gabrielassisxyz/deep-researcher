---
type: source
source_type: paper
title: "To What Extent Does Agent-generated Code Require Maintenance? An Empirical Study"
publisher: "arXiv"
url: "https://arxiv.org/html/2605.06464v1"
author: "Shota Sawada, Tatsuya Shirai, Yutaro Kashiwa, Ken'ichi Yamaguchi, Hiroshi Iwata, Hajimu Iida"
published: 2026-05-07
accessed: 2026-07-12
confidence: medium
used_for: [agentic-code, maintenance, conflicting-evidence, non-speed-outcomes]
---

# Sawada et al. Agent-Generated Code Maintenance

## Source Type

arXiv empirical study of agent-generated pull requests and subsequent maintenance.

## Method

Analysis of the AIDev dataset, GitHub data, more than 1,000 files, about 3,200 changes, and 100 popular repositories.

## Key Evidence

- The paper reports AI-generated files receive less frequent maintenance than human-authored code, and updates affect only a small fraction of file size.
- The most frequent modifications to AI-generated code are feature extensions, whereas human-authored updates focus on bug fixes.
- Human developers perform the large majority of maintenance.

## Caveats

Lower observed maintenance can mean lower burden, but it can also reflect newer code, less usage, selection effects, or unobserved quality differences. The study is about agent-generated PRs, not experienced-developer speed.

## Practical Implication

This is useful conflicting evidence against a simple "AI code always creates more maintenance" claim.
