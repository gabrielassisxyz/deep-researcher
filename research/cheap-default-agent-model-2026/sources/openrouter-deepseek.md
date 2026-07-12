---
type: source
source_type: aggregator
title: "OpenRouter — DeepSeek V4 Flash / V4 Pro model listings"
publisher: "OpenRouter"
url: "https://openrouter.ai/deepseek/deepseek-chat"
author: null
published: null
accessed: 2026-07-12
confidence: medium
used_for: [deepseek-v4-flash-identity, architecture, tool-calling-via-openrouter]
---

# OpenRouter — DeepSeek listings

Scraped 2026-07-12 (the `deepseek-chat` page, which lists V4 Flash and V4 Pro as siblings).

## Key facts

- **DeepSeek V4 Flash**: "efficiency-optimized MoE, 284B total / 13B activated, 1M context." "Reasoning efforts `high` and `xhigh` supported." "Well suited for coding assistants, chat systems, and agent workflows where responsiveness and cost efficiency are important."
- **DeepSeek V4 Pro**: "1.6T total / 49B activated, 1M context," "advanced reasoning, coding, and long-horizon agent workflows."
- Both support OpenAI, Anthropic Messages, and Responses API formats through OpenRouter.
- DeepSeek V3 (the page scraped directly) shows real provider pricing $0.20–0.40 in / $0.80–1.30 out across StreamLake/DeepInfra/Novita, with tool-call error rates 3.3–11.75% and structured-output error rates 0.96–47.11% **depending on provider** — a concrete demonstration that the hosting provider matters for tool-call reliability, not just the model.

## Why this source matters

Corroborates V4-Flash architecture and confirms it is the same model family as the official DeepSeek API. The provider-variance in tool-call error rates on V3 is a useful warning that **through LiteLLM/OpenRouter, the provider routing affects tool reliability** — relevant to the user's LiteLLM setup. Aggregator, so medium.