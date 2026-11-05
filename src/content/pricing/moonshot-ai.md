---
image: "/images/ai/pricing-moonshot-ai.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: moonshot-ai
currency: USD
billing_mode: pay_as_you_go
models:
  - model: kimi-k3
    input_price_per_1m: 3.0
    output_price_per_1m: 15.0
    cached_input_price_per_1m: 0.3
    notes:
      - "Cache write: $3.00 (TTL 5min) or $6.00 (TTL 1h)"
      - "Context: 1,048,576"
      - "Access requires min $1 top-up"
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.7-code
    input_price_per_1m: 0.95
    output_price_per_1m: 4.0
    cached_input_price_per_1m: 0.19
    notes:
      - "Context: 262,144"
      - "Thinking always on"
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.7-code-highspeed
    input_price_per_1m: 1.9
    output_price_per_1m: 8.0
    cached_input_price_per_1m: 0.38
    notes:
      - "Same model as k2.7-code at ~180 tokens/s"
      - "Context: 262,144"
    official_source: https://platform.kimi.ai/docs/pricing/chat
  - model: kimi-k2.6
    input_price_per_1m: 0.95
    output_price_per_1m: 4.0
    cached_input_price_per_1m: 0.16
    notes:
      - "Visual + text; thinking and non-thinking modes"
      - "Context: 262,144"
    official_source: https://platform.kimi.ai/docs/pricing/chat
last_verified: "2026-09-20"
sources:
  - source_name: Kimi API — pricing (chat)
    source_url: https://platform.kimi.ai/docs/pricing/chat
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**Short answer.** Moonshot prices Kimi K3 at $3.00/$15.00 — flagship rates, 20x the input price of its own K2.7-Code at $0.95/$4.00 — and sells a Highspeed variant at exactly double the price for roughly 1.7x the throughput. The gap between its flagship and its coding model is the widest intra-provider spread in this database.

## The four models

| Model | Input | Output | Out/in | Cache | Context |
|---|---|---|---|---|---|
| Kimi K3 | $3.00 | $15.00 | 5.00 | $0.30 (10%) | 1M |
| K2.7-Code | $0.95 | $4.00 | 4.21 | $0.19 (20%) | 262K |
| K2.7-Code Highspeed | $1.90 | $8.00 | 4.21 | $0.38 (20%) | 262K |
| K2.6 | $0.95 | $4.00 | 4.21 | $0.16 (16.8%) | 262K |

Output at 5x input on K3 is the steepest ratio among the flagships here, which makes long-form generation on K3 markedly more expensive than the headline input price suggests.

## Highspeed math

The Highspeed variant doubles both input and output for about 1.7x the throughput (the provider quotes ~180 tokens/s against the standard tier). Per token you pay 2x; per second of wall-clock you pay roughly 1.18x. That is a reasonable trade only when latency is the binding constraint — interactive coding assistants, live review tools — and a pure loss for batch generation.

## K3 versus K2.7-Code

K3 is the 1M-context flagship; K2.7-Code is a 262K coding specialist at one-third the input price. For repository work inside 262K tokens, the specialist is dramatically cheaper and, on coding benchmarks, competitive. The flagship earns its price on long-context tasks and general reasoning, not on code.

## Our view

**Kimi's pricing is the most tiered in the market, and buyers should exploit it.** Few teams need a 1M-context flagship for every call. Routing code and short-context work to K2.7-Code and reserving K3 for genuinely long inputs cuts spend by 60-70% with little quality loss on the routed tasks.

**The 20x input spread between K3 and K2.7-Code is the single biggest intra-provider lever in this database.** No competitor offers a comparable step down within one family, and most Kimi buyers do not use it.

**Highspeed is priced correctly for what it is and wrongly for what most buyers want.** 2x price for 1.7x throughput is a latency product; if your workload is throughput-bound rather than latency-bound, it is a 18% cost increase per unit of work.

**A 10% cache rate on the flagship is weaker than it looks.** Zhipu and MiniMax offer 18-20%; on a cache-heavy agent loop, K3's caching saves less than its competitors' at similar list prices.
