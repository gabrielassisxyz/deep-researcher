---
type: source
source_type: official-pricing
publisher: OpenAI
title: OpenAI API pricing
url: https://developers.openai.com/api/docs/pricing
accessed: 2026-07-04
confidence: high
---

# OpenAI API Pricing

## Summary

OpenAI's pricing page lists standard and alternate pricing lanes for GPT-5.5 family models. The standard GPT-5.5 row shows context-qualified GPT-5.5 pricing for less than 272K context, while OpenRouter independently lists a 1.05M context entry for the same model identifier. The dossier uses the official OpenAI page for direct price claims and OpenRouter as an availability/context cross-check.

## Pricing Used

| Model row | Input | Cached input | Output | Caveat |
| --- | ---: | ---: | ---: | --- |
| `gpt-5.5 (<272K context length)` | $5 / MTok | $0.50 / MTok | $30 / MTok | Official standard row extracted from OpenAI pricing page. |
| `gpt-5.5-pro (<272K context length)` | $30 / MTok | not listed | $180 / MTok | Official standard row extracted from OpenAI pricing page. |
| `gpt-5.4-mini` | $0.75 / MTok | $0.075 / MTok | $4.50 / MTok | Cheaper OpenAI alternative. |
| `gpt-5.4-nano` | $0.20 / MTok | $0.02 / MTok | $1.25 / MTok | Cheapest OpenAI alternative in the extracted current rows. |

## Claims Used

- GPT-5.5 is substantially more expensive than OpenAI's mini and nano variants.
- GPT-5.5 Pro is a high-cost escalation model, not a default execution model.

## Limitations

The page contains multiple pricing panes. The dossier cites only rows whose model label and price columns were directly extracted.
