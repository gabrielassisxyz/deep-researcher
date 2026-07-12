---
type: model-note
model: Claude Sonnet 4.6
provider: Anthropic
verified_identifier: claude-sonnet-4-6
status: verified-superseded
updated: 2026-07-04
confidence: high
---

# Claude Sonnet 4.6

## Evidence Summary

Anthropic's docs reference Claude Sonnet 4.6 in pricing and later-model platform support contexts [[sources/anthropic-pricing]] [[sources/anthropic-claude-models-overview]]. Pricing is $3 / MTok input, $0.30 / MTok cache hit, and $15 / MTok output [[sources/anthropic-pricing]]. OpenRouter lists `anthropic/claude-sonnet-4.6` with 1M context [[sources/openrouter-models-api]].

## Routing Implication

Use Sonnet 4.6 only when an integration is pinned to it or when its observed behavior is already validated in a workflow. Sonnet 5 has better current positioning and introductory pricing, so Sonnet 4.6 is not the preferred new-routing choice.

## Caveats

Some sources may list older context or benchmark assumptions for Sonnet 4.6. Recheck exact provider context and pricing before using it for a new long-context workflow.
