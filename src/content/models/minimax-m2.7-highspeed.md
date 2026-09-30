---
image: "/images/ai/models-minimax-m2.7-highspeed.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: minimax-m2.7-highspeed
model_name: MiniMax-M2.7-Highspeed
provider: minimax
model_family: MiniMax M2.7
canonical_model: minimax-m2.7
release_date: "2026-03-18"
status: active
context_window: 204800
capabilities:
  reasoning: true
  tool_calling: true
  vision: false
open_weight: true
license: "Custom NON-COMMERCIAL license (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution 'Built with MiniMax M2.7' required)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.6
  output_price_per_1m: 2.4
  currency: USD
  pricing_ref: minimax
official_api: true
cloud_providers:
  - MiniMax Platform
regions:
  - china
  - international
known_limitations:
  - "Parameter counts are not published in the official MiniMax-M2.7 model card (HF)"
  - "Text-only input; interleaved thinking always on (cannot be disabled via API)"
  - "Must echo full assistant content (thinking blocks) back in multi-turn history"
last_verified: "2026-09-27"
sources:
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax API platform — pay-as-you-go pricing (intl)
    source_url: https://platform.minimax.io/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** MiniMax-M2.7-Highspeed is the same "self-evolving" text model as [MiniMax-M2.7](/models/minimax-m27/), served as a higher-throughput billing SKU on the MiniMax Platform. **Why it matters.** It is one of three speed-tier variants the database records across the Chinese API layer — alongside [Kimi K2.7 Code Highspeed](/models/kimi-k27-code-highspeed/) and [GLM-5.3-FlashX](/models/glm-53-flashx/) — which together mark throughput-tiered billing as a settled practice rather than a one-off. **Key characteristics.** ~100 tokens/s output (vendor claim — "same quality, faster"), exactly 2x the standard M2.7 price ($0.60 input / $2.40 output per 1M tokens), on the same 204,800-token, text-only, always-on-thinking, non-commercial-licensed model. **What a professional should know.** The only documented differences from the parent are throughput and price; the full model definition lives on the [MiniMax-M2.7](/models/minimax-m27/) page, which is the canonical entry.

## How it differs from MiniMax-M2.7

The only documented differences are **throughput and price**. The standard M2.7 serves at ~60 tokens/s at $0.30 / $1.20; the Highspeed variant serves at ~100 tokens/s at exactly 2x the price ($0.60 / $2.40). Parameter counts, the 204,800-token context window, text-only input, always-on interleaved thinking and the custom non-commercial license are identical to the parent entry. This is a pure throughput tier, not a distinct model.

## Pricing implications

China AI Hub analysis indicates the 2x price buys roughly 1.7x output speed (~60 → ~100 tokens/s), which is a meaningful sub-linear return on the premium — you pay a full 2x for a 1.7x speedup, so the value depends entirely on whether latency or cost dominates your workload. At 2x, MiniMax's Highspeed premium matches the Moonshot norm (K2.7 Code Highspeed is also 2x) but sits below Zhipu's FlashX outlier (~2.5x). The cache-read price ($0.06) is unchanged from the parent, so agent loops that re-read context keep their discount even at the higher speed. See the [choosing-by-price guide](/guides/choosing-by-price/).

## Why speed tiers exist

China AI Hub analysis indicates throughput-tiered billing is a serving-economics strategy, not a model strategy: the vendor runs the same weights on faster (and costlier) inference capacity and recovers that cost as a price multiplier, while keeping a single model definition. The database now records this pattern at three labs — MiniMax (M2.7 Highspeed), Moonshot (K2.7 Code Highspeed) and Zhipu (FlashX) — which signals the practice has become standard across the Chinese API layer rather than a one-off. For MiniMax, the Highspeed tier is a companion to its flagship [MiniMax-M3](/models/minimax-m3/), which serves long-context and multimodal work at a higher capability level. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research.

## API, coding, and agent implications

The Highspeed tier inherits the parent's operational constraints: interleaved thinking that is always on and cannot be disabled, and the requirement to echo full assistant content (including thinking blocks) back in multi-turn history. For latency-sensitive interactive use — chat, agent loops, tool-calling bursts where per-token latency is the bottleneck — the faster throughput can pay for itself; for throughput- or cost-bound batch work, the standard tier is the same model at half the price. Parameter counts remain undisclosed. See the [coding hub](/models/coding/) and [reasoning models](/technology/reasoning-models/).

## When to choose Highspeed vs standard

China AI Hub analysis indicates the choice reduces to a latency-versus-cost trade-off on the same model, with the added wrinkle that the 2x premium here buys only ~1.7x speed. Latency-bound interactive workloads favor the Highspeed tier; cost-bound or batch workloads favor the standard [MiniMax-M2.7](/models/minimax-m27/) tier. Because the throughput gain is vendor-reported and not independently measured, the real-world break-even depends on whether the faster tier actually delivers the claimed ~100 tokens/s in your workload.

## The documentation gap

Parameter counts are not published for M2.7 (or its Highspeed variant), and the throughput figure (~100 tokens/s) is a vendor claim with no independent measurement recorded. China AI Hub analysis indicates this is a deliberate documentation economy — the vendor documents the speed tier as a price-and-throughput delta only — which is reasonable but leaves the speed claim unverified.

## China AI Hub analysis

China AI Hub analysis indicates that MiniMax-M2.7-Highspeed is best read as a pricing product, not a model product: it packages the same non-commercial-licensed text model into a higher-throughput, 2x-price SKU, and its significance is what it reveals about the market rather than what it adds technically. Its 1.7x-speed-for-2x-price ratio makes it the least efficient speed premium of the three highspeed tiers the database records, which suggests MiniMax prices the tier conservatively rather than competing aggressively on throughput-per-dollar. The absence of separately published parameter and capability data means any independent evaluation of the speed tier must route through the [parent page](/models/minimax-m27/), which is the canonical entry.

## What is uncertain

- The ~100 tokens/s throughput figure is vendor-reported and not independently measured.
- Parameter counts are not published for M2.7 or its Highspeed variant.
- Whether the 2x premium corresponds to a proportionally faster serving tier is not documented (the claimed speedup is ~1.7x, not 2x).

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-models-minimax-m2.7-highspeed-1 | MiniMax API platform — model overview (CN) | https://platform.minimaxi.com/docs/guides/models-intro | Official documentation | — | 2026-09-20 | high | — |
| src-models-minimax-m2.7-highspeed-2 | MiniMax API platform — pay-as-you-go pricing (intl) | https://platform.minimax.io/docs/guides/pricing-paygo.md | Official documentation | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (pricing and the 204,800-token context from MiniMax's docs), **Vendor-reported claim** (the ~100 tokens/s throughput figure), and **China AI Hub analysis** (our synthesis, introduced as such). The full model definition is documented on the [MiniMax-M2.7](/models/minimax-m27/) page.*
