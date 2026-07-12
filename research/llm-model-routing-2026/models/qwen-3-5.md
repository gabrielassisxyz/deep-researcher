---
type: model-note
model: Qwen3.5 / Qwen 3.5
provider: Alibaba Qwen
verified_identifier: multiple OpenRouter Qwen3.5 entries
status: partially-verified
updated: 2026-07-04
confidence: medium
---

# Qwen3.5 / Qwen 3.5

## Evidence Summary

The official Qwen3 repository verifies Qwen3 and Qwen3-2507 families, but this pass did not find an official Qwen source verifying a single exact `Qwen3.5` release name [[sources/qwen3-github]]. OpenRouter lists several Qwen3.5 entries, including `qwen/qwen3.5-plus-20260420`, `qwen/qwen3.5-9b`, `qwen/qwen3.5-35b-a3b`, `qwen/qwen3.5-27b`, `qwen/qwen3.5-122b-a10b`, `qwen/qwen3.5-flash-02-23`, and `qwen/qwen3.5-397b-a17b` [[sources/openrouter-models-api]].

## Routing Implication

Treat Qwen3.5 as a family of available aggregator-routed models rather than one verified first-party model. For coding work, prefer exact, verified Qwen3-Coder or Qwen3-2507 variants when the integration supports them, or require a smoke-test harness before production routing.

## Caveats

Confidence is medium because the exact requested model name is corroborated by OpenRouter but not by an official Qwen source in this pass.
