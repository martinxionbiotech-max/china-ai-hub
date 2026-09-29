---
benchmark_id: cmmlu
benchmark_name: CMMLU
description: "A comprehensive Chinese benchmark measuring massive multitask language understanding across 67 subjects, from STEM and humanities to China-specific knowledge such as driving rules."
task_type: "Chinese multiple-choice knowledge and reasoning questions across 67 subjects"
dataset_size: "67 subjects from elementary to advanced professional level; multiple-choice with 4 options and a single correct answer; a 5-question development set and a 100+ question test set per subject"
evaluation_method: "Multiple-choice; evaluated in zero-shot and five-shot settings, with and without chain-of-thought"
scoring: "Accuracy (% correct); the random baseline is 25%"
contamination_notes: "CMMLU maintainers verify API-only models for data contamination before listing them on the leaderboard; questions include China-specific answers less common in English training data."
limitations: "Multiple-choice format measures recognition and reasoning within fixed options, not free-form generation or grounding. Zero-shot and five-shot scores are not directly comparable. No Chinese model in the China AI Hub database currently publishes a CMMLU score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Li et al. — CMMLU: Measuring massive multitask language understanding in Chinese"
    source_url: https://arxiv.org/abs/2306.09212
    source_type: academic
    published_date: "2023-06"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "CMMLU official repository"
    source_url: https://github.com/haonan-li/CMMLU
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "CMMLU dataset card (Hugging Face)"
    source_url: https://huggingface.co/datasets/haonan-li/cmmlu
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** CMMLU measures massive multitask language understanding in Chinese across 67 subjects — from computational STEM to humanities, social sciences and China-specific knowledge such as Chinese driving rules. It is the Chinese-context counterpart to MMLU, and is designed so that a good score reflects genuine Chinese-domain knowledge rather than transfer from English training data.

## What it measures

CMMLU tests whether a model holds broad knowledge and reasoning ability **in the Chinese language and cultural context**. Its 67 subjects span natural science, social science, engineering and the humanities, and deliberately include many questions whose answers are China-specific — driving regulations, Chinese law, and other topics that are not well represented in English-language corpora. This is the benchmark's central design choice: it is meant to reveal whether a model has actually absorbed Chinese-domain knowledge, not whether it can translate an English answer.

A useful reference point from the paper is the **25% random baseline** and the observation that most models of its era struggled to reach even 50% average accuracy even with few-shot examples and chain-of-thought. That gap is why CMMLU became a standard Chinese evaluation target.

## How it works

CMMLU is a **multiple-choice** benchmark. Each question offers four options with a single correct answer, and models are evaluated in both **zero-shot and five-shot** settings, with and without chain-of-thought. The few-shot setting provides in-context examples from the same subject, which tests how well the model adapts to a Chinese task format.

Scoring is **accuracy** — the percentage of questions answered correctly — reported per subject and as an overall average. Because the subjects range from elementary to advanced professional level, the average is a breadth signal, while per-subject breakdowns show domain-specific strengths and weaknesses.

The benchmark is maintained in the `haonan-li/CMMLU` repository, with a public leaderboard and a Hugging Face dataset card. Notably, the maintainers **verify API-only models for data contamination** before adding them to the leaderboard — a rare safeguard against the "the model memorised the test" problem.

## What it does NOT measure

CMMLU does not measure free-form generation, factual grounding, coding, agentic behaviour or multimodal understanding — the multiple-choice format constrains the answer to four fixed options. It also does not produce a single comparable number across settings: a five-shot score is not the same measurement as a zero-shot score, and mixing them silently is a common error.

Like C-Eval, CMMLU is a dataset whose scores are self-reported by model builders (or reproduced by third parties on their own harnesses); the benchmark itself does not independently grade every model.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes a CMMLU score. The tracked models — [Qwen3.8-Max](/models/qwen38-max/), [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [GLM-5.3](/models/glm-53/) and others — publish on international and coding benchmarks but not on CMMLU. This page therefore records **no evaluations**, and we do not import CMMLU numbers from third-party leaderboards or vendor marketing. Treat any CMMLU figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read CMMLU results

China AI Hub analysis: a CMMLU score is a Chinese-domain knowledge signal, most useful for questions about localised knowledge tasks (education, regulation, consumer content). Before citing a number, confirm the shot setting (zero-shot vs five-shot), the subject coverage, and whether chain-of-thought was used. The version-and-setting discipline that applies across this database — never compare scores from different modes — applies here too; see [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Related entities

- Models: [Qwen3.8-Max](/models/qwen38-max/) · [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) · [GLM-5.3](/models/glm-53/) — Chinese general-purpose flagships, the natural CMMLU candidates.
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and methodology from the primary paper and official repository), **China AI Hub analysis** (our synthesis of how to read scores, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published a CMMLU result.*
