---
type: model-note
model: MiniMax M3
provider: MiniMax
verified_identifier: MiniMax-M3
status: verified
updated: 2026-07-04
confidence: high
---

# MiniMax M3

## Evidence Summary

MiniMax verifies M3 as a coding and agentic model with 1M context and native multimodality [[sources/minimax-m3-official]]. The model page says the API supports up to 1M tokens with a 512K guaranteed minimum and claims strong coding, browsing, paper reproduction, and long-horizon autonomous optimization examples [[sources/minimax-m3-official]]. The GitHub repository describes M3 as native multimodal with 428B total parameters and 23B active parameters [[sources/minimax-m3-github]]. OpenRouter lists `minimax/minimax-m3` with about 1M context and low token prices [[sources/openrouter-models-api]].

## Routing Implication

MiniMax M3 is a strong candidate for cheap long-context coding, agentic implementation, multimodal document/code analysis, and high-volume agent fleets. Use frontier escalation for ambiguous design and high-stakes final review until independent evals corroborate the vendor claims.

## Caveats

The best performance examples are vendor-provided. Treat M3 as promising but validate with project-specific coding/review tests.
