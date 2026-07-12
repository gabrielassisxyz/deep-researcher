---
type: source
source_type: official-pricing
publisher: Google
title: Gemini API pricing
url: https://ai.google.dev/gemini-api/docs/pricing
accessed: 2026-07-04
confidence: high
---

# Google Gemini API Pricing

## Summary

Google's Gemini pricing page lists Gemini 3.1 Pro Preview and Gemini 3.5 Flash pricing sections. The Gemini 3.1 Pro Preview paid row includes tiered pricing based on prompt length and context caching prices. The page also distinguishes free and paid tiers, with paid tier data not used to improve products.

## Pricing Used

| Model | Input | Output | Context caching | Caveat |
| --- | ---: | ---: | ---: | --- |
| `gemini-3.1-pro-preview` | $2 / MTok up to 200K, $4 / MTok above 200K | $12 / MTok up to 200K, $18 / MTok above 200K | $0.20 / MTok up to 200K, $0.40 / MTok above 200K plus storage | Official paid-tier row. |
| `gemini-3.5-flash` | section verified | section verified | section verified | Exact numeric row extraction was less reliable than OpenRouter cross-check. |

## Claims Used

- Gemini 3.1 Pro Preview is cheaper than GPT-5.5, Opus 4.8, and Fable 5 on input/output token list price.
- Gemini 3.1 Pro's price increases for prompts above 200K tokens.
- Gemini 3.5 Flash is cheaper and faster according to OpenRouter/BenchLM cross-checks, but exact official pricing values should be rechecked before procurement.

## Limitations

The dynamic pricing page made Gemini 3.5 Flash numeric extraction unreliable in this pass. The dossier uses Google for availability and pricing-section existence, and OpenRouter/BenchLM for numeric cross-checks.
