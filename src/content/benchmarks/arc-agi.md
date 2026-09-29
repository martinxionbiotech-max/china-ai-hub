---
benchmark_id: arc-agi
benchmark_name: ARC-AGI
description: "The Abstraction and Reasoning Corpus for AGI: grid-based visual reasoning tasks that are trivial for humans but have historically defeated frontier language models, used to measure general fluid intelligence."
task_type: "Grid-based abstract visual reasoning — infer an input→output transformation and apply it to new grids"
dataset_size: "ARC-AGI-1: 400 training + 400 public evaluation tasks; newer families (ARC-AGI-2, ARC-AGI-3) add fresh task sets"
evaluation_method: "A task is solved if the model produces the correct output grid for every test input (up to 3 trials per input)"
scoring: "Accuracy (% of tasks solved); a task counts only if all test inputs are correct"
contamination_notes: "Evaluation tasks are held out; ARC-AGI-2 and ARC-AGI-3 introduce new task families to counter overfitting to ARC-AGI-1."
limitations: "ARC-AGI measures a specific form of abstraction, not general model quality; visual-grid reasoning is only weakly correlated with useful real-world task performance. No Chinese model in the China AI Hub database currently publishes an ARC-AGI score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Chollet — On the Measure of Intelligence (introducing ARC)"
    source_url: https://arxiv.org/abs/1911.01547
    source_type: academic
    published_date: "2019-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "ARC-AGI repository (fchollet)"
    source_url: https://github.com/fchollet/ARC-AGI
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "ARC Prize / ARC-AGI"
    source_url: https://arcprize.org
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** ARC-AGI is the **Abstraction and Reasoning Corpus**, a benchmark of grid-based visual reasoning tasks that are trivially easy for humans but have historically defeated even frontier language models. It is designed to measure general fluid intelligence — learning a rule from a few examples and applying it to a new case — rather than memorised knowledge.

## What it measures

ARC-AGI measures **abstraction and few-shot generalisation**. Each task shows a small set of input grids and their corresponding output grids, and the model must infer the underlying transformation and produce the correct output grid for unseen test inputs. The transformations are things humans grasp instantly — pattern completion, symmetry, counting, object manipulation — but they are deliberately built on priors that are "as close as possible to innate human priors", in François Chollet's framing.

The benchmark's central claim is that scaling and memorisation do not by themselves produce this kind of fluid intelligence, which is why ARC-AGI became a reference for the "is scaling enough to reach AGI?" debate.

## How it works

A task is counted as **solved** only if the model produces the correct output grid for **every** test input in the task, including the correct grid dimensions. Each test input allows up to **3 trials** — a standardised rule that applies to both humans and AI systems.

Scoring is **accuracy**: the percentage of tasks solved. The original release (ARC-AGI-1) contains 400 training tasks and 400 public evaluation tasks. Newer families — **ARC-AGI-2** and **ARC-AGI-3** — introduce fresh task sets specifically to counter overfitting to ARC-AGI-1, so scores are only comparable within a single benchmark version. The benchmark is maintained in the `fchollet/ARC-AGI` repository and by ARC Prize (`arcprize.org`).

## What it does NOT measure

ARC-AGI is a deliberately narrow probe of a specific cognitive ability. It does **not** measure language, knowledge, coding, or useful real-world task performance, and success on ARC-AGI does not translate directly into practical assistant quality. Conversely, a poor ARC-AGI score does not mean a model is useless — it means the model lacks a particular kind of fluid abstraction that humans have and most LLMs historically lacked.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes an ARC-AGI score. The tracked reasoning models — [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), [Qwen3.8-Max](/models/qwen38-max/), [Kimi K3](/models/kimi-k3/) and others — publish on GPQA Diamond, HLE and coding benchmarks, but not on ARC-AGI. This page records **no evaluations**, and we do not import ARC-AGI numbers from third-party sources. Treat any ARC-AGI figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read ARC-AGI results

China AI Hub analysis: ARC-AGI is best read as a measure of *fluid abstraction*, not overall model quality, and only within a single benchmark version. Its value is diagnostic — separating memorisation-driven performance from generalisation — rather than as a buying criterion. See [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/), [How to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [state of China's AI models](/research/state-of-chinas-ai-models-2026/).

## Related entities

- Models: [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) · [Qwen3.8-Max](/models/qwen38-max/) · [Kimi K3](/models/kimi-k3/) — the reasoning flagships that would be the natural ARC-AGI candidates.
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design, scoring and task format from the primary paper and official repository), **China AI Hub analysis** (our synthesis of what ARC-AGI does and does not tell you, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published an ARC-AGI result.*
