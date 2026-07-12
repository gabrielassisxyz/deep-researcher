---
type: research-intake
slug: ai-coding-productivity
topic: "Do AI coding agents actually make experienced developers faster?"
status: assumptions-recorded
created: 2026-07-12
updated: 2026-07-12
---

# Intake

## Gate -1: External review setup

Read from `.deep-research.conf`:

- **Research model:** `pi:glm-5.2`
- **Second opinion (Gate 8.4):** `codex` — one independent re-research run.
- **Review panel (Gate 8.5):** `agy codex claude:opus`, 1 loop.
- **Depth budget:** 6 rounds / 40 sources.

User explicitly instructed both external checks to run, and to proceed non-interactively.

## Primary objective

Determine whether AI coding agents produce a **real, measurable** productivity gain for
**experienced developers** working in **codebases they already know**, and — critically —
under what conditions. The user is deciding how far to commit to an AI-agent-centric
workflow and whether to recommend it to others.

## Target decisions

1. Whether to continue investing personal workflow around AI coding agents.
2. Whether to recommend this workflow to other experienced developers.
3. Under what conditions (task type, codebase familiarity, task ambiguity) the gain is
   supported by evidence vs. not.

## Audience

A single experienced developer (Gabriel) who builds with AI agents daily. Also the
colleagues/peers he might recommend the workflow to. Technical, skeptical of vendor
marketing, willing to act on a nuanced answer.

## Use cases

- Daily software development in a familiar codebase using AI coding agents (Cursor,
  Copilot, Claude Code, Codex, etc.).
- Greenfield vs. maintenance work.
- Boilerplate vs. novel logic.
- Well-specified vs. ambiguous tasks.

## Comparison axes

- **Speed** (time-to-completion) — the headline axis.
- **Task type** (greenfield / existing codebase / boilerplate / novel / ambiguous).
- **Developer experience level** (junior vs. senior).
- **Codebase familiarity** (known vs. unknown).
- **Non-speed effects**: defect rate, review burden, code comprehension, maintenance cost.
- **Measured vs. self-reported** divergence (explicitly requested).
- **Source independence**: vendor vs. independent vs. peer-reviewed.

## Confidence threshold

- Vendor performance claims: capped at `medium` (Gate 4.5 rule).
- Independent measured evidence needed for any `high` performance claim.
- Fit claims ("does this make *me* faster"): ceiling `low` from web evidence; must be named
  as unanswerable with a proposed local evaluation.

## Output requirements

- Evidence found AND evidence looked for but not found (both lists required).
- Sources typed honestly: vendor / independent / self-reported / peer-reviewed.
- Decision guide: conditions under which the gain is supported vs. not.
- "What the web cannot settle" section with a concrete local evaluation.
- Full search ledger in `log.md`.

## Exclusions

- "Is AI useful" in the generic sense.
- Product comparisons / which tool is best (unless relevant to the productivity question).
- Marketing literature not making a testable claim.
- The user deliberately did NOT provide candidate studies, papers, or URLs.

## Non-interactive assumptions

Proceeding with assumptions rather than blocking. Key assumptions:

- "Experienced developer" = someone with several years of professional experience, able to
  review code for correctness, not a novice who must trust AI output uncritically.
- "Real work" = tasks that ship, not toy/leetcode benchmarks in isolation (though benchmark
  studies are relevant evidence if they measure experienced devs on realistic tasks).
- "Productivity" = primarily time-to-completion, with defect/quality as secondary axes.
- The user wants the honest answer even if it is "the gains are smaller than claimed" or
  "the evidence does not support a general answer."

## Decision frame

Decide how far to commit to an AI-agent-centric workflow — and whether to recommend it —
based on the conditions under which measured evidence (not self-report) shows a productivity
gain for experienced developers on familiar codebases, weighted by non-speed effects
(defects, review burden, comprehension) and by where measured vs. self-reported speedup
diverge.