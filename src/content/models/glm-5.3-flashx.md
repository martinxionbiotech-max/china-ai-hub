---
image: "/images/ai/models-glm-5.3-flashx.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: glm-5.3-flashx
model_name: GLM-5.3-FlashX
provider: zhipu-ai
model_family: GLM-5.3-Flash
canonical_model: glm-5.3-flash
status: active
open_weight: false
license: proprietary
self_hosting: false
api_available: true
pricing:
  input_price_per_1m: 0.37
  output_price_per_1m: 1.25
  currency: USD
  pricing_ref: zhipu-ai
official_api: true
known_limitations:
  - "Context window, capabilities and benchmark results are not published on the official Z.ai pricing page; not publicly documented as of 2026-09-27"
last_verified: "2026-09-27"
sources:
  - source_name: Z.ai — API pricing (official)
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-09-27"
    confidence: high
---

**What it is.** GLM-5.3-FlashX is Zhipu AI's international-region Flash-tier speed SKU: the same underlying model as [GLM-5.3-Flash](/models/glm-53-flash/), served at higher throughput under a separate billing SKU. **Why it matters.** It is the database's clearest example of throughput-tiered billing — you pay a premium to buy serving speed, not a different model — and it sits alongside Moonshot's and MiniMax's highspeed variants as evidence that speed tiers are now standard in the Chinese API layer. **Key characteristics.** $0.37 input / $1.25 output per 1M tokens (cached $0.075) versus $0.15 / $0.50 for Flash, and up to 200 tokens/s (vendor-reported). **What a professional should know.** Context window, capabilities and benchmark results are not published separately for FlashX — the full model definition lives on the [GLM-5.3-Flash](/models/glm-53-flash/) page, which is the canonical entry.

## How it differs from GLM-5.3-Flash

The only documented differences are **throughput and price**. FlashX is priced at $0.37 input / $1.25 output per 1M tokens versus $0.15 / $0.50 for Flash — roughly 2.5x the input and output rate — for faster serving (up to 200 tokens/s, vendor-reported). Context window, capabilities and benchmark results are not published separately on the official Z.ai pricing page as of 2026-09-27; all other fields are the same as the parent entry.

## Pricing implications

China AI Hub analysis indicates the 2.5x premium is the operative fact, and it is a notable outlier: the database records the other two highspeed variants — [Kimi K2.7 Code Highspeed](/models/kimi-k27-code-highspeed/) and [MiniMax-M2.7-Highspeed](/models/minimax-m27-highspeed/) — at exactly 2x their parent tiers, whereas FlashX charges ~2.5x. The cached-input rates ($0.075 vs $0.03) scale at the same ratio, so the premium persists even for cache-heavy agent loops. See the [choosing-by-price guide](/guides/choosing-by-price/).

## Why speed tiers exist

China AI Hub analysis indicates throughput-tiered billing is a serving-economics strategy, not a model strategy: the vendor runs the same weights on faster (and costlier) inference capacity and recovers that cost as a price multiplier, while keeping a single model definition. The database now records this pattern at three labs — Moonshot (K2.7 Code Highspeed), MiniMax (M2.7 Highspeed) and Zhipu (FlashX) — which signals the practice has become standard across the Chinese API layer rather than a one-off. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research.

## When to choose FlashX vs Flash

China AI Hub analysis indicates the choice reduces to a latency-versus-cost trade-off on the same model. For latency-sensitive or throughput-bound workloads — interactive chat, GUI/browser agents, visual coding loops where token-generation speed is the bottleneck — the 2.5x premium may pay for itself. For cost-bound or batch work, the standard [GLM-5.3-Flash](/models/glm-53-flash/) tier is the same model at a lower price. One further difference the database records: Flash is open-weight, whereas FlashX is a closed API SKU — the speed tier exists only as a served endpoint, not a downloadable artifact.

## The documentation gap

Context window, capabilities and benchmark results are not published separately for FlashX; they inherit from the parent model's page. China AI Hub analysis indicates this is a deliberate documentation economy — the vendor documents the speed tier as a price-and-throughput delta only, and expects buyers to read the parent's card for the model definition — which is reasonable but leaves the throughput claim (200 tokens/s) as a vendor-reported figure with no independent measurement recorded.

## China AI Hub analysis

China AI Hub analysis indicates that GLM-5.3-FlashX is best read as a pricing product, not a model product: it packages the same GLM-5.3-Flash capability into a higher-throughput, higher-price SKU, and its significance is what it reveals about the market rather than what it adds technically. Its 2.5x premium — above the 2x norm set by Moonshot and MiniMax — makes it the most expensive speed tier in the collection relative to its parent, which suggests Zhipu is pricing for latency-hungry international users rather than competing on raw throughput-per-dollar. The absence of separately published context, capability and benchmark data means any independent evaluation of the speed tier must route through the [parent page](/models/glm-53-flash/), which is the canonical entry.

## What is uncertain

- Context window, capabilities and benchmark results are not published separately for FlashX; they are documented only on the parent page.
- The 200 tokens/s throughput figure is vendor-reported and not independently measured.
- Whether the 2.5x (rather than 2x) premium corresponds to a proportionally faster serving tier is not documented.

## Sources

- [Z.ai — API pricing (official)](https://docs.z.ai/guides/overview/pricing)

*Labels used above: **Official fact** (pricing and the Flash/FlashX billing split from Z.ai's pricing page), **Vendor-reported claim** (the 200 tokens/s throughput figure), and **China AI Hub analysis** (our synthesis, introduced as such). The full model definition is documented on the [GLM-5.3-Flash](/models/glm-53-flash/) page.*
