---
type: intake
slug: cheap-default-agent-model-2026
topic: "A cheap default model for a coding-agent harness (opencode/pi/Claude Code/Codex via LiteLLM)"
status: decision-ready
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [llm, coding-agent, model-routing, cost, fit]
---

# Intake

## Primary objective

Pick a **cheap default model** for the bulk of coding-agent work — the model that runs
first on any task before escalation — and decide **at what point escalating to a frontier
model actually pays for itself**.

## Target decisions

1. Which model is the **default executor** in the user's agent harnesses.
2. What is the **escalation rule** from the cheap default to a frontier model.
3. What does this actually **cost at the user's volume** vs. a frontier-only baseline.

## Audience

A single developer (Gabriel) running coding agents through **opencode, pi, Claude Code,
and Codex** against a **LiteLLM proxy**. Has a homelab with a single RX 580 GPU; assumes
hosted APIs unless local inference is genuinely viable.

## Use cases / workflow constraints

- Long, multi-file work in a **real repository** — not one-shot benchmark tasks. This is
  the axis the user most distrusts benchmark numbers on.
- Agent loops where **tool calling and instruction adherence are non-negotiable**. A model
  that writes lovely code but cannot reliably call a tool is useless.
- The default runs on **nearly every task**, so price per token dominates.

## Comparison axes

- **Price per token** (dominant axis — budget matters more than ceiling).
- **Long multi-file repo work** quality (the distrusted axis).
- **Tool-calling reliability** (non-negotiable).
- **Instruction adherence** (non-negotiable).
- **Open weights** (a plus, not a requirement).
- **Local inference viability** (only if genuinely viable on an RX 580 — unlikely).
- **Context window** (matters for long repo work).

## Confidence threshold

High for facts (existence, price, context, identifiers). Independent evidence required for
performance claims — **vendor pages do not count as neutral witnesses for quality**. Fit
claims ("right for my work") are explicitly **unanswerable from web research** and must be
named as such, with the local evaluation that would settle them.

## Output preferences

- The **discovered candidate set**, including rejected models with reasons.
- A **routing recommendation**: default executor + escalation rule.
- A **cost model** at the user's volume vs. frontier-only baseline.
- An **explicit statement of what could not be settled** (the fit question), plus the
  experiment the user would have to run to settle it.
- Dossier under `research/cheap-default-agent-model-2026/`.

## Exclusions

- Do not spend time on local inference unless it is genuinely viable on an RX 580.
- No second opinion, no Gemini review (non-interactive run).

## Decision frame

Choose the **cheapest model that is sufficient as a default executor** for the bulk of
agent work, reserving frontier models for cases where evidence shows they materially
improve outcomes — and define the **escalation threshold** at which paying for a frontier
model is justified by the task's difficulty, not by habit.

## External review settings

- Second opinion: **disabled** (user specified non-interactive).
- Gemini review: **disabled** (user specified non-interactive).

## Assumptions (non-interactive run)

- "My volume" is not specified. Assumption: a heavy individual developer — roughly
  **5–15 million tokens/day** across harnesses, mostly input (repo reads) with a
  minority of output. Cost model will be parametric so the user can plug in real numbers.
- "Frontier model" baseline assumed to be a top-tier model in the ~$3–15/M-input,
  ~$15–75/M-output range (e.g. GPT-5-class / Claude Opus-class / Gemini Pro-class). The
  cost model will name the specific frontier reference used.
- Currency: USD, per-million-token pricing as listed by the provider. Cache and batch
  discounts noted where relevant but not assumed by default.
- Date context: 2026-07-12. Model landscape and prices move fast; every price is
  captured with its source and access date.