---
name: deep-research
description: Use when the user asks for deep research, source-backed exploration, benchmark research, or an auditable Markdown research dossier.
---

# Deep Research Dossier

Read `opencode/prompts/deep-research.md` in full and follow it as the controlling workflow.

The primary output must be a focused Markdown dossier under `research/<topic-slug>/`, with local source notes, frontmatter, wikilinks, `evidence.md`, `open-questions.md`, and `log.md`.

If the user provides a target directory, use it exactly. If not, derive a lowercase kebab-case slug from the research topic.

Use optional domain folders only when they fit the research topic. Examples: `models/`, `products/`, `vendors/`, `papers/`, `entities/`, `concepts/`, `datasets/`, or `benchmarks/`. Do not create a folder just because an example mentions it.

Before intake, ask whether the user wants an external Gemini review loop through `agy`, and if yes, ask for the maximum number of loops. Do this before any other interview question. In non-interactive runs, default to no Gemini review unless the request explicitly enables it and provides a maximum loop count.

## Research Intake

Do not treat the topic as the objective. Before research, extract or ask for:

- Primary objective.
- Target decisions.
- Audience.
- Use cases.
- Comparison axes.
- Confidence threshold.
- Output requirements.
- Exclusions.

If the prompt already contains these fields, write them into `intake.md` and continue. If high-impact fields are missing, ask at most 5 concrete questions before starting live research. If running non-interactively, write explicit assumptions in `intake.md` and keep conclusions conservative.

After intake and before live research, write `research-contract.md`. The contract operationalizes the request into objective, decision frame, scope, out-of-scope, key questions, comparison axes, evidence requirements, expected artifacts, success criteria, assumptions, risks, and output directory. Use it as the source of truth for the plan and final audit.

The research contract must also include:

- Coverage plan for decision-critical entities, concepts, products, models, vendors, papers, benchmark families, or other units of analysis.
- Gemini review settings: enabled or disabled, maximum loops, and stop condition.

## Prompt Robustness

The workflow must work even when the user's prompt is imperfect. Convert vague requests into a decision-ready research frame by:

- Restating the decision the research should support.
- Turning broad topics into concrete subquestions.
- Defining comparison axes before searching.
- Naming source quality requirements before trusting claims.
- Separating facts, estimates, inferences, and unknowns.
- Creating a task or use-case taxonomy when the user needs recommendations.
- Producing a decision matrix when the user must choose between tools, models, vendors, or approaches.
- Highlighting when a cheaper or simpler option is sufficient.
- Highlighting when a premium option is justified by evidence.

## Gap Follow-Up

Classify gaps as high, medium, or low impact. If a high-impact gap could change the final decision or synthesis, run at least one targeted follow-up attempt before finalizing. Mark each high-impact gap as `resolved`, `partially resolved`, or `blocked`.

## Depth And Confidence

Do not let standalone domain notes become shallow placeholders. If a decision-critical unit gets a standalone note, cover its status, identifiers or variants, decision-relevant attributes, best evidence, caveats, conflicts, practical implication, and claim-level confidence. If the available evidence is thin, mark the note as `status: stub` or keep the unit in a comparison table instead.

Distinguish source confidence, claim confidence, and recommendation confidence. Official sources can support high-confidence facts about availability, pricing, identifiers, or documented behavior, but recommendations inferred from those facts are usually medium confidence unless direct evidence supports the user's workflow. Aggregator-only claims and vendor-authored performance claims cannot exceed medium confidence unless independently corroborated.

## Gemini Review Loop

When Gemini review is enabled, follow Gate 8.5 from `opencode/prompts/deep-research.md`. Use `agy/prompts/deep-research-review.md` as the reviewer prompt template. The Gemini reviewer should produce a findings report, not rewrite the dossier directly. The main agent owns fixes, false-positive classification, and the final audit.
