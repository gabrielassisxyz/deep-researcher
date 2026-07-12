---
type: model
name: "GLM-5.2"
vendor: "Z.ai (Zhipu)"
status: draft
confidence: medium
last_verified: 2026-07-12
sources: [sources/openlm-glm-5.2, sources/llm-stats-leaderboards]
---

# GLM-5.2

The **open-weight, long-horizon** candidate. **Discovered** via the GLM-5.z.ai blog search. Most relevant to the user's "long, multi-file work in a real repository" axis because its vendor positioning is explicitly long-horizon agent tasks.

## Identity / facts (high confidence)

- 744B-A40B MoE, **1M-token context**, MIT open-source license, "no regional limits." (Source: [[sources/openlm-glm-5.2]])
- Effort control (`reasoning_effort`: `max` default, `high`; `enable_thinking=false`).
- Inference frameworks: SGLang, vLLM, Transformers, KTransformers, Unsloth — i.e. self-hostable, but at 744B it needs a datacenter, not an RX 580.

## Pricing (low–medium confidence)

GLM-5 listed at $1.00/$3.20 per M on llm-stats. **GLM-5.2 price not confirmed** (not on the openlm page). More expensive than DeepSeek V4-Flash and MiniMax M3. (Source: [[sources/llm-stats-leaderboards]])

## Performance (medium confidence, vendor)

- **Terminal-Bench 2.1: 81.0** (vendor) vs Claude Opus 4.8 85.0, GLM-5.1 62.0 — "within a few points of Claude Opus 4.8." (Source: [[sources/openlm-glm-5.2]])
- SWE-bench Pro: 62.1 (vendor). (Source: [[sources/openlm-glm-5.2]])

## Decision-relevant caveats

- Price unconfirmed and likely higher than the two leaders.
- Terminal-Bench numbers are vendor-reported.
- Open weights are a plus per the user's contract, but unusable on an RX 580.

## Practical implication

GLM-5.2 is the strongest **long-horizon** story and the only open-weight option near frontier on Terminal-Bench. For a *cheap default* it is likely too expensive per token and its price is unconfirmed. Better as a considered alternative or a long-horizon escalation target than the daily default. Keep on the watchlist; not the recommendation.