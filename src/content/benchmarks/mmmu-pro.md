---
benchmark_id: mmmu-pro
benchmark_name: MMMU-Pro
description: "Multimodal, multi-discipline understanding benchmark with college-level questions requiring reasoning."
evaluations:
  - benchmark: MMMU-Pro
    model: kimi-k3
    score: "81.6 (83.4 with tools)"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: MMMU-Pro
    model: kimi-k2.5
    score: 78.5
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
limitations: "All scores are vendor-reported and not independently verified. With-tools and without-tools results are not directly comparable."
last_verified: "2026-09-20"
sources:
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi K2.5 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
