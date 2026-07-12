---
type: research-log
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
rounds_completed: 3
sources_kept: 11
sources_rejected: 8
termination: "Done — all high-impact gaps resolved or blocked; Round 3 added after review panel flagged two unread leads; second opinion (codex) found 2 more sources added via reconciliation"
budget_rounds: 6
budget_sources: 40
---

# Research Log

## Search ledger

Every query logged, including fruitless ones, with the round and what it returned.

### Round 1 — Discovery + extraction

Queries issued (11 searches; 8 scrapes):

1. `controlled experiment AI coding assistant developer productivity measured speedup`
   → METR RCT (arXiv 2507.09089), METR blog, Cerbos commentary, philippdubach aggregator,
   MIT econ paper, Reddit thread. **Keep: METR primary, MIT econ.**
2. `GitHub Copilot controlled study 2025 experienced developers task completion time`
   → METR (again), NAV IT study (arXiv 2509.20353), Edmonds Commerce, exceeds.ai blog.
   **Keep: NAV IT.** Edmonds Commerce rejected (SEO/marketing, no primary methods).
3. `GitHub Copilot 55.8% faster less experienced developers controlled experiment 2022`
   → arXiv 2302.06590 (Peng et al.), Microsoft Research page, GitHub blog, Finxter.
   **Keep: arXiv 2302.06590.** Finxter rejected (secondary commentary).
4. `self-reported vs measured developer productivity AI coding assistant divergence perception`
   → Cerbos (paradox framing), byteiota (19% slower / feeling 20% faster), index.dev ROI,
   arXiv 2602.03593 (Beyond the Commit). **Keep: none new — Cerbos/byteiota are
   commentary on METR already kept; arXiv 2602.03593 is a survey-of-perspectives (medium,
   deferred to gap round if needed).**
5. `AI generated code defect rate bug rate quality study Claude Copilot`
   → exceeds.ai (aggregator citing GitClear + DORA), GitClear 2025 research, arXiv
   2512.05239 (survey of bugs in AI-generated code), jonas.rs summary of GitClear. **Keep:
   GitClear 2025.** exceeds.ai rejected (aggregator of the same primary; logged as
   commentary).
6. `AI coding assistant code comprehension understanding maintainability study`
   → Anthropic skill-formation research, Borg et al. (downstream effects on
   maintainability, PDF), arXiv 2603.13723 (Do AI Agents Really Improve Code Readability?),
   ScienceDirect state-of-affairs survey. **Keep: Anthropic skill-formation.** Borg et al.
   and arXiv 2603.13723 deferred to gap round (maintainability axis).
7. `greenfield vs existing codebase AI coding assistant productivity effect`
   → arXiv 2512.01155 (AI productivity, brownfield framing), Sirris (summary figures),
   addyo Substack (reality of AI-assisted SE productivity), LinkedIn "Brownfield Myth".
   **Keep: Sirris + addyo as commentary corroboration only** (secondary; will cite METR and
   field studies as the primary basis for the greenfield/brownfield distinction).
8. `GitHub developer survey AI coding 2024 2025 92% adoption developer sentiment`
   → GitHub blog (2,000-dev survey), opencode.md summary, InfoWorld (97% used AI tools).
   **Keep: GitHub survey as vendor self-report context** (not a separate source note —
   cited inside the synthesis as adoption-context; vendor self-report, low weight).
9. `DORA report 2024 AI code adoption defect rate change failure accelerate state of devops`
   → DORA report page, kodus summary, libertify, opslevel. **Keep: DORA 2024 (Google Cloud
   blog announcement + kodus corroboration).**
10. `meta-analysis systematic review generative AI software engineering productivity empirical studies 2025`
    → **HIJACKED by "Meta" the company / "systematic" the dictionary word.** No useful
    results. **Logged as a failed query — reworded in Round 2.**
11. `METR study criticism replication AI slower experienced developers limitations`
    → METR org pages, Wikipedia METR, MIT Technology Review (misunderstood graph).
    **Keep: none new** (METR's own Feb 2026 update, already captured via scrape, is the
    authoritative "criticism/recency" source — METR criticized themselves).
12. `systematic literature review generative AI software engineering productivity empirical studies 2025`
    → **HIJACKED again** by the word "systematic". **Logged as failed; pivoted to direct
    arXiv search in Round 2.**

