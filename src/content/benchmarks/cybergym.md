---
image: "/images/ai/benchmarks-cybergym.webp"
image_credit: "AI-generated illustration (Seedream)"
benchmark_id: cybergym
benchmark_name: CyberGym
description: "Cybersecurity agent benchmark focused on vulnerability discovery tasks."
task_type: "Cybersecurity vulnerability analysis (real-world vulnerability discovery)"
dataset_size: "Large-scale task suite sourced from ARVO and OSS-Fuzz (~240GB data)"
evaluation_method: "Docker-isolated environments; agents analyze vulnerabilities and generate proofs of concept; pre-/post-patch versions"
scoring: "Success rate on vulnerability analysis tasks (PoC generation)"

evaluations:
  - benchmark: CyberGym
    model: deepseek-v4-1-flash
    score: 88.1
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: CyberGym
    model: deepseek-v4-pro
    score: 83.3
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: CyberGym
    model: glm-5.3
    score: 84.5
    model_version: "vuln discovery (GLM-5.2: 77.2)"
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
limitations: "All scores are vendor-reported and not independently verified."
last_verified: "2026-09-20"
sources:
  - source_name: "CyberGym official repository (Sunblaze UC Berkeley)"
    source_url: https://github.com/sunblaze-ucb/cybergym
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
---
Cybersecurity agent benchmark focused on vulnerability discovery tasks. The table below lists 3 recorded evaluations across 3 models: deepseek-v4-1-flash, deepseek-v4-pro, glm-5.3. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
