---
image: "/images/ai/pricing-minimax.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: minimax
currency: USD
region: "International"
billing_mode: pay_as_you_go
models:
  - model: minimax-m3
    input_price_per_1m: 0.3
    output_price_per_1m: 1.2
    cached_input_price_per_1m: 0.06
    note: "Standard tier, <=512K input (permanent 50% off vs list $0.60/$2.40). >512K input: $0.60/$2.40, cache $0.12. Priority tier (service_tier=priority) = 1.5x. China platform: ¥2.1 / ¥8.4 (<=512K), ¥4.2 / ¥16.8 (>512K)."
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
  - model: minimax-m2.7
    input_price_per_1m: 0.3
    output_price_per_1m: 1.2
    cached_input_price_per_1m: 0.06
    note: "Cache write $0.375 per 1M tokens. China platform: ¥2.1 / ¥8.4."
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
  - model: minimax-m2.7-highspeed
    input_price_per_1m: 0.6
    output_price_per_1m: 2.4
    cached_input_price_per_1m: 0.06
    note: "Cache write $0.375 per 1M tokens. China platform: ¥4.2 / ¥16.8."
    official_source: https://platform.minimax.io/docs/guides/pricing-paygo.md
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax API platform — pay-as-you-go pricing (intl)
    source_url: https://platform.minimax.io/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax API platform — pay-as-you-go pricing (CN)
    source_url: https://platform.minimaxi.com/docs/guides/pricing-paygo.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
MiniMax open platform publishes pay-as-you-go API pricing in USD for the International region, covering 3 model(s): minimax-m3, minimax-m2.7, minimax-m2.7-highspeed. Per-model input, output and cached rates are listed in the table below with links to the official source for each row; Prices change frequently — verify against the official pricing page before making decisions.
