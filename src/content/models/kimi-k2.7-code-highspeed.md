---
image: "/images/ai/models-kimi-k2.7-code-highspeed.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: kimi-k2.7-code-highspeed
model_name: Kimi K2.7 Code Highspeed
provider: moonshot-ai
model_family: Kimi K2.7
canonical_model: kimi-k2.7-code
status: active
context_window: 262144
capabilities:
  reasoning: true
  coding: true
open_weight: null
api_available: true
pricing:
  input_price_per_1m: 1.9
  output_price_per_1m: 8.0
  currency: USD
  pricing_ref: moonshot-ai
official_api: true
cloud_providers:
  - Moonshot AI Platform
known_limitations:
  - "Architecture and parameter counts are not publicly disclosed by Moonshot for the K2.7 series (API-only coding models)"
  - "Output speed ~180 tokens/s, up to 260 tokens/s in short-context scenarios (official model list)"
  - "Thinking is always on; temperature/top_p/n/penalties are fixed and must not be passed"
  - "Max output ceiling not stated in the fetched docs (256K context)"
last_verified: "2026-09-27"
sources:
  - source_name: Kimi API platform — model list
    source_url: https://platform.kimi.ai/docs/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi API — pricing (chat)
    source_url: https://platform.kimi.ai/docs/pricing/chat
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Kimi K2.7 Code Highspeed is the same coding model as [Kimi K2.7 Code](/models/kimi-k27-code/), served as a higher-throughput billing SKU on the Moonshot AI Platform. **Why it matters.** It is one of three speed-tier variants the database records across the Chinese API layer — alongside [MiniMax-M2.7-Highspeed](/models/minimax-m27-highspeed/) and [GLM-5.3-FlashX](/models/glm-53-flashx/) — which together mark throughput-tiered billing as a settled industry practice rather than a one-off. **Key characteristics.** ~180 tokens/s output (up to 260 tokens/s in short contexts), exactly 2x the standard K2.7 Code price ($1.90 input / $8.00 output per 1M tokens), on the same 256K-context, always-on-thinking, closed-weight model. **What a professional should know.** The only documented differences from the parent are throughput and price; the full model definition lives on the [Kimi K2.7 Code](/models/kimi-k27-code/) page, which is the canonical entry.

## How it differs from Kimi K2.7 Code

The only documented differences are **throughput and price**. The standard K2.7 Code is priced at $0.95 / $4.00; the Highspeed variant is exactly 2x ($1.90 / $8.00, cache hits $0.38) for roughly double the output throughput (~180 vs the standard tier's implied baseline, up to 260 tokens/s in short contexts). The 256K context window, always-on thinking, fixed sampling parameters (temperature/top_p/n/penalties) and closed-weight API-only status are identical to the parent entry. This is a pure speed tier, not a distinct model.

## Pricing implications

China AI Hub analysis indicates the 2x premium is the operative fact, and it is the market norm: Moonshot (K2.7 Code Highspeed) and MiniMax (M2.7 Highspeed) both charge exactly 2x their parent tiers, while Zhipu's FlashX is the outlier at ~2.5x. For Moonshot specifically, the doubled output price ($8.00) is the steepest highspeed output rate in the collection — higher than MiniMax's $2.40 and Zhipu's $1.25 — which means the premium is only justified when output-token throughput is genuinely the bottleneck. Cache hits at $0.38 (20% of input) preserve the parent's agent-loop discount. See the [choosing-by-price guide](/guides/choosing-by-price/).

## Why speed tiers exist

China AI Hub analysis indicates throughput-tiered billing is a serving-economics strategy, not a model strategy: the vendor runs the same weights on faster (and costlier) inference capacity and recovers that cost as a price multiplier, while keeping a single model definition and a single model card. The database now records this pattern at three labs — Moonshot, MiniMax and Zhipu — which signals the practice has become standard across the Chinese API layer. For Moonshot, the K2.7 Highspeed tier is the latency-sensitive counterpart to its flagship [Kimi K3](/models/kimi-k3/), which sits at a higher price for frontier reasoning rather than speed. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research.

## API, coding, and agent implications

The Highspeed tier inherits the parent's coding posture: always-on thinking and fixed sampling (temperature/top_p/n/penalties), which the parent page records as a deliberate trade of deterministic-output control for a curated reasoning-heavy coding response. For interactive coding and agent loops where per-token latency is the bottleneck — an IDE autocomplete, a terminal agent, a tight feedback loop — the faster throughput can pay for itself; for batch or cost-bound coding work, the standard tier is the same model at half the price. Architecture and parameter counts remain undisclosed for the K2.7 series. See [choosing-a-coding-model](/guides/choosing-a-coding-model/) and the [coding hub](/models/coding/).

## When to choose Highspeed vs standard

China AI Hub analysis indicates the choice reduces to a latency-versus-cost trade-off on the same model. Latency-sensitive or throughput-bound workloads — interactive coding, agent loops, short-context bursts where the model hits the 260 tokens/s ceiling — favor the Highspeed tier. Cost-bound or batch workloads favor the standard [Kimi K2.7 Code](/models/kimi-k27-code/) tier. Because the price multiplier is exactly 2x but the throughput gain is vendor-reported and not independently measured, the real-world break-even point depends on whether the faster tier actually halves wall-clock time in your workload.

## The documentation gap

Context window, capabilities and benchmark results are not published separately for the Highspeed tier; they inherit from the parent model's page, which itself records no benchmark scores and no disclosed architecture for the K2.7 series. China AI Hub analysis indicates this is a deliberate documentation economy — the vendor documents the speed tier as a price-and-throughput delta only — which is reasonable but leaves the ~180–260 tokens/s figure as a vendor-reported claim with no independent measurement recorded.

## China AI Hub analysis

China AI Hub analysis indicates that Kimi K2.7 Code Highspeed is best read as a pricing product, not a model product: it packages the same closed-weight coding model into a higher-throughput, 2x-price SKU, and its significance is what it reveals about the market rather than what it adds technically. Its $8.00 output rate makes it the most expensive highspeed output tier in the collection relative to its peers, which suggests Moonshot prices the tier for latency-hungry coding users rather than competing on throughput-per-dollar. The absence of separately published context, capability and benchmark data means any independent evaluation of the speed tier must route through the [parent page](/models/kimi-k27-code/), which is the canonical entry.

## What is uncertain

- The ~180–260 tokens/s throughput figures are vendor-reported and not independently measured.
- Context window, capabilities and benchmark results are not published separately; they are documented only on the parent page.
- Whether the 2x premium corresponds to a proportionally faster serving tier is not documented.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-kimi-k2.7-code-highspeed-1 | Kimi API platform — model list | https://platform.kimi.ai/docs/models.md | Official documentation | — | 2026-09-20 | high | — |
| src-models-kimi-k2.7-code-highspeed-2 | Kimi API — pricing (chat) | https://platform.kimi.ai/docs/pricing/chat | Official documentation | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (pricing and the 256K context from Kimi's model list), **Vendor-reported claim** (the ~180–260 tokens/s throughput figures), and **China AI Hub analysis** (our synthesis, introduced as such). The full model definition is documented on the [Kimi K2.7 Code](/models/kimi-k27-code/) page.*
