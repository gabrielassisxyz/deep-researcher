---
type: source
source_type: official
title: "MiniMax M3 — model page (minimaxi.com)"
publisher: "MiniMax"
url: "https://www.minimaxi.com/models/text/m3"
author: null
published: 2026-06
accessed: 2026-07-12
confidence: high
used_for: [minimax-m3-identity, context, agent-claims, harness-integration]
---

# MiniMax M3 model page

Scraped 2026-07-12. Official MiniMax model page (Chinese). Confirms M3 identity and capabilities.

## Key facts

- **MiniMax-M3**, model id `MiniMax-M3` in API (`https://api.minimaxi.com/v1/text/chatcompletion_v2`).
- 1M-token context window (≥512K usable). Native multimodal. MiniMax Sparse Attention (MSA) architecture.
- Vendor claims: "frontier coding & agentic capabilities," autonomous task decomposition, tool calling, multi-step reasoning. BrowseComp 83.5 (claims > Opus 4.7 79.3). Demo: 12-hour autonomous ICLR paper reproduction, 147-iteration CUDA kernel optimization (9.4× speedup).
- **Explicit harness integration**: lists Claude Code, Roo Code, Kilo Code, Cline, Codex CLI, **OpenCode**, Droid, TRAE, Grok CLI, Cursor — i.e. the user's harnesses are supported.
- Auto cache, no setup. Token Plan subscription available.

## Pricing (from llm-stats aggregator, not this page)

$0.30/$1.20 per M (in/out) — aggregator-sourced, medium confidence. Not confirmed on this official page (pricing lives on `platform.minimaxi.com/subscribe/token-plan`).

## Why this source matters

M3 is the strongest **price-for-performance** candidate on SWE-bench Verified at 0.805 for $0.30/$1.20 — within 5 points of Claude Sonnet 5 (0.852) at ~1/10 the output price, and it explicitly supports the user's harnesses (OpenCode, Claude Code, Codex). Performance claims are vendor (cap medium).