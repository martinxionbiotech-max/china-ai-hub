---
benchmark_id: coding-agent-benchmarks
benchmark_name: "Coding and Terminal Benchmarks"
description: "SWE-bench, Terminal-Bench, DeepSWE and LiveCodeBench compared: what each measures about coding models, the scores Chinese models publish, and the harness problem."
task_type: "Repository-level issue resolution, command-line task completion, software engineering and competitive programming"
dataset_size: "SWE-bench 2,294 issues (Verified 500) · Terminal-Bench containerised tasks · DeepSWE repository tasks · LiveCodeBench rolling contest problems"
evaluation_method: "Agentic runs against real repositories and containers, graded by tests passing; LiveCodeBench by hidden test cases"
scoring: "Percent resolved (pass@1 unless stated); LiveCodeBench pass@1 per problem"
caveat: "Coding results are only comparable inside the same harness: SWE-bench Verified, full SWE-bench and agentic variants produce very different numbers, and Terminal-Bench scores move with the time limit, retry budget and whether the agent may install packages. A vendor quoting a coding benchmark without its variant and harness has told you almost nothing."
contamination_notes: "SWE-bench issues are public and older splits are likely contaminated; LiveCodeBench filters by publication date for exactly this reason. Treat pre-2025 SWE-bench numbers as upper bounds."
limitations: "Harness details are rarely published in full. Where a vendor reports only a headline, this page records the number with its source type and does not adjust it."
member_ids: [swe-bench, terminal-bench, deepswe, livecodebench]
last_verified: "2026-11-05"
evaluations:
  - benchmark: SWE-bench
    model: qwen3.8-max
    score: 67.7
    model_version: "Pro"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: SWE-bench
    model: minimax-m3
    score: 59.0
    model_version: "Pro"
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/blog/minimax-m3
  - benchmark: SWE-bench
    model: kimi-k2.5
    score: 76.8
    model_version: "Verified"
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: SWE-bench
    model: minimax-m2
    score: 69.4
    model_version: "Verified"
    metric: accuracy
    date: "2025-10"
    source_type: vendor_reported
    source_url: https://github.com/MiniMax-AI/MiniMax-M2
  - benchmark: SWE-bench
    model: minimax-m2
    score: 56.5
    model_version: "Multilingual"
    metric: accuracy
    date: "2025-10"
    source_type: vendor_reported
    source_url: https://github.com/MiniMax-AI/MiniMax-M2
  - benchmark: Terminal-Bench
    model: deepseek-v4-1-flash
    score: 90.6
    model_version: "2.1"
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench
    model: deepseek-v4-pro
    score: 87.9
    model_version: "2.1"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench
    model: qwen3.8-max
    score: 86.6
    model_version: "2.1"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: Terminal-Bench
    model: kimi-k3
    score: 88.3
    model_version: "2.1"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: Terminal-Bench
    model: minimax-m3
    score: 66.0
    model_version: "2.1"
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/blog/minimax-m3
  - benchmark: Terminal-Bench
    model: glm-5.3
    score: 28.3
    model_version: "3.0"
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: Terminal-Bench
    model: glm-5.2
    score: 4.6
    model_version: "3.0"
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: Terminal-Bench
    model: kimi-k2.5
    score: 50.8
    model_version: "2.0"
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: Terminal-Bench
    model: minimax-m2
    score: 46.3
    model_version: "version not stated in source"
    metric: accuracy
    date: "2025-10"
    source_type: vendor_reported
    source_url: https://github.com/MiniMax-AI/MiniMax-M2
  - benchmark: DeepSWE
    model: deepseek-v4-1-flash
    score: 74.2
    model_version: "v1.1"
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE
    model: deepseek-v4-pro
    score: 62.7
    model_version: "version not stated in source"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE
    model: qwen3.8-max
    score: 56.6
    model_version: "v1.1"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: DeepSWE
    model: kimi-k3
    score: 67.5
    model_version: "67.3 with mini-SWE-agent harness"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: DeepSWE
    model: glm-5.3
    score: 66.9
    model_version: "v1.1"
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
  - benchmark: DeepSWE
    model: glm-5.3-flash
    score: 63.4
    model_version: "v1.1"
    metric: accuracy
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
sources:
  - source_name: "SWE-bench official repository"
    source_url: https://github.com/SWE-bench/SWE-bench
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: Qwen3.8-2.4T-A95B model card
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax M3 official blog post
    source_url: https://www.minimax.cn/blog/minimax-m3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K2.5 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "Terminal-Bench official repository (laude-institute)"
    source_url: https://github.com/laude-institute/terminal-bench
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "DeepSWE official repository (DataCurve)"
    source_url: https://github.com/datacurve-ai/deep-swe
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
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
---

