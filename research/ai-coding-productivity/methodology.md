---
type: methodology
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
---

# Methodology

## Search strategy

- Discovery via Firecrawl `firecrawl_search` (the only search tool available; no
  Context7 / Browser Use used). Issued 19 distinct queries across 2 rounds, logged in
  `log.md` including the 7 that were hijacked by name collisions (Meta, DORA, Dell'Acqua,
  Borg, "systematic") and the 2 that found nothing useful.
- Varying phrasing deliberately to avoid echo-chamber retrieval: "controlled experiment",
  "experienced developers", "self-reported vs measured divergence", "defect rate",
  "comprehension", "greenfield vs existing", "review burden", "agentic 2026".
- Searched for **evidence that contradicts the popular claim** per user instruction
  (METR's slowdown, DORA's stability hit, GitClear's cloning, Horikawa's maintainability
  degradation, Anthropic's comprehension deficit) — not only for confirming evidence.
- Followed citation trails: the Cui/Demirer paper cites and contextualizes Peng et al.
  and the BCG/Dell'Acqua study, so those are represented via the field-experiment paper.
- No candidate studies were provided by the user (deliberate). All sources were
  discovered by search.

## Source tiers (per Gate 4.5 claim typing)

- **Tier 1 — Independent RCT / peer-reviewed**: METR early-2025 (arXiv, independent
  nonprofit), NAV IT (HICSS-59), Horikawa (MSR '26). Performance claims can reach
  high (for the studied setting).
- **Tier 2 — Independent field RCT, mixed independence**: Cui/Demirer (vendor data,
  independent academic analysis, pre-registered AEARCTR-0014530). Capped **medium** (mixed
  independence, vendor data, activity-not-time metric).
- **Tier 3 — Vendor RCT**: Peng et al. (GitHub/Microsoft), Anthropic skill-formation.
  Performance capped at medium per the rule "a vendor is not a neutral witness about
  its own product." Anthropic's comprehension finding is unusually candid and so treated
  slightly above a pure marketing claim.
- **Tier 4 — Independent observational / large survey**: DORA 2024 (Google-sponsored,
  independent program), GitClear 2025 (code-quality vendor, not AI vendor). Medium.
- **Tier 5 — Self-report survey**: METR 2026 survey. High for "what people say"; low for
  "what is true."
- **Tier 6 — Commentary/aggregator**: Cerbos, byteiota, exceeds.ai, Reddit, addyo
  Substack. Used only for framing/corroborating direction, never as primary evidence.

## Benchmark / metric interpretation

- **Time-to-task** (Peng, METR) — the cleanest speed metric, but Peng's is a single lab
  task and METR's is real PRs.
- **Activity throughput** (Cui/Demirer PRs/commits/builds; NAV IT commits) — a proxy for
  work done, NOT for value or time. A 26% PR increase is not a 26% speedup; it could even
  be more trial-and-error. Cui/Demirer flag this themselves.
- **DORA four-metric delivery performance** (throughput + stability) — the system-level
  metric. The divergence between DORA's individual-level self-report and system-level
  delivery is itself the finding.
- **Maintainability Index / Cyclomatic Complexity / code-clone rates** (Horikawa,
  GitClear) — code-quality proxies, imperfect but directionally informative.
- **Quiz / comprehension** (Anthropic) — short-term, not longitudinal.

## Why no vendor performance claim is at high confidence

Per Gate 4.5: a vendor is a primary source about existence/price and a marketer about
quality. Peng et al. (GitHub/Microsoft) and Anthropic are vendors; their performance
claims are capped at medium regardless of method quality. The Cui/Demirer paper is the
  borderline case — vendor data, but independent academic economists (MIT/Wharton/Princeton)
  led the analysis and pre-registered it; treated as mixed-independence, capped at
  medium for the pooled throughput effect (activity-not-value metric, mixed independence);
  lower for the senior subgroup (small, ns).

## What "experienced developer" and "familiar codebase" mean here

- METR: 5 yrs avg experience on the studied repos (experienced + familiar).
- Cui/Demirer: enterprise developers across tenure/seniority; "senior" / "long-tenure"
  subgroups defined by median split (experienced, codebase familiarity not measured).
- Peng: recruited developers, mixed experience, single unfamiliar (greenfield) task.
- NAV IT: public-sector developers, existing codebase, experience not stratified.
- Anthropic: 52 mostly-junior engineers, unfamiliar library.

The user's condition (experienced + familiar) is **directly matched only by METR**, and
only on two of three axes: population and codebase familiarity. **METR mismatches on tool
generation**: its arm used early-2025 Cursor + Claude 3.5/3.7 in a chat/autocomplete
workflow, while the user is a daily agentic (Claude Code-class, with scaffolding) user.
METR's own caveat list names "heavier agent scaffolding" as an untested condition. So
METR carries disproportionate weight for the *question* (it is the only study on the
right population and condition), but its weight for the *current answer* is limited by
the tool-era mismatch and by the fact that its authors retired the early-2025 number.
The late-2025 follow-up that would resolve the tool-era gap is uninterpretable. This is
why the synthesis leads with "the current state is unmeasured."

## Limits of this dossier

- Non-interactive; no follow-up questions to the user. Assumptions in `intake.md`.
- Firecrawl search returned several name-collision hijacks; targeted direct scrapes
  filled the gaps where possible. The BCG/Dell'Acqua Harvard study is represented via
  Cui/Demirer's citation, not directly captured.
- Paywalled / email-gated full text (GitClear methodology details) not fully captured;
  abstracts and corroborating aggregators used.
- The fit question is structurally unanswerable from web evidence; only a local
  evaluation can settle it (decision-guide.md).