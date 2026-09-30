---
image: "/images/ai/models-doubao-seed-evolving.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: doubao-seed-evolving
model_name: Doubao Seed Evolving
provider: bytedance
model_family: Doubao Seed
version: rolling
release_date: "2026-06"
status: active
context_window: 1048576
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
  input_price_per_1m: 6.0
  output_price_per_1m: 30.0
  currency: CNY
  pricing_ref: bytedance
official_api: true
cloud_providers:
  - Volcengine Ark
regions:
  - china
known_limitations:
  - "Architecture and parameter counts are not publicly disclosed by ByteDance for the Seed 2.1 series (API-only model)"
  - "Rolling model: at least one version update per week; capabilities can change under the same model ID"
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
  - source_name: Ark model release announcements
    source_url: https://docs.volcengine.com/docs/ark/model-release-announcement
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Doubao Seed Evolving is ByteDance's rolling, versionless model, first released June 2026 and updated at least once per week under a single stable model ID. **Why it matters.** It is ByteDance's continuously-updated 1M-context model, positioned for agent and coding scenarios, and it represents a distinct delivery model — "no versions" — that trades reproducibility for always-current capability. **Key characteristics.** 1M-token context (raised from 256K in a July 2026 update), 262,144 max output, deep thinking, multimodal understanding, GUI task handling, tool calling and structured output. **What a professional should know.** Capabilities can change under the same model ID, architecture is not disclosed, the API is cn-beijing only, and pricing is 6.00 CNY input / 30.00 CNY output per 1M tokens (cache hits 1.20).

## Architecture and parameters

ByteDance discloses no architecture or parameter counts for the Seed series, and the database records that absence. China AI Hub analysis indicates the rolling model compounds the opacity: not only is the architecture hidden, but the very identity of the model changes weekly, so any performance characterization is a moving target. See [Mixture-of-Experts](/technology/mixture-of-experts/) for the architectural context ByteDance does not provide.

## What the context window actually means

The 1M-token context (raised from 256K in July 2026) with a 262,144 output ceiling positions Seed Evolving for the long-horizon agent and deep-research workloads ByteDance names, with a mid-tier generation headroom. See the [context-window research](/research/chinese-ai-context-windows/) and the [long-context hub](/models/long-context/).

## Pricing implications

6.00 CNY input / 30.00 CNY output per 1M tokens, cache hits 1.20 (20% of input) — identical list price to the Seed 2.1 Pro model. China AI Hub analysis indicates the 5x input-to-output ratio is the Seed family's generation-premium signature, and Evolving's price parity with Pro means the premium is for the rolling update cadence and 1M context, not for a higher capability tier. See [choosing-by-price](/guides/choosing-by-price/).

## API, coding, and agent implications

ByteDance positions Seed Evolving for agent and coding scenarios, with tool calling, structured output, GUI task handling and computer use documented. The operational caveat is the rolling model ID: capabilities can change week to week, so any pinned integration or evaluation is at risk of drift. See [computer use](/technology/computer-use/) and [AI agents](/technology/ai-agents/).

## Open weights and license

Proprietary, closed weight, no self-hosting. See [open weight vs API](/research/open-weight-vs-api-structural-analysis/).

## Benchmark interpretation

No benchmark scores are recorded for Seed Evolving in the database. This is an absence of evidence, and the rolling nature makes it structurally hard to benchmark — any published number would describe only the snapshot at that moment.

## What the benchmarks do not prove

With no recorded benchmarks, there is nothing with which to rank Seed Evolving against competitors, and its agent/coding positioning rests on vendor claims rather than published numbers. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** agent and coding workloads inside ByteDance's China ecosystem that benefit from weekly capability updates and 1M context, and teams willing to accept version drift for always-current output. **Less suited:** reproducibility-sensitive production (no pinned version), international API consumers (cn-beijing only), and any adoption decision requiring published architecture or benchmark evidence.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | High |
| Coding | Moderate |
| Structured API workflows | High |
| Agent orchestration | High |
| Local self-hosted deployment | No evidence |
| GUI automation | High |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates Seed Evolving is ByteDance's bet on continuous delivery as a differentiator: a versionless, weekly-updated 1M model that competes on always-current capability rather than on a documented checkpoint. Against the versioned [Seed 2.1 Turbo](/models/doubao-seed-2-1-turbo/) (256K, half price) and [Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) (1M, same price), Evolving sits at the top on context and update cadence but sacrifices the reproducibility that a pinned version provides — a genuine trade-off, not a pure upgrade. The combination of rolling identity, hidden architecture and cn-beijing-only serving makes independent verification unusually difficult, which is the defining constraint for international adopters. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) and the [rise of Chinese AI agents](/research/rise-of-chinese-ai-agents/) research.

## What is uncertain

- Architecture and parameter counts are not publicly disclosed.
- No benchmark scores are published, and the rolling model makes any score snapshot-specific.
- Capabilities can change weekly under the same model ID.
- The API is served from cn-beijing only; no international endpoint was verified.

## Sources

- [Ark official model list](https://docs.volcengine.com/docs/ark/model-list?lang=zh)
- [Ark official model pricing](https://docs.volcengine.com/docs/ark/model-pricing?lang=zh)
- [Ark model release announcements](https://docs.volcengine.com/docs/ark/model-release-announcement)

*Labels used above: **Official fact** (context, capabilities, pricing and the rolling update model from Ark's docs) and **China AI Hub analysis** (our synthesis, always introduced as such). No benchmark evidence is currently recorded for this model.*
