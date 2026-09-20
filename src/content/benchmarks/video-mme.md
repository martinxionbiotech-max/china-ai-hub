---
benchmark_id: video-mme
benchmark_name: Video-MME
description: "Video understanding benchmark spanning various video durations and domains."
evaluations:
  - benchmark: Video-MME
    model: kimi-k3
    score: 90.0
    model_version: "with subtitles"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: Video-MME
    model: kimi-k2.5
    score: 87.4
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
limitations: "All scores are vendor-reported and not independently verified. Subtitle usage differs between evaluations."
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
