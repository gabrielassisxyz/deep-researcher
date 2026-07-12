---
type: log
slug: cheap-default-agent-model-2026
topic: "A cheap default model for a coding-agent harness"
created: 2026-07-12
updated: 2026-07-12
depth_budget_rounds: 6
depth_budget_sources: 40
rounds_run: 2
queries_issued: 21
sources_kept: 8
sources_rejected: 7
termination: "Done"
---

# Search Ledger

Every query is logged here, including fruitless ones. Sources are traced to the query (or citation trail) that surfaced them. A source that appeared from nowhere is assumed, not discovered.

## Round 1 — Discovery

Queries issued (5 batched + 5 batched + 3 batched = 13):

1. `cheap LLM coding agent default model 2026 API price per token` → surfaced costgoat, fungies, apidog, agentdeals, benchlm aggregators (SEO content, not kept) and **dev.to agentic-coding article** (kept, [[sources/devto-agentic-coding-2026]]).
2. `Aider leaderboard LLM coding benchmark 2026 pass rate` → surfaced aider.chat/docs/leaderboards (kept, [[sources/aider-leaderboard]]), steel.dev, llm-stats (kept).
3. `SWE-bench verified leaderboard 2026 cheap models results` → surfaced steel.dev, swebench.com, **llm-stats SWE-bench Verified** (kept, [[sources/llm-stats-leaderboards]]).
4. `best cheap LLM for coding agents tool calling reliability 2026` → surfaced evolink.ai (kept, [[sources/evolink-coding-agents-guide]]), costbench, llmwise, dev.to.
5. `Artificial Analysis LLM coding agent index 2026 price performance` → **JUNK** (single irrelevant result: a senior-living careers page). Logged as fruitless.
6. `DeepSeek V4 flash API pricing 2026 per million tokens` → surfaced deepseek.com homepage (not pricing) repeatedly.
7. `Qwen3 Coder hosted API pricing 2026 tool calling` → surfaced qwen.ai blog, HF, GitHub QwenLM/Qwen3 (context only).
8. `GLM Kimi MiniMax cheap coding LLM API 2026 agent tool calling` → surfaced z.ai/blog, openlm.ai/glm-5.2 (kept, [[sources/openlm-glm-5.2]]), github zai-org/GLM-5.
9. `DeepSeek API platform pricing page api-platform.deepseek.com 2026 V4 flash` → surfaced deepseek.com homepage repeatedly (SEO).
10. `Artificial Analysis coding agent index 2026 price performance` → **JUNK** again (same senior-living page). Fruitless.
11. `"DeepSeek V4 Flash" OR "deepseek-v4-flash" tool calling function calling issues problems` → deepseek.com homepage only. Fruitless (no independent reports surfaced).
12. `MiniMax M3 API pricing 2026 official documentation token` → surfaced minimax.io, minimaxi.com/models/text/m3 (kept, [[sources/minimax-m3-page]]).
13. `Gemini 3 Flash pricing API 2026 per million tokens` → **JUNK** (Google Translate pages). Fruitless.

Scrapes (Round 1): aider.chat/docs/leaderboards, llm-stats.com/benchmarks/aider-polyglot, llm-stats.com/benchmarks/swe-bench-verified, api-docs.deepseek.com/quick_start/pricing, openlm.ai/glm-5.2, minimaxi.com/models/text/m3, dev.to/danishashko/..., evolink.ai/blog/best-llm-for-coding-agents-api-cost-reliability, openrouter.ai/deepseek/deepseek-chat.

**Candidate set discovered (the prompt named none):** DeepSeek V4-Flash-Max, DeepSeek V4-Pro-Max, MiniMax M3, MiniMax M2.5, MiMo-V2.5-Pro, Step-3.5-Flash, Qwen3.7-Plus, GLM-5/5.2, Kimi K2.6, Qwen3-Coder 480B. Frontier baselines: Claude Sonnet 5, Claude Opus 4.8, GPT-5.5, Gemini 3.1 Pro.

## Round 2 — Targeted follow-up (gap closure)

Queries issued (4 + 4 = 8):