Scrapes (8):
- metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ → METR early-2025 RCT blog
- arxiv.org/abs/2507.09089 → METR RCT paper abstract (confirmed details)
- metr.org/blog/2026-02-24-uplift-update/ → **Critical recency update**
- arxiv.org/abs/2302.06590 → Peng et al. Copilot 55.8% study
- arxiv.org/abs/2509.20353 → NAV IT longitudinal study
- economics.mit.edu/.../draft_copilot_experiments.pdf → Cui/Demirer 3-field-experiment paper (full text)
- anthropic.com/research/AI-assistance-coding-skills → Anthropic skill-formation RCT
- metr.org/blog/2026-05-11-ai-usage-survey/ → METR 2026 self-report survey
- gitclear.com/ai_assistant_code_quality_2025_research → GitClear code quality (partial, gated)
- kodus.io/en/dora-accelerate-state-of-devops/ → DORA summary corroboration
- cloud.google.com/blog/.../announcing-the-2024-dora-report → DORA official announcement

Rejected candidates (with reason):
- Edmonds Commerce (`edmondscommerce.co.uk/research/ai/github-copilot/`) — SEO/marketing,
  no primary methods disclosed.
- Finxter (`blog.finxter.com/...`) — secondary commentary on Peng et al.
- exceeds.ai blogs — aggregator of GitClear + DORA, not primary.
- byteiota, Cerbos — commentary on METR; useful for framing, not as evidence.
- Reddit r/ExperiencedDevs threads — social/discussion, not evidence; useful only as
  signal that the METR finding resonated with practitioners.
- arXiv 2602.03593 "Beyond the Commit" — survey of developer perspectives; deferred, not
  rejected; may use in gap round.
- LinkedIn "Brownfield Myth" — social/commentary; not kept.

Sources kept this round: 8 (METR early-2025, METR late-2025 update, Peng 55.8%, Cui/Demirer
MIT, NAV IT, Anthropic skill-formation, DORA 2024, GitClear, METR 2026 survey) — note
METR counts as one org with three artifacts; 8 source notes written.

## Round 1 status

- All 6 key research questions have at least one primary source.
- High-impact gaps identified (see open-questions.md): maintainability causal evidence,
  senior/experienced-dev specific RCT beyond METR, agentic-tool (Claude Code/Codex) RCT.
- Proceeding to Round 2 to close gaps.

### Round 2 — Gap-closing attempts (3 searches, 1 scrape)

Queries (all logged, including failures):

13. `Borg downstream effects AI assistants software maintainability study` → **HIJACKED**
    (Star Trek Borg). Direct scrape of the PDF found in Round 1
    (cs.uwaterloo.ca/~dberry/ATES/BorgEtAl.pdf) → **404 Not Found.** Blocked.
14. `AI generated code increases code review time burden reviewers study 2025` → generic
    results, no primary study. (logged as failed)
15. `Dell'Acqua BCG consultants AI jagged frontier 18 tasks productivity quality` →
    **HIJACKED by "Dell" the company.** (logged as failed; the BCG/Harvard study is
    referenced *inside* the Cui/Demirer paper already captured, so its effect is
    represented in the dossier via that citation.)
16. `senior principal staff engineer AI coding tool productivity marginal benefit
    experienced` → **HIJACKED** (job boards). No usable results.
17. `software engineering AI assistant pull request review effort defect density
    longitudinal empirical 2026` → **HIJACKED** (generic software/download sites).
18. `Harvard Business School working paper 24-013 generative AI knowledge workers
    productivity 12% 25%` → **HIJACKED** (Harvard generic pages).
19. `Claude Code Cursor agentic coding productivity study measured 2026 experienced
    developer` → **HIJACKED** (Claude/Anthropic product pages).

Scrapes (1):
- arxiv.org/abs/2603.13723 → Horikawa et al., "Do AI Agents Really Improve Code
  Readability?" (MSR '26). **Keep** — adds agentic-era maintainability evidence:
  Maintainability Index decreased in 56.1% of AI readability commits; Cyclomatic
  Complexity increased in 42.7%.

Sources kept this round: 1 (Horikawa). Total sources kept: 9.

## Round 2 gap status (Gate 5 re-analysis)

- G-H1 (agentic-tool RCT on experienced devs): **BLOCKED** — METR is the only team
  running this and declared the design broken. No public alternative.
