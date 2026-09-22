---
benchmark_id: swe-bench
benchmark_name: SWE-bench
description: "Software engineering benchmark family built from real GitHub issues, with Pro, Verified and Multilingual variants."
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
limitations: "Pro, Verified and Multilingual variants are different test sets and are not comparable to each other; the variant is recorded per evaluation. All scores are vendor-reported and not independently verified."
last_verified: "2026-09-20"
sources:
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
    confidence: high
---
Software engineering benchmark family built from real GitHub issues, with Pro, Verified and Multilingual variants. The table below lists 5 recorded evaluations across 4 models: qwen3.8-max, minimax-m3, kimi-k2.5, minimax-m2. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
