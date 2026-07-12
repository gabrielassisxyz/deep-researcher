---
type: model-note
model: Kimi K2.7 Code
provider: Moonshot AI
verified_identifier: kimi-k2.7-code
status: verified
updated: 2026-07-06
confidence: high
---

# Kimi K2.7 Code

## Evidence Summary

Kimi verifies `kimi-k2.7-code` and `kimi-k2.7-code-highspeed` in official docs [[sources/kimi-k2-7-code]] [[sources/kimi-model-list]]. The model list gives 256K context [[sources/kimi-model-list]]. Kimi claims the model improves instruction compliance, long-context coding, long-horizon coding success, and agentic capability over K2.6 [[sources/kimi-k2-7-code]]. OpenRouter lists `moonshotai/kimi-k2.7-code` at low cost relative to frontier models [[sources/openrouter-models-api]].

**Multimodal:** Kimi K2.7 Code is **natively multimodal**, accepting image and video input via the MoonViT vision encoder at 256K context, per Ollama Cloud's model library [[sources/ollama-cloud-kimi-k2-7-code]]. This capability was missed in the initial pass, which only consulted Moonshot's `platform.kimi.ai` docs (framed as a coding model). It is material because the Ollama Cloud serving path (`...:cloud`) is what the local LiteLLM proxy routes `kimi-k2.7` through, so vision input is available today without a config change.

## Routing Implication

Kimi K2.7 Code is one of the strongest candidates for "clear spec to implementation" work, especially when tasks are decomposed, tests exist, and a frontier model reviews the plan or final result. The high-speed variant is relevant for iterative coding agents.

## Caveats

Kimi's performance deltas are mostly vendor claims in this pass. Treat it as medium confidence for replacing frontier models on complex work until your own harness validates it.

Multimodal *support* is confirmed, but vision *quality* on dense UI / small-text OCR (game HUDs, item tooltips, cluttered screenshots) is unquantified [[sources/ollama-cloud-kimi-k2-7-code]]. Do not assume strong screenshot-reading accuracy without a task-specific eval; escalate to a stronger multimodal model (e.g. Gemini 3.5 Flash / 3.1 Pro) if item/stat reading proves unreliable.
