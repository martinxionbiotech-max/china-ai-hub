---
image: "/images/ai/models-deepseek-v4-pro.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: deepseek-v4-pro
model_name: DeepSeek-V4-Pro
provider: deepseek
model_family: DeepSeek-V4
version: "0813"
aliases:
  - deepseek-v4-pro-0813
release_date: "2026-04-24 (V4 Preview) / 2026-08-13 (GA)"
status: deprecated
architecture: "MoE: 1.6T total / 49B active parameters"
parameter_information:
  total_parameters: "1.6T"
  active_parameters: "49B"
context_window: 1048576
maximum_output: 393216
capabilities:
  reasoning: true
  coding: true
  math: true
  vision: false
  tool_calling: true
  function_calling: true
  structured_output: true
open_weight: true
license: MIT
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.66
  output_price_per_1m: 1.98
  currency: USD
  pricing_ref: deepseek
official_api: true
cloud_providers:
  - DeepSeek Platform
regions:
  - unknown
benchmark_results:
  - benchmark: HLE
    score: "42.7 (60.0 with tools)"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench 2.1
    score: 87.9
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE
    score: 62.7
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Agents' Last Exam
    score: 25.7
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
known_limitations:
  - "Deprecation announced 2026-09-10: news page says V4-Pro requests will route to V4.1-Flash after 2026-09-14 until V4.1-Pro launches, but the same-day change log says V4-Pro API service continues with unchanged billing - the official pages conflict"
  - "Vision not supported"
  - "Open-weight HF checkpoint last modified 2026-06-22; unclear whether it matches the 0813 GA checkpoint"
  - "Pricing is peak/off-peak: listed prices are off-peak; peak is 2x"
last_verified: "2026-09-20"
sources:
  - source_name: DeepSeek API docs — Models & Pricing
    source_url: https://api-docs.deepseek.com/quick_start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek-V4 Preview release
    source_url: https://www.deepseek.com/en/news/v4-preview/
    source_type: official
    published_date: "2026-04-24"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V4-Pro
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** DeepSeek-V4-Pro is DeepSeek's flagship open-weight model: a 1.6T-parameter Mixture-of-Experts (MoE) with 49B active parameters, released under the MIT license. It served on the API from the V4 Preview (2026-04-24) and was updated to the 0813 GA checkpoint on 2026-08-13. **Why it matters.** It was DeepSeek's top-tier model for agentic coding, world knowledge and math/STEM before the V4.1 family began rolling out, and it remains one of the largest open-weight MoE models in the China AI Hub database. **Key characteristics.** A 1,048,576-token context window, 393,216-token maximum output, thinking (default) and non-thinking modes with `reasoning_effort` low/high/max, JSON output and tool calling — but no vision. **What a professional should know.** Deprecation was announced 2026-09-10, and the official pages disagree on whether the V4-Pro API continues unchanged after 2026-09-14 or routes requests to V4.1-Flash until V4.1-Pro launches. Anyone planning production workloads should resolve that conflict against the current change log before committing.

## Architecture and parameters

DeepSeek-V4-Pro is a sparse MoE: 1.6 trillion total parameters with 49 billion active per token. That 3.1% activation ratio is what makes the model economical to serve — only a small expert subset computes on any given input, so per-token cost is driven by active, not total, parameters. The trade-off, standard for MoE designs, is that total parameters still dictate memory and self-hosting footprint, which is why a 1.6T model is a multi-GPU deployment even though inference is sparse. See the site's [Mixture-of-Experts](/technology/mixture-of-experts/) explainer and the [Chinese MoE architectures research](/research/chinese-ai-moe-architectures/) for how this activation dial compares across labs.

## What the context window actually means

A 1,048,576-token context means V4-Pro can hold roughly 700,000–800,000 English words of working material in a single request — enough for whole-repository code review, multi-document legal or financial analysis, or very long agent traces. The 393,216-token output ceiling is large but a fraction of input, so V4-Pro is best read as a *long-input analysis* tool rather than a long-form *generation* tool. See the [context-window research](/research/chinese-ai-context-windows/) for how this input/output split fits the wider market.

