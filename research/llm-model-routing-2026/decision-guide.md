---
type: decision-guide
status: complete
updated: 2026-07-04
confidence: medium
---

# Decision Guide

## Task Taxonomy

| Task class | Verification ease | Failure cost | Typical bottleneck |
| --- | --- | --- | --- |
| Ambiguous planning and brainstorming | low | medium to high | framing, assumptions, trade-offs |
| Architecture and technical strategy | low | high | second-order effects, integration risk |
| Task decomposition and spec writing | medium | high | completeness and dependency ordering |
| Implementation from a clear spec | high | medium | execution accuracy and local context |
| Debugging | medium | medium to high | hypothesis quality and tool use |
| Refactoring | high if tests exist | medium | behavior preservation |
| Code review | medium | high | missed edge cases and security issues |
| Long-context analysis | medium | medium | context capacity and retrieval accuracy |
| Documentation work | high | low to medium | consistency and source grounding |
| Multimodal work | medium | medium | modality support and grounding |
| General research | medium | medium to high | source quality and synthesis |
| Bulk extraction or transformation | high | low | throughput and price |

## Routing Matrix

| Task type | Recommended tier | Candidate models | Confidence | Evidence |
| --- | --- | --- | --- | --- |
| Ambiguous planning | frontier | Claude Fable 5, Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro, Claude Sonnet 5 | high | Official positioning for highest capability, complex reasoning/coding, and agentic coding [[sources/anthropic-claude-models-overview]] [[sources/openai-gpt-5-5-guide]] [[sources/google-gemini-models]] |
| Architecture trade-offs | frontier | Claude Opus 4.8, Fable 5, GPT-5.5, Gemini 3.1 Pro | high | High ambiguity and high failure cost; frontier models are officially positioned for complex reasoning and agentic coding [[sources/anthropic-claude-models-overview]] [[sources/openai-gpt-5-5-guide]] |
| Task decomposition | frontier or upper-mid | Claude Sonnet 5, Opus 4.8, GPT-5.5, Gemini 3.1 Pro | high | Decomposition errors propagate; Sonnet 5 has lower frontier pricing during intro window [[sources/anthropic-pricing]] |
| Spec writing | upper-mid/frontier | Claude Sonnet 5, Gemini 3.1 Pro, GPT-5.5, Opus 4.8 | medium | Needs reasoning and instruction fidelity; evidence is mostly official positioning and benchmark category inference [[sources/artificial-analysis-methodology]] |
| Implementation from clear spec | cheaper specialist | Kimi K2.7 Code, DeepSeek V4 Pro/Flash, MiniMax M3, GLM-5.2, Qwen3.5 variants, Gemma 4 | medium | Official coding/agentic positioning and low-cost verified pricing, but many quality claims are vendor or aggregator evidence [[sources/kimi-k2-7-code]] [[sources/deepseek-pricing]] [[sources/minimax-m3-official]] [[sources/zai-glm-5-github]] [[sources/gemma-4-huggingface]] |
| Debugging | tiered | Start cheaper: Kimi K2.7, DeepSeek V4 Pro, GLM-5.2; escalate to Opus 4.8/GPT-5.5/Sonnet 5 | medium | Debugging is verifiable when tests reproduce the issue; ambiguous root-cause work benefits from frontier review [[sources/livebench]] [[sources/artificial-analysis-methodology]] |
| Refactoring | cheaper with tests | DeepSeek V4 Flash/Pro, Kimi K2.7 Code, MiniMax M3, Gemma 4, Qwen3.5 variants | medium | Behavior-preserving work can be constrained by tests; cheaper models have strong cost advantage [[sources/deepseek-pricing]] [[sources/openrouter-models-api]] |
| Code review | frontier reviewer | Opus 4.8, Fable 5, GPT-5.5, Sonnet 5, Gemini 3.1 Pro | high | Review has high missed-defect cost and low direct verification; frontier models are justified as judges/escalators [[sources/anthropic-claude-models-overview]] [[sources/openai-gpt-5-5-guide]] |
| Long-context repo analysis | long-context specialist | Gemini 3.1 Pro, Gemini 3.5 Flash, MiniMax M3, DeepSeek V4 Pro/Flash, GLM-5.2, Claude current models | medium | 1M context entries are verified by official or OpenRouter sources; quality still task-dependent [[sources/google-gemini-models]] [[sources/minimax-m3-official]] [[sources/deepseek-pricing]] [[sources/openrouter-models-api]] |
| Documentation work | cheaper/fast | Gemini 3.5 Flash, DeepSeek V4 Flash, Gemma 4, MiniMax M3, Qwen3.5 variants | medium | Low failure cost and high verification ease; speed and cost matter [[sources/benchlm]] [[sources/openrouter-models-api]] |
| Multimodal work | modality-first | Gemini 3.1 Pro, Gemini 3.5 Flash, MiniMax M3, Gemma 4, Claude current models | medium | Official multimodal support varies; Gemini and Gemma/MiniMax have strong modality-specific positioning [[sources/google-gemini-models]] [[sources/gemma-4-huggingface]] [[sources/minimax-m3-official]] [[sources/anthropic-claude-models-overview]] |
| General research | tiered | First pass: Gemini 3.5 Flash, DeepSeek V4 Flash, Gemma 4; final synthesis: Gemini 3.1 Pro, GPT-5.5, Opus 4.8 | medium | Research benefits from cheap broad collection and frontier synthesis/review; LiveBench and AA support task category separation [[sources/livebench]] [[sources/artificial-analysis-methodology]] |
| Bulk extraction | cheapest sufficient | DeepSeek V4 Flash, Gemma 4, Gemini 3.5 Flash, Qwen3.5 Flash | medium | High verification ease and low unit cost dominate [[sources/deepseek-pricing]] [[sources/openrouter-models-api]] |

