---
provider_id: bytedance
currency: CNY
region: china
billing_mode: pay_as_you_go
models:
  - model: doubao-seed-2-1-pro
    input_price_per_1m: 6.0
    output_price_per_1m: 30.0
    cached_input_price_per_1m: 1.2
    note: "Standard tier. Low-priority tier ~50%: 3.00/15.00. Context cache storage 0.017 CNY per 1M tokens per hour."
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
  - model: doubao-seed-evolving
    input_price_per_1m: 6.0
    output_price_per_1m: 30.0
    cached_input_price_per_1m: 1.2
    note: "Standard tier. Pricing row matches Doubao Seed 2.1 Pro."
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
  - model: doubao-seed-2-1-turbo
    input_price_per_1m: 3.0
    output_price_per_1m: 15.0
    cached_input_price_per_1m: 0.6
    note: "Standard tier. Low-latency tier: 6.00/30.00. Low-priority tier: 1.50/7.50."
    official_source: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
last_verified: "2026-09-20"
sources:
  - source_name: Ark official model pricing
    source_url: https://docs.volcengine.com/docs/ark/model-pricing?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
ByteDance Volcengine Ark publishes pay-as-you-go API pricing in CNY for the china region, covering 3 model(s): doubao-seed-2-1-pro, doubao-seed-evolving, doubao-seed-2-1-turbo. Per-model input, output and cached rates are listed in the table below with links to the official source for each row; Prices change frequently — verify against the official pricing page before making decisions.
