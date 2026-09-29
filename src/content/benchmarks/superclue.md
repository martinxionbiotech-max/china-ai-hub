---
benchmark_id: superclue
benchmark_name: SuperCLUE
description: "A Chinese comprehensive evaluation system for large models, organised around four ability quadrants — language understanding and generation, professional knowledge, agent capability and safety — refined into 12 base capabilities."
task_type: "Chinese multi-part evaluation spanning language understanding/generation, professional knowledge, agent capability and safety"
dataset_size: "Multi-part rolling evaluation across four ability quadrants and 12 base capabilities; no fixed single question count (periodic leaderboard releases)"
evaluation_method: "Combines objective multiple-choice questions with multi-turn open-ended questions and agent/tool-use tasks; scored by the CLUE team rather than self-reported"
scoring: "Composite total score (总分) with sub-scores per quadrant (e.g. OPEN multi-turn, open questions, objective questions)"
contamination_notes: "SuperCLUE maintains public and hidden test sets and runs its own evaluation, reducing reliance on vendor self-reported scores."
limitations: "The composite score aggregates heterogeneous sub-tasks, so a single total hides capability-specific strengths. Leaderboard snapshots are time-stamped and not comparable across dates. No Chinese model in the China AI Hub database currently publishes a SuperCLUE score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "SuperCLUE: A Comprehensive Chinese Large Language Model Benchmark"
    source_url: https://arxiv.org/abs/2307.15020
    source_type: academic
    published_date: "2023-07"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "SuperCLUE official repository (CLUEbenchmark)"
    source_url: https://github.com/CLUEbenchmark/SuperCLUE
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "SuperCLUE official website"
    source_url: https://www.superclueai.com/
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** SuperCLUE is a Chinese comprehensive evaluation system for large language models, organised around four ability quadrants — language understanding and generation, professional knowledge and skills, agent capability, and safety — refined into 12 base capabilities. It is the CLUE benchmark team's flagship, and its distinguishing feature is that the CLUE team runs the evaluation itself, including multi-turn open questions and agent tasks.

## What it measures

SuperCLUE measures a Chinese model's **overall** capability rather than a single skill. Its four quadrants cover: (1) language understanding and generation; (2) professional skills and knowledge; (3) agent capability — tool use and task planning; and (4) safety. These expand into 12 base capabilities, and the benchmark has also produced specialised tracks such as **SuperCLUE-Agent** (Chinese-native agent tasks) and **SuperCLUE-Safety** (multi-turn adversarial safety).

The result is a benchmark that tries to answer "how good is this Chinese model, all things considered" — a different question from the single-skill benchmarks like C-Eval (knowledge) or a coding benchmark. That breadth is its value, and also the reason its headline number needs careful reading.

## How it works

SuperCLUE is a **multi-part, team-run evaluation**. Unlike a static multiple-choice dataset, it combines objective questions with multi-turn open-ended questions and agent/tool-use tasks, and the CLUE team scores the responses rather than asking vendors to self-report. The headline output is a **composite total score (总分)**, with sub-scores for components such as OPEN multi-turn, open-ended questions and objective questions.

Because it runs on a periodic leaderboard cycle, SuperCLUE scores are **time-stamped snapshots**: a September leaderboard and a December leaderboard are different evaluations and are not directly comparable. The official website (`superclueai.com`) and the `CLUEbenchmark/SuperCLUE` repository publish the methodology and the rankings.

## What it does NOT measure

Three limits are worth stating. First, the composite total **hides** capability-specific strengths — a model strong in professional knowledge but weak in agent tool-use can have the same total as one with the opposite profile. Second, because the CLUE team's rubric and human scoring evolve between releases, cross-version comparisons are unreliable. Third, SuperCLUE is a Chinese-language evaluation: it does not measure English performance, coding depth, or the long-context and reasoning regimes that international benchmarks target.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes a SuperCLUE score. The tracked models — [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/), [GLM-5.3](/models/glm-53/), [Qwen3.8-Max](/models/qwen38-max/) and others — publish on international and coding benchmarks, not on SuperCLUE. This page therefore records **no evaluations**, and we do not import SuperCLUE numbers from the public leaderboard. Treat any SuperCLUE figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read SuperCLUE results

China AI Hub analysis: SuperCLUE's composite is best read by its **quadrant sub-scores**, not the headline total, and only within a single leaderboard snapshot. Its agent and safety tracks are its most distinctive contributions, because they measure capabilities that pure multiple-choice benchmarks miss. As with every benchmark here, confirm the version and date before comparing; see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Related entities

- Models: [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) · [GLM-5.3](/models/glm-53/) · [Qwen3.8-Max](/models/qwen38-max/) — Chinese flagships that would be the natural SuperCLUE subjects.
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and methodology from the primary paper and official repository), **China AI Hub analysis** (our synthesis of how to read the composite score, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published a SuperCLUE result.*
