---
type: source
source_type: paper
title: "The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers"
publisher: "MIT / Microsoft / Wharton (working paper)"
url: "https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf"
author: "Kevin Zheyuan Cui, Mert Demirer, Sonia Jaffe, Leon Musolff, Sida Peng, Tobias Salz"
published: 2025-02
accessed: 2026-07-12
confidence: medium
used_for: [measured-speedup, experience-level, field-experiment, throughput-metric]
independence: mixed
---

# Cui/Demirer MIT Three-Field-Experiments

Three RCTs at Microsoft, Accenture, and a Fortune 100 electronics manufacturer. 4,867
developers total. Real workplace. This is the strongest *field* evidence of a positive
effect.

## Setup

- Random access to GitHub Copilot (autocomplete, not agentic).
- Outcomes: pull requests, commits, builds, build success rate.
- Instrumental-variable estimates (treatment assignment as instrument for usage).
- Microsoft experiment only: tenure and seniority observed.

## Key results

- **Pooled: +26.08% (SE 10.3%) in completed tasks/week** (pull requests) for users.
- +13.55% commits, +38.38% builds.
- **Heterogeneity: gains concentrated in short-tenure and junior developers.**
  - Short tenure: +27% to +39% across outcomes.
  - Long tenure: +8% to +13% (smaller, not statistically significant).
  - Junior: +21% to +40%; Senior: +7% to +16%.
  - Less productive devs gained more.
- Build success rate: no negative effect at Microsoft; negative at Accenture (-20.72%**).
  Authors flag the increase in builds may reflect more trial-and-error coding → possible
  long-run quality concern.

## Important caveats

- **Metric is activity (PRs/commits/builds), not value or time-to-ship.** Authors note
  coding is only part of a developer's job; time saved on coding may not become more coding.
- Long-tenure/senior effects are noisy and "not statistically significant at conventional
  levels" — the pattern is consistent but underpowered for that subgroup.
- Microsoft and GitHub authors are on the paper (mixed independence) — but the design is
  a genuine pre-registered RCT (AEARCTR-0014530) and economists at MIT/Wharton lead the
  analysis. Treat as independently-analyzed vendor data.
- Authors explicitly note their 26% is "substantially smaller than the 58% decrease" from
  the lab study — field effects are smaller than lab effects.

## Claim typing

- Fact (RCTs run, methods): high.
- Performance (Copilot autocomplete increases PR throughput, esp. for juniors/short-tenure):
  medium — genuine field RCT, but activity-not-value metric and mixed independence;
  capped at medium per Gate 4.5.
- Performance (effect on experienced/senior devs): medium but SMALL — the data show a
  smaller, statistically-ns effect for seniors. This is the key nuance for the dossier.
- Fit (does this make an experienced dev faster on real work): LOW — metric is throughput,
  not task time; senior effect is weak.