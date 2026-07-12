---
type: research-contract
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, research-contract, second-opinion]
---

# Research Contract

## Research Objective

Determine what controlled or measured evidence exists about whether AI coding agents make experienced developers measurably faster on real work in codebases they already know, and state where the evidence supports, contradicts, or cannot answer that claim.

## Evaluation Frame

The core claim is a performance-and-fit claim. The web can help evaluate general measured effects under studied conditions, but it cannot settle expected impact for a specific developer, team, or repository without a local evaluation.

## Target Judgments

- Whether measured speed gains exist for experienced developers.
- Whether gains hold in existing, familiar codebases rather than greenfield or toy settings.
- Whether measured results diverge from self-reported productivity.
- Whether non-speed outcomes create hidden costs.
- Which local evaluation would settle the question for a given team.

## Scope

Included:

- Controlled experiments, randomized trials, quasi-experiments, field experiments, observational telemetry studies, and repository/process metric studies.
- Peer-reviewed or working papers, independent research labs, company field studies with disclosed methods, and vendor studies treated with source-appropriate skepticism.
- Evidence about assistants and agents when relevant to coding productivity.
- Contradictory evidence and negative findings.

Out of scope:

- Pure opinion pieces, surveys without measured outcomes, testimonials, and adoption statistics except as context.
- Pricing or feature comparison of coding-agent products.
- The primary dossier in `research/ai-coding-productivity/`.

## Key Research Questions

1. What controlled or measured evidence exists, excluding pure self-report?
2. What does the best evidence say about experienced developers specifically?
3. What evidence targets existing codebases and codebases already familiar to the developer?
4. How do results vary by task type and task ambiguity?
5. Where do self-reported speedups diverge from measured speedups?
6. What non-speed effects appear in defects, review burden, comprehension, maintenance, security, or code quality?
7. Why do conflicting studies conflict?
8. What evidence was searched for but not found?
9. What local evaluation would settle the user-specific question?

## Evidence Requirements

Source priority:

1. Peer-reviewed papers or preprints with transparent methods and data.
2. Independent controlled studies or field experiments.
3. Company-authored field experiments with disclosed methods, typed honestly as vendor-authored or employer-authored.
4. Instrumented observational studies and repository-metric analyses.
5. Surveys only for perception gaps, never as direct measured-speed evidence.
6. Vendor marketing only for vendor claims, not for high-confidence performance conclusions.

Claim typing:

- Fact claims can be supported by primary or official sources.
- Performance claims require controlled or measured evidence. Vendor-authored performance claims are capped at medium confidence.
- Fit claims about a specific developer/team/codebase are low confidence from web evidence alone and require local evaluation.

## Coverage Plan

Search for at least these evidence families from scratch:

- Randomized or controlled Copilot studies.
- Field experiments in companies or repositories.
- METR or similar real-task studies on experienced developers.
- Studies contrasting self-reported and measured productivity.
- DORA/DevOps Research and Assessment or similar reports with organizational metrics.
- Code quality, maintainability, review, and security studies.
- Contradictory or null-result papers.
- Evidence about codebase familiarity and existing-code tasks.

## Expected Artifacts

- `README.md`
- `intake.md`
- `research-contract.md`
- `methodology.md`
- `evidence.md`
- `synthesis.md`
- `decision-guide.md`
- `open-questions.md`
- `log.md`
- `sources/` with one note per major source

## Success Criteria

- At least 5 distinct Firecrawl discovery queries before any source extraction.
- Every kept source traces to the search ledger or a citation trail.
- Every major claim cites local source notes.
- Contradictory evidence is included, not buried.
- Self-report and measured-speed evidence are explicitly separated.
- High-impact gaps are marked exactly `resolved` or `blocked`, or the dossier declares budget exhaustion.

## Depth Budget

Maximum 6 follow-up rounds or 40 kept sources, whichever comes first. The target is not to spend the full budget; it is to close or block all high-impact gaps.

## Review Settings

This run is the independent Gate 8.4 second-opinion run requested by the user. A recursive second opinion is disabled.

Gemini/review-panel loop: disabled for this second-opinion run unless explicitly invoked later. The final dossier must say it was not review-panel checked.

## Risks And Ambiguities

- Much evidence studies assistants such as GitHub Copilot rather than fully autonomous coding agents.
- Many studies use students, short tasks, or unfamiliar repositories, limiting transfer to experienced developers in known codebases.
- Company telemetry may be realistic but confounded.
- Self-reported speedup can diverge from measured outcomes and should be treated as a separate construct.
- Published evidence may lag current tool capabilities.

## Output Directory

`research/ai-coding-productivity-second-opinion/`
