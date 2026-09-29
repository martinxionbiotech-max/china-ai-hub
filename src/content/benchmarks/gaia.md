---
benchmark_id: gaia
benchmark_name: GAIA
description: "A benchmark for general AI assistants: 466 real-world questions requiring reasoning, multi-modality handling, web browsing and tool use, where humans score 92% and early frontier assistants far lower."
task_type: "Real-world question answering requiring reasoning, web browsing, multi-modality and tool use"
dataset_size: "466 questions across three difficulty levels; answers to 300 of them are held out for the leaderboard"
evaluation_method: "Questions are conceptually simple for humans but require tool use; graded by exact-match against a single ground-truth answer"
scoring: "Exact-match accuracy (% correct); a question is passed only if the final answer matches exactly"
contamination_notes: "300 of the 466 questions are retained privately for leaderboard evaluation, reducing training-set leakage."
limitations: "Exact-match scoring is strict and can understate near-correct answers. Results depend on the tool/search scaffolding a model is given, so scores are not comparable across different setups. No Chinese model in the China AI Hub database currently publishes a GAIA score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Mialon et al. — GAIA: a benchmark for General AI Assistants"
    source_url: https://arxiv.org/abs/2311.12983
    source_type: academic
    published_date: "2023-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "GAIA benchmark (Hugging Face)"
    source_url: https://huggingface.co/gaia-benchmark
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** GAIA is a benchmark for **general AI assistants**, built on real-world questions that are conceptually easy for a human but require an AI to chain together reasoning, web browsing, multi-modality and tool use. Its headline contrast — humans at 92% versus GPT-4-with-plugins at roughly 15% at release — makes it a benchmark of *agentic competence*, not knowledge.

## What it measures

GAIA measures whether an assistant can actually **get things done** on real-world questions: look something up, read a document or image, run a computation, and return the single correct answer. The questions are deliberately simple for humans ("what is X in Y") but require an AI to orchestrate multiple tools — search, browsing, file handling, code execution — to succeed.

The benchmark's philosophy inverts the usual trend of ever-harder expert questions. Instead of asking things hard for humans (law, chemistry), GAIA asks things *easy* for humans but hard for AI precisely because they demand tool-use proficiency and robustness. This is why it became a key reference for measuring agentic assistants rather than raw model knowledge.

## How it works

GAIA consists of **466 questions across three difficulty levels**. Each question has a single ground-truth answer, and grading is **exact-match**: a model's final answer must match the reference exactly to count as correct. There is no partial credit, which makes the metric strict and reproducible.

Two design choices matter. First, **300 of the 466 answers are held out privately** for leaderboard evaluation, reducing the risk that a model simply memorised the test. Second, performance depends heavily on the **tool scaffolding** the model is given — what search API, browser and code executor it can call. The same model can score very differently under different scaffolding, which is the single most important caveat when comparing GAIA numbers. The benchmark is hosted on Hugging Face (`gaia-benchmark`) with a public leaderboard.

## What it does NOT measure

GAIA does not measure raw knowledge or reasoning in isolation — a model with encyclopaedic knowledge but no reliable tool orchestration will score poorly. The strict exact-match grading can understate near-correct answers (a slightly malformed but essentially correct response scores zero). And because results depend on scaffolding, GAIA scores are **not comparable across different tool setups**; a number is only meaningful alongside a description of the tools the model was allowed to use.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes a GAIA score. The tracked models — [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [Qwen3.8-Max](/models/qwen38-max/) and others — publish on reasoning and coding benchmarks, but not on GAIA. This page records **no evaluations**, and we do not import GAIA numbers from the public leaderboard. Treat any GAIA figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read GAIA results

China AI Hub analysis: GAIA is best read as an **agentic-capability** signal, not a general model ranking. Before citing a number, confirm the tool scaffolding, the difficulty-level mix, and whether the answer was graded by exact match. The same scaffolding-and-mode discipline that governs this database applies: see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/), [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [agent ecosystem research](/research/rise-of-chinese-ai-agents/).

## Related entities

- Models: [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) · [Qwen3.8-Max](/models/qwen38-max/) — the agent-capable flagships that would be the natural GAIA candidates.
- Comparison: [DeepSeek-V4-Pro vs Qwen3.8-Max](/comparisons/deepseek-v4-pro-vs-qwen38-max/).
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and methodology from the primary paper and official repository), **China AI Hub analysis** (our synthesis of how to read scores, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published a GAIA result.*
