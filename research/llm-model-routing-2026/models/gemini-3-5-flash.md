---
type: model-note
model: Gemini 3.5 Flash
provider: Google
verified_identifier: gemini-3.5-flash
status: verified
updated: 2026-07-04
confidence: high
---

# Gemini 3.5 Flash

## Evidence Summary

Google lists `gemini-3.5-flash` as a stable Gemini model [[sources/google-gemini-models]]. OpenRouter lists 1M context and $1.50 / MTok prompt, $9 / MTok completion pricing [[sources/openrouter-models-api]]. BenchLM reports Gemini 3.5 Flash as a current model with strong speed, including 284.2 tokens/sec and 18.55s latency, and an overall score below the top frontier models but high for a Flash-tier model [[sources/benchlm]].

## Routing Implication

Use Gemini 3.5 Flash for high-volume research assistance, summarization, documentation, structured extraction, and implementation tasks where speed matters and errors are checked by tests or review. Escalate to Gemini 3.1 Pro or another frontier model for ambiguous planning, high-stakes synthesis, or final review.

## Caveats

Official numeric pricing extraction was incomplete in this pass, so exact procurement pricing should be rechecked with Google before budget commitments.