## Cheaper Model Is Sufficient

| Scenario | Use cheaper model when | Candidate models | Confidence |
| --- | --- | --- | --- |
| Clear implementation task | Spec, acceptance tests, and file boundaries are known. | Kimi K2.7 Code, DeepSeek V4 Pro, MiniMax M3, GLM-5.2 | medium |
| Mechanical refactor | Behavior is protected by tests, type checks, snapshots, or diff review. | DeepSeek V4 Flash/Pro, Kimi K2.7, Gemma 4, Qwen3.5 | medium |
| Documentation rewrite | Source material is local and claims can be checked. | Gemini 3.5 Flash, DeepSeek V4 Flash, Gemma 4 | medium |
| Structured extraction | Output schema is strict and validation is automatic. | DeepSeek V4 Flash, Gemini 3.5 Flash, Qwen3.5 Flash | medium |
| Long-context low-ambiguity scan | Need to inspect many files or documents, not make final judgments. | DeepSeek V4, MiniMax M3, Gemini 3.5 Flash, GLM-5.2 | medium |
| Draft research notes | Sources are collected separately and a reviewer will check synthesis. | Gemini 3.5 Flash, DeepSeek V4 Flash, Gemma 4 | medium |

The common pattern is verifiability. If the task can be checked with tests, schemas, linters, citations, or deterministic comparison, cheaper models are often enough.

## Frontier Model Is Justified

| Scenario | Why frontier is justified | Candidate models | Confidence |
| --- | --- | --- | --- |
| Ambiguous scope | The model must decide what matters before execution begins. | Fable 5, Opus 4.8, GPT-5.5, Gemini 3.1 Pro, Sonnet 5 | high |
| Architecture decision | Wrong trade-offs create persistent cost. | Opus 4.8, Fable 5, GPT-5.5 | high |
| Hard decomposition | Downstream cheap execution depends on the task graph being right. | Sonnet 5, Opus 4.8, GPT-5.5 | high |
| Final implementation review | Review failures are hard to catch automatically. | Opus 4.8, Fable 5, GPT-5.5, Sonnet 5 | high |
| Security or correctness risk | Tests may not cover adversarial or edge-case behavior. | Fable 5, Opus 4.8, GPT-5.5 | medium |
| Complex multimodal synthesis | Multiple modalities and reasoning layers interact. | Gemini 3.1 Pro, Fable 5, MiniMax M3 as cheaper candidate | medium |
| High-impact research synthesis | Source conflicts and uncertainty need careful judgment. | GPT-5.5, Gemini 3.1 Pro, Opus 4.8 | medium |

## Review And Escalation Policy

Escalate from a cheaper model to a frontier reviewer when any of these triggers occur:

- The cheaper model changes architecture, security boundaries, auth, billing, data migrations, or public APIs.
- The cheaper model cannot produce a passing test or a credible root-cause explanation after two attempts.
- The task requires judging trade-offs rather than executing a known plan.
- The change touches many modules or crosses ownership boundaries.
- The model proposes deleting data, broad rewrites, or irreversible operations.
- The output is persuasive but weakly cited, especially in research.
- The task is high-cost to roll back.

Default policy:

1. Frontier model writes or reviews the plan for ambiguous work.
2. Cheaper model executes bounded subtasks.
3. Cheap model self-checks with tests, citations, or schemas.
4. Frontier model reviews final diff, evidence, and unresolved risks.
5. If the frontier reviewer finds systemic errors, re-plan with frontier and re-execute in smaller chunks.

## Cost-Performance Discussion

On list price, the strongest cost contrast is between frontier models and DeepSeek V4. Claude Fable 5 is $10 / $50 per MTok input/output; Opus 4.8 is $5 / $25; GPT-5.5 is $5 / $30; Gemini 3.1 Pro Preview is $2 / $12 up to 200K; DeepSeek V4 Flash is $0.14 / $0.28 cache-miss input/output; DeepSeek V4 Pro is $0.435 / $0.87 [[sources/anthropic-pricing]] [[sources/openai-pricing]] [[sources/google-gemini-pricing]] [[sources/deepseek-pricing]].

For repeated implementation loops, this gap is large enough that even moderate quality loss can be economically acceptable if review catches failures. For one-shot strategic decisions, the cost of a worse answer can dwarf token costs, so frontier models remain justified.

Latency also matters. BenchLM reports Gemini 3.5 Flash at 284.2 tokens/sec and 18.55s latency, making it attractive for high-volume workflows [[sources/benchlm]]. Kimi documents a high-speed K2.7 Code variant around 180 tokens/sec and up to 260 tokens/sec in short-context scenarios [[sources/kimi-k2-7-code]]. These speed signals support routing fast models to iterative work, not final judgment.
