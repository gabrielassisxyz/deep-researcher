---
type: model-note
model: Claude Opus 4.8
provider: Anthropic
verified_identifier: claude-opus-4-8
status: verified
updated: 2026-07-04
confidence: high
---

# Claude Opus 4.8

## Evidence Summary

Anthropic recommends Claude Opus 4.8 as the starting point for complex agentic coding and enterprise work when the user is unsure which model to choose [[sources/anthropic-claude-models-overview]]. Pricing is $5 / MTok input, $0.50 / MTok cache hit, and $25 / MTok output [[sources/anthropic-pricing]]. BenchLM places Opus 4.8 among top current models but flags leaderboard evidence as aggregator-level [[sources/benchlm]].

## Routing Implication

Use Opus 4.8 for high-value coding review, architecture, planning, complex agent loops, and ambiguous debugging. It is often a better first frontier choice than Fable 5 when cost matters, because Anthropic positions it directly for agentic coding at half Fable's token price.

## Caveats

Opus 4.8 and later Opus models use a newer tokenizer that may produce more tokens for the same text, so effective cost can be workload-dependent [[sources/anthropic-pricing]].
