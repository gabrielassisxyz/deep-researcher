---
type: evidence-ledger
status: complete
updated: 2026-07-04
confidence: medium
---

# Evidence Ledger

| Claim | Confidence | Evidence | Caveat |
| --- | --- | --- | --- |
| GPT-5.5 is a verified OpenAI model positioned for complex reasoning and coding. | high | OpenAI latest model guide [[sources/openai-gpt-5-5-guide]] | Official positioning, not a benchmark. |
| GPT-5.5 standard pricing is $5 / MTok input, $0.50 / MTok cached input, and $30 / MTok output for the extracted context-qualified row. | high | OpenAI pricing [[sources/openai-pricing]] | Pricing panes vary by context and mode. |
| Claude Fable 5, Opus 4.8, Sonnet 5, and Sonnet 4.6 are verified Claude model entries. | high | Anthropic model overview and pricing [[sources/anthropic-claude-models-overview]] [[sources/anthropic-pricing]] | Sonnet 4.6 is superseded. |
| Anthropic recommends Opus 4.8 for complex agentic coding and Fable 5 for highest capability workloads. | high | Anthropic model overview [[sources/anthropic-claude-models-overview]] | Vendor recommendation. |
| Claude Sonnet 5 is temporarily cheaper through 2026-08-31. | high | Anthropic pricing [[sources/anthropic-pricing]] | Recheck after date passes. |
| Gemini 3.1 Pro is verified as `gemini-3.1-pro-preview`. | high | Google Gemini models [[sources/google-gemini-models]] | Preview status matters for production stability. |
| Gemini 3.1 Pro official paid price is $2 / $12 per MTok input/output up to 200K and $4 / $18 above 200K. | high | Google Gemini pricing [[sources/google-gemini-pricing]] | Dynamic page; values were extractable for Pro Preview. |
| Gemini 3.5 Flash is a verified stable model and useful as fast cheaper model. | medium | Google model list and BenchLM speed data [[sources/google-gemini-models]] [[sources/benchlm]] | Numeric speed is aggregator evidence. |
| Kimi K2.7 Code exact identifier is `kimi-k2.7-code`, with a high-speed variant and 256K context. | high | Kimi docs and model list [[sources/kimi-k2-7-code]] [[sources/kimi-model-list]] | Performance deltas are vendor claims. |
| GLM-5.2 is an official Z.ai open-weight model aimed at complex systems and agentic tasks. | high | Z.ai repository [[sources/zai-glm-5-github]] | Benchmark claims in repository are vendor-authored. |
| MiniMax M2.7 is verified and positioned for complex agent and coding workflows. | high | MiniMax M2.7 official page [[sources/minimax-m2-7-official]] | Benchmark values are vendor claims. |
| MiniMax M3 has official 1M context, 512K guaranteed minimum, native multimodality, and coding/agentic positioning. | high | MiniMax M3 page and repository [[sources/minimax-m3-official]] [[sources/minimax-m3-github]] | Performance examples are vendor demonstrations. |
| DeepSeek V4 Pro and V4 Flash are verified exact API identifiers. | high | DeepSeek official pricing docs [[sources/deepseek-pricing]] | Pricing docs do not prove task quality. |
| DeepSeek V4 Flash is one of the cheapest verified broad-use options in scope. | high | Official DeepSeek pricing [[sources/deepseek-pricing]] | Actual quality still requires tests or benchmarks. |
| Gemma 4 is an Apache 2.0 open model family with multimodal support, 128K-256K context, and coding/function-calling capabilities. | high | Google Gemma 4 model cards [[sources/gemma-4-huggingface]] | Benchmark table is publisher-authored. |
| Qwen3.5 exists as multiple OpenRouter-routed entries, but was not verified as a single official Qwen release in this pass. | medium | Qwen3 repo and OpenRouter API [[sources/qwen3-github]] [[sources/openrouter-models-api]] | Treat exact model choice as integration-specific. |
| Aggregator-only model availability and pricing should be capped at medium confidence. | high | Intake confidence rule and OpenRouter source nature [[intake]] [[sources/openrouter-models-api]] | Primary sources override aggregator rows. |
| Artificial Analysis supports task-family evaluation rather than a single leaderboard answer. | high | AA methodology categories and weights [[sources/artificial-analysis-methodology]] | Text-only English index. |
| LiveBench supports objective, category-based benchmark interpretation. | high | LiveBench methodology [[sources/livebench]] | Scraped current leaderboard rows were unavailable. |
| BenchLM is useful for cross-checking model rank, context, pricing, and speed, but should not be treated as primary evidence. | medium | BenchLM leaderboard and methodology summary [[sources/benchlm]] | Aggregator and provisional coverage caveats. |
| The central routing hypothesis is mostly supported. | medium | Combined cost, model-positioning, and benchmark-methodology evidence [[sources/anthropic-claude-models-overview]] [[sources/openai-gpt-5-5-guide]] [[sources/deepseek-pricing]] [[sources/artificial-analysis-methodology]] | Direct A/B workflow studies were not found in this pass. |
