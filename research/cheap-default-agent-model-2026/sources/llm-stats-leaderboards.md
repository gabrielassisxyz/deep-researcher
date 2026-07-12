---
type: source
source_type: aggregator
title: "LLM Stats — SWE-bench Verified & Aider-Polyglot leaderboards"
publisher: "LLM Stats (llm-stats.com)"
url: "https://llm-stats.com/benchmarks/swe-bench-verified"
author: null
published: null
accessed: 2026-07-12
confidence: medium
used_for: [cross-model-swe-bench-scores, pricing-context, candidate-discovery]
---

# LLM Stats leaderboards

Scraped 2026-07-12 (both SWE-bench Verified and Aider-Polyglot pages). Aggregator that collates self-reported and verified model scores. Pages note "last updated July 2026"; SWE-bench Verified tracks 103 models, Aider-Polyglot 22.

## Caveat

- Aggregator, not primary. Scores are marked "self-reported" (0 verified on both pages at scrape time). Serves as **discovery** and cross-check, not as the final word on any single model.
- Page presented a "Quick verification / Confirm you're human" interstitial; data tables loaded after. Treat prices shown as indicative; corroborate with vendor docs.

## SWE-bench Verified — cheap candidates + frontier reference (top 50)

| # | Model | Score | Context | $/M in | $/M out |
| --- | --- | --- | --- | --- | --- |
| 1 | Claude Fable 5 | 0.950 | 1.0M | $10 | $50 |
| 3 | Claude Opus 4.8 | 0.886 | 1.0M | $5 | $25 |
| 5 | Claude Sonnet 5 | 0.852 | 1.0M | $3 | $15 |
| 8 | **DeepSeek-V4-Pro-Max** | **0.806** | 1.0M | $1.60 | $3.20 |
| 9 | Gemini 3.1 Pro | 0.806 | 1.0M | $2.50 | $15 |
| 10 | **MiniMax M3** | **0.805** | 1.0M | **$0.30** | **$1.20** |
| 11 | Qwen3.7 Max | 0.804 | 1.0M | $1.25 | $3.75 |
| 12 | Kimi K2.6 | 0.802 | 262K | $0.75 | $3.50 |
| 12 | **MiniMax M2.5** | **0.802** | 1.0M | **$0.30** | **$1.20** |
| 16 | **DeepSeek-V4-Flash-Max** | **0.790** | 1.0M | **$0.10** | **$0.20** |
| 17 | MiMo-V2.5-Pro | 0.789 | 1.0M | $0.43 | $0.87 |
| 19 | Gemini 3 Flash | 0.780 | 1.0M | $0.50 | $3.00 |
| 21 | GLM-5 | 0.778 | 200K | $1.00 | $3.20 |
| 22 | Qwen3.7-Plus | 0.777 | 1.0M | $0.32 | $1.28 |
| 37 | Step-3.5-Flash | 0.744 | 66K | $0.10 | $0.40 |
| 44 | Claude Haiku 4.5 | 0.733 | 200K | $1.00 | $5.00 |

## Aider-Polyglot (llm-stats view, 22 models)

GPT-5 0.880, Gemini 2.5 Pro Preview 06-05 0.822, o3 0.813, Gemini 2.5 Pro 0.765, DeepSeek-V3.2-Exp 0.745, DeepSeek-R1-0528 0.716, Gemini 2.5 Flash 0.619, Qwen3-Coder 480B 0.618, Kimi K2 0.600, GPT-4.1 0.516, GPT-4.1 mini 0.347, Gemini 2.5 Flash-Lite 0.267, GPT-4.1 nano 0.098.

## Why this source matters

This is the source that **surfaced the candidate set** the user did not name: DeepSeek-V4-Flash-Max, MiniMax M3/M2.5, MiMo-V2.5-Pro, Step-3.5-Flash, Qwen3.7-Plus, GLM-5. It is aggregator-only, so all scores cap at medium confidence and must be corroborated for any single model's performance claim.