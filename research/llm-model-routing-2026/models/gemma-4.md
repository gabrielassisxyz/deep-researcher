---
type: model-note
model: Gemma 4
provider: Google
verified_identifier: Gemma 4 family
status: verified-open-model
updated: 2026-07-04
confidence: high
---

# Gemma 4

## Evidence Summary

Google's Gemma 4 model cards describe an Apache 2.0 open model family with E2B, E4B, 26B A4B, and 31B variants [[sources/gemma-4-huggingface]]. The family supports text and image input, text output, audio on smaller models, 128K to 256K context, thinking, function calling, coding, and multimodal tasks [[sources/gemma-4-huggingface]]. Vendor benchmark tables report strong LiveCodeBench v6, MMLU Pro, GPQA Diamond, and vision scores for the 31B and 26B A4B variants [[sources/gemma-4-huggingface]]. OpenRouter lists Gemma 4 API entries with 262K context and very low pricing [[sources/openrouter-models-api]].

## Routing Implication

Gemma 4 is best for local or low-cost execution, privacy-sensitive workloads, on-device/edge experiments, bulk documentation, extraction, and bounded coding where deployment control matters more than maximum frontier quality. Use frontier review for ambiguous architecture or high-stakes code.

## Caveats

The model-card benchmark scores are publisher claims. OpenRouter availability is aggregator evidence.
