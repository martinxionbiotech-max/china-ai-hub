---
provider_id: zhipu-ai
currency: USD
region: "International (Z.ai)"
billing_mode: pay_as_you_go
models:
  - model: glm-5.3
    input_price_per_1m: 1.4
    output_price_per_1m: 4.4
    cached_input_price_per_1m: 0.26
    note: "Cache storage limited-time free. China platform (BigModel): ¥8 / ¥28, cached hit ¥2. Batch API = 50% of standard price for supported models."
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.3-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.5
    cached_input_price_per_1m: 0.03
    note: "China platform: ¥0.8 / ¥2.8, cached ¥0.23."
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.3-flashx
    input_price_per_1m: 0.37
    output_price_per_1m: 1.25
    cached_input_price_per_1m: 0.075
    note: "China platform: ¥2 / ¥7, cached ¥0.57. Not yet on the GLM Coding Plan."
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.2
    input_price_per_1m: 1.4
    output_price_per_1m: 4.4
    cached_input_price_per_1m: 0.26
    note: "China platform: ¥8 / ¥28, cached ¥2."
    official_source: https://docs.z.ai/guides/overview/pricing
last_verified: "2026-09-20"
sources:
  - source_name: Z.ai pricing
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: BigModel pricing docs (CNY)
    source_url: https://docs.bigmodel.cn/cn/guide/start/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
Zhipu AI Z.AI platform publishes pay-as-you-go API pricing in USD for the International (Z.ai) region, covering 4 model(s): glm-5.3, glm-5.3-flash, glm-5.3-flashx, glm-5.2. Per-model input, output and cached rates are listed in the table below with links to the official source for each row; Prices change frequently — verify against the official pricing page before making decisions.
