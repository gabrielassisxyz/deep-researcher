---
type: dossier-index
status: complete
updated: 2026-07-04
confidence: medium
---

# LLM Model Routing Research Dossier

## Purpose

This dossier collects evidence for routing AI coding and research work to the cheapest sufficiently reliable model tier, while reserving frontier models for tasks where evidence supports a material quality gain.

## Key Files

- [[intake]]: research objective, scope, confidence rules, and success criteria.
- [[methodology]]: search plan, source tiers, and interpretation rules.
- [[synthesis]]: main findings and hypothesis assessment.
- [[decision-guide]]: task taxonomy, routing matrix, cheaper-model analysis, frontier-justified analysis, and escalation policy.
- [[evidence]]: claim-level evidence ledger.
- [[open-questions]]: unresolved gaps and follow-up status.
- [[log]]: research activity log.
- [[models/gpt-5-5]], [[models/claude-fable-5]], [[models/claude-opus-4-8]], [[models/claude-sonnet-5]], [[models/claude-sonnet-4-6]], [[models/gemini-3-1-pro]], [[models/gemini-3-5-flash]], [[models/glm-5-2]], [[models/kimi-k2-7-code]], [[models/gemma-4]], [[models/qwen-3-5]], [[models/minimax-m2-7]], [[models/minimax-m3]], [[models/deepseek-v4-pro]], [[models/deepseek-v4-flash]]: model notes.
- `sources/`: local source notes for every source cited in the synthesis, decision guide, or evidence ledger.

## Bottom Line

The working hypothesis is mostly supported: use frontier models for ambiguous planning, architecture trade-offs, hard decomposition, high-stakes review, difficult synthesis, and escalation; use cheaper specialist models for bounded implementation, mechanical refactoring, documentation, extraction, and high-volume drafts when tests or reviewer gates exist.

The important refinement is that "cheaper" is not the same as "weak." DeepSeek V4 Pro/Flash, Kimi K2.7 Code, MiniMax M3, GLM-5.2, Gemma 4, and Qwen3.5-family entries can be cost-effective specialists, but several rely on vendor or aggregator evidence and should be validated against local task harnesses before replacing a frontier model on high-stakes work.
