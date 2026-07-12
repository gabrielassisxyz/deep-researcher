---
type: research-contract
slug: ai-coding-productivity
status: active
created: 2026-07-12
updated: 2026-07-12
budget_rounds: 6
budget_sources: 40
second_opinion: codex
review_panel: "agy codex claude:opus"
review_loops: 1
---

# Research Contract

## Research objective

Determine whether AI coding agents produce a real, measurable productivity gain for
experienced developers working in codebases they already know, and characterize the
conditions under which the gain holds or fails. Produce an auditable dossier that supports a
personal-commitment and recommendation decision.

## Decision frame

Decide how far to commit to an AI-agent-centric workflow — and whether to recommend it —
based on the conditions under which **measured** evidence (not self-report) shows a
productivity gain for experienced developers on familiar codebases, weighted by non-speed
effects (defects, review burden, comprehension) and by where measured vs. self-reported
speedup diverge.

## Target decisions / judgments

1. Continue / deepen / pull back from an AI-agent-centric personal workflow.
2. Recommend (or not) to other experienced developers, and with what caveats.
3. A condition map: task type × codebase familiarity × experience level → supported / not.

## Audience and intended use

Gabriel (experienced developer, daily AI-agent user) and peers he may advise. Technical,
skeptical of vendor numbers.

## Scope

- IN: Controlled studies, RCTs, quasi-experiments, measured-productivity studies, and large
  surveys on AI coding assistants/agents and developer productivity, especially for
  experienced/senior developers and existing/familiar codebases. Non-speed effects (defects,
  review burden, comprehension, maintenance). Measured-vs-self-reported divergence.
- OUT: Generic "is AI useful" commentary; pure tool feature comparisons; non-coding AI
  productivity; marketing without a testable claim; pure vibe checks with no methodology.

## Key research questions

1. What **controlled or measured** evidence exists (RCTs, experiments, quasi-experiments,
   instrumentation) on AI coding agents/assistants and developer speed?
2. Does the effect differ by **task type** (greenfield vs. existing codebase, boilerplate vs.
   novel logic, well-specified vs. ambiguous)?
3. Does it differ by **developer experience level** and by **codebase familiarity**?
4. Where evidence conflicts, **why** (methods, populations, tasks, measurement)?
5. What is the effect on **non-speed outcomes**: defect rate, review burden, code
   comprehension, maintenance cost?
6. Does **self-reported** speedup diverge from **measured** speedup, and by how much?

## Comparison axes / evaluation criteria

- Magnitude of measured speedup (and sign — can be negative).
- Population: junior vs. senior/experienced.
- Codebase familiarity: novel vs. known.
- Task type: greenfield / maintenance / boilerplate / novel logic / ambiguous.
- Source independence: vendor / independent / peer-reviewed / self-reported survey.
- Non-speed effects (defects, review, comprehension, maintenance).
- Recency (tooling changes fast).

## Evidence requirements and source priority

Priority order:
1. Peer-reviewed RCTs/experiments (highest).
2. Independent (non-vendor) measured studies with stated methodology.
3. Independent surveys with measured/behavioral components.
4. Vendor-published studies (fact source about their own product; performance capped at
   `medium`).
5. Self-reported surveys (evidence of perception, not of effect).
6. Commentary / blog / social (low; contextual only).

Vendor performance claims cannot exceed `medium` confidence without independent
corroboration. Fit claims capped at `low` and named as unanswerable from web evidence.

## Coverage plan (decision-critical units)

Units of analysis to cover with at least minimum fields. **Note (amended after review
panel): study notes live in `sources/*.md`, not a separate `papers/` directory — they
carry the required study-note fields (population, task, method, effect size, source
independence, recency, caveats) and `papers/` would duplicate them. This amendment is
recorded here so the contract and the delivered dossier agree.**
- **Studies**: each major measured/controlled study gets a `sources/*.md` note with population,
  task, method, effect size, source independence, recency, caveats.
- **Task-type effects**: evidence per category.
- **Experience-level effects**: junior vs. senior findings.
- **Familiarity effects**: known vs. unknown codebase.
- **Non-speed effects**: defects, review burden, comprehension, maintenance.
- **Measured-vs-self-reported divergence**: dedicated section.
- **Major vendor studies** (Microsoft/GitHub Copilot, Google, etc.): typed as vendor,
  capped confidence, but recorded because they are widely cited.

## Expected artifacts

- `README.md`, `intake.md`, this contract, `methodology.md`, `evidence.md`,
  `open-questions.md`, `log.md`, `synthesis.md`, `decision-guide.md`.
- `sources/*.md` per major source (study notes live here, not in `papers/` — see coverage
  plan amendment above).
- `review/` for second opinion and panel outputs.

## Success criteria

- Every performance claim typed; vendor claims not at `high`.
- Measured-vs-self-reported divergence explicitly addressed.
- Condition map exists (task × experience × familiarity).
- Non-speed effects covered or explicitly marked as gap.
- Every high-impact gap is `resolved` or `blocked` (no `partially resolved`).
- Fit question named unanswerable with a concrete local evaluation.
- Search ledger non-empty with queries AND rejections logged.

## Assumptions

- Non-interactive; see `intake.md`.
- "Experienced developer" = several years professional experience.
- "Real work" = shippable tasks; benchmark studies still count if realistic.
- Productivity primarily = time-to-completion.

## Risks, ambiguities, terms needing definition

- "Agent" vs. "assistant" (Copilot autocomplete vs. Cursor/Claude Code agentic) — tools
  evolved fast; older studies may measure Copilot autocomplete, not agents. Must distinguish.
- Publication bias (positive results more likely published; vendors publish wins).
- Survivorship / self-selection in surveys.
- Rapid tool change makes older studies stale; recency matters.
- "Familiarity" rarely isolated as a variable.

## Second opinion / review settings

- **Second opinion:** enabled, model `codex`, 1 independent run on the research questions
  only.
- **Review panel:** enabled, models `agy codex claude:opus`, 1 loop. Stop when no reviewer
  raises an actionable issue.
- These run AFTER the Gate 5/6 loop reaches done/budget.

## Output directory

`research/ai-coding-productivity/`