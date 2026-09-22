---
image: "/images/ai/benchmarks-automationbench.webp"
image_credit: "AI-generated illustration (Seedream)"
benchmark_id: automationbench
benchmark_name: AutomationBench
description: "Benchmark of computer-use automation tasks."
evaluations:
  - benchmark: AutomationBench
    model: deepseek-v4-1-flash
    score: 54.8
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: AutomationBench
    model: deepseek-v4-pro
    score: 31.8
    model_version: "Public"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: AutomationBench
    model: qwen3.8-max
    score: 27.3
    model_version: "Pass@1"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: AutomationBench
    model: glm-5.3-flash
    score: 48.8
    model_version: "GLM-5.2: 26.2"
    metric: accuracy
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
limitations: "All scores are vendor-reported and not independently verified. Pass@1 vs other sampling settings differ between vendors."
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3-Flash model page
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
Benchmark of computer-use automation tasks. The table below lists 4 recorded evaluations across 4 models: deepseek-v4-1-flash, deepseek-v4-pro, qwen3.8-max, glm-5.3-flash. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
