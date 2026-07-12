---
type: source
source_type: official-pricing
publisher: DeepSeek
title: Models and pricing
url: https://api-docs.deepseek.com/quick_start/pricing
accessed: 2026-07-04
confidence: high
---

# DeepSeek Models And Pricing

## Summary

DeepSeek's official API docs verify `deepseek-v4-flash` and `deepseek-v4-pro`. Both support thinking and non-thinking modes, 1M context, and up to 384K output. The page says legacy `deepseek-chat` and `deepseek-reasoner` names will be deprecated on 2026-07-24 15:59 UTC and mapped to non-thinking and thinking modes of `deepseek-v4-flash`, respectively.

## Pricing Used

| Model | Context | Max output | Cache-hit input | Cache-miss input | Output | Concurrency |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `deepseek-v4-flash` | 1M | 384K | $0.0028 / MTok | $0.14 / MTok | $0.28 / MTok | 2500 |
| `deepseek-v4-pro` | 1M | 384K | $0.003625 / MTok | $0.435 / MTok | $0.87 / MTok | 500 |

## Claims Used

- DeepSeek V4 Pro and V4 Flash are verified exact public API model identifiers.
- DeepSeek V4 Flash is extremely low-cost relative to frontier models.
- DeepSeek V4 Pro is still far cheaper than GPT-5.5, Claude Opus 4.8, or Gemini 3.1 Pro on official list price.

## Limitations

The pricing page verifies availability and price but does not provide task-quality benchmarks.
