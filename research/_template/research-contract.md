---
type: research-contract
status: draft
updated: YYYY-MM-DD
confidence: low
---

# Research Contract

## Research Objective

State the operationalized research objective.

## Decision Or Evaluation Frame

State the decision, judgment, or evaluation this research must support.

## Target Decisions Or Judgments

- Decision or judgment the dossier should make easier.

## Audience And Intended Use

Name who will use the research and how they will use it.

## Scope

List what is included.

## Out Of Scope

List what is excluded.

## Key Research Questions

- Question that must be answered to satisfy the objective.

## Comparison Axes Or Evaluation Criteria

| Axis | Why it matters | Priority |
| --- | --- | --- |

## Evidence Requirements

Define source priority, freshness, confidence threshold, and citation expectations.

## Coverage Plan

List the decision-critical units of analysis and the minimum fields each standalone note must cover. If a unit has thin evidence, mark it as `status: stub` or keep it in a comparison table.

## Expected Artifacts

List required dossier files and optional domain notes.

## Success Criteria

- Concrete condition that means the research is good enough.

## Assumptions

List assumptions made from missing prompt details.

## Risks And Ambiguities

List terms, scope edges, or evidence risks that may change the result.

## Depth Budget

The Gate 5/6 loop runs until every high-impact gap is `resolved` or `blocked`. This is the
ceiling that stops it running forever — not a target to hit.

- Maximum rounds: 6
- Maximum sources: 40
- On exhaustion: stop, and state the still-open high-impact gaps in `synthesis.md`, in
  `log.md`, and in the final answer. Never let a budget-exhausted dossier read as complete.

## Claim Types In Scope

Which of the three does this research have to answer? (Gate 4.5)

- [ ] **Fact** — existence, identifiers, price, availability. Vendor docs can settle these.
- [ ] **Performance** — is A better than B. Needs independent evidence; vendor claims cap at `medium`.
- [ ] **Fit** — is A right *for this user*. **Web evidence caps at `low`.** If this box is
      ticked, the dossier's honest headline is likely "measure it locally", and the
      deliverable should include the evaluation design, not a confident recommendation.

## Second Opinion (independent triangulation)

A second model researching the same question *independently*, whose disagreement with the
first is treated as a finding. Distinct from the Gemini review below, which critiques a
finished dossier and therefore inherits its blind spots.

- Enabled: false
- Model / harness:
- Scope: the key research questions, answered without sight of the first dossier.
- Stop condition: agreements raise confidence; disagreements become high-impact gaps and
  re-enter the Gate 5/6 loop.

## Gemini Review

- Enabled: false
- Maximum loops: 0
- Stop condition: stop when the reviewer finds no actionable factual, citation, structure, depth, or confidence-calibration issues.

## Output Directory

`research/<topic-slug>/`
