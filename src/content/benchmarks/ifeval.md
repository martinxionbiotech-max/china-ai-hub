---
benchmark_id: ifeval
benchmark_name: IFEval
description: "Instruction-Following Eval: a benchmark of verifiable instructions ('write over 400 words', 'mention a keyword at least 3 times') that checks whether a model actually obeys precise natural-language constraints, scored by rule-checking rather than an LLM judge."
task_type: "Instruction following on verifiable natural-language constraints (length, format, keyword counts, etc.)"
dataset_size: "25 types of verifiable instructions; approximately 500 prompts, each containing one or more verifiable instructions"
evaluation_method: "Prompts carry rule-checkable instructions; a program verifies whether each constraint was satisfied"
scoring: "Strict accuracy and prompt-level / instruction-level accuracy (fraction of instructions followed)"
contamination_notes: "Rule-checked verification (not an LLM judge) reduces evaluator bias; the verifiable-instruction format is not tied to a single knowledge cutoff."
limitations: "IFEval measures only mechanical, rule-checkable instruction following — it does not capture semantic quality, helpfulness or correctness of the response content. No Chinese model in the China AI Hub database currently publishes an IFEval score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Zhou et al. — Instruction-Following Evaluation for Large Language Models (IFEval)"
    source_url: https://arxiv.org/abs/2311.07911
    source_type: academic
    published_date: "2023-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "IFEval — Google Research (instruction_following_eval)"
    source_url: https://github.com/google-research/google-research/tree/master/instruction_following_eval
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** IFEval — **Instruction-Following Eval** — measures whether a model actually obeys precise, verifiable natural-language instructions, such as "write more than 400 words" or "mention the keyword 'AI' at least three times". It is graded by a deterministic program rather than an LLM judge, which makes it a reproducible test of instruction discipline.

## What it measures

IFEval measures a specific and under-tested capability: **instruction following**. Rather than asking whether an answer is *good*, it asks whether the model did exactly what it was told. The prompts carry "verifiable instructions" — constraints that can be checked mechanically, like word counts, number of sections, keyword mentions, or formatting requirements.

This matters for function-calling and agent use, where a model that paraphrases the intent but ignores a hard constraint will break a downstream system. IFEval's focus on rule-checkable constraints makes it the standard reference for this slice of reliability.

## How it works

IFEval defines **25 types of verifiable instructions** and builds approximately **500 prompts**, each containing one or more of them. After generation, a **deterministic program** checks each constraint — not a language-model judge — and reports:

- **Strict accuracy** — the fraction of prompts where *every* instruction was followed;
- **Prompt-level accuracy** — prompts where all instructions satisfied;
- **Instruction-level accuracy** — the fraction of individual instructions followed.

The rule-based verification is the benchmark's key strength: it removes the evaluator bias and reproducibility problems that plague LLM-judged benchmarks. The code and data are in Google Research's `instruction_following_eval` repository.

## What it does NOT measure

IFEval measures only **mechanical, rule-checkable** instruction following. It does not measure semantic quality, helpfulness, correctness of the answer's content, or open-ended reasoning — a model can follow every instruction and still produce a useless or wrong answer. It is a narrow reliability probe, not a general capability score.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes an IFEval score. The tracked models — [Qwen3.8-Max](/models/qwen38-max/), [GLM-5.3](/models/glm-53/), [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) and others — publish on reasoning and coding benchmarks but not on IFEval. This page records **no evaluations**, and we do not import IFEval numbers from third-party sources. Treat any IFEval figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read IFEval results

China AI Hub analysis: IFEval is best read as a **reliability** metric for instruction and function-calling discipline, most relevant to developers building structured pipelines. Distinguish strict accuracy from prompt-level accuracy — the stricter the aggregation, the more it rewards complete compliance. As with every benchmark, confirm the exact setting before comparing; see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## IFEval and function calling

IFEval matters for the same reason function calling and structured output matter in this database: a model that paraphrases an instruction but ignores a hard constraint will break a downstream pipeline, however fluent its answer. IFEval isolates exactly that risk by testing only **rule-checkable** constraints and grading them with a deterministic program. This is its defining virtue — it removes the evaluator bias and irreproducibility of LLM-judged benchmarks — and its defining limit: it says nothing about whether the answer content is actually good.

The three aggregation levels deserve emphasis when reading a score. **Strict accuracy** requires every instruction in a prompt to be followed; **instruction-level accuracy** counts individual instructions satisfied even within a partially-failed prompt. A model can post a high instruction-level number and a much lower strict number, so the aggregation must be stated. For models in this database that advertise function-calling and structured output — such as [Qwen3.8-Max](/models/qwen38-max/) — an IFEval-style measure would be the natural reliability check, though none publishes one yet.

## Related entities

- Models: [Qwen3.8-Max](/models/qwen38-max/) · [GLM-5.3](/models/glm-53/) · [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) — the structured-output and function-calling flagships that would be the natural IFEval candidates.
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and scoring from the primary paper and official repository), **China AI Hub analysis** (our synthesis of what IFEval tells you, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published an IFEval result.*
