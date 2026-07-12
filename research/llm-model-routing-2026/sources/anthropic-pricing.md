---
type: source
source_type: official-pricing
publisher: Anthropic
title: Claude pricing
url: https://platform.claude.com/docs/en/about-claude/pricing
accessed: 2026-07-04
confidence: high
---

# Anthropic Pricing

## Summary

Anthropic's pricing page lists per-million-token prices for current Claude models. It also explains prompt caching columns and notes that Opus 4.7 and later, Fable 5, Mythos 5, and Sonnet 5 use a newer tokenizer that may produce about 30% more tokens for the same text, depending on workload.

## Pricing Used

| Model | Base input | Cache hit | Output |
| --- | ---: | ---: | ---: |
| Claude Fable 5 | $10 / MTok | $1 / MTok | $50 / MTok |
| Claude Opus 4.8 | $5 / MTok | $0.50 / MTok | $25 / MTok |
| Claude Sonnet 5 through 2026-08-31 | $2 / MTok | $0.20 / MTok | $10 / MTok |
| Claude Sonnet 5 starting 2026-09-01 | $3 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Sonnet 4.6 | $3 / MTok | $0.30 / MTok | $15 / MTok |

## Claims Used

- Sonnet 5 has temporary introductory pricing through 2026-08-31.
- Opus 4.8 is roughly half the token price of Fable 5 and more expensive than Sonnet.
- Tokenizer differences mean direct dollar comparisons across Claude generations should be adjusted for workload tokenization.

## Limitations

Prices are time-sensitive and may differ on partner cloud platforms.
