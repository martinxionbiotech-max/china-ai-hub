---
benchmark_id: terminal-bench
benchmark_name: Terminal-Bench
description: "Terminal-based agent benchmark (shell commands, file operations, package management and other command-line tasks)."
evaluations:
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
limitations: "Benchmark versions (2.0 / 2.1 / 3.0) are not comparable to each other; the version is recorded per evaluation. All scores are vendor-reported and not independently verified."
last_verified: "2026-09-20"
sources:
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
    confidence: high
---
Terminal-based agent benchmark (shell commands, file operations, package management and other command-line tasks). The table below lists 9 recorded evaluations across 9 models: deepseek-v4-1-flash, deepseek-v4-pro, qwen3.8-max, kimi-k3, minimax-m3, glm-5.3, glm-5.2, kimi-k2.5, minimax-m2. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
