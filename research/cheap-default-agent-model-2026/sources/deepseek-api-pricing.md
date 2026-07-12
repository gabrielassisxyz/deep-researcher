---
type: source
source_type: official
title: "DeepSeek API Docs — Models & Pricing"
publisher: "DeepSeek"
url: "https://api-docs.deepseek.com/quick_start/pricing"
author: null
published: null
accessed: 2026-07-12
confidence: high
used_for: [deepseek-v4-flash-pricing, tool-calling, context-window, identifiers]
---

# DeepSeek API Docs — Models & Pricing

Scraped 2026-07-12. Official DeepSeek API documentation.

## Key facts captured

- Current production model: **`deepseek-v4-flash`** (replaces deprecated `deepseek-chat` non-thinking and `deepseek-reasoner` thinking; deprecation 2026-07-24 15:59 UTC).
- Premium tier: **`deepseek-v4-pro`**.
- Base URLs: `https://api.deepseek.com` (OpenAI format), `https://api.deepseek.com/anthropic` (Anthropic format — notable for Claude-Code-style harnesses via LiteLLM).
- Context length: **1M tokens**. Max output: **384K tokens**.
- **Tool Calls: ✓. JSON Output: ✓.** Chat Prefix Completion (beta), FIM Completion (beta, non-thinking only).
- Thinking mode: supports both non-thinking and thinking (default).

## Pricing (per 1M tokens, USD)

| Model | Input (cache hit) | Input (cache miss) | Output |
| --- | --- | --- | --- |
| deepseek-v4-flash | $0.0028 | **$0.14** | **$0.28** |
| deepseek-v4-pro | $0.003625 | $0.435 | $0.87 |

- Concurrency limit: 2500 (flash), 500 (pro).
- "Product prices may vary and DeepSeek reserves the right to adjust them."

## Why this source is high-confidence for facts

Official vendor docs. These are primary-source facts (existence, identifiers, pricing, tool-calling support, context). Per claim-typing rules, this source does **not** establish performance/quality claims — only facts.