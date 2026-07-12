---
type: evidence
slug: cheap-default-agent-model-2026
topic: "Cheap default model for a coding-agent harness"
created: 2026-07-12
updated: 2026-07-12
---

# Evidence Ledger

Claim-level evidence. Each row ties a claim to a source note, a claim type (Fact / Performance / Fit), and a confidence ceiling per the claim-typing rules.

## Facts (ceiling high)

| Claim | Value | Source | Confidence | Notes |
| --- | --- | --- | --- | --- |
| DeepSeek V4-Flash exists, id `deepseek-v4-flash` | yes | [[sources/deepseek-api-pricing]] | high | Official docs. `deepseek-chat`/`deepseek-reasoner` deprecated 2026-07-24. |
| DeepSeek V4-Flash pricing | $0.14/M in (cache miss), $0.28/M out, $0.0028/M cache hit | [[sources/deepseek-api-pricing]] | high | Official. |
| DeepSeek V4-Flash context / max output | 1M / 384K | [[sources/deepseek-api-pricing]] | high | Official. |
| DeepSeek V4-Flash tool calling & JSON | ✓ both | [[sources/deepseek-api-pricing]] | high | Official feature table. |
| DeepSeek V4-Flash OpenAI + Anthropic format base URLs | yes | [[sources/deepseek-api-pricing]] | high | Notable for LiteLLM/Claude-Code harnesses. |
| DeepSeek V4-Flash concurrency | 2500 | [[sources/deepseek-api-pricing]] | high | Official. |
| DeepSeek V4-Flash architecture | 284B total / 13B active MoE | [[sources/openrouter-deepseek]] | medium | OpenRouter listing. |
| MiniMax M3 exists, id `MiniMax-M3`, 1M context, native tool calling | yes | [[sources/minimax-m3-page]] | high | Official model page. |
| MiniMax M3 explicit harness support (Claude Code, OpenCode, Codex CLI, Cline, Cursor) | yes | [[sources/minimax-m3-page]] | high | Official page lists these. |
| MiniMax M3 pricing | $0.30/$1.20 per M (in/out) | [[sources/llm-stats-leaderboards]] | medium | Aggregator only; not on the official page scraped. Confirm on platform.minimaxi.com before relying. |
| GLM-5.2 exists, 744B-A40B MoE, 1M context, MIT license | yes | [[sources/openlm-glm-5.2]] | high | Official. |
| GLM-5 pricing | $1.00/$3.20 per M | [[sources/llm-stats-leaderboards]] | medium | Aggregator; GLM-5.2 price not confirmed. |
| Gemini 3 Flash pricing | $0.50/$3.00 per M | [[sources/llm-stats-leaderboards]] | medium | Aggregator. |
| Frontier baseline: Claude Sonnet 5 $3/$15, Opus 4.8 $5/$25, GPT-5.5 ~$5/$30 | as listed | [[sources/devto-agentic-coding-2026]], [[sources/llm-stats-leaderboards]] | high (Sonnet/Opus official), medium (GPT-5.5) | Dev.to corroborates. |

## Performance (ceiling medium; vendor claims cap at medium)

| Claim | Value | Source | Confidence | Type |
| --- | --- | --- | --- | --- |
| DeepSeek-V4-Flash-Max SWE-bench Verified | 0.790 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator, self-reported. |
| DeepSeek-V4-Pro-Max SWE-bench Verified | 0.806 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator. |
| MiniMax M3 SWE-bench Verified | 0.805 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator, self-reported. |
| MiniMax M2.5 SWE-bench Verified | 0.802 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator. |
| Claude Sonnet 5 SWE-bench Verified | 0.852 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator, vendor-reported. |
| Claude Opus 4.8 SWE-bench Verified | 0.886 | [[sources/llm-stats-leaderboards]] | medium | Performance — aggregator, vendor-reported. |
| GPT-5.5 SWE-bench Verified | 0.887 (dev.to) | [[sources/devto-agentic-coding-2026]] | medium | Performance — blog citing vendor. |
| DeepSeek V4-Flash SWE-bench Verified | ~79% (vendor single-attempt) | [[sources/devto-agentic-coding-2026]] | medium | Performance — blog citing vendor. |
| DeepSeek-V3.2-Exp Aider Polyglot | 74.2% (reasoner) / 70.2% (chat) for $1.30 / $0.88 | [[sources/aider-leaderboard]] | medium | Performance — independent eval, but V3.2 not V4. |
| GLM-5.2 Terminal-Bench 2.1 | 81.0 (vendor) vs Claude Opus 4.8 85.0 | [[sources/openlm-glm-5.2]] | medium | Performance — vendor claim. |
| GLM-5.2 SWE-bench Pro | 62.1 (vendor) | [[sources/openlm-glm-5.2]] | medium | Performance — vendor claim. |
| Harness swing on Terminal-Bench 2.0 | same model swings 30–50pp by harness | [[sources/devto-agentic-coding-2026]] | medium | Performance — practitioner claim, no controlled cite. |
| SWE-bench contamination / OpenAI stopped reporting | OpenAI publicly stopped reporting SWE-bench Verified early 2026 | [[sources/devto-agentic-coding-2026]] | medium | Commentary citing OpenAI. |
| DeepSeek V4-Flash tool-call reliability | "Good — improving" | [[sources/evolink-coding-agents-guide]] | medium | Performance — vendor-blog practitioner rating. |
| DeepSeek V4-Flash rate-limit risk | "High — variable availability" | [[sources/evolink-coding-agents-guide]] | medium | Performance — vendor-blog rating. |
| DeepSeek V4-Flash production readiness | "Medium — check status" | [[sources/evolink-coding-agents-guide]] | medium | Performance — vendor-blog rating. |
| DeepSeek V3 tool-call error rate by provider | 3.3% (Novita) – 11.75% (StreamLake) | [[sources/openrouter-deepseek]] | medium | Performance — OpenRouter measured on V3. |
| Routing pattern (community) | 60–80% cheap, 20–40% frontier | [[sources/devto-agentic-coding-2026]] | low–medium | Commentary/social pattern. |

## Fit (ceiling low — the web cannot settle these)

| Claim | Value | Source | Confidence | Type |
| --- | --- | --- | --- | --- |
| DeepSeek V4-Flash is the right default **for this user's repos/task mix** | unanswerable | n/a | low (ceiling) | Fit — requires local evaluation. |
| Cheap heuristic (touches >N files or red test) beats model self-assessment for escalation | plausible, unverified for this user | [[sources/devto-agentic-coding-2026]] (comment) | low | Fit — practitioner heuristic. |