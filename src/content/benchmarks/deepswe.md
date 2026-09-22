---
benchmark_id: deepswe
benchmark_name: DeepSWE
description: "Software engineering benchmark built from real-world issues and pull requests."
evaluations:
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
limitations: "All scores are vendor-reported and not independently verified. Some vendors do not state the benchmark version; unversioned scores should not be compared with versioned ones."
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
Software engineering benchmark built from real-world issues and pull requests. The table below lists 6 recorded evaluations across 6 models: deepseek-v4-1-flash, deepseek-v4-pro, qwen3.8-max, kimi-k3, glm-5.3, glm-5.3-flash. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
