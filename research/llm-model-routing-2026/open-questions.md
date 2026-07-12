---
type: open-questions
status: complete
updated: 2026-07-04
confidence: medium
---

# Open Questions

## High-Impact Gaps

| Gap | Impact | Follow-up performed | Status | Result |
| --- | --- | --- | --- | --- |
| Are `deepseek-v4-pro` and `deepseek-v4-flash` real official model IDs? | high | Checked DeepSeek official API pricing docs. | resolved | Official docs verify both IDs, 1M context, 384K max output, and pricing [[sources/deepseek-pricing]]. |
| Is `Qwen3.5` a single official public model? | high | Checked official Qwen3 repository and OpenRouter API. | partially resolved | OpenRouter lists multiple Qwen3.5 entries, but official Qwen source checked here verifies Qwen3/Qwen3-2507 rather than a single Qwen3.5 release [[sources/qwen3-github]] [[sources/openrouter-models-api]]. |
| Can vendor claims for Kimi K2.7 Code, MiniMax M3, MiniMax M2.7, GLM-5.2, and Gemma 4 be independently confirmed? | high | Checked LiveBench, Artificial Analysis methodology, BenchLM, OpenRouter, and official sources. | partially resolved | Official availability is verified. Independent methodology exists, but many specific 2026 model scores remain aggregator or vendor evidence in this pass. |
| Should Gemini 3.1 Pro Preview be used in production? | high | Checked Google model docs and pricing. | partially resolved | The model is official but preview. Use for high-value work with regression checks and fallbacks [[sources/google-gemini-models]]. |
| What is the exact official Gemini 3.5 Flash price? | medium | Checked Google pricing and OpenRouter. | partially resolved | Official pricing section exists, but exact numeric extraction was unreliable. OpenRouter and BenchLM provide cross-check values at medium confidence [[sources/google-gemini-pricing]] [[sources/openrouter-models-api]] [[sources/benchlm]]. |
| Do frontier models materially outperform cheaper models in this user's exact coding/research workflow? | high | Reviewed public evidence and methodology. | open | Public benchmarks are suggestive, but the decisive evidence would be a local evaluation harness using this user's task taxonomy. |

## Recommended Follow-Up

Build a small routing eval harness before making permanent defaults:

- Use 5 to 10 representative tasks per class: planning, spec writing, implementation, debugging, refactoring, review, long-context analysis, documentation, multimodal, and research synthesis.
- Score outputs by correctness, time-to-acceptable-output, review defects, tool calls, cost, latency, and need for escalation.
- Compare at least one frontier model, one mid/frontier-lite model, and three cheaper candidates.
- Keep frontier final review as the safety net until cheaper models pass repeated local tasks.

## Unknowns Too Weak To Decide

- Whether Qwen3.5 should be treated as one model family, multiple provider aliases, or a moving aggregator category.
- Whether Kimi K2.7 Code, MiniMax M3, GLM-5.2, and DeepSeek V4 maintain quality under long multi-file repo edits rather than benchmark tasks.
- Whether GPT-5.5's value over Sonnet 5, Opus 4.8, and Gemini 3.1 Pro is material for this user's specific planning and review tasks.
- Whether MiniMax M3's long-horizon demonstrations generalize to ordinary engineering repositories.
- Whether DeepSeek V4 Flash's extremely low price changes optimal routing enough to use it as the default first-pass executor.
