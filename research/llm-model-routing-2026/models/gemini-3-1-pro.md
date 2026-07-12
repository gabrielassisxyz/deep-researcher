---
type: model-note
model: Gemini 3.1 Pro
provider: Google
verified_identifier: gemini-3.1-pro-preview
status: verified-preview
updated: 2026-07-04
confidence: high
---

# Gemini 3.1 Pro

## Evidence Summary

Google lists `gemini-3.1-pro-preview` as a preview model for advanced intelligence, complex problem solving, agentic capabilities, and coding [[sources/google-gemini-models]]. Official pricing for Gemini 3.1 Pro Preview is $2 / MTok input and $12 / MTok output up to 200K tokens, then $4 / MTok input and $18 / MTok output above 200K tokens [[sources/google-gemini-pricing]]. OpenRouter lists a 1M context entry [[sources/openrouter-models-api]]. BenchLM ranks Gemini 3.1 Pro near the top, with strong overall, reasoning, and coding signals at medium confidence [[sources/benchlm]].

## Routing Implication

Gemini 3.1 Pro is a strong frontier choice for general research, multimodal-heavy work, long-context synthesis, and cost-sensitive frontier reasoning. Its preview status makes it less conservative than stable models for production-critical deterministic pipelines.

## Caveats

The exact verified identifier is preview. For production routing, require periodic regression checks and fallback to a stable model.
