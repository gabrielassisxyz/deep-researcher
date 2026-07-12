---
type: methodology
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, methodology]
---

# Methodology

## Search Strategy

This was an independent second-opinion run. It did not read `research/ai-coding-productivity/`.

Discovery began with Firecrawl search, as required by the workflow. Firecrawl returned one highly relevant METR source but performed poorly on several GitHub/Copilot and self-report queries, returning generic homepages or dictionary pages. Because the search tool was available but low-recall for this topic, additional web search was used as a fallback and every query is recorded in [[log]].

Searches deliberately targeted:

- Controlled and randomized studies.
- Experienced developers and familiar repositories.
- Field experiments in companies.
- Self-report versus measured-output divergence.
- Negative, null, and contradictory evidence.
- Non-speed costs: bugs, review, comprehension, maintainability, coordination, and delivery stability.

## Source Typing

- **Independent / nonprofit**: METR task-level experiments and updates.
- **Vendor-authored or vendor-affiliated**: GitHub/Microsoft/Copilot studies, Anthropic study, Uplevel, GitClear, DORA/Google Cloud.
- **Self-reported**: DORA individual productivity, BNY Mellon survey/interviews, NAV interviews, METR self-report survey context.
- **Measured but not controlled**: NAV commit metrics, GitClear code-operation metrics, OSS observational studies.
- **Peer-reviewed**: no peer-reviewed controlled trial was found that exactly matches experienced developers doing familiar-codebase work. Several sources are arXiv preprints or working papers.

## Claim Typing Rules

- **Performance claims** require measured or controlled evidence. Vendor-authored performance claims are capped at medium confidence.
- **Self-report claims** are evidence about perception, not measured speed.
- **Fit claims** about a specific developer, team, or repository cannot be settled by web evidence.

## Interpretation Rules

Task-completion speed, PR throughput, commit activity, code quality, review burden, and perceived productivity are treated as different outcomes. They are not collapsed into one productivity number.

Greenfield toy or short tasks are not treated as evidence for mature familiar-codebase work unless explicitly labeled as indirect evidence.

## Evidence Limits

The literature is moving quickly. Some 2025 evidence is already partly stale for 2026 agentic tools. Conversely, the newest 2026 evidence is often survey-based, observational, or methodologically unsettled.
