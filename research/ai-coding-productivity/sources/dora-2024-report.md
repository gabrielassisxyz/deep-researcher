---
type: source
source_type: official
title: "Announcing the 2024 DORA Report (Accelerate State of DevOps)"
publisher: "Google Cloud / DORA"
url: "https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report"
author: "Nathen Harvey, Derek DeBellis"
published: 2024-10-22
accessed: 2026-07-12
confidence: medium
used_for: [non-speed-effects, delivery-stability, defect-rate, survey-self-report, systemic-effects]
independence: mixed
---

# DORA 2024 Report

Industry-standard DevOps research program (Google-sponsored). 39,000+ professionals
surveyed. The broadest dataset on *systemic* delivery effects. Self-report survey, not RCT.

## Key findings on AI

- 75%+ of respondents rely on AI for at least one daily task.
- 1/3 of respondents reported "moderate" to "extreme" productivity increases from AI
  (self-report).
- A 25% increase in AI adoption is associated with:
  - +7.5% documentation quality
  - +3.4% code quality (self-reported)
  - +3.1% code review speed
- **BUT: AI adoption associated with -1.5% delivery throughput and -7.2% delivery
  stability** (the DORA four-metric delivery performance cluster).
- 39% reported little-to-no trust in AI-generated code.

## Why this is a keystone finding

This is the cleanest evidence of the **local-vs-systemic divergence** the user asked about:
individuals *feel* faster and report better code quality, yet *organizational delivery
metrics get slightly worse*. The authors' hypothesis: faster code generation → larger
change packages → more instability and failures.

- Caveat: survey/self-report + correlational. Not causal. DORA themselves say "AI does not
  appear to be a panacea" and stress small-batch-size + testing as necessary complements.
- Mixed independence: Google-sponsored but DORA is an established independent research
  program with a decade of methodology. Treat as independent-leaning-aggregator.

## Claim typing

- Fact (report exists, methodology described): high.
- Performance (AI adoption correlates with worse delivery stability/throughput at org
  level, despite positive self-report): medium — large survey, correlational, but the
  divergence pattern is the finding, not the magnitude.
- Fit: LOW — population-level, not the user's workflow.