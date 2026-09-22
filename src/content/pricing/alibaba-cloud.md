---
image: "/images/ai/pricing-alibaba-cloud.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: alibaba-cloud
currency: USD
region: "Singapore (International)"
billing_mode: pay_as_you_go
models:
  - model: qwen3.8-max
    input_price_per_1m: 2.0
    output_price_per_1m: 6.0
    cached_input_price_per_1m: 0.25
    note: "Beijing and Global regions (HK/Frankfurt/US/Tokyo): $1.65 input / $4.951 output. Beijing batch: 50% off. Explicit cache creation $2.5, explicit cache read $0.17 (Singapore). Free quota: 1M tokens, 90 days (Singapore)."
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - model: qwen3.8-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.47
    cached_input_price_per_1m: 0.016
    note: "Beijing and Global regions: $0.113 / $0.382. Explicit cache creation $0.2, read $0.016 (Singapore). Batch inference not supported."
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
  - model: qwen3.7-plus
    input_price_per_1m: 0.4
    output_price_per_1m: 1.6
    note: "Up to 256K context tier. 256K-1M tier: $1.2 / $4.8. Beijing: $0.276/$1.101 and $0.826/$3.301. Limited-time 20% console discount. Thinking billed same as output."
    official_source: https://www.alibabacloud.com/help/en/model-studio/model-pricing
last_verified: "2026-09-20"
sources:
  - source_name: Model Studio — model pricing
    source_url: https://www.alibabacloud.com/help/en/model-studio/model-pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
Alibaba Cloud Model Studio publishes pay-as-you-go API pricing in USD for the Singapore (International) region, covering 3 model(s): qwen3.8-max, qwen3.8-flash, qwen3.7-plus. Per-model input, output and cached rates are listed in the table below with links to the official source for each row; Prices change frequently — verify against the official pricing page before making decisions.
