---
type: source
source_type: aggregator-api
publisher: OpenRouter
title: OpenRouter models API
url: https://openrouter.ai/api/v1/models
accessed: 2026-07-04
confidence: medium
---

# OpenRouter Models API

## Summary

OpenRouter's public models API provides cross-provider model identifiers, pricing, and context windows. It corroborates the existence and API identifiers for many requested models, including `openai/gpt-5.5`, `anthropic/claude-fable-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-sonnet-5`, `anthropic/claude-sonnet-4.6`, `google/gemini-3.1-pro-preview`, `google/gemini-3.5-flash`, `z-ai/glm-5.2`, `moonshotai/kimi-k2.7-code`, `minimax/minimax-m3`, `minimax/minimax-m2.7`, `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `google/gemma-4-31b-it`, and several Qwen3.5 variants.

## Claims Used

- OpenRouter confirms cross-provider availability and list pricing for exact model identifiers.
- OpenRouter lists context windows of about 1M for GPT-5.5, current Claude models, Gemini 3.1 Pro, Gemini 3.5 Flash, GLM-5.2, MiniMax M3, DeepSeek V4 Pro, and DeepSeek V4 Flash.
- OpenRouter verifies Qwen3.5 model entries even though official Qwen corroboration was not found in this pass.

## Limitations

Aggregator-only claims are capped at medium confidence. Provider pricing, routing, and availability can differ from the upstream vendor, and aggregator names may not match first-party model names exactly.