**Short answer.** Four benchmarks dominate Chinese coding claims: SWE-bench, Terminal-Bench, DeepSWE and LiveCodeBench. They measure different things — repository issue resolution, command-line work, end-to-end software engineering and competitive programming — and their scores are only comparable within the same harness version.

## The four, side by side

| Benchmark | Task | Unit of work | What a high score means |
|---|---|---|---|
| SWE-bench | Fix a real GitHub issue | One repository, one patch | Can localise and repair code in a large codebase |
| Terminal-Bench | Complete a task in a shell | Container session | Can operate a terminal, install, inspect and recover |
| DeepSWE | Multi-step software engineering | Repository task, multiple steps | Can plan and execute across files |
| LiveCodeBench | Solve a contest problem | Single function | Strong algorithmic reasoning, low contamination |

The distinction is practical. A model that leads SWE-bench may fail Terminal-Bench, because the second requires environment manipulation rather than code reading. A model that leads LiveCodeBench may be a poor agent, because contest problems are single-shot.

## SWE-bench

The benchmark that made "agentic coding" measurable: 2,294 real GitHub issues, with a Verified subset of 500 human-checked items. The model must produce a patch that makes the failing tests pass without breaking others.

Three things decide the number: the subset (Verified vs full), the harness (which tools the agent may use, how many attempts), and the model's context handling on a large repository. Vendors frequently report "SWE-bench" without stating any of the three.

## Terminal-Bench

Tasks are completed inside a container: install a package, fix a config, recover a broken service. Scoring is task success within a time limit.

This is the closest public proxy for "can the model operate a computer", and it is also the most harness-sensitive: time limit, retry policy and network access change results materially. A Terminal-Bench score with no stated budget is a demo, not a measurement.

## DeepSWE

Multi-step software engineering tasks that require planning across files rather than a single patch. Its value is that it separates "can write a function" from "can carry out a change", which is the actual job.

Because the harness varies, DeepSWE numbers should be read as a relative signal between models evaluated by the same lab, not as an absolute capability level.

## LiveCodeBench

Contest-style problems published after model training cut-offs, which makes it the least contaminated coding benchmark in the set. The trade-off is narrowness: a single function against hidden tests measures algorithmic reasoning, not engineering.

Its date window moves, so a LiveCodeBench score is only comparable within the same problem range.

## The harness problem

Every benchmark in this group is really a benchmark of a *system*: model plus tools plus retry policy plus time budget. Two vendors reporting the same benchmark name may be measuring different systems, and neither may publish enough detail to tell.

Practical rule: compare only numbers published with the same harness version, and treat any cross-vendor comparison without harness disclosure as indicative at best.

## Our read

**SWE-bench Verified is the only coding number worth tracking across vendors — and only when the harness is stated.** The full set is contaminated and the agentic variants are incomparable. A vendor that reports "SWE-bench 70%" without saying Verified, harness and attempts has produced a marketing figure.

**Terminal-Bench is the better predictor of agent reliability, and almost nobody publishes it properly.** Real work happens in a shell: installs fail, paths are wrong, services need restarting. Models that score well here tend to survive production; models that only score on SWE-bench often do not.

**LiveCodeBench's contamination control is its whole value.** If you need to know whether a model can reason about algorithms rather than recall solutions, this is the cleanest signal available — provided the date window is stated.

**Judge coding models on failure recovery, not first-attempt success.** None of these benchmarks measures what buyers actually experience: how the model behaves after a test fails. That gap is why leaderboard leaders can disappoint in a real repository.
