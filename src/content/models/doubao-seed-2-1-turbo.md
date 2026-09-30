---
image: "/images/ai/models-doubao-seed-2-1-turbo.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: doubao-seed-2-1-turbo
model_name: Doubao Seed 2.1 Turbo
provider: bytedance
model_family: Doubao Seed
version: "260628"
aliases:
  - doubao-seed-2-1-turbo-260628
release_date: "2026-06"
status: active
context_window: 262144
maximum_output: 262144
capabilities:
  reasoning: true
  vision: true
  tool_calling: true
  structured_output: true
  agent_capability: true
  computer_use: true
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 3.0
  output_price_per_1m: 15.0
  currency: CNY
  pricing_ref: bytedance
official_api: true
cloud_providers:
  - Volcengine Ark
regions:
  - china
known_limitations:
  - "Architecture and parameter counts are not publicly disclosed by ByteDance for the Seed 2.1 series (API-only model)"
  - "API served from cn-beijing region only; no international endpoint verified as of 2026-09-20"
  - "No open-weight release; no self-hosting"
last_verified: "2026-09-27"
sources:
  - source_name: Ark official model list
    source_url: https://docs.volcengine.com/docs/ark/model-list?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark official model pricing
    source_url: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Doubao Seed 2.1 Turbo is the lower-priced variant of ByteDance's Seed 2.1 family, served through the Volcengine Ark API with a 256K-token context window. **Why it matters.** It carries the same documented capability set as the Pro model — including GUI task handling and computer use — at half the price, making it ByteDance's entry point to the Seed 2.1 agent surface. **Key characteristics.** 262,144-token context and 262,144-token maximum output, deep thinking, multimodal understanding, tool calling, structured output, agent capability and computer use. **What a professional should know.** Architecture and parameter counts are not disclosed, the API is served from cn-beijing only (no international endpoint verified as of 2026-09-20), and pricing is in CNY — 3.00 input / 15.00 output per 1M tokens, cache hits 0.60.

## Architecture and parameters

ByteDance discloses no architecture or parameter counts for the Seed 2.1 series, and the database records that absence rather than estimating. China AI Hub analysis indicates this is the same closed-strategy posture the database records for all Doubao Seed models — no weights, no architecture card, capabilities and price instead. See [Mixture-of-Experts](/technology/mixture-of-experts/) for the architectural context ByteDance does not provide, and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 262,144-token context with a matching 262,144 output ceiling is a balanced mid-tier profile — a quarter of the Pro model's 1M input, but with a relatively generous output headroom for its class. It suits single-session agent tasks and multimodal document work, but not the long-horizon, 1M-window workloads ByteDance reserves for Pro and Evolving. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

3.00 CNY input / 15.00 CNY output per 1M tokens, cache hits at 0.60 (20% of input) — exactly half the Pro model's 6.00 / 30.00. China AI Hub analysis indicates the 5x input-to-output ratio matches the Seed family's generation-premium posture, and the half-price positioning is the defining fact: buyers get the full Seed 2.1 capability surface at half cost in exchange for a quarter of the context. A higher-priced low-latency tier (6.00 / 30.00) is also listed. See the [Turbo vs Pro comparison](/comparisons/doubao-seed-2-1-pro-vs-doubao-seed-2-1-turbo/) and [choosing-by-price](/guides/choosing-by-price/).

## API, coding, and agent implications

Seed 2.1 Turbo documents tool calling, structured output, agent capability, GUI task handling and computer use — the same broad agent surface as Pro, at half price. The operational caveat is regional: cn-beijing only, with no international endpoint verified, and CNY billing. See [computer use](/technology/computer-use/) and [AI agents](/technology/ai-agents/).

## Open weights and license

Proprietary, closed weight, no self-hosting. Like all Doubao Seed models, no downloadable weights are offered. See [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

No benchmark scores are recorded for Seed 2.1 Turbo in the database. This is an absence of evidence, not evidence of absence — ByteDance has not published Turbo-specific benchmark results on the fetched official pages.

## What the benchmarks do not prove

With no recorded benchmarks, there is nothing with which to rank Seed 2.1 Turbo against competitors, and its agent/coding claims rest on vendor positioning rather than published numbers. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** agent and computer-use applications within ByteDance's China ecosystem, GUI task handling, multimodal document analysis, and cost-sensitive workloads that need the Seed 2.1 capability surface at half price. **Less suited:** international API consumers (cn-beijing only), long-horizon 1M-context workloads, and any adoption decision requiring published architecture or benchmark evidence.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Moderate |
| Coding | Moderate |
| Structured API workflows | High |
| Agent orchestration | High |
| Local self-hosted deployment | No evidence |
| GUI automation | High |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates Seed 2.1 Turbo is ByteDance's price-tiered entry to the Seed 2.1 agent surface: it deliberately halves the Pro model's price and quarters its context, while keeping the capability set — including computer use — intact, which is a clean value trade rather than a capability cut. Against the rolling [Seed Evolving](/models/doubao-seed-evolving/) model, Turbo is the versioned, lower-cost alternative with a pinned checkpoint (260628), whereas Evolving is the 1M-context, continuously-updated premium line — so the choice between them is less about ability than about price, context size and reproducibility. The cn-beijing-only serving and absent benchmarks are the two adoption constraints that should be verified before production use. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research and the [multimodal hub](/models/multimodal/).

## What is uncertain

- Architecture and parameter counts are not publicly disclosed.
- No benchmark scores are published for Seed 2.1 Turbo.
- The API is served from cn-beijing only; no international endpoint was verified.
- The higher-priced low-latency tier's throughput is not separately documented.

## Sources

- [Ark official model list](https://docs.volcengine.com/docs/ark/model-list?lang=zh)
- [Ark official model pricing](https://docs.volcengine.com/docs/ark/model-pricing?lang=zh)

*Labels used above: **Official fact** (capabilities, pricing and region from Ark's docs) and **China AI Hub analysis** (our synthesis, always introduced as such). No benchmark evidence is currently recorded for this model.*
