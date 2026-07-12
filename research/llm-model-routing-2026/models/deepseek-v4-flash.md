---
type: model-note
model: DeepSeek V4 Flash
provider: DeepSeek
verified_identifier: deepseek-v4-flash
status: verified
updated: 2026-07-04
confidence: high
---

# DeepSeek V4 Flash

## Evidence Summary

DeepSeek's official API docs verify `deepseek-v4-flash` with 1M context, 384K max output, thinking and non-thinking modes, JSON output, tool calls, and extremely low prices: $0.0028 / MTok cache-hit input, $0.14 / MTok cache-miss input, and $0.28 / MTok output [[sources/deepseek-pricing]]. The same page says legacy `deepseek-chat` and `deepseek-reasoner` names map to non-thinking and thinking modes of `deepseek-v4-flash` until deprecation on 2026-07-24 15:59 UTC [[sources/deepseek-pricing]].

## Routing Implication

DeepSeek V4 Flash is the cheapest verified broad-use candidate in this dossier. Use it for high-volume extraction, draft implementation, mechanical refactors, documentation passes, and first-pass research triage. Escalate aggressively for ambiguous design, security-sensitive changes, or failures under test.

## Caveats

Low price does not prove reliability. Use deterministic checks, tests, and reviewer escalation.
