---
provider_id: moonshot-ai
currency: USD
billing_mode: pay_as_you_go
models:
  - model: kimi-k3
    input_price_per_1m: 3.0
    output_price_per_1m: 15.0
    cached_input_price_per_1m: 0.3
    note: "Cache write: $3.00 (TTL 5min) or $6.00 (TTL 1h). Context 1,048,576. Access requires min $1 top-up."
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.7-code
    input_price_per_1m: 0.95
    output_price_per_1m: 4.0
    cached_input_price_per_1m: 0.19
    note: "Context 262,144. Thinking always on."
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.7-code-highspeed
    input_price_per_1m: 1.9
    output_price_per_1m: 8.0
    cached_input_price_per_1m: 0.38
    note: "Same model as k2.7-code at ~180 tokens/s. Context 262,144."
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.6
    input_price_per_1m: 0.95
    output_price_per_1m: 4.0
    cached_input_price_per_1m: 0.16
    note: "Visual + text; thinking and non-thinking modes. Context 262,144."
    official_source: https://platform.kimi.ai/docs/pricing/chat
last_verified: "2026-09-20"
sources:
  - source_name: Kimi API — pricing (chat)
    source_url: https://platform.kimi.ai/docs/pricing/chat
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
