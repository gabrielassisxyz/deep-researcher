---
type: model-note
model: GLM-5.2
provider: Z.ai
verified_identifier: GLM-5.2
status: verified-open-weight
updated: 2026-07-04
confidence: high
---

# GLM-5.2

## Evidence Summary

Z.ai's repository verifies GLM-5.2 and GLM-5.2-FP8, with 744B total parameters and 40B active parameters [[sources/zai-glm-5-github]]. The repository positions GLM-5 for complex systems engineering and long-horizon agentic tasks. OpenRouter lists `z-ai/glm-5.2` with a 1M context window and low pricing relative to frontier closed models [[sources/openrouter-models-api]]. BenchLM lists GLM-5.2 as a current open model with strong overall and coding/knowledge category signals, at aggregator confidence [[sources/benchlm]].

## Routing Implication

GLM-5.2 is a candidate cheaper coding and agentic model when open-weight deployment, long context, or cost control matter. Use it for bounded implementation, tool-driven work, and codebase analysis with review gates.

## Caveats

Most detailed capability claims are vendor-authored. Use independent regression tests before assigning it high-stakes planning or final review.
