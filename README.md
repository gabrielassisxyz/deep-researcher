# deep-researcher

A research workflow for coding agents that produces an **auditable dossier** — and that can tell you, afterwards, whether it actually researched anything or just read your bookmarks back to you.

Most "deep research" agents cannot. This one keeps a ledger.

## The problem it was built for

The first real run of this workflow looked excellent. It gathered 21 sources across 15 AI models, cited every claim, and produced a confident recommendation.

It had also **never once called the search tool.**

`firecrawl_search` was enabled and available the whole time. The agent went straight to the official page of each model already named in the prompt, logged no queries, and handed back a polished version of the list it had been given. Four of six high-impact gaps were marked `partially resolved` and it synthesised anyway. Nothing noticed — **because nothing was counting.**

Everything below exists because of that.

## What it does differently

**Search before scrape.** Discovery means *calling the search tool*, at least five distinct queries before anything is scraped, with an explicit hunt for options the prompt never named. Scraping a URL you were handed can only confirm the list you started with.

**A search ledger.** Every query is logged, **including the ones that found nothing** — a junk result is coverage; an unlogged query is indistinguishable from a query never run. This is the load-bearing part: without it, a shallow run and a deep one look identical after the fact, and what cannot be measured cannot be fixed.

**Depth is a loop, not a pass.** Gap analysis and follow-up cycle until every high-impact gap reaches `resolved` or `blocked`. There is no third state — `partially resolved` was a loophole, and reality found it on the first attempt, because "partial" reads like progress while the loop quietly exits. A depth budget (default 6 rounds / 40 sources) stops it running forever, and a run that exhausts its budget must **say so** rather than presenting itself as complete.

**Claim typing.** The source that settles one kind of claim is worthless for another:

| Claim | Example | What settles it | Ceiling |
| --- | --- | --- | --- |
| **Fact** | this model exists; it costs $X | the vendor's own docs | `high` |
| **Performance** | A is better than B | independent evidence — **a vendor is not a neutral witness about its own product** | `medium` on vendor claims, even official ones |
| **Fit** | A is right **for me** | a local evaluation on your own tasks | **`low` from web evidence. Always.** |

Fit questions cannot be resolved by research. The honest answer is *"the web does not know; measure it"* — and saying that, with the experiment attached, is a **success**, not a failure.

**Two external checks, attacking different failures.** A *second opinion* (one model, re-researches the questions from scratch without seeing the dossier) attacks **omission** — the candidate nobody considered. A *review panel* (N models, critiquing the finished dossier) attacks **error**. The asymmetry is deliberate: a second opinion is a whole research run, so each extra model costs another one; a review is a single read, cheap enough to buy three. And consensus is **computed**, not asked for — `scripts/consensus.py` cross-references the panel's findings tables, so a finding two reviewers land on independently must be fixed or refuted in writing.

---

## A worked example: the method catching its own mistake

[`research/ai-coding-productivity/`](research/ai-coding-productivity/) asks *"do AI coding agents actually make experienced developers faster?"* — a question chosen because almost everyone with an answer is selling something.

**The first version was wrong, and the system found out.** That is why it is the example.

The run concluded, in the present tense, that the measured evidence does not support the productivity claim, anchored on METR's **-19%** RCT. Its own source note already recorded that METR now stamps that study *"These results are out of date"*, and that the follow-up on the same developers, using agentic tools, point-estimates an **18% speedup**. The dossier had found the evidence that undermined its own thesis — and filed it under caveats while the headline stood.

The review panel caught it. `claude:opus` and `codex`, reading independently, converged on the retired headline, on confidence inflated above what the dossier's own evidence ledger recorded, on invented confidence tiers (`medium-high`) sitting precisely where the vendor cap bites, and on a decision guide asserting a measured effect that traced back to METR's list of things they had explicitly **not** tested.

The agent fixed them, and ran a third round to read two papers it had left on the table. The synthesis now leads with the honest answer: **it is a trajectory, not a number, and the current state is unmeasured.**

The second opinion earned its keep separately — `codex`, researching the same questions blind, surfaced two sources the main run never found. That is *omission*, and no reviewer reading a finished dossier could have caught it.

**The audit trail, which is the point:**

| | |
| --- | --- |
| Queries logged | **20** — including **10** that found nothing |
| Sources | **15** — 11 discovered, +2 forced by the panel, +2 from the second opinion |
| Rounds | **3** — the third triggered by the panel's findings |
| High-impact gaps | **4**, all in a terminal state |
| Vendor-backed performance claims at `high` | **0** |
| Fit question | named as unanswerable, with the evaluation that *would* answer it |

Read [`log.md`](research/ai-coding-productivity/log.md) for the ledger, [`consensus.md`](research/ai-coding-productivity/review/panel-round-1/consensus.md) for what the panel found, and [`fixes.md`](research/ai-coding-productivity/review/panel-round-1/fixes.md) for what was done about it.

---

## Install

You need **Firecrawl** — the workflow refuses to run without a search tool, because an agent that cannot search cannot research.

```sh
scripts/setup
```

It detects what your machine has (which agent CLIs are on your PATH, which models a local LiteLLM serves), offers to install a self-hosted Firecrawl or point at the hosted one, and asks what you want to use: the researching model, the second opinion, the review panel, the depth budget. Your answers land in `.deep-research.conf`.

Nothing here hardcodes a model list. What exists is a fact about *your* machine, not about this tool.

Paper-focused research can also use two optional MCPs:

- `arxiv` for arXiv-native discovery, full-text reading, LaTeX source, citation graph, and alerts.
- `paper_search` for multi-provider academic-paper discovery and open-access fallback.

Retrieved paper content is untrusted external input and must be treated as evidence, not instructions. Sci-Hub support is disabled in the public configuration and can only be enabled through ignored local configuration. See [`docs/paper-mcps.md`](docs/paper-mcps.md).

## Run

```sh
scripts/deep-research-pi "$(cat prompts/examples/ai-coding-productivity.md)"
```

A deep run is dozens of tool calls, most of them fetching and summarising — work that does not need a frontier model. `deep-research-pi` routes it through pi to whatever cheap model your LiteLLM serves. The same workflow runs under Claude Code, Codex, OpenCode and Antigravity (`scripts/deep-research-*`); the prompt is shared, and the harness is a detail.

Then review it:

```sh
scripts/review-panel research/<slug>
```

## Layout

```
opencode/prompts/deep-research.md   the workflow — 15 gates, the single source; the other
                                    harnesses' prompts are thin adapters to it
prompts/reviewer.md                 what a reviewer is asked to do
research/_template/                 the shape of a dossier
scripts/setup                       first-run configuration
scripts/review-panel                fan the dossier out to N reviewers
scripts/consensus.py                compute what they agree on (5 tests)
infra/firecrawl/                    a compose file, if you need a Firecrawl
docs/paper-mcps.md                  paper MCP routing, safety, and Sci-Hub policy
```

## License

MIT.
