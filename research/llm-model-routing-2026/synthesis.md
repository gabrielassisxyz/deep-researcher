---
type: synthesis
status: complete
updated: 2026-07-04
confidence: medium
---

# Synthesis

## Executive Judgment

The user's working hypothesis is mostly validated. Frontier models are justified for ambiguous planning, architecture trade-offs, difficult decomposition, high-stakes final review, and complex synthesis. Cheaper strong coding or agentic models are often sufficient for implementation from a clear spec, mechanical refactoring, documentation passes, structured extraction, and first-pass research triage when the workflow has tests, acceptance criteria, and escalation gates.

The hypothesis needs two refinements:

- Some "cheap" models are no longer merely fallback models. DeepSeek V4 Pro/Flash, Kimi K2.7 Code, MiniMax M3, GLM-5.2, Gemma 4, and Qwen3.5-family models have enough official or aggregator evidence to treat them as serious execution candidates, not only drafts [[sources/deepseek-pricing]] [[sources/kimi-k2-7-code]] [[sources/minimax-m3-official]] [[sources/zai-glm-5-github]] [[sources/gemma-4-huggingface]] [[sources/openrouter-models-api]].
- Model routing should be task-tiered, not leaderboard-tiered. Artificial Analysis and LiveBench both reinforce the need to look at agents, coding, reasoning, long context, and instruction following separately instead of relying on one global rank [[sources/artificial-analysis-methodology]] [[sources/livebench]].

## Verified Model Status

| Requested name | Verified status | Best exact identifier evidence |
| --- | --- | --- |
| GPT 5.5 | verified | `gpt-5.5` in OpenAI docs and pricing [[sources/openai-gpt-5-5-guide]] [[sources/openai-pricing]] |
| Opus 4.8 | verified | `claude-opus-4-8` in Anthropic docs [[sources/anthropic-claude-models-overview]] |
| Sonnet 4.6 | verified, superseded | `claude-sonnet-4.6` pricing and OpenRouter entry [[sources/anthropic-pricing]] [[sources/openrouter-models-api]] |
| Sonnet 5 | verified | `claude-sonnet-5` in Anthropic docs [[sources/anthropic-claude-models-overview]] |
| Gemini 3.1 Pro | verified preview | `gemini-3.1-pro-preview` [[sources/google-gemini-models]] |
| Gemini 3.5 Flash | verified stable | `gemini-3.5-flash` [[sources/google-gemini-models]] |
| GLM-5.2 | verified | GLM-5.2 official repository [[sources/zai-glm-5-github]] |
| Kimi K2.7-Code | verified spelling variant | `kimi-k2.7-code` [[sources/kimi-k2-7-code]] |
| Gemma4 | verified family | Gemma 4 family model cards [[sources/gemma-4-huggingface]] |
| Qwen3.5 / Qwen 3.5 | partially verified | OpenRouter entries; no official Qwen corroboration found in this pass [[sources/openrouter-models-api]] [[sources/qwen3-github]] |
| MiniMax-m2.7 | verified | MiniMax M2.7 official page [[sources/minimax-m2-7-official]] |
| MiniMax-m3 | verified | MiniMax M3 official page and repository [[sources/minimax-m3-official]] [[sources/minimax-m3-github]] |
| DeepSeek v4 Pro | verified | `deepseek-v4-pro` official API docs [[sources/deepseek-pricing]] |
| DeepSeek v4 flash | verified | `deepseek-v4-flash` official API docs [[sources/deepseek-pricing]] |
| Fable | verified as Claude Fable 5 | `claude-fable-5` [[sources/anthropic-claude-models-overview]] |

## Cost-Performance Pattern

Frontier list prices vary widely. Fable 5 is $10 / MTok input and $50 / MTok output; Opus 4.8 is $5 / $25; GPT-5.5 is $5 / $30; Gemini 3.1 Pro Preview is $2 / $12 up to 200K and $4 / $18 above 200K; Sonnet 5 is temporarily $2 / $10 through 2026-08-31 [[sources/anthropic-pricing]] [[sources/openai-pricing]] [[sources/google-gemini-pricing]].

Cheaper execution models can be orders of magnitude cheaper. DeepSeek V4 Flash is $0.14 / MTok cache-miss input and $0.28 / MTok output, with 1M context and 384K max output; DeepSeek V4 Pro is $0.435 / $0.87 [[sources/deepseek-pricing]]. OpenRouter lists Kimi K2.7 Code, GLM-5.2, MiniMax M3, Gemma 4, Qwen3.5 variants, and Gemini 3.5 Flash at substantially lower prices than top frontier models [[sources/openrouter-models-api]].

The decision implication is direct: once the task is decomposed and verifiable, the marginal value of a frontier model often drops below its marginal cost. The exception is when the task remains ambiguous, cross-cutting, high-risk, or hard to verify.

## Task Evidence Pattern

Benchmark methodology sources support a task-family view. Artificial Analysis weights agentic tasks, coding, scientific reasoning, and general tasks separately, and its methodology explicitly separates multimodal and multilingual evaluation from the text-only Intelligence Index [[sources/artificial-analysis-methodology]]. LiveBench separates reasoning, coding, agentic coding, mathematics, data analysis, language, and instruction following, with objective ground-truth scoring rather than LLM judges [[sources/livebench]].

BenchLM is useful as a cross-check because it reports task categories, context, pricing, speed, and confidence indicators, but its evidence remains aggregator-level. It places frontier models near the top while also showing Gemini 3.5 Flash, DeepSeek V4 Pro, GLM-5.2, and other cheaper models as practical contenders in specific categories [[sources/benchlm]].

## Practical Conclusion

Use a two-pass or three-pass workflow for expensive work:

1. Frontier or strong planner: clarify requirements, decompose tasks, identify risks, and set acceptance tests.
2. Cheaper specialist executor: implement bounded tasks, run tests, produce diffs, generate docs, or process sources.
3. Frontier reviewer: review design, correctness, security, edge cases, and whether the implementation actually satisfies the spec.

This pattern preserves the main benefits of frontier models where they matter most while capturing most of the cost savings from cheaper models during repeated execution.
