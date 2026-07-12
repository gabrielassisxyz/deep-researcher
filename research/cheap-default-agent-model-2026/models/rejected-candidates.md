---
type: model
name: "Rejected / not-shortlisted candidates"
vendor: "various"
status: draft
confidence: medium
last_verified: 2026-07-12
sources: [sources/llm-stats-leaderboards, sources/aider-leaderboard, sources/devto-agentic-coding-2026, sources/evolink-coding-agents-guide]
---

# Rejected / not-shortlisted candidates

The user explicitly asked to see the ones that did not make the cut. Each rejection is tied to a reason from the comparison axes.

## Rejected as cheap default

| Model | SWE-bench / Aider | Price | Rejection reason |
| --- | --- | --- | --- |
| **Qwen3-Coder 480B** | Aider 0.618 | $0.30/$1.50 (dev.to) | Tool-call reliability "Moderate — verify before production" (evolink). Good for self-host, weaker as a hosted agent default than DeepSeek/MiniMax at similar or higher price. Watchlist. (Sources: [[sources/evolink-coding-agents-guide]], [[sources/aider-leaderboard]]) |
| **Gemini 3 Flash** | 0.780 | $0.50/$3.00 | Output price 10× DeepSeek V4-Flash; tiered Gemini pricing above 200K input punishes exactly the long-repo context the user wants. Better as a big-context escalation tool than a default. (Source: [[sources/llm-stats-leaderboards]]) |
| **Kimi K2.6** | 0.802 | $0.16/$4.00 (dev.to) / $0.75/$3.50 (llm-stats) | Strong long-horizon demos, but output price 14× DeepSeek and pricing inconsistent across sources. Open-weight (1T MoE, not RX-580-viable). Better as long-horizon escalation. (Sources: [[sources/devto-agentic-coding-2026]], [[sources/llm-stats-leaderboards]]) |
| **GLM-5 / GLM-5.2** | GLM-5 SWE-bench 0.778; GLM-5.2 T-Bench 2.1 81.0 | $1.00/$3.20 (GLM-5) | Price unconfirmed for 5.2; likely too expensive for a *cheap* default. Kept as a watchlist long-horizon option. See [[models/glm-5.2]]. |
| **MiMo-V2.5-Pro** | 0.789 | $0.43/$0.87 | Strong score and cheap, but vendor is Xiaomi, limited independent agent-loop validation and harness-integration evidence. Risky as a *default* without local eval. Watchlist. (Source: [[sources/llm-stats-leaderboards]]) |
| **Step-3.5-Flash** | 0.744 | $0.10/$0.40 | Cheap and decent, but only 66K context — below what long multi-file repo work needs. Rejected on context. (Source: [[sources/llm-stats-leaderboards]]) |
| **DeepSeek V4-Pro / V4-Pro-Max** | 0.806 | $0.435/$0.87 (promo) → $1.74/$3.48 | The "Pro" tier is the escalation model, not the cheap default. Listed as the in-family escalation target. (Sources: [[sources/deepseek-api-pricing]], [[sources/llm-stats-leaderboards]]) |
| **GPT-4.1-mini / nano, gpt-4o-mini** | Aider 32.4% / 8.9% / 3.6% | cheap | Far too weak on Aider for agent editing. Rejected on quality. (Source: [[sources/aider-leaderboard]]) |
| **Claude Haiku 4.5** | 0.733 | $1.00/$5.00 | Capable but 5–18× the output price of DeepSeek V4-Flash for lower SWE-bench. Rejected on price-for-performance. (Source: [[sources/llm-stats-leaderboards]]) |
| **Grok 4.3** | ~73% | $1.25/$2.50 | Cheaper than frontier but 9× DeepSeek V4-Flash output for lower SWE-bench. Cache costs reportedly 50× DeepSeek's. Rejected on price-for-performance. (Source: [[sources/devto-agentic-coding-2026]]) |
| **Codestral 25.01, Llama 4 Maverick, Qwen2.5-Coder-32B, Gemma-3-27B** | Aider ≤16% / ≤15.6% / ≤16.4% / 4.9% | various | Too weak on Aider; dev.to: "neither broke into the top tier for coding-agent use in early 2026." Rejected on quality. (Sources: [[sources/aider-leaderboard]], [[sources/devto-agentic-coding-2026]]) |
| **Local inference (any)** | n/a | n/a | RX 580 (~8GB VRAM) cannot run the smallest credible candidate (DeepSeek V4-Flash is 284B/13B-active MoE). Local inference not viable; rejected per user's own assumption. (Source: [[sources/openrouter-deepseek]]) |

## Frontier baselines (not candidates for the cheap default — kept for the escalation comparison)

| Model | SWE-bench | Price | Role |
| --- | --- | --- | --- |
| Claude Sonnet 5 | 0.852 | $3/$15 | Frontier workhorse baseline for cost model |
| Claude Opus 4.8 | 0.886 | $5/$25 | Frontier ceiling |
| GPT-5.5 | 0.887 | ~$5/$30 | Frontier alternative |
| Gemini 3.1 Pro | 0.806 | $2–$4/$12–$18 | Big-context frontier |

(Sources: [[sources/llm-stats-leaderboards]], [[sources/devto-agentic-coding-2026]])