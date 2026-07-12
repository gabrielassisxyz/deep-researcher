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

## Second Opinion (Gate 8.4) — one model, attacks omission

**One** model re-researches the key questions *from scratch*, without seeing this dossier.
It exists to catch what was never looked for — the candidate that was missed, the angle
nobody took. A reviewer reading the finished dossier structurally cannot do that.

One model, not several: a second opinion is a **whole research run**, so each extra model
is another full run's cost. The value is in having *any* independent look, not in having
many.

- Enabled: false
- Model / harness: (one, from `docs/reviewers.md` — prefer a different lineage than the
  model doing the research)
- Scope: the key research questions only — never this dossier's findings or sources.
- Outcome: agreement raises confidence; disagreement becomes a high-impact gap and
  re-enters the Gate 5/6 loop. A unit of analysis it found and we did not is a **coverage
  failure**, and is logged as one.
- **Skipped is a normal choice** (it doubles the research cost). Say so in `log.md` either way.

## Review Panel (Gate 8.5) — N models, attacks error

Reviewers read the **finished dossier** and critique it. This is where triangulation
belongs: reviewing is cheap (one read, no crawling), so several models can do it, and
**disagreement between reviewers is itself signal** — a finding all three flag is almost
certainly real; a finding only one flags is probably that model's bias.

- Enabled: false
- Models: (any number, from `docs/reviewers.md`. Default panel:
  `pi:glm-5.2 pi:kimi-k2.7 pi:deepseek-v4-pro-high` — three labs, all cheap. Prefer
  different lineages: a panel that shares blind spots agrees with itself about exactly the
  things it is collectively wrong about.)
- Maximum loops: 0
- Consensus rule: a finding raised by **2 or more** reviewers is treated as real and must be
  fixed or explicitly refuted. A finding raised by exactly one is triaged on its merits.
  Reviewers contradicting each other is not a finding — it is a gap, and goes back to Gate 5/6.
- Stop condition: stop when no reviewer finds an actionable factual, citation, structure,
  depth, or confidence-calibration issue.
- **Can be switched off to save money — not recommended.** A review is one read of a finished
  dossier: the cheapest check available, and the last thing standing between a confident,
  well-cited, *wrong* dossier and a decision made on it. If it is off, `log.md` and the final
  answer must say so — an unreviewed dossier that doesn't mention it reads exactly like one
  that passed.

## Output Directory

`research/<topic-slug>/`
