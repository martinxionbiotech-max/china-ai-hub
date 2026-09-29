---
image: "/images/ai/models-deepseek-v4-1-flash.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: deepseek-v4-1-flash
model_name: DeepSeek-V4.1-Flash
provider: deepseek
model_family: DeepSeek-V4.1
release_date: "2026-09-10"
status: active
architecture: "552B-parameter MoE; Causal Encoder-Decoder; 8B active parameters on input, 16B on output"
parameter_information:
  total_parameters: "552B"
  active_parameters: "8B (input) / 16B (output)"
context_window: 1048576
maximum_output: 393216
capabilities:
  reasoning: true
  coding: true
  vision: true
  tool_calling: true
  function_calling: true
  structured_output: true
open_weight: true
license: MIT
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.15
  output_price_per_1m: 0.6
  currency: USD
  pricing_ref: deepseek
official_api: true
cloud_providers:
  - DeepSeek Platform
regions:
  - unknown
benchmark_results:
  - benchmark: GPQA Diamond
    score: 90.9
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: HLE
    score: 36.8
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Codeforces
    score: 3471
    metric: rating
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: Terminal-Bench 2.1
    score: 90.6
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: DeepSWE v1.1
    score: 74.2
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
known_limitations:
  - "Pricing is peak/off-peak: listed prices are off-peak; peak (01:00-04:00 and 06:00-10:00 UTC, Mon-Fri) is 2x"
  - "Benchmarks are vendor-reported using DeepSeek Harness (minimal mode, max effort); not independently verified"
  - "HLE score is on the pure-text subset (39.1 on that subset; 36.8 full)"
  - "Legacy API names deepseek-v4-flash and deepseek-v4-flash-vision-exp route to V4.1-Flash"
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
  - source_name: DeepSeek-V4.1-Flash release announcement
    source_url: https://www.deepseek.com/en/news/deepseek-v4-1-flash/
    source_type: official
    published_date: "2026-09-10"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — DeepSeek-V4.1-Flash
    source_url: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** DeepSeek-V4.1-Flash is DeepSeek's current standard API model (`deepseek-flash`), released 2026-09-10 with MIT-licensed open weights. It is the smallest member of the V4.1 "asymmetric architecture" family: a 552B-parameter MoE that activates only 8B parameters on input and 16B on output. **Why it matters.** It is the model most DeepSeek API callers will actually touch, and it now carries the 1M-token context window at flash-tier pricing — long context no longer costs a premium at the entry tier. **Key characteristics.** 1,048,576-token context, 393,216-token output, thinking (default) and non-thinking modes, native vision, JSON output and tool calling. **What a professional should know.** Pricing is peak/off-peak (off-peak $0.15 input / $0.60 output per 1M tokens, peak 2x), and the benchmark scores are vendor-reported via the DeepSeek Harness, not independently re-measured.

## Architecture and parameters

V4.1-Flash is the most aggressively sparse model in the database: 552B total parameters but only 8B active on input and 16B on output — a roughly 1.4% / 2.9% activation split, the only published input/output activation asymmetry in the collection. DeepSeek describes it as a Causal Encoder-Decoder MoE and claims 1/4 the HBM and 1/8 the SSD KV-cache storage of the previous generation. China AI Hub analysis: the architectural logic is cost — at $0.15 input, only a model this sparse can sustain margin. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 1M-token context at flash price is the notable fact here: V4.1-Flash is one of three flash-tier models (with Qwen3.8-Flash and GLM-5.3-Flash) that deliver the 1M window at the $0.15 floor. Practically this means long-document analysis, whole-repo context and extended agent traces are now available at entry pricing. The 393,216-token output is generous but still a fraction of input — treat it as long-input analysis, not long-form generation. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

Off-peak $0.15 input / $0.60 output, cache hits at $0.003, peak 2x during the documented weekday windows (01:00–04:00 and 06:00–10:00 UTC). The 4x input-to-output ratio and near-zero cache pricing reward agent workloads that re-read a large context across many turns. This is the price point the rest of the market converged on; see [pricing-changed research](/research/chinese-ai-model-pricing-changed/).

## API, coding, and agent implications

V4.1-Flash is the agentic-coding workhorse of the current DeepSeek lineup: vendor-reported Terminal-Bench 2.1 (90.6), Codeforces 3471, and DeepSWE v1.1 (74.2) are strong signals for terminal, competitive-programming and repository-scale agent tasks. Native vision and tool calling make it usable in multimodal agent loops, not just text. Legacy API names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` route here, so existing integrations continue to work. See the [DeepSeek-V4.1-Flash vs GLM-5.3-Flash](/comparisons/deepseek-v4-1-flash-vs-glm-53-flash/) comparison.

## Open weights and license

MIT-licensed and self-hostable. The same caveat as other large open models applies: weights exist, but running a 552B MoE (even sparse) requires substantial GPU memory, and the sparse/encoder-decoder design is non-trivial to serve efficiently outside DeepSeek's own stack. See [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

All five rows are vendor-reported. GPQA Diamond 90.9 signals strong graduate-level science QA; HLE 36.8 (39.1 on the pure-text subset) is a modest absolute score on the hardest knowledge exam; Codeforces 3471 is a competitive-programming rating, not an accuracy percentage, so it is not directly comparable to the other rows. The vendor notes these were produced with DeepSeek Harness in minimal mode at max effort.

## What the benchmarks do not prove

Vendor-reported scores under a specific harness do not generalize to your workload and are not comparable to other vendors' numbers without matching harness, benchmark version and tool setup. The HLE row illustrates the pitfall directly: a 36.8 "full" vs 39.1 "pure-text subset" gap that can be cited either way. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** high-volume API workloads, agentic coding, long-context analysis at low cost, multimodal (vision) tasks, and anything where cache-friendly re-reading dominates. **Less suited:** peak-time latency-sensitive or budget-critical jobs that cannot avoid the 2x peak window, and self-hosters without the GPU capacity for a 552B sparse model.

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

China AI Hub analysis indicates that V4.1-Flash is the clearest expression of the market's price-per-token economics: a 1.4%-activation MoE that delivers frontier-adjacent coding scores at the $0.15 floor. It inherits the V4-Pro's agentic-coding strengths while cutting active compute roughly 6x. The main risk is verification — every headline number is vendor-reported — and the peak/off-peak structure, which quietly doubles cost outside off-peak hours. As the successor to the now-deprecated V4-Pro API, it is the model DeepSeek's platform is standardizing on.

## Market position and outlook

China AI Hub analysis indicates V4.1-Flash is where DeepSeek's price-per-token strategy becomes explicit: at 1.4% activation it is the most aggressively sparse model in the collection, and its $0.15 off-peak input price is part of a three-way convergence the database documents — DeepSeek, Alibaba (Qwen3.8-Flash) and Zhipu (GLM-5.3-Flash) all list the same $0.15 flash-tier input. What distinguishes V4.1-Flash in that trio is the combination of 1M context, native vision and a 393K output ceiling at the floor price, which is why it has become the default entry point for DeepSeek's API. Legacy routing (`deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` → V4.1-Flash) further consolidates that position. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [context-window](/research/chinese-ai-context-windows/) research for the cross-lab comparison.

## What is uncertain

- Benchmark scores are vendor-reported via the DeepSeek Harness and not independently verified.
- The HLE score differs between the full set (36.8) and the pure-text subset (39.1).
- Serving regions are not disclosed.

## Sources

- [DeepSeek API docs — Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek API Change Log](https://api-docs.deepseek.com/updates)
- [DeepSeek-V4.1-Flash release announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
- [Hugging Face model card — DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores published by DeepSeek), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
