---
type: model
name: "DeepSeek V4-Flash"
vendor: "DeepSeek"
status: draft
confidence: medium
last_verified: 2026-07-12
sources: [sources/deepseek-api-pricing, sources/openrouter-deepseek, sources/llm-stats-leaderboards, sources/devto-agentic-coding-2026, sources/evolink-coding-agents-guide, sources/aider-leaderboard]
---

# DeepSeek V4-Flash

The leading cheap-default candidate by price-for-performance. **Discovered** via the SWE-bench Verified leaderboard (llm-stats) and corroborated by official docs.

## Identity / facts (high confidence)

- Model id: `deepseek-v4-flash` (replaces `deepseek-chat` non-thinking and `deepseek-reasoner` thinking; deprecation 2026-07-24). (Source: [[sources/deepseek-api-pricing]])
- API: OpenAI format `https://api.deepseek.com` and **Anthropic format `https://api.deepseek.com/anthropic`** — the latter is important for Claude-Code-style harnesses via LiteLLM. (Source: [[sources/deepseek-api-pricing]])
- Architecture: 284B total / 13B active MoE, 1M context, 384K max output. (Source: [[sources/openrouter-deepseek]])
- Native tool calling ✓, JSON output ✓, thinking + non-thinking modes. (Source: [[sources/deepseek-api-pricing]])
- Concurrency limit 2500. (Source: [[sources/deepseek-api-pricing]])

## Pricing (high confidence, official)

| | per 1M tokens |
| --- | --- |
| Input (cache miss) | **$0.14** |
| Input (cache hit) | $0.0028 |
| Output | **$0.28** |

Roughly **20–30× cheaper** than Claude Sonnet 5 ($3/$15) on input and **~50× cheaper** on output. (Source: [[sources/deepseek-api-pricing]], [[sources/llm-stats-leaderboards]])

## Performance (medium confidence)

- SWE-bench Verified: **0.790** (DeepSeek-V4-Flash-Max, self-reported via aggregator). (Source: [[sources/llm-stats-leaderboards]])
- ~79% vendor-reported single-attempt. (Source: [[sources/devto-agentic-coding-2026]])
- Aider Polyglot: V4-Flash not yet on the board; the closest proxy, **DeepSeek-V3.2-Exp Chat, scored 70.2% for $0.88** across the full 225-task benchmark, and V3.2-Exp Reasoner 74.2% for $1.30. (Source: [[sources/aider-leaderboard]])
- Tool-call reliability: "Good — improving" (practitioner rating). (Source: [[sources/evolink-coding-agents-guide]])

## Decision-relevant caveats

- **Availability/rate limits**: rated "High — variable availability"; production readiness "Medium — check status." For a default executor that runs on nearly every task, this is the single biggest risk. Mitigation: configure a fallback in LiteLLM. (Source: [[sources/evolink-coding-agents-guide]])
- **Provider variance**: through OpenRouter/aggregators, V3 tool-call error rates ranged 3.3–11.75% across providers; the hosting provider matters for tool reliability, not just the model. (Source: [[sources/openrouter-deepseek]])
- **Community framing**: "Flash is more like Haiku: great as a fast tier, not your only model." (Source: [[sources/devto-agentic-coding-2026]])

## Practical implication

For a LiteLLM proxy, V4-Flash is the strongest "cheap default" on price and the only cheap candidate with a native **Anthropic-format endpoint** (useful for Claude Code). The risk is availability; pair it with a frontier fallback (Claude Sonnet 5 / Opus) and a cheap secondary (MiniMax M3 or Qwen3-Coder) so outages and rate limits don't stall the loop.

## Claim-level confidence

- Facts (price, id, context, tool calling): **high**.
- Performance (SWE-bench, Aider proxy, tool-call rating): **medium**.
- Fit (right for this user): **low** — unanswerable from web evidence; see `decision-guide.md` for the local eval.