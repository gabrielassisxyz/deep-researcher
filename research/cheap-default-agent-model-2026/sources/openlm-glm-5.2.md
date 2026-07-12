---
type: source
source_type: official
title: "GLM-5.2 — Built for Long-Horizon Tasks (OpenLM.ai)"
publisher: "Z.ai (OpenLM.ai)"
url: "https://openlm.ai/glm-5.2/"
author: "GLM-5 Team"
published: 2026-06-13
accessed: 2026-07-12
confidence: high
used_for: [glm-5.2-identity, terminal-bench-scores, long-horizon-claims, open-weights]
---

# GLM-5.2 (OpenLM.ai)

Scraped 2026-07-12. Official Z.ai / OpenLM page for GLM-5.2.

## Key facts

- **GLM-5.2**: 744B-A40B (MoE), **1M-token context**, MIT open-source license, "no regional limits."
- Benchmark claims (vendor): **Terminal-Bench 2.1 = 81.0** (vs Claude Opus 4.8 = 85.0, vs GLM-5.1 = 62.0); **SWE-bench Pro = 62.1** (vs GLM-5.1 = 58.4).
- "Effort level control" (`reasoning_effort`: `max` default, `high`). Thinking off via `enable_thinking=false`.
- Inference frameworks: SGLang, vLLM, Transformers, KTransformers, Unsloth.
- GLM-5 = 744B params (40B active), 28.5T pretraining tokens, integrates DeepSeek Sparse Attention.

## Why this source matters

GLM-5.2 is a **discovered** candidate the user did not name — an open-weight, 1M-context, long-horizon-optimized model whose vendor claims put it within a few points of Claude Opus 4.8 on Terminal-Bench 2.1 (the long-horizon agent benchmark most relevant to the user's axis). Pricing not on this page; GLM-5 listed at $1.00/$3.20 on llm-stats. Performance claims are vendor (cap medium). Identity/context/open-weights facts are high.