14. `Terminal-Bench 2.1 leaderboard 2026 coding agent benchmark results` → **JUNK** (Windows Terminal, terminal simulator sites). Fruitless. Gap M3 blocked.
15. `OpenRouter DeepSeek V4 Flash MiniMax M3 Qwen3 Coder pricing 2026` → surfaced openrouter.ai (kept, [[sources/openrouter-deepseek]]), costgoat free-models list.
16. `DeepSeek V4 Flash review coding agent problems rate limits reliability 2026` → deepseek.com homepage only. Fruitless. Gap H2 blocked (no independent V4-Flash reliability data).
17. `coding agent model routing cheap default vs escalate frontier 2026` → **JUNK** (codecademy, freecodecamp, learn-to-code sites). Fruitless.
18. `DeepSeek V4 Flash Claude Code opencode tool calling reliability real world` → deepseek.com homepage only. Fruitless. Gap H2 stays blocked.
19. `DeepSeek V4 Flash rate limit availability outage 2026 production` → deepseek.com homepage only. Fruitless. Gap H2/H4 stays blocked.
20. `MiniMax M3 coding agent review reddit 2026 tool calling real world` → minimax.io homepage, minimaxi.com (already scraped). No independent review. Gap M4 blocked.
21. `SWE-bench Verified independent reproduction vendor reported gap contamination 2026` → **JUNK** (Society of Women Engineers). Fruitless. Gap H1 blocked (no independent V4-Flash reproduction).

Scrapes (Round 2): none new — Round 1 scrapes + the dev.to/evolink/openrouter scrapes covered the evidence.

## Sources kept (8)

1. [[sources/deepseek-api-pricing]] — official, facts (high)
2. [[sources/aider-leaderboard]] — benchmark, independent (medium)
3. [[sources/llm-stats-leaderboards]] — aggregator (medium) — **discovery source**
4. [[sources/devto-agentic-coding-2026]] — commentary, real-world (medium)
5. [[sources/evolink-coding-agents-guide]] — commentary, tool-call reliability + rate limits (medium)
6. [[sources/openlm-glm-5.2]] — official, facts (high)
7. [[sources/minimax-m3-page]] — official, facts (high)
8. [[sources/openrouter-deepseek]] — aggregator, architecture + provider variance (medium)

## Sources rejected (not kept), with reasons

- costgoat.com, fungies.io, apidog.com, agentdeals.dev, benchlm.ai — SEO/aggregator pricing-list sites; no primary value beyond llm-stats (already kept). Redundant.
- steel.dev leaderboards — aggregator; llm-stats already covers the same ground.
- llmwise.ai, costbench.com — SEO "best of" content; dev.to is strictly better.
- swebench.com (the homepage) — would have been useful for independent reproductions, but the page is an SPA leaderboard and the scrape returned only the overview; the independent-reproduction gap (H1) stayed blocked.
- qwen.ai blog, HF Qwen3, GitHub QwenLM/Qwen3 — used for context on Qwen3-Coder; rejected as standalone sources because Qwen3-Coder was cut from the shortlist (tool-call reliability "Moderate — verify before production," per evolink).
- The various DeepSeek homepage / chat pages returned by nearly every DeepSeek query — not pricing/docs; rejected.
- The Google Translate / Windows Terminal / codecademy / freecodecamp / Society of Women Engineers pages returned by junk queries — irrelevant; rejected.

## Gap resolution summary

| Gap | Round | Status |
| --- | --- | --- |
| H1 (independent V4-Flash SWE-bench) | 2 | blocked — no independent reproduction in searchable sources |
| H2 (V4-Flash tool-call reliability at volume) | 2 | blocked — only proxy (V3) + practitioner ratings; no V4 measurement |
| H3 (MiniMax M3 official pricing) | 2 | blocked — login-gated page |
| H4 (fit for this user) | inherent | blocked — unanswerable by web research; resolved by local eval in [[decision-guide]] |
| M1 (Flash vs Flash-Max price discrepancy) | 2 | blocked — treat official $0.14/$0.28 as truth |
| M2 (GLM-5.2 price) | 2 | blocked — not on openlm page |
| M3 (Terminal-Bench independent leaderboard) | 2 | blocked — searches returned junk |
| M4 (M3 independent agent-loop validation) | 2 | blocked — vendor demos only |

## Termination

**`Done`** — every high-impact gap reached `resolved` or `blocked`; none `partially resolved`. The last round (Round 2) surfaced no new high-impact gap. Budget consumed: 2 of 6 rounds, 8 of 40 sources. No second opinion, no Gemini review (non-interactive run, per user).