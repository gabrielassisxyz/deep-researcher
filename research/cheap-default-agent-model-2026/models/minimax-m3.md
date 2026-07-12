---
type: model
name: "MiniMax M3"
vendor: "MiniMax"
status: draft
confidence: medium
last_verified: 2026-07-12
sources: [sources/minimax-m3-page, sources/llm-stats-leaderboards, sources/evolink-coding-agents-guide]
---

# MiniMax M3

The strongest **price-for-performance** candidate on SWE-bench Verified, and the only cheap candidate that explicitly lists the user's harnesses. **Discovered** via the SWE-bench Verified leaderboard.

## Identity / facts (high confidence)

- Model id: `MiniMax-M3`. API: `https://api.minimaxi.com/v1/text/chatcompletion_v2` (OpenAI-compatible). (Source: [[sources/minimax-m3-page]])
- 1M-token context (≥512K usable), MiniMax Sparse Attention, native multimodal, native tool calling, auto cache. (Source: [[sources/minimax-m3-page]])
- **Explicit harness integration**: Claude Code, Roo Code, Kilo Code, Cline, Codex CLI, **OpenCode**, Droid, TRAE, Grok CLI, Cursor. The user's harnesses (opencode, Claude Code, Codex) are all supported. (Source: [[sources/minimax-m3-page]])

## Pricing (medium confidence — aggregator only)

$0.30/$1.20 per M (in/out) per llm-stats. **Not confirmed on the official model page** (pricing lives on `platform.minimaxi.com/subscribe/token-plan`, not scraped). Confirm before relying. (Source: [[sources/llm-stats-leaderboards]])

## Performance (medium confidence)

- SWE-bench Verified: **0.805** (self-reported via aggregator) — within ~5 points of Claude Sonnet 5 (0.852) at ~1/10 the output price and ~1/12 the input price. (Source: [[sources/llm-stats-leaderboards]])
- Vendor demos: 12-hour autonomous ICLR paper reproduction; 147-iteration CUDA kernel optimization (9.4× speedup, 1959 tool calls, zero human intervention); BrowseComp 83.5 (claims > Opus 4.7 79.3). (Source: [[sources/minimax-m3-page]]) — these are vendor demos, cap medium.

## Decision-relevant caveats

- Pricing is aggregator-sourced — verify on the official token-plan page.
- Tool-call reliability not independently rated by the evolink source (M3 is newer than that guide's coverage). Needs the local eval.
- M2.5 (predecessor) also scores 0.802 at the same price — a fallback within the same family if M3 has growing pains.

## Practical implication

If the verified price holds, M3 is arguably the best **quality-per-dollar** cheap default — higher SWE-bench than DeepSeek V4-Flash-Max (0.805 vs 0.790) at slightly higher price ($0.30/$1.20 vs $0.10/$0.20... note: llm-stats lists V4-Flash-Max at $0.10/$0.20, cheaper than the official DeepSeek $0.14/$0.28 — a discrepancy to resolve). M3's explicit OpenCode/Claude-Code/Codex support reduces integration friction. The trade-off vs DeepSeek: higher per-token cost, but stronger reported coding score and (per vendor) more robust long-horizon agent demos.

## Claim-level confidence

- Facts (id, context, harness support, native tool calling): **high**.
- Pricing: **medium** (aggregator only).
- Performance: **medium** (aggregator/vendor).
- Fit: **low** (unanswerable).