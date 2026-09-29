---
benchmark_id: aime
benchmark_name: AIME
description: "The American Invitational Mathematics Examination, repurposed as a benchmark: 15 integer-answer math problems used to test a model's advanced mathematical reasoning, with scores typically reported for AIME 2024 or AIME 2025."
task_type: "Advanced competition mathematics — 15 integer-answer problems"
dataset_size: "15 problems per exam (integer answers from 000 to 999); benchmark scores typically report AIME 2024 or AIME 2025"
evaluation_method: "Models answer each problem; graded by exact match against the integer answer"
scoring: "Accuracy (% of 15 problems answered correctly); the raw exam score is 0–15"
contamination_notes: "AIME is a fixed public exam, so models trained after a given year may have seen its problems; vendors differ in which year(s) they report."
limitations: "AIME is an exam, not a versioned benchmark, so scores are only comparable when the same year is reported. Exact-match integer grading gives no partial credit for correct reasoning with a wrong final answer. No Chinese model in the China AI Hub database currently publishes an AIME score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Mathematical Association of America — American Invitational Mathematics Examination (AIME)"
    source_url: https://maa.org/math-competitions/american-invitational-mathematics-examination-aime
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "Mathematical Association of America — Competitions"
    source_url: https://maa.org/math-competitions
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** AIME is the **American Invitational Mathematics Examination** — a 15-problem, integer-answer competition exam — repurposed as a benchmark of advanced mathematical reasoning. Because it is difficult, exact-answer and widely reported by frontier model builders (typically as AIME 2024 or AIME 2025), it became a de-facto standard for "how good is this model at hard math".

## What it measures

AIME measures advanced competition mathematics: algebra, number theory, combinatorics and geometry at a level well above standard benchmarks. Its problems are not multiple-choice — each requires a derived integer answer, which means a model must actually *reason* to a correct result rather than rank four options. This makes AIME a stronger signal of genuine mathematical ability than a multiple-choice math test.

As a benchmark, AIME is usually reported as accuracy on a specific year's exam. The 2024 and 2025 papers are the most common targets in modern model cards, so "AIME 2024" and "AIME 2025" function as two distinct, year-labelled sub-benchmarks.

## How it works

Each AIME exam has **15 problems** with integer answers from 000 to 999. Grading is **exact-match**: a model's answer must equal the reference integer to count. There is no partial credit, and the raw score runs from 0 to 15; benchmarks typically report this as a percentage or as "X/15 correct".

Because AIME is a fixed public exam administered by the Mathematical Association of America (MAA), the benchmark has no versioning of its own — the *year* is the version. This is the single most important fact when reading AIME numbers: an "AIME 90%" that does not state the year is uninterpretable.

## What it does NOT measure

AIME does not measure general language ability, coding, agentic skill or breadth of knowledge — it is a narrow, deep test of competition math. Its exact-match grading gives no partial credit, so a model that reasons correctly but makes one arithmetic slip scores the same as one that cannot start. And because the exam is public, a model trained after a given year may have memorised that year's problems, which is why the freshest exam (AIME 2025) is the more contamination-resistant target.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes an AIME score. The tracked reasoning models — [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [Kimi K3](/models/kimi-k3/), [Qwen3.8-Max](/models/qwen38-max/) and others — publish on GPQA Diamond, HLE and coding benchmarks, but not on AIME. This page records **no evaluations**, and we do not import AIME numbers from third-party leaderboards or vendor reports. Treat any AIME figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read AIME results

China AI Hub analysis: AIME is a high-signal but narrow math metric, and its scores are only meaningful when the **year** is stated and matched against a model's training cutoff. It is best used to compare mathematical-reasoning strength, not overall model quality. The same year-and-mode discipline applies here as elsewhere in the database: see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Related entities

- Models: [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) · [Kimi K3](/models/kimi-k3/) · [Qwen3.8-Max](/models/qwen38-max/) — the reasoning flagships that would be the natural AIME candidates.
- Comparison: [DeepSeek-V4-Pro vs Kimi K3](/comparisons/deepseek-v4-pro-vs-kimi-k3/).
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (exam format and grading from the MAA), **China AI Hub analysis** (our synthesis of how to read year-labelled scores, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published an AIME result.*