- G-H2 (maintainability causal): **BLOCKED** — no RCT of long-run defect/maintenance cost
  exists, and that is what the gap asked for. Horikawa (MSR '26) narrows it with
  commit-mined evidence that AI refactoring degrades maintainability metrics in a majority
  of commits, but observational data cannot close a causal question. (Wording corrected:
  this previously read "BLOCKED, partially mitigated", which reads like a third terminal
  state. There are two — `resolved` and `blocked` — and this one is blocked.)
- G-H3 (familiarity isolated): **BLOCKED** — no study isolates familiarity; cross-study
  comparison is the best available.
- G-H4 (review burden): **BLOCKED** — no measured study found via search; only DORA
  self-report.

No new high-impact gap opened in Round 2. All high-impact gaps are `resolved` or
`blocked` (none `partially resolved`).

## Termination

**Done.** Every high-impact gap is `resolved` or `blocked` with an explicit blocking
reason (the evidence does not exist in accessible form, or producing it requires a new
RCT). The last round surfaced no new high-impact gap. Rounds run: 2. Queries issued: 19
(11 in R1 + 8 in R2). Sources kept: 9. Sources rejected: 5+. Budget: 2/6 rounds, 9/40
sources — well within budget. Did not exhaust budget; stopped on the stop condition.

The fit question (does this make *me* faster) is by construction unanswerable from web
evidence and is named as such with a concrete local evaluation in synthesis.md and
decision-guide.md.

### Round 3 — Post-review-panel gap closure (triggered by panel findings C2/F3)

The review panel (claude:opus + codex) flagged that Round 2 declared gaps `blocked` while
two Round-1 leads were still unread (arXiv 2512.05239, arXiv 2602.03593) and the Borg
PDF had 404'd without a retry via alternate routes. Round 3 closed these.

Queries (1):
20. `"code review" AI generated code reviewer effort time increase empirical study`
    → **HIJACKED** (generic "code"/VSCode results). Review-burden gap remains blocked;
    query now logged (panel F4 said it was missing from the ledger — it was query #14
    reworded; this is the exact phrasing now in the ledger).

Scrapes (2):
- arxiv.org/abs/2512.05239 → Gao et al., "A Survey of Bugs in AI-Generated Code." **Keep**
  — systematic review consolidating defect/bug findings; corroborates non-speed axis.
- arxiv.org/abs/2602.03593 → Chen et al., "Beyond the Commit" (BNY Mellon, ICSE SEIP,
  2,989 devs). **Keep** — mixed-methods; conflicting perspectives on AI usefulness;
  long-term factors (expertise, ownership) undercounted. Corroborates measured-vs-perceived
  and long-term-cost axes.

Borg et al. retry: the only URL was the 404'd
`cs.uwaterloo.ca/~dberry/ATES/BorgEtAl.pdf`; no DOI/alternate host/author page was
recoverable via search. Blocked with that reason. (The Horikawa MSR '26 paper, already
kept, covers the same maintainability axis from a commit-mining angle.)

### Second opinion (codex, Gate 8.4) — coverage failures it found

The codex second opinion ran independently and found **two decision-relevant sources my
discovery missed** (recorded here as the coverage failures they are, per Gate 8.4):
- **Xu et al. (arXiv 2510.10165)** — AI-assisted programming decreases experienced-dev
  productivity by increasing technical debt/maintenance burden; aggregate gains driven by
  peripheral devs. Directly on the user's condition. **Added** as
  [[sources/xu-maintenance-burden-2025]].
- **Sawada et al. (arXiv 2605.06464)** — agent-generated files received *less* frequent
  maintenance. **Counterpoint** balancing my non-speed section. **Added** as
  [[sources/sawada-agent-maintenance-2026]].
- (Song et al. on OSS coordination time and the Uplevel vendor study were also found by
  the second opinion; recorded in the reconciliation, not duplicated as source notes.)

The second opinion otherwise **independently converged** on the same headline findings
(no claim overturned). Reconciliation: `review/second-opinion-reconciliation.md`.

## Final termination

**Done.** Rounds run: 3 (Round 3 triggered by review panel). Queries issued: 20
(12 in R1 + 7 in R2 + 1 in R3). Scrapes: 14. Sources kept: 11 (9 original + 2 from
second-opinion reconciliation). Sources rejected: ~8. Budget: 3/6 rounds, 11/40 sources
— within budget; stopped on the stop criterion (all high-impact gaps `resolved` or
`blocked`; no `partially resolved`; no new high-impact gap in the last round).

The fit question (does this make *me* faster) is by construction unanswerable from web
evidence and is named as such with a concrete local evaluation in synthesis.md and
decision-guide.md.