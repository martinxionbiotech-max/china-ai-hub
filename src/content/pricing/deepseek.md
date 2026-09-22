---
image: "/images/ai/pricing-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: deepseek
currency: USD
billing_mode: pay_as_you_go
models:
  - model: deepseek-v4-1-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.6
    cached_input_price_per_1m: 0.003
    note: "Off-peak rates (all times except 01:00-04:00 and 06:00-10:00 UTC Mon-Fri). Peak = 2x: $0.30 input / $1.20 output / $0.006 cache hit. Concurrency limit 2500. No batch pricing listed."
    official_source: https://api-docs.deepseek.com/quick_start/pricing
  - model: deepseek-v4-pro
    input_price_per_1m: 0.66
    output_price_per_1m: 1.98
    cached_input_price_per_1m: 0.022
    note: "Off-peak rates; peak = 2x: $1.32 input / $3.96 output / $0.044 cache hit. Concurrency limit 500. Deprecation announced 2026-09-10 (service continuation per change log)."
    official_source: https://api-docs.deepseek.com/quick_start/pricing
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
---
DeepSeek API publishes pay-as-you-go API pricing in USD, covering 2 model(s): deepseek-v4-1-flash, deepseek-v4-pro. Per-model input, output and cached rates are listed in the table below with links to the official source for each row; Peak/off-peak differentials are noted per model where applicable. Prices change frequently — verify against the official pricing page before making decisions.
