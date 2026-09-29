---
image: "/images/ai/models-glm-5.2.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.2
model_name: GLM-5.2
provider: zhipu-ai
model_family: GLM-5
release_date: "2026-06-16"
status: deprecated
architecture: "744B total / 40B active (open weights, BF16/FP8)"
parameter_information:
  total_parameters: "744B"
  active_parameters: "40B"
context_window: 1048576
maximum_output: 163840
benchmark_results:
  - benchmark: HLE
    score: "40.5 (text-only)"
    metric: accuracy
    date: "2026-06"
    source_type: vendor_reported
    source_url: https://huggingface.co/zai-org/GLM-5.2
  - benchmark: HLE
    score: "54.7 (w/ tools)"
    metric: accuracy
    date: "2026-06"
    source_type: vendor_reported
    source_url: https://huggingface.co/zai-org/GLM-5.2
  - benchmark: SWE-bench Pro
    score: "62.1"
    metric: resolved
    date: "2026-06"
    source_type: vendor_reported
    source_url: https://huggingface.co/zai-org/GLM-5.2
capabilities:
  reasoning: true
  coding: true
  vision: false
  tool_calling: true
  agent_capability: true
open_weight: true
license: "MIT (pure open, no regional limits per official model card)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 1.4
  output_price_per_1m: 4.4
  currency: USD
  pricing_ref: zhipu-ai
official_api: true
cloud_providers:
  - Z.ai
  - BigModel
regions:
  - international
  - china
known_limitations:
  - "Superseded by GLM-5.3 (same base model, improved post-training) but still listed on the API pricing page at the same price"
  - "Text-only input; reasoning supports high/max only"
last_verified: "2026-09-27"
sources:
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai pricing
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai release notes
    source_url: https://docs.z.ai/release-notes/new-released
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — GLM-5.2 (benchmarks, license, 1M context)
    source_url: https://huggingface.co/zai-org/GLM-5.2
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

**What it is.** GLM-5.2 (2026-06-16) is Zhipu AI's previous flagship text model: a 744B-total / 40B-active open-weight model with a 1M-token context window, released under the MIT license. **Why it matters.** It is the direct predecessor of GLM-5.3 and remains listed on the API pricing page at the same price, making it a live reference point for the post-training gains of its successor. **Key characteristics.** Text-only input, reasoning in high/max modes, 1M context, 163,840 max output. **What a professional should know.** It is deprecated and superseded by GLM-5.3 (same base model, improved post-training), so new workloads should prefer GLM-5.3 — but GLM-5.2 remains billable and is worth tracking if you pinned a specific checkpoint.

## Architecture and parameters

GLM-5.2 is a 744B-total / 40B-active MoE (~5.4% activation), with open weights in BF16 and FP8. It shares this base with GLM-5.3, which means the entire GLM-5.2→5.3 delta is post-training, not architecture. China AI Hub analysis: that makes the pair a clean controlled comparison for how much post-training alone can move a fixed model. See [Mixture-of-Experts](/technology/mixture-of-experts/).

## What the context window actually means

The 1M-token context with a 163,840 output cap sits between GLM-5.3's 131K and DeepSeek's 393K on generation headroom. As a long-input analysis tool it matches the frontier norm. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

$1.40 input / $4.40 output per 1M tokens (cached $0.26) — identical to GLM-5.3. Because the successor costs the same, there is no price reason to stay on GLM-5.2; the pricing page simply has not retired it. See the [pricing-changed research](/research/chinese-ai-model-pricing-changed/).

## API, coding, and agent implications

Vendor-reported HLE 40.5 (text-only) / 54.7 (with tools) and SWE-bench Pro 62.1 describe the pre-5.3 capability baseline. The with-tools HLE delta is the same agentic pattern seen across the database. For coding and agent work, GLM-5.3's claimed post-training gains (including the private Code Bench "50%" improvement) argue for the successor. See [GLM agent-oriented AI](/research/glm-agent-oriented-ai/).

## Open weights and license

Open weight, MIT license — described in the official model card as "pure open, no regional limits," which is notably cleaner than the Apache-2.0-with-verification note on GLM-5.3. Teams that specifically want an MIT-licensed 1M-context GLM checkpoint may prefer 5.2 on licensing grounds despite the deprecation. See [licensing explained](/research/chinese-ai-model-licensing-explained/).

## Benchmark interpretation

The three rows are vendor-reported. HLE 40.5 (54.7 with tools) and SWE-bench Pro 62.1 are the GLM-5.2 baseline against which GLM-5.3's improvements are claimed. The with-tools HLE delta (40.5 → 54.7) mirrors the agentic pattern seen across the database, where tool access raises the ceiling on the hardest knowledge benchmarks. These scores are useful as a historical baseline, not as a current competitive signal.

## Context and output in practice

The 1M-token input window places GLM-5.2 at the frontier norm of its release wave, but its 163,840-token output cap is worth noting because it actually exceeds GLM-5.3's 131,072 ceiling — an artifact of the two models' separate documentation rather than a capability regression. For long-input analysis (multi-document review, codebase-wide context) the input window is what matters; for generation, both models are long-input tools rather than long-form generators.

## What the benchmarks do not prove

Scores are vendor-reported and predate the 5.3 successor; they say nothing about GLM-5.3's actual gains, which rest on a private benchmark. As a deprecated model, the main utility is historical comparison. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** text-only long-context analysis where an MIT-licensed (no-verification) open checkpoint is specifically required, and historical/regression baselines against GLM-5.3. **Less suited:** any new production workload (deprecated, superseded), vision/multimodal input, and cost-optimization (same price as the better successor).

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | High |
| Structured API workflows | Moderate |
| Agent orchestration | High |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates GLM-5.2's residual value is almost entirely as a licensing option and a historical baseline: its MIT "pure open" label is cleaner than its successor's Apache-2.0-with-caveat, and its benchmark set is the reference point for GLM-5.3's claimed gains. For everyone else, the model is deprecated at identical pricing, which makes staying on it a strictly dominated choice — the successor costs the same and improves on the same base.

## Market position and outlook

China AI Hub analysis indicates GLM-5.2 illustrates a recurring pattern in the database: deprecation is not retirement. The 2026-09-10 DeepSeek change-log reversal kept DeepSeek-V4-Pro's API running past its announced cutoff, and GLM-5.2 similarly remains billable on Z.ai's pricing page at the same $1.40/$4.40 as its successor. The practical consequences are threefold: existing integrations continue to function, the model stays useful as a regression baseline for measuring GLM-5.3's claimed post-training gains, and its MIT "pure open, no regional limits" label keeps it relevant for teams that specifically want a permissive, no-verification 1M-context GLM checkpoint. For everyone else the model is a strictly dominated choice — the successor costs the same and improves on the same base. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and [licensing explained](/research/chinese-ai-model-licensing-explained/) research.

## What is uncertain

- It is superseded by GLM-5.3 but remains billable at the same price — a deprecation without retirement.
- Benchmark scores are vendor-reported and predate the GLM-5.3 successor.
- GLM-5.3's claimed gains rest on the private Z.ai Code Bench and cannot be independently reproduced.

## Sources

- [Z.ai docs — GLM-5.3 model page](https://docs.z.ai/guides/llm/glm-5.3)
- [Z.ai pricing](https://docs.z.ai/guides/overview/pricing)
- [Z.ai release notes](https://docs.z.ai/release-notes/new-released)
- [Hugging Face model card — GLM-5.2](https://huggingface.co/zai-org/GLM-5.2)

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores published by Zhipu), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
