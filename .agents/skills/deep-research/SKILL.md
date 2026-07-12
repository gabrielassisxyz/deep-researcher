---
name: deep-research
description: Use when the user asks for deep research, source-backed exploration, benchmark research, or an auditable Markdown research dossier.
---

# Deep Research Dossier

Read `opencode/prompts/deep-research.md` in full and follow it as the controlling workflow.

The primary output must be a focused Markdown dossier under `research/<topic-slug>/`, with local source notes, frontmatter, wikilinks, `evidence.md`, `open-questions.md`, and `log.md`.

If the user provides a target directory, use it exactly. If not, derive a lowercase kebab-case slug from the research topic.

Use optional domain folders only when they fit the research topic. Examples: `models/`, `products/`, `vendors/`, `papers/`, `entities/`, `concepts/`, `datasets/`, or `benchmarks/`. Do not create a folder just because an example mentions it.

Before intake, ask which external checks to run — a **second opinion** (a different model researches the same questions independently; disagreement becomes a gap) and/or a **Gemini review loop** through `agy` (a skeptical critique of the finished dossier). They are complements: the second opinion attacks omission, the review attacks error. Ask before any other interview question. In non-interactive runs, default both to disabled unless the request explicitly enables them.

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

## Depth Is A Loop, Not A Pass

Gates 5 and 6 **cycle**. Classify gaps as high, medium, or low impact; then keep looping —
gap analysis, targeted search, re-analyse — until every high-impact gap is `resolved` or
`blocked`. Those are the only two terminal states.

`partially resolved` is **not** a status. It means the loop goes round again, with whatever
is still missing as the next query. The only other way out is the depth budget in
`research-contract.md` (default 6 rounds / 40 sources) running out — and that must be
declared in the synthesis and the final answer, never quietly assumed.

## Search Before You Scrape

Discovery means calling Firecrawl's **search** tool (`firecrawl_search` under opencode,
`mcp_firecrawl_firecrawl_search` under pi — list your tools and use whichever searches; if
none exists, stop and say so rather than answering from memory).
Scraping a URL the user already named is retrieval: it
confirms the list you were given and never surfaces the option nobody mentioned. Issue at
least 5 distinct queries before scraping, deliberately search for units of analysis the
user did *not* name, and log every query — including the ones that found nothing — in the
`log.md` search ledger. An unlogged query is indistinguishable from a query never run.

## Claim Typing

Before the gap analysis, type every claim that matters (Gate 4.5), because the source that
settles one type is worthless for another:

- **Fact** (it exists, it costs X) — vendor docs settle it. Ceiling `high`.
- **Performance** (A is better than B) — needs independent evidence. **A vendor is not a
  neutral witness about its own product**: official-source performance claims cap at `medium`.
- **Fit** (A is right *for this user*) — **the web cannot settle it at all.** Ceiling `low`.
  Name it as unanswerable and propose the local evaluation that would answer it.

## Depth And Confidence

Do not let standalone domain notes become shallow placeholders. If a decision-critical unit gets a standalone note, cover its status, identifiers or variants, decision-relevant attributes, best evidence, caveats, conflicts, practical implication, and claim-level confidence. If the available evidence is thin, mark the note as `status: stub` or keep the unit in a comparison table instead.

Distinguish source confidence, claim confidence, and recommendation confidence. Official sources can support high-confidence facts about availability, pricing, identifiers, or documented behavior, but recommendations inferred from those facts are usually medium confidence unless direct evidence supports the user's workflow. Aggregator-only claims and vendor-authored performance claims cannot exceed medium confidence unless independently corroborated.

## Gemini Review Loop

When Gemini review is enabled, follow Gate 8.5 from `opencode/prompts/deep-research.md`. Use `agy/prompts/deep-research-review.md` as the reviewer prompt template. The Gemini reviewer should produce a findings report, not rewrite the dossier directly. The main agent owns fixes, false-positive classification, and the final audit.
