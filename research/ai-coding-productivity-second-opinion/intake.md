---
type: intake
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, evidence-review, second-opinion]
---

# Intake

## User Prompt

The user asks whether AI coding agents actually make experienced developers measurably faster on real work in a codebase they already know. The prompt explicitly excludes generic usefulness and asks for controlled or measured evidence, evidence contradicting popular speedup claims, and evidence where self-reported speedup diverges from measured speedup.

Required slug: `ai-coding-productivity-second-opinion`.

This run is an independent Gate 8.4 second opinion. It must not read the primary run in `research/ai-coding-productivity/`.

## Extracted Objective

Assess what evidence supports, weakens, or fails to support the claim that AI coding agents measurably speed up experienced developers doing real work in familiar existing codebases.

## Decision Frame

Decide when it is evidence-supported to expect productivity gains from AI coding agents, when the evidence does not support that expectation, and what local evaluation would settle the question for a specific team or codebase.

## Target Judgments

- Whether controlled or measured studies show faster delivery for experienced developers.
- Whether results differ by task type, developer experience, and codebase familiarity.
- Whether subjective productivity impressions diverge from measured productivity.
- What trade-offs appear in defects, review burden, comprehension, and maintenance cost.
- What remains unanswerable without a local evaluation.

## Audience

An experienced developer or technical decision-maker who wants a sober, source-backed answer, not vendor marketing.

## Use Cases

- Deciding whether to adopt or expand AI coding agents for experienced developers.
- Designing a local trial that measures real workflow impact.
- Interpreting vendor claims, surveys, lab studies, field experiments, and peer-reviewed papers.

## Comparison Axes

- Measured speed or throughput.
- Task type: greenfield, existing codebase, boilerplate, novel logic, bug fixing, ambiguous tasks, well-specified tasks.
- Population: student, novice, professional, experienced developer, open-source maintainer.
- Codebase familiarity: known codebase, unfamiliar codebase, toy task, real repository.
- Non-speed outcomes: defects, review burden, maintainability, comprehension, security, code quality.
- Evidence type and independence.

## Confidence Threshold

Claims that influence the answer need controlled experiments, instrumented field studies, repository/process metrics, or well-described benchmark methodology. Vendor-authored performance claims are capped at medium confidence unless independently corroborated. Self-reported productivity alone is evidence about perception, not measured speed.

## External Check Settings

`.deep-research.conf` was present. It lists `RESEARCH_MODEL="pi:glm-5.2"`, `SECOND_OPINION="codex"`, `REVIEW_PANEL="agy codex claude:opus"`, `REVIEW_LOOPS="1"`, `MAX_ROUNDS="6"`, and `MAX_SOURCES="40"`.

This run is the configured Codex Gate 8.4 second opinion. No recursive second opinion will be run. Because the user requested an independent second-opinion run and did not ask for review-panel execution of that second-opinion dossier, review-panel execution is recorded as disabled for this run unless explicitly invoked later.

## Assumptions

- "AI coding agents" includes coding assistants and agentic coding tools when they materially generate, edit, or guide code. The evidence base often studies GitHub Copilot or assistant-style tools rather than fully autonomous agents, so the synthesis must distinguish them.
- "Experienced developer" means professional or high-skill developers, not students or novices.
- "Measurably faster" means measured task completion time, throughput, cycle time, PR delivery metrics, or experimentally observed completion, not self-reported speed.
- "Real work in a codebase they already know" is the strictest target condition. Evidence from toy tasks, unfamiliar repositories, and student subjects is relevant only as indirect evidence.
- The run is non-interactive, so missing preferences are handled conservatively.

## Exclusions

- No reliance on the primary run's sources, findings, or synthesis.
- No unsourced claims from memory.
- No treating vendor marketing, surveys, or testimonials as measured productivity evidence.