## Pricing implications

List pricing is off-peak $0.66 input / $1.98 output per 1M tokens; peak windows are 2x (see the known-limitations list). The 3x input-to-output ratio is typical — output tokens bill at a premium because they consume more inference capacity. For long-context work this matters doubly: filling a 1M-token window and generating long outputs multiplies cost quickly, so cache-hit pricing and batch scheduling are where real savings live. Prices trace to the [DeepSeek pricing page](/pricing/deepseek/) and were verified 2026-09-20.

## API, coding, and agent implications

V4-Pro was DeepSeek's agentic-coding flagship: vendor-reported Terminal-Bench 2.1 (87.9) and DeepSWE (62.7) place it in the top tier of the database for terminal and repository-scale agent tasks. It exposes JSON output and tool calls, so it slots directly into function-calling and agent harnesses — the same machinery the [DeepSeek Harness](/agents/deepseek-harness/) product builds on. The deprecation notice is the operational caveat: with the V4.1 family superseding it, new integrations should prefer [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) unless a specific V4-Pro checkpoint is required. See the [DeepSeek vs Kimi K3](/comparisons/deepseek-v4-pro-vs-kimi-k3/) and [DeepSeek vs Qwen3.8-Max](/comparisons/deepseek-v4-pro-vs-qwen38-max/) comparisons for workload-level differences.

## Open weights and license

V4-Pro is MIT-licensed open weight and self-hostable. MIT is the most permissive standard license in the database — no attribution or revenue thresholds, unlike the conditional custom licenses used elsewhere. The practical caveat is verification: the Hugging Face checkpoint was last modified 2026-06-22, and it is not documented whether it matches the 0813 GA API checkpoint. Self-hosters should pin against that uncertainty. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

All four listed scores are vendor-reported. HLE 42.7 (60.0 with tools), Terminal-Bench 2.1 87.9, DeepSWE 62.7, and Agents' Last Exam 25.7 describe a strong coding/agentic profile with a modest absolute score on the hardest knowledge exam. The gap between the HLE base score and its with-tools score is itself informative: tool access materially raises the ceiling, which is the pattern behind agentic evaluation generally.

## What the benchmarks do not prove

These numbers do not establish that V4-Pro beats any specific competitor, and they cannot be compared across vendors without matching benchmark versions, evaluation harnesses and tool setups. The `source_type` is `vendor_reported` for every row — none are independently re-measured. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/) and the [benchmark-methodology research](/research/benchmark-methodology-divergence/) for the comparability traps.

## Suitable and less suitable workloads

**Well-suited:** agentic coding, repository-scale software work, long-document analysis, math/STEM reasoning, and any open-weight deployment where a permissive license and self-hosting matter. **Less suited:** vision and multimodal tasks (not supported), low-latency or low-cost chat where the flash tier is cheaper, and any production dependency that cannot tolerate the post-2026-09-14 deprecation ambiguity.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | High |
| Structured API workflows | High |
| Agent orchestration | High |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates that V4-Pro's situation — a large, MIT-licensed flagship marked deprecated while its API status is in flux — illustrates how quickly China's frontier layer turns over. Its off-peak $0.66/$1.98 pricing and 49B-active MoE design made it a strong cost/performance point at launch, but the V4.1 family's asymmetric, cheaper architecture superseded it within months. The model remains relevant to self-hosters who want a permissive 1.6T checkpoint, but API buyers should treat it as legacy and verify the current routing before reliance.

## What is uncertain

- The deprecation status is conflicting: the news page says V4-Pro routes to V4.1-Flash after 2026-09-14, but the same-day change log says the API continues unchanged.
- Whether the Hugging Face checkpoint (last modified 2026-06-22) matches the 0813 GA checkpoint is not documented.
- Serving regions are not disclosed.
- All four benchmark scores are vendor-reported; no independent third-party measurement is recorded.

## Sources

- [DeepSeek API docs — Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek API Change Log](https://api-docs.deepseek.com/updates)
- [DeepSeek-V4 Preview release](https://www.deepseek.com/en/news/v4-preview/)
- [Hugging Face model card — DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores published by DeepSeek), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
