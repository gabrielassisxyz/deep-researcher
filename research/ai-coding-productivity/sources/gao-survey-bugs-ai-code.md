---
type: source
source_type: paper
title: "A Survey of Bugs in AI-Generated Code"
publisher: "arXiv"
url: "https://arxiv.org/abs/2512.05239"
author: "Ruofan Gao, Amjed Tahir, Peng Liang, Teo Susnjak, Foutse Khomh"
published: 2025-12-04
accessed: 2026-07-12
confidence: medium
used_for: [non-speed-effects, defect-rate, bugs, systematic-review]
independence: independent
---

# Survey of Bugs in AI-Generated Code (Gao et al. 2025)

Independent systematic literature review. Added in Round 3 after the review panel flagged
it as a deferred-but-unread lead. Consolidates the scattered bug/defect findings.

## Setup

- Systematic analysis of existing AI-generated-code literature.
- Classifies bug types and patterns by model; discusses remediation.

## Key findings (from abstract)

- AI-generated code has well-documented quality concerns: bugs, defects, trust and
  maintenance challenges.
- Findings were "scattered and lack a systematic summary" prior to this review — this is
  the consolidation.
- Provides a classification of bug types/patterns per model family and mitigation
  strategies.

## Why this matters for the dossier

- Corroborates the non-speed-effects axis (Q5) from a systematic-review angle: the defect
  concerns in DORA (stability), GitClear (clones), Horikawa (maintainability metrics) are
  not idiosyncratic; this review aggregates the broader literature confirming bugs/defects
  in AI-generated code are a documented, patterned phenomenon.
- Caveat: a survey of surveys — does not introduce new measured data; consolidates
  existing studies. Confidence reflects that.

## Claim typing

- Fact (review exists): high.
- Performance (AI-generated code has documented bug/defect patterns): medium — systematic
  review, independent, but aggregates rather than measures anew.