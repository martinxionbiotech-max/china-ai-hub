---
benchmark_id: livecodebench
benchmark_name: LiveCodeBench
description: "A contamination-controlled coding benchmark that continuously collects fresh problems from LeetCode, AtCoder and Codeforces contests, plus self-repair, code-execution and test-output-prediction tasks."
task_type: "Competitive-programming code generation plus self-repair, code execution and test-output prediction"
dataset_size: "Continuously growing; initially 300+ problems from LeetCode, AtCoder and Codeforces contests (from May 2023 onward, updated over time)"
evaluation_method: "Models solve fresh contest problems released after a cutoff date; graded by executing code against hidden test cases"
scoring: "Pass@1 accuracy (% of problems solved correctly on the first submission)"
contamination_notes: "Problems are drawn from contests after a fixed cutoff date specifically to avoid contamination; the benchmark keeps adding new problems to stay ahead of training leakage."
limitations: "Pass@1 depends on sampling temperature and prompting, and on the execution sandbox. Newer problems are added continuously, so a score is always tied to a specific snapshot. No Chinese model in the China AI Hub database currently publishes a LiveCodeBench score, so this page records no evaluations."
last_verified: "2026-09-29"
sources:
  - source_name: "Jain et al. — LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"
    source_url: https://arxiv.org/abs/2403.07974
    source_type: academic
    published_date: "2024-03"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "LiveCodeBench website"
    source_url: https://livecodebench.github.io/
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "LiveCodeBench repository"
    source_url: https://github.com/LiveCodeBench/LiveCodeBench
    source_type: benchmark_org
    last_verified: "2026-09-29"
    confidence: high
---

**Short answer.** LiveCodeBench is a **contamination-controlled coding benchmark** that continuously collects fresh problems from LeetCode, AtCoder and Codeforces contests, and grades models by executing their code against hidden tests. Its purpose is to give a coding score that cannot be gamed by memorising an old test set.

## What it measures

LiveCodeBench measures real coding ability on problems that post-date a model's training cutoff. It draws from three competitive-programming platforms and adds new problems over time, so the benchmark stays ahead of training-data contamination — the failure mode that makes older benchmarks like HumanEval and MBPP increasingly unreliable.

Beyond code generation, LiveCodeBench also measures a **broader set of code capabilities**: self-repair (fixing a failing program), code execution (predicting what a program outputs), and test-output prediction. This makes it a more holistic coding benchmark than a pure "write a function" suite.

## How it works

LiveCodeBench collects problems from periodic contests on **LeetCode, AtCoder and Codeforces**, applying a time cutoff so that only problems published after a model's knowledge cutoff are eligible. A model's solution is then **executed against hidden test cases**, and a problem counts as solved only if the code passes the tests.

Scoring is **pass@1** — the fraction of problems solved correctly on the first submission. Because pass@1 depends on sampling temperature and prompting, it is a single-pass signal and is not the same as pass@k or a "best-of-n" figure. The benchmark is hosted at `livecodebench.github.io`, with the problem set and toolkit in the `LiveCodeBench/LiveCodeBench` repository, and it has evaluated dozens of base and instruction-tuned models.

## What it does NOT measure

LiveCodeBench does not measure general reasoning, knowledge or non-coding agentic skill. Pass@1 also has structural limits: it rewards a specific first-shot style and can understate models that improve with self-repair or longer sampling budgets. And because the problem set grows continuously, any score is tied to a **specific snapshot** — a "LiveCodeBench 60%" from one date is not the same measurement as a "LiveCodeBench 60%" from a year later.

## Chinese model results

**Not publicly documented.** As of 2026-09-29, no model page in the China AI Hub database publishes a LiveCodeBench score. The tracked coding models — [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/), [Kimi K2.7 Code](/models/kimi-k27-code/), [GLM-5.3-Flash](/models/glm-53-flash/) and others — publish on Terminal-Bench, SWE-bench and DeepSWE instead. This page records **no evaluations**, and we do not import LiveCodeBench numbers from third-party leaderboards. Treat any LiveCodeBench figure seen elsewhere as outside this database until a tracked model publishes one.

## How to read LiveCodeBench results

China AI Hub analysis: LiveCodeBench's value is its contamination control, which makes it a more trustworthy coding signal than older static benchmarks — provided the score's snapshot date and pass@1 setting are stated. For choosing a coding model, pair it with agentic-coding signals rather than reading it in isolation; see [Choosing a coding model](/guides/choosing-a-coding-model/), [Benchmark Methodology Divergence](/research/benchmark-methodology-divergence/) and [Chinese AI coding models](/research/chinese-ai-coding-models/).

## Related entities

- Models: [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) · [Kimi K2.7 Code](/models/kimi-k27-code/) · [GLM-5.3-Flash](/models/glm-53-flash/) — the coding-focused models that would be the natural LiveCodeBench candidates.
- Comparison: [DeepSeek-V4.1-Flash vs Qwen3.8-Flash](/comparisons/deepseek-v4-1-flash-vs-qwen38-flash/).
- See all [benchmarks](/benchmarks/).

*Labels used on this page: **Official fact** (benchmark design and methodology from the primary paper and official repository), **China AI Hub analysis** (our synthesis of how to read scores, introduced as such). No **vendor-reported claim** or **third-party evidence** is recorded for this benchmark, because no tracked Chinese model has published a LiveCodeBench result.*
