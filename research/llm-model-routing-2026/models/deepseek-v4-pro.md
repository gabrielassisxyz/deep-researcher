---
type: model-note
model: DeepSeek V4 Pro
provider: DeepSeek
verified_identifier: deepseek-v4-pro
status: verified
updated: 2026-07-04
confidence: high
---

# DeepSeek V4 Pro

## Evidence Summary

DeepSeek's official API docs verify `deepseek-v4-pro` with 1M context, 384K max output, thinking and non-thinking modes, JSON output, tool calls, and low prices: $0.003625 / MTok cache-hit input, $0.435 / MTok cache-miss input, and $0.87 / MTok output [[sources/deepseek-pricing]]. OpenRouter corroborates a `deepseek/deepseek-v4-pro` entry with 1M context [[sources/openrouter-models-api]]. BenchLM lists DeepSeek V4 Pro as a strong open/current model at medium confidence [[sources/benchlm]].

## Routing Implication

DeepSeek V4 Pro is a prime cheaper-model candidate for implementation, debugging, refactoring, long-context processing, and bounded reasoning when low cost matters. It is cheap enough to use broadly, but final review should still escalate for ambiguous or high-stakes tasks.

## Caveats

The official source verifies pricing and capability flags, not quality. Quality claims need independent benchmark or project-specific test evidence.
