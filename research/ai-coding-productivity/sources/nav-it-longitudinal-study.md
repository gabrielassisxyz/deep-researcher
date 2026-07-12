---
type: source
source_type: paper
title: "Developer Productivity With and Without GitHub Copilot: A Longitudinal Mixed-Methods Case Study"
publisher: "arXiv / HICSS-59"
url: "https://arxiv.org/abs/2509.20353"
author: "Viktoria Stray, Elias Goldmann Brandtzæg, Viggo Tellefsen Wivestad, Astri Barbala, Nils Brede Moe"
published: 2025-09-24
accessed: 2026-07-12
confidence: medium
used_for: [measured-vs-perceived, field-study, existing-codebase, throughput-metric]
independence: independent
---

# NAV IT Longitudinal Mixed-Methods Study

Independent academic study. Published at HICSS-59 (peer-reviewed venue). Large real-world
dataset. Directly addresses the measured-vs-self-reported divergence question.

## Setup

- NAV IT, large Norwegian public-sector agile org.
- 26,317 non-merge commits across 703 repos over 2 years.
- 25 Copilot users vs 14 non-users (observational, not RCT).
- Commit-based activity metrics + surveys + 13 interviews.

## Key results

- Copilot users were **consistently more active than non-users even before adopting
  Copilot** → selection: already-productive devs adopted.
- **No statistically significant change in commit-based activity for Copilot users after
  adoption** (minor increases only).
- **"Discrepancy between changes in commit-based metrics and the subjective experience of
  productivity"** — developers *felt* more productive, but activity metrics didn't move.

## Why this matters

- This is real-work, existing-codebase, public-sector (likely experienced) developers.
- It captures the exact divergence the user predicted: self-report says "more productive,"
  measured activity says "no change."
- Caveat: commits are a proxy, and a poor one. If AI lets you write the same value in fewer
  commits, flat commits could still be a real gain. The authors are careful not to claim
  AI does nothing — they claim the *measured activity signal* doesn't move while the
  *subjective experience* does.

## Claim typing

- Fact (study exists, data described): high.
- Performance (Copilot doesn't increase commit throughput in this org): high for this
  org, medium as a general claim (observational, n=39 devs in activity analysis).
- Fit: LOW — activity proxy.