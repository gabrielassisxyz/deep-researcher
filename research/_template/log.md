---
type: research-log
status: active
updated: YYYY-MM-DD
rounds_used: 0
sources_used: 0
budget: "6 rounds / 40 sources"
---

# Research Log

> This log is the audit trail of *how* the research was done, and it is the only thing that
> can tell a shallow run from a deep one after the fact. A dossier with no search ledger is
> a dossier that cannot be trusted to have looked.

## Search Ledger

**Every search query goes here — including the ones that found nothing.**
A query that returned junk is coverage; a query never logged is indistinguishable from a
query never run.

| # | Round | Query | Results kept | Results rejected (and why) |
| --- | --- | --- | --- | --- |
| 1 | 1 | | | |

## Sources Rejected

Candidates that were found and deliberately not used. This is evidence of breadth.

| Source | Why rejected |
| --- | --- |

## Rounds

Rounds are **not** a fixed set of three. Gates 5 and 6 loop until every high-impact gap is
`resolved` or `blocked`, or until the budget in `research-contract.md` runs out. Add one
section per round actually run.

### Round 1: Discovery

- What triggered it: the research contract.
- Queries issued (see ledger):
- Units of analysis found that the user did NOT name:
- Sources kept:
- Sources rejected:

### Round N: Gap Follow-Up

- What triggered it: which high-impact gap, from which round.
- Queries issued (see ledger):
- What closed: gap -> `resolved`, with the source that closed it.
- What opened: any new high-impact gap this round surfaced.
- Budget consumed so far: N rounds / N sources.

> `partially resolved` is not a terminal state. If a gap is neither `resolved` nor
> `blocked`, the loop continues — write the missing piece as the next round's query.

## Termination

State which one ended the research, explicitly:

- [ ] **Done** — every high-impact gap is `resolved` or `blocked`, and the last round
      surfaced no new high-impact gap.
- [ ] **Budget exhausted** — the ceiling was reached with gaps still open. **List them
      here and in the synthesis.** A dossier that ran out of budget is honest; one that
      ran out of budget and reads as complete is not.

## Audit (Gate 8)

- Unsupported claims removed or qualified:
- Dates, versions, and exact identifiers checked:
- Claim typing checked (Gate 4.5): no vendor source used to support a performance claim at
  `high`; no fit claim asserted above `low` from web evidence alone.
- Search ledger is non-empty and every source traces back to a query or a citation trail:
- Remaining gaps:
