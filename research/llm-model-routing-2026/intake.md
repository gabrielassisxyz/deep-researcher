---
type: intake
status: complete
updated: 2026-07-04
confidence: medium
---

# Research Intake

## Primary Objective

Collect reliable, source-backed evidence for deciding which LLM model tier to use for each AI coding and research workflow task, with special attention to when a cheaper model is sufficient and when a frontier model is worth the extra cost.

## Decision Frame

Choose the cheapest model that is sufficiently reliable for each task class, while reserving frontier models for ambiguous planning, architecture trade-offs, difficult decomposition, high-stakes review, long-context synthesis, multimodal work, or escalation cases where evidence shows a material quality gain.

## Target Decisions

- When to use a frontier model such as Fable, Opus 4.8, GPT-5.5, Sonnet 5, or Gemini 3.1 Pro.
- When to use a cheaper model such as Kimi K2.7-Code, GLM-5.2, Qwen 3.5, MiniMax, Gemma, or DeepSeek.
- Which models or model tiers fit planning, brainstorming, task decomposition, spec writing, implementation from a clear spec, debugging, refactoring, code review, long-context analysis, documentation work, multimodal work, and general research.
- Where a frontier model materially improves outcomes.
- Where the marginal gain of a frontier model is likely too small to justify the cost.

## Audience

Technical decision-maker or engineering lead routing coding and research tasks across LLMs. The reader can understand benchmarks, API pricing, latency, context windows, and model identifiers.

## Models In Scope

- GPT 5.5
- Opus 4.8
- Sonnet 4.6
- Sonnet 5
- Gemini 3.1 Pro
- Gemini 3.5 Flash
- GLM-5.2
- Kimi K2.7-Code
- Gemma4
- Qwen3.5 / Qwen 3.5
- Minimax-m2.7
- Minimax-m3
- Deepseek v4 Pro
- Deepseek v4 flash
- Fable, because it appears in the user's target decisions even though it was not in the main model list

## Use Cases

- Ambiguous planning and brainstorming.
- Architecture trade-off analysis.
- Task decomposition.
- Specification writing.
- Implementation from a clear specification.
- Debugging.
- Refactoring.
- Code review.
- Long-context repository or document analysis.
- Documentation work.
- Multimodal work.
- General research and source synthesis.
- Review, judging, and escalation after cheaper-model implementation.

## Comparison Axes

| Axis | Why it matters | Priority |
| --- | --- | --- |
| Task quality evidence | The routing decision must be tied to task evidence, not only a generic leaderboard rank. | high |
| Pricing | The core decision is cost-performance routing. | high |
| Latency and throughput | Cheaper or smaller models may be better when fast iteration matters. | high |
| Context window | Long-context analysis and documentation workflows can fail if the model cannot ingest enough context. | high |
| Coding benchmark evidence | Several target tasks are coding-focused. | high |
| Reasoning and agentic evidence | Planning, decomposition, debugging, and review depend on reasoning beyond syntax generation. | high |
| Multimodal capability | Required for multimodal work routing. | medium |
| Availability and exact model identifier | Nonexistent or renamed models cannot be routed reliably. | high |
| License and deployment constraints | Open-weight or self-hostable models may matter for private code or cost control. | medium |
| Benchmark methodology | Benchmark claims need contamination, metric, date, and model identifier caveats. | high |

## Confidence Threshold

- `high`: a claim is supported by a directly relevant primary source, or by multiple strong sources with compatible methodology and exact model identifiers.
- `medium`: a claim is supported by one reputable aggregator, benchmark, or third-party evaluation, or by a primary source that is indirect for the decision.
- `low`: a claim is supported only by commentary, social posts, stale data, unclear model identifiers, or inference from adjacent models.
- Aggregator-only evidence must not be marked higher than `medium`, even when the aggregator appears reliable.
- A model name that cannot be verified as an exact public model identifier must be treated as an unknown or alias candidate.

## Output Requirements

- A source-backed research dossier in Markdown.
- One note per important model.
- Source notes for every source used in synthesis, decision guide, or evidence ledger.
- An evidence ledger with claim-level citations.
- A task taxonomy for AI coding and research workflows.
- A model routing matrix: task type to recommended model tier, candidate models, confidence, and evidence.
- A "cheaper model is sufficient" analysis.
- A "frontier model is justified" analysis.
- A review and escalation policy.
- A cost-performance discussion using pricing, latency, context window, throughput, and benchmark/task evidence when available.
- A clear list of unknowns where evidence is too weak to decide.

## Source Priorities

1. Official model cards, system cards, release notes, API docs, pricing pages, and repositories.
2. Independent benchmark leaderboards and benchmark methodology pages.
3. Reproducible public evaluations, papers, and credible third-party test suites.
4. Aggregators for pricing, availability, context window, throughput, and benchmark cross-reference.
5. Commentary only as a lead or low-confidence context.

## Assumptions

- The research should be current as of 2026-07-04.
- The exact model names in the prompt may include unreleased models, private aliases, future names, or spelling variants. The dossier will separate verified public model identifiers from unverified names.
- The task is decision-oriented, so `decision-guide.md` is required.
- The research should prioritize practical routing over a single global ranking.
- The accidental mixed-language fragment in the prompt is treated as workflow guidance: use a generic core dossier, optional domain folders, proportional source notes, strict confidence, and an objective-level final audit.

## Exclusions

- No recommendation will rely on unsourced social commentary.
- No model will be treated as available merely because a similarly named model exists.
- No benchmark score will be generalized to a task type without caveats about the benchmark's scope and method.
