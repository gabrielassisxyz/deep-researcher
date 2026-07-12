---
type: model-note
model: GPT-5.5
provider: OpenAI
verified_identifier: gpt-5.5
status: verified
updated: 2026-07-04
confidence: high
---

# GPT-5.5

## Evidence Summary

OpenAI identifies `gpt-5.5` as its flagship model for complex reasoning and coding, while recommending smaller GPT-5.4 variants for lower-latency or lower-cost workloads [[sources/openai-gpt-5-5-guide]]. Official pricing for `gpt-5.5 (<272K context length)` is $5 / MTok input, $0.50 / MTok cached input, and $30 / MTok output [[sources/openai-pricing]]. OpenRouter lists `openai/gpt-5.5` with a 1.05M context window and the same $5 / $30 per MTok prompt/completion price class [[sources/openrouter-models-api]].

## Routing Implication

Use GPT-5.5 for ambiguous reasoning, planning, complex debugging, architecture trade-offs, final review, and research synthesis when the output quality matters more than cost. Do not default to it for well-scoped implementation loops when Kimi K2.7 Code, DeepSeek V4, MiniMax, GLM, or a smaller OpenAI model can be constrained by tests and reviewer escalation.

## Caveats

OpenAI's guide is official but high-level. Task-specific benchmark evidence should be used before making GPT-5.5 the default for a narrow workload.
