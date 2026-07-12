# Golden Test Prompt: LLM Model Decision Routing Research

I need deep research that collects as much reliable data as possible about these LLM models:

- GPT 5.5
- Opus 4.8
- Sonnet 4.6
- Sonnet 5
- Gemini 3.1 Pro
- Gemini 3.5 Flash
- GLM-5.2
- Kimi K2.7-Code
- Gemma4
- Qwen3.5
- Minimax-m2.7
- Minimax-m3
- Deepseek v4 Pro
- Deepseek v4 flash
- Qwen 3.5

Use these model information aggregators as starting points:

- https://livebench.ai/#/?highunseenbias=true
- https://artificialanalysis.ai/leaderboards/models
- https://benchlm.ai/
- https://openrouter.ai/models
- https://artificialanalysis.ai/methodology/intelligence-benchmarking

Do not limit yourself to these links. Explore other links, sublinks, official sources, benchmark pages, model cards, release notes, and independent sources. Focus on depth.

## Primary Objective

The primary objective is to collect reliable evidence for deciding which model to use for each task type, especially when a cheaper model is sufficient and a frontier model is not worth the extra cost.

I care less about a generic leaderboard ranking and more about practical model routing decisions.

The decision I want to support:

- When should I use a frontier model such as Fable, Opus 4.8, GPT-5.5, Sonnet 5, or Gemini 3.1 Pro?
- When is a cheaper model such as Kimi K2.7-Code, GLM-5.2, Qwen 3.5, MiniMax, Gemma, or DeepSeek sufficient?
- Which models are best suited for planning, brainstorming, task decomposition, spec writing, implementation from a clear spec, debugging, refactoring, code review, long-context analysis, documentation work, and general research?
- Where does a frontier model materially improve outcomes, and where is the marginal gain likely too small to justify the cost?

My current working hypothesis is:

- Frontier models are likely worth using for ambiguous planning, brainstorming, architecture trade-offs, difficult task decomposition, and final implementation review.
- Once tasks are decomposed from a clear spec, a cheaper strong coding model such as Kimi K2.7-Code may be competent enough to execute the tasks.
- A frontier model may still be useful as a reviewer, judge, or escalation model after cheaper models implement the work.

Validate, refine, or falsify this hypothesis using evidence.

## Required Decision Outputs

Create decision-oriented outputs, not only model summaries:

- A task taxonomy for AI coding/research workflows.
- A model routing matrix: task type -> recommended model tier -> candidate models -> confidence -> evidence.
- A "cheaper model is sufficient" table.
- A "frontier model is justified" table.
- A review/escalation policy for when to hand work from a cheaper model to a stronger model.
- A cost/performance discussion using pricing, latency, context window, throughput, and benchmark/task evidence when available.
- A clear list of unknowns where evidence is too weak to decide.

## Research Focus

The research focus must be:

- Depth
- Exploration
- Veracity and information quality
- Practical routing decisions
- Cost-performance trade-offs
- Evidence-backed sufficiency thresholds

## Evidence Requirements

Prioritize evidence in this order:

1. Official model cards, system cards, release notes, API docs, pricing pages, and repositories.
2. Independent benchmark leaderboards and benchmark methodology pages.
3. Reproducible public evaluations, papers, and credible third-party test suites.
4. Aggregators for pricing, availability, context window, throughput, and benchmark cross-reference.
5. Commentary only as a lead or low-confidence context.

For benchmark claims, preserve the exact model identifier, benchmark name, metric, date/version, source URL, and caveats.

Do not treat a model as better for a task just because it has a higher general ranking. Tie recommendations to task evidence, cost, latency, context, reliability, and the actual decision frame.

Save Markdown notes with what you find, including local source notes and citations supporting the claims you write.
