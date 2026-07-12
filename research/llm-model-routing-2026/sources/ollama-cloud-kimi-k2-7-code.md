---
type: source
source_type: official-docs
publisher: Ollama (Ollama Cloud model library)
title: Kimi K2.7 Code (Ollama Cloud)
url: https://ollama.com/library/kimi-k2.7-code
accessed: 2026-07-06
confidence: high
---

# Kimi K2.7 Code (Ollama Cloud)

## Summary

Ollama's Cloud model library page for `kimi-k2.7-code` documents the model as
natively multimodal. It states: "Native multimodal: Supports image and video
input via the MoonViT vision encoder, with a 256K token context window."

This is the deployment variant reached through Ollama Cloud (`...:cloud`), which
is the backend used by the local LiteLLM proxy for the `kimi-k2.7` alias
(`openai/kimi-k2.7-code:cloud`, `api_base: https://ollama.com/v1`).

## Claims Used

- Kimi K2.7 Code accepts **image and video input** natively (not text-only).
- The vision path is the **MoonViT** vision encoder.
- Context window is **256K tokens**, consistent with Kimi's own model list.
- The multimodal capability is available on the **Ollama Cloud** serving path.

## Limitations

The page confirms that image/video input is *supported*, but does not quantify
vision quality on dense UI / small-text OCR tasks (e.g. game HUDs, item
tooltips). "Multimodal support exists" should not be read as "strong at reading
cluttered UI screenshots" without an independent, task-specific evaluation.
