---
type: external-review
reviewer: claude:opus
round: 1
status: complete
verdict: needs-fixes
---

# Review — claude:opus — Round 1

**Scope note (read this before weighing my findings).** Network access was denied in this
session, so I could **not** re-fetch the primary sources to verify that the numbers in
`sources/*.md` match what the papers actually say. Everything below is an audit of (a) whether
the source notes support the claims that cite them, (b) internal consistency across the
dossier, and (c) calibration against the contract's own rules. External fact-verification of
the 2026-dated sources (METR uplift update, METR 2026 survey, Horikawa MSR '26, Anthropic
skill-formation) remains **unperformed by me** — a later round should do it, because four of
the nine sources are the load-bearing recency evidence and none of them were independently
re-checked.

The dossier is genuinely good research with a genuinely misleading front page. Its own
caveats contradict its own headline, and the reader who stops at the headline — which is the
reader the README is written for — gets the wrong answer.

## Findings

| ID | Severity | Target | Finding | Why it matters | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| F1 | critical | synthesis.md:14 | The bottom line asserts in the present tense that "the measured evidence does not support the popular claim," anchored on METR's -19%. The dossier's own source note (`sources/metr-early-2025-rct.md:51`) records that METR's blog now carries the banner **"These results are out of date,"** and that the follow-up on the *same original developers* with agentic tools point-estimates an **18% speedup**. The reversal appears only in the Q1 list ("now superseded"), in a caveats block, and in README caveat #1 — never in the headline, and never in "What to tell others" (decision-guide.md:110). | The single most decision-relevant fact in the dossier is that the crux number is retired by the people who produced it, and the most recent measurement of the user's own population points the *other way*. A reader acting on the headline is acting on a number its authors withdrew. This is the difference between "AI probably makes you slower" and "nobody currently knows, and the last look suggested the opposite." | Rewrite the bottom line, the README headline, and the "What to tell others" script to lead with the *trajectory*: the only clean RCT on this condition (early-2025 tools) found a 19% slowdown; its successor, on late-2025 agentic tools, point-estimates a speedup but is uninterpretable due to selection; **the current state is unmeasured**. Keep "measure it yourself" as the conclusion — it survives the correction, and is in fact strengthened by it. |
| F2 | major | synthesis.md:68 | Sign conventions collide. `evidence.md:17` says "**+19%** completion time" (positive = slower). `synthesis.md:39` says "**-19%** (slower), CI +2% to +39%" (negative = slower, positive CI = slower). The Q2 table at `synthesis.md:66-69` puts "**+55.8%** time" (meaning *faster*) one row above "**-19%** time" (meaning *slower*) — the same column, the same unit, opposite conventions. The late-2025 note (`sources/metr-late-2025-uplift-update.md:29`) uses a third framing ("18% speedup, CI -38% to +9%"). | The headline number of the entire dossier cannot be read unambiguously by a careful reader, and a careless one will read the Q2 table as saying METR found devs 19% *faster*. This is the number the whole recommendation turns on. | Adopt one convention and restate every figure in it. Recommended: **"% change in completion time; positive = slower."** Then METR early-2025 = +19% (CI +2 to +39), Peng = −55.8%, METR late-2025 original devs = −18% (CI −38 to +9). |
| F3 | major | log.md:152 | Termination declares all four high-impact gaps `blocked` after **2 of 6 rounds and 9 of 40 sources** — while two candidate sources found in Round 1 were never read: arXiv 2512.05239 (survey of bugs in AI-generated code, `log.md:41`) and arXiv 2602.03593 ("Beyond the Commit", `log.md:37`, explicitly marked "**deferred, not rejected; may use in gap round**"). The gap round then ran and did not use them. Borg et al. 404'd once (`log.md:113`) with no attempt at a DOI, an alternate host, or the authors' pages. | "Blocked" is supposed to mean *the evidence does not exist in accessible form*. Here it means *the search stopped with two-thirds of the budget unspent and two known leads unopened*. G-H2 (maintainability/defects) and G-H4 (review burden) are exactly the gaps those two unread papers speak to. The contract's success criterion "every high-impact gap is resolved or blocked" is being self-graded as met on a technicality. | Run Round 3: read arXiv 2512.05239 and arXiv 2602.03593; retry Borg et al. via DOI/Semantic Scholar/author page. Re-declare G-H2 and G-H4 only after that. |
| F4 | major | open-questions.md:42 | G-H4 (review burden) is justified by a query — `"code review" AI generated code reviewer effort time increase study arxiv` — that **does not appear anywhere in log.md's ledger**. The ledger's nearest entries are #14 and #17, both worded differently. | The ledger is the dossier's audit surface; the README (`:101`) tells the auditor to start there and says "if a source appears nowhere in the ledger, it was assumed, not discovered." The same standard must apply to the *searches* that justify a `blocked` verdict. A gap closed by an unlogged query is unauditable. | Log the query in `log.md` if it was run; if it was not run, run it, and re-derive G-H4's status from what it returns. |
| F5 | major | synthesis.md:192 | Confidence inflation between the ledger and the synthesis. The synthesis rates **high**: "effect-by-task-type gradient" and "heterogeneity toward juniors." `evidence.md:56` and `evidence.md:77` rate the very same two claims **medium-high**. Their entire evidentiary base is Peng et al. (vendor lab) plus Cui/Demirer (Microsoft/GitHub authors on the paper, senior subgroup non-significant) — no independent, non-vendor measured study of the junior-vs-senior gradient exists in the dossier. | The contract (`research-contract.md:84`) and the calibration rules cap vendor performance claims at medium absent independent corroboration. "High" is not available for either claim, and these are the two claims that carry the "recommend it to juniors" half of the decision guide. | Downgrade both to **medium** in the synthesis confidence summary, or name the independent corroboration that would lift them. |
| F6 | major | evidence.md:43 | The dossier invents confidence values off the scale — `medium-high` (Claims 1.4, 2.1, 3.1), `medium-low` (1.4), `low-medium` (5.4) — and uses them precisely where the cap bites. `methodology.md:33` states this explicitly: Cui/Demirer is "**Capped medium-high**." That is not a cap; it is a tier invented *above* the cap for a paper with the vendor's own employees as co-authors. | The three-value scale (high/medium/low) exists so that the vendor cap is enforceable. A hyphenated intermediate value makes the cap unfalsifiable — you can always be "just above medium." | Collapse to the three-value scale. Cui/Demirer's pooled throughput claim → **medium** (mixed independence, pre-registered, but vendor data and an activity-not-time metric). |
| F7 | major | decision-guide.md:24 | The row "Experienced dev, unfamiliar codebase" reports the measured effect as "**Likely positive**" and recommends "**Use it for exploration**." No such measurement exists in the dossier. The claim traces to METR's *list of things they did not test* (`sources/metr-early-2025-rct.md:47`: "Plausible AI helps ... devs in unfamiliar codebases — **not tested here**"). Meanwhile the dossier's one piece of actual evidence on unfamiliar material — the Anthropic RCT (`evidence.md:59`, Claim 2.2) — found **no significant speedup and 17% lower comprehension**. | An untested plausibility, floated by the authors of a different study as a limitation, has been promoted into a positive effect estimate and a usage recommendation — and it contradicts the dossier's own Claim 2.2. This is the exact failure mode the fit-claim cap exists to prevent. | Change the cell to "**Unknown — no measured evidence.** The nearest RCT (Anthropic, novel library) found no significant speedup and reduced comprehension." Adjust the recommendation accordingly. |
| F8 | major | decision-guide.md:22 | The condition matrix attributes "**+55.8% lab**" to the row "Junior / new dev, greenfield, well-specified." Peng et al.'s 55.8% is the **pooled treatment effect over a mixed-experience recruited sample** (`sources/github-copilot-55-percent-study.md:22-30`); the junior-vs-senior heterogeneity is reported as a *direction*, not as a 55.8% junior-subgroup estimate. | The single most-cited number in the literature is being re-pointed at a subgroup it does not describe — inside the table that drives the recommendation. The dossier's own decision-guide.md:113 says never to repeat that number without its context, and then does so. | State the pooled effect (−55.8% time, whole treatment group, vendor lab, single greenfield JS task) and note the junior subgroup gained more, magnitude unquantified in the note. |
| F9 | major | README.md:49 | Tier mislabeling. NAV IT is listed under "**Tier 1 (independent RCT / peer-reviewed)**" and its frontmatter says `confidence: high` (`sources/nav-it-longitudinal-study.md:10`) — but the study is **observational, not an RCT** (its own note, `:26`: "25 Copilot users vs 14 non-users (observational, not RCT)"), n=39 devs, with an admitted selection effect (adopters were already more active), and the same note's claim typing says "**medium** as a general claim." | The tier list is how a skimming reader weighs the evidence base, and it currently shows three Tier-1 RCTs when there are two (METR, Horikawa — and Horikawa is commit-mining, not an RCT either). The frontmatter and the body of the same file disagree about its confidence. | Retier NAV IT as independent observational/longitudinal (peer-reviewed venue, not RCT); set frontmatter `confidence: medium`; reword the Tier-1 heading so it does not claim RCT status for commit-mined work. |
| F10 | major | evidence.md:113 | Claim 5.2's specific figures (cloned lines 8.3%→12.3%; moved/refactored 25%→<10%) come from GitClear, whose primary methodology the dossier **could not fully access** — `log.md:80` records the scrape as "**partial, gated**" and the source note (`:37`) admits "some figures are from secondary aggregators (**exceeds.ai**) citing this work." exceeds.ai is a source the dossier explicitly **rejected** (`log.md:87`). | Numbers may be laundered through an aggregator the dossier rejected by name, and the note does not say which figures were read from the primary and which from the aggregator. Per the calibration rules, aggregator-only claims cannot exceed medium — and here they cannot even be attributed. | Mark in the source note exactly which figures were verified against the gated primary and which came via aggregator; if the split cannot be established, drop the precise percentages and keep only the direction. |
| F11 | major | methodology.md:77 | "The user's condition (experienced + familiar) is **directly matched only by METR**. That is why METR carries disproportionate weight." The match is on *population and familiarity only*. METR's arm used **early-2025 Cursor + Claude 3.5/3.7** in a chat/autocomplete workflow; Gabriel is a daily **agentic** user (Claude Code-class, with scaffolding). METR's own caveat list (`sources/metr-early-2025-rct.md:45`) names "heavier agent scaffolding" as an untested condition. | The dossier justifies METR's disproportionate weight with a "direct match" that is a two-out-of-three match, and the axis it mismatches on — tool generation — is the axis the dossier elsewhere argues is decisive (`synthesis.md:102`, "Tool era ... Capabilities changed"). The weighting argument undercuts itself. | Say plainly: METR matches on population and familiarity, mismatches on tool generation, and METR names the user's tool practice as untested. Weight it accordingly — high evidentiary value for the *question*, limited for the *current answer*. |
| F12 | minor | log.md:22 | The ledger cannot count itself. Round 1 header says "**11 searches**" and then lists **12** numbered queries. Round 2 header says "**3 searches**" and lists **7** (#13–#19). Termination says "**19 (11 in R1 + 8 in R2)**." Frontmatter says `sources_rejected: 8`; termination says "Sources rejected: **5+**"; README says "**8+** rejected." | The ledger is the one artifact whose credibility is its arithmetic. Three mutually inconsistent counts of the same searches invite the question of whether the searches were reconstructed after the fact rather than logged as they ran. I do not believe they were — the failures and hijacks are too specific to be invented — but the dossier should not be inviting the question. | Recount and reconcile: one number per round, matching the numbered list, propagated to frontmatter, termination, and README. |
| F13 | minor | synthesis.md:56 | "Plus **three** large observational/survey sources: DORA 2024, GitClear 2025, METR 2026 survey, Horikawa MSR '26." Four are listed. | Trivial, but it is in the paragraph that inventories the evidence base. | Say four, or split Horikawa out (it is commit-mining, not a survey). |
| F14 | minor | research-contract.md:105 | The contract's expected artifacts and coverage plan require a **`papers/*.md` note per major study**. No `papers/` directory exists; every note lives in `sources/`. The notes do carry the required fields (population, task, method, effect size, independence, recency, caveats), so this is nominal — but the dossier self-grades the coverage plan as met. | A contract that is silently renegotiated at delivery time is not a contract. The substance is fine; the bookkeeping is not. | Amend the contract to say study notes live in `sources/`, or create `papers/`. Do not leave it implicit. |

## False-Positive Risks

Ranked by how likely I am to be wrong.

- **F10 (GitClear laundering) is my least certain.** I am inferring from "partial, gated" plus
  "some figures are from secondary aggregators" that the headline percentages *might* be
  aggregator-sourced. They may well have been read directly off the free portion of the
  GitClear page. If so, the fix collapses to a one-line clarification in the source note and
  the finding is minor, not major. But the dossier cannot currently tell me which it is, and
  that inability is itself the point.
- **F11 (METR weighting) is a judgment call, not an error.** The dossier *does* disclose the
  tool-era mismatch elsewhere; my complaint is that it does not carry the disclosure into the
  sentence that justifies the weighting. A reasonable person could call this a style
  objection. I think it matters because the weighting sentence is what a skimmer reads, but I
  hold it more loosely than F1–F8.
- **F9 (NAV IT tiering)** — "Tier 1 (independent RCT / **peer-reviewed**)" can be read as a
  disjunction, in which case NAV IT (HICSS-59) qualifies on the second limb and the label is
  defensible. The `confidence: high` frontmatter contradicting the body's "medium" is not
  defensible either way, so the finding survives, but possibly at reduced severity.
- **F5/F6 (confidence inflation)** — I am confident these are real, but they are the kind of
  finding a reviewer raises to look rigorous. To be explicit about why they are not noise:
  the vendor cap is the one rule in this contract that has teeth, and "medium-high" is
  precisely the move that removes them.
- **I did not verify a single external fact.** If any of the 2026-dated sources are
  misreported — or do not exist — I would not have caught it. My clean-ness on factual
  accuracy is an artifact of my constraints, not a finding. **Do not read the absence of
  factual-error findings from me as corroboration.**

## What The Dossier Got Right

Quite a lot, and I want to be specific because F1 is harsh.

- **The search ledger is real.** Nineteen-odd queries with results, seven documented
  name-collision hijacks ("Meta", "Dell", "Borg" → Star Trek), a 404 on the Borg PDF, and
  named rejections with reasons. This is what discovery actually looks like when it happens,
  and it is the single strongest signal that this dossier was researched rather than recalled.
  My F3 and F12 are complaints about where it *stopped* and how it *counted* — not about
  whether it happened.
- **It actively hunted disconfirming evidence** (methodology.md:19) and found it. A dossier
  written to please a daily AI-agent user would not lead with a slowdown.
- **The measured-vs-self-reported divergence section is excellent** and is the dossier's real
  contribution: it replicates across an RCT, a longitudinal study, and an industry survey, and
  the dossier resists the temptation to overclaim the magnitude.
- **The local self-experiment (decision-guide.md:49-84) is the best thing in here.** It is
  concrete, correctly powered-ish, pre-registers the task list, and — crucially — names the
  exact failure that broke METR's own follow-up (dropping hard tasks from the no-AI arm) and
  tells the user not to repeat it. That is a researcher who read the sources rather than
  skimmed them. It is also, notably, the recommendation that **survives F1 intact**.
- **Vendor studies are labeled and capped**, and the Anthropic study's comprehension finding
  is credited as unusually candid without being credulous about it.
