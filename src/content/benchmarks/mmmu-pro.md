---
image: "/images/ai/benchmarks-mmmu-pro.webp"
image_credit: "AI-generated illustration (Seedream)"
benchmark_id: mmmu-pro
benchmark_name: MMMU-Pro
description: "Multimodal, multi-discipline understanding benchmark with college-level questions requiring reasoning."
task_type: "Multimodal understanding and reasoning (college-level, multi-discipline)"
dataset_size: "1,730 questions in standard format plus 1,730 vision-augmented variants (3,460 total); parent MMMU = 11.5K questions across 6 disciplines, 30 subjects"
evaluation_method: "Multiple-choice questions with interleaved images; vision-only input setting removes text leakage"
scoring: "Accuracy (% correct answers)"

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
  - source_name: "MMMU official repository"
    source_url: https://github.com/MMMU-Benchmark/MMMU
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
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
Multimodal, multi-discipline understanding benchmark with college-level questions requiring reasoning. The table below lists 2 recorded evaluations across 2 models: kimi-k3, kimi-k2.5. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
