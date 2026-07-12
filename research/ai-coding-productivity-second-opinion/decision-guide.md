---
type: decision-guide
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, decision-guide]
---

# Decision Guide

## When The Gain Is Supported

Expect measurable gains when most of these are true:

- The task is **well-specified** and has clear acceptance tests.
- The work is **implementation-heavy**: boilerplate, glue code, simple CRUD, docs, tests, examples, migrations, or mechanical refactors.
- The developer is **less experienced**, newer to the stack, or spends meaningful time searching for syntax/API examples.
- The code path is **low-risk** and easy to review.
- The team measures **end-to-end delivery**, not just generated lines or first-draft speed.

Evidence basis: [[sources/peng-github-copilot-controlled-experiment]], [[sources/cui-high-skilled-work-field-experiments]], [[sources/stray-nav-copilot-longitudinal]].

## When The Gain Is Not Supported

Do not assume measurable gains when most of these are true:

- The developer is **senior, long-tenured, or deeply familiar** with the codebase.
- The task is **ambiguous**, architecture-heavy, or requires debugging subtle behavior.
- The codebase is mature, large, and has high quality standards.
- Review and integration dominate implementation time.
- The team already has strong internal libraries, tests, and developer tooling.
- AI output increases PR size, duplicated code, or review burden.

Evidence basis: [[sources/metr-early-2025-rct]], [[sources/cui-high-skilled-work-field-experiments]], [[sources/xu-maintenance-burden-2025]], [[sources/gitclear-code-quality-2025]], [[sources/uplevel-copilot-quantitative-study]].

## Decision Matrix

| Work type | Evidence-supported expectation | Use AI? | Measurement priority |
| --- | --- | --- | --- |
| Boilerplate and scaffolding | Likely faster | Yes | Review time, defects, duplication |
| Short greenfield implementation | Likely faster | Yes | Completion time and correctness |
| Tests and docs | Plausibly faster | Yes, with review | Accuracy and maintainability |
| Familiar-codebase bug fix | Uncertain | Trial only | Active time, test pass rate, regression defects |
| Mature-codebase feature | Uncertain to negative | Trial only | End-to-end cycle time, PR review cycles |
| Ambiguous design/debugging | Not established | Use as assistant, not delegate | Decision quality and rework |
| Large PR generation | Risky | Avoid without strict review | PR size, reviewer burden, post-merge defects |
| Junior onboarding | Short-term speed possible; learning risk | Use explanation-first | Comprehension checks |

## Adoption Rule

Adopt AI coding tools as a **measured workflow change**, not as a blanket productivity assumption.

Minimum rollout:

- Baseline current cycle time, review cycles, defect rate, PR size, and developer self-report for four weeks.
- Run an AI-allowed versus AI-limited trial for comparable tasks.
- Separate senior and junior developers in analysis.
- Separate familiar and unfamiliar codebases.
- Count review and rework time as part of the task.
- Stop using line count, commit count, or accepted suggestion count as primary ROI metrics.

## Local Evaluation That Would Settle It

Run a randomized local study:

- 20 to 40 real backlog tasks.
- Stratify by task type and risk.
- Randomize AI access by task or developer-week.
- Record expected speedup before work and perceived speedup after work.
- Measure active human time, wall-clock time, agent waiting time, review cycles, defects, PR size, and two-to-four-week rework.
- Require predeclared acceptance tests or reviewer acceptance criteria.
- Analyze the experienced/familiar-codebase slice separately.

This is the only way to answer the fit question for a specific team.
