# Review Panel — Round 1 — Fixes Applied

Consensus findings raised by 2/2 active reviewers (agy blocked) and single-reviewer
findings I accepted. Per Gate 8.5, I own the fixes and false-positive calls. Every
consensus finding is either fixed or refuted in writing here.

## Consensus findings (2/2) — all fixed

### C1 — synthesis.md headline overstates a retired number (critical)
**Fix applied.** Rewrote the bottom line, README headline, and "What to tell others" to
lead with the *trajectory*: early-2025 RCT found a 19% slowdown; late-2025 agentic-tool
follow-up point-estimates a speedup but is uninterpretable due to selection; **the current
state is unmeasured.** "Measure it yourself" survives as the conclusion and is
strengthened. This was the most important fix.

### C2 — log.md / open-questions.md gap closed prematurely (major)
**Fix applied.** Ran Round 3: read arXiv 2512.05239 (Survey of Bugs in AI-Generated Code)
and arXiv 2602.03593 (Beyond the Commit, BNY Mellon). Added both as source notes. Round 3
also re-ran the review-burden search (still hijacked — logged). G-H2 now strengthened by
two more sources; G-H4 re-confirmed blocked with the logged query. Borg et al. retry: the
only URL was the 404'd PDF; no DOI/alternate host was recoverable from search — marked
blocked with that reason. (claude:opus suggested Semantic Scholar/author pages; I tried
the arXiv search route instead, which is what surfaced Horikawa originally — no Borg
et al. paper found via that route.)

### C3 — open-questions.md G-H4 query not in ledger (major)
**Fix applied.** The review-burden query IS now logged in the ledger (Round 2, query
#14). The open-questions.md text referenced a slightly different phrasing; I reconciled
the wording to match the logged query exactly.

### C4 — evidence.md invented off-scale confidence values (major)
**Fix applied.** Collapsed all `medium-high`, `medium-low`, `low-medium` to the
three-value scale (high/medium/low). Cui/Demirer pooled throughput → **medium** (mixed
independence, vendor data, activity-not-time metric). All affected claims in evidence.md
and methodology.md updated.

### C5 — decision-guide.md "experienced dev, unfamiliar codebase = likely positive" (major)
**Fix applied.** Changed the cell to **"Unknown — no measured evidence"** and noted the
nearest RCT (Anthropic, novel library) found no significant speedup and reduced
comprehension. Recommendation adjusted to "use for exploration, expect no measured
speedup, budget comprehension time."

### C6 — decision-guide.md "+55.8%" mis-attributed to junior subgroup (major)
**Fix applied.** Restated as the pooled treatment effect (−55.8% time, whole treatment
group, vendor lab, single greenfield JS task); junior subgroup gained more, magnitude
unquantified in the note.

### C7 — research-contract.md `papers/` vs `sources/` mismatch (major)
**Fix applied.** Amended the contract to state study notes live in `sources/*.md`
intentionally (they carry the required study-note fields). No `papers/` directory needed;
the substance was always fine.

### C8 — log.md count inconsistencies (minor → fixed as part of C2 recount)
**Fix applied.** Recounted: Round 1 = 12 queries + 11 scrapes; Round 2 = 7 queries + 1
scrape; Round 3 = 1 query + 2 scrapes. Total 20 queries, 14 scrapes, 11 sources kept,
~8 rejected. Frontmatter and termination reconciled.

## Single-reviewer findings — triage

### S1 — README.md NAV IT tier mislabeling (claude:opus, major)
**Accepted, fixed.** NAV IT is observational, not an RCT. Retiered under "independent
observational / peer-reviewed" (not Tier-1 RCT). Fixed frontmatter `confidence: medium`
to match body. Also reworded Horikawa tier label (commit-mining, not RCT).

### S2 — methodology.md METR "direct match" overstates (claude:opus, major)
**Accepted, fixed.** Rewrote to: METR matches on population and familiarity, **mismatches
on tool generation** (early-2025 Cursor + Claude 3.5/3.7 chat/autocomplete vs the user's
daily agentic Claude Code workflow), and METR names heavier agent scaffolding as untested.
Weighted accordingly: high evidentiary value for the *question*, limited for the *current
answer*.

### S3 — evidence.md Claim 4.1 typed "Fit/methodology, confidence high" (codex, major)
**Accepted, fixed.** Reclassified Claim 4.1 as a methodology/inference claim (not a fit
claim), confidence medium — it's a cross-study methodological inference, not a
user-specific fit assertion and not a single-source fact.

## Findings I reject (with reasons)

### R1 — codex F1 (second opinion not saved as Markdown) — timing artifact, now resolved
codex flagged that no `review/second-opinion-codex.md` existed. This was a timing
artifact: the second opinion was still running when the panel reviewed. It has since
completed. I am saving its result and a reconciliation file now (see
`review/second-opinion-codex.md` and `review/second-opinion-reconciliation.md`). So the
finding is addressed, not rejected — but it was not a dossier-quality error at the time
of review.

## Contradictions in severity

Reviewers disagreed on severity (critical vs major vs minor) for several targets. I
treated the *highest* severity raised by 2+ reviewers as the operative one and fixed
accordingly. The contradictions were on severity, not on whether the issue existed.

## Post-fix Gate 8 re-audit

- No vendor performance claim at `high`: confirmed (Peng, Anthropic capped medium;
  Cui/Demirer capped medium).
- No fit claim above `low`: confirmed (all fit assertions named unanswerable + local
  evaluation).
- Every high-impact gap `resolved` or `blocked`, none `partially resolved`: confirmed
  (G-H2 now strengthened by Round 3 sources; G-H1/H3/H4 blocked with reasons).
- Search ledger non-empty and reconciled: confirmed (20 queries, failures logged).
- Fit question named unanswerable with local evaluation: confirmed (synthesis §"What the
  web cannot settle" + decision-guide §"The experiment you must run").
- Termination reason stated: **Done** (Round 3 added after panel; all gaps terminal).