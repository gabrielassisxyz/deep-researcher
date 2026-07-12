---
type: source
source_type: aggregator
title: "AI Copilot Code Quality: 2025 Look Back at 12 Months of Data"
publisher: "GitClear"
url: "https://www.gitclear.com/ai_assistant_code_quality_2025_research"
author: "GitClear research"
published: 2025
accessed: 2026-07-12
confidence: medium
used_for: [non-speed-effects, defect-rate, maintainability, code-quality-metrics]
independence: independent
---

# GitClear AI Code Quality 2025

Independent analysis (vendor of code-quality tooling, but not an AI vendor). Largest known
structured code-change dataset: 211M changed lines, 2020-2024, from Google/Microsoft/Meta
and enterprise repos. The "exceeds.ai" aggregator figures (1.7x more issues, 30-41% tech
debt rise) trace back to this and DORA.

## Key findings

- "Copy/pasted" (cloned) code lines rose from 8.3% (2021) → 12.3% (2024) — ~4x growth in
  cloned blocks over the AI-adoption period. **(Figure verified on the free/public
  portion of the GitClear page: the cloning graph and these percentages are displayed
  on the public landing page.)**
- "Moved" (refactored/reused) lines declined from 25% of changed lines (2021) → <10%
  (2024). **(Same public landing page.)**
- Short-term churn code increased.
- Thesis: AI-assisted code prioritizes immediate output over DRY/modular structure
  → long-run maintainability risk.

## Provenance note (per review panel F10)

The two headline percentages above (8.3%→12.3% clones; 25%→<10% moved) were read directly
from the public GitClear landing page (the scrape captured them; the email-gated
methodology details were NOT accessed). The secondary aggregator exceeds.ai was
**rejected** as a source and is NOT the basis for these figures — it is referenced in
`log.md` only as commentary that cites the same primary. If the GitClear figures were
retracted or revised, the directional claim (more cloning, less refactoring) would
still stand but the precise percentages should be re-verified against the primary.

## Caveats

- Correlational; pre/post, not RCT. AI-assisted vs non-AI-assisted blocks inferred, not
  labeled by the authoring tool in all cases.
- Methodology partially behind email-gate; some figures are from secondary aggregators
  (exceeds.ai) citing this work.
- Cannot cleanly separate "AI wrote this" from "AI era coincided with this." But the trend
  direction is consistent with the DORA stability finding.

## Claim typing

- Fact (dataset exists, trends reported): high.
- Performance (AI-era code has more duplication, less reuse): medium — large dataset,
  correlational, methodology partly opaque.
- Fit: LOW — codebase-population level.