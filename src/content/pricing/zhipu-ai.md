---
image: "/images/ai/pricing-zhipu-ai.webp"
image_credit: "AI-generated illustration (Seedream)"
provider_id: zhipu-ai
currency: USD
region: "International (Z.ai)"
billing_mode: pay_as_you_go
models:
  - model: glm-5.3
    input_price_per_1m: 1.4
    output_price_per_1m: 4.4
    cached_input_price_per_1m: 0.26
    notes:
      - "Cache storage: limited-time free"
      - "China platform (BigModel): ¥8 / ¥28, cache hit ¥2"
      - "Batch API: 50% of standard price"
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.3-flash
    input_price_per_1m: 0.15
    output_price_per_1m: 0.5
    cached_input_price_per_1m: 0.03
    notes:
      - "China platform: ¥0.8 / ¥2.8, cache ¥0.23"
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.3-flashx
    input_price_per_1m: 0.37
    output_price_per_1m: 1.25
    cached_input_price_per_1m: 0.075
    notes:
      - "China platform: ¥2 / ¥7, cache ¥0.57"
      - "Not yet on the GLM Coding Plan"
    official_source: https://docs.z.ai/guides/overview/pricing
  - model: glm-5.2
    input_price_per_1m: 1.4
    output_price_per_1m: 4.4
    cached_input_price_per_1m: 0.26
    notes:
      - "China platform: ¥8 / ¥28, cache ¥2"
    official_source: https://docs.z.ai/guides/overview/pricing
last_verified: "2026-11-05"
sources:
  - source_name: Z.ai pricing
    source_url: https://docs.z.ai/guides/overview/pricing
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
  - source_name: BigModel pricing docs (CNY)
    source_url: https://docs.bigmodel.cn/cn/guide/start/pricing
    source_type: official
    last_verified: "2026-11-05"
    confidence: high
---

**Short answer.** Zhipu prices three tiers of the same family with a 9x spread: GLM-5.3 at $1.40/$4.40, GLM-5.3-Flash at $0.15/$0.50, and GLM-5.3-FlashX at $0.37/$1.25. The older GLM-5.2 sits at exactly the flagship price, which tells you something about how the company wants you to choose.

## The ladder

| Model | Input | Output | Out/in | Cache | Position |
|---|---|---|---|---|---|
| GLM-5.3 | $1.40 | $4.40 | 3.14 | $0.26 (18.6%) | Flagship |
| GLM-5.2 | $1.40 | $4.40 | 3.14 | $0.26 | Previous flagship |
| GLM-5.3-FlashX | $0.37 | $1.25 | 3.38 | $0.075 | Speed tier |
| GLM-5.3-Flash | $0.15 | $0.50 | 3.33 | $0.03 (20%) | Volume tier |

The output/input ratios are unusually consistent — 3.1 to 3.4 across all four — which means the tiers differ in absolute price, not in shape. Choosing between them does not change how your workload's cost scales; it changes the multiplier.

## FlashX is a latency purchase

At $0.37 input against Flash's $0.15, FlashX costs 2.47x for a faster serving tier of the same underlying generation. That is a reasonable premium if you are serving an interactive product where time-to-first-token is visible to users, and a bad one for batch work, where it buys nothing.

The China platform prices tell the same story in CNY: ¥2 / ¥7 against ¥0.8 / ¥2.8 — the same 2.5x relationship, regionally consistent.

## The GLM-5.2 problem

GLM-5.2 is priced identically to GLM-5.3. There is no discount for the older model, no sunset price, no incentive to move traffic onto the previous generation. A buyer comparing the two should treat 5.2 as a fallback for compatibility, not as a cheaper option — because it is not one.

## Our view

**Zhipu's tiering is the cleanest in the Chinese market to reason about.** Four models, one shape, a 9x span from Flash to flagship. You can pick a tier on cost and know exactly what multiple you are accepting.

**Flash is the default and the flagship is the exception.** At $0.15/$0.50 with a 20% cache rate, Flash covers most workloads; the 9x step to GLM-5.3 should be justified by a measured task failure, not by a benchmark gap.

**Paying for FlashX instead of the flagship is often the better upgrade.** If the problem is latency rather than capability, 2.47x buys speed; 9.3x buys parameters you may not need.

**A same-price older model is a signal about inventory.** Zhipu is not trying to clear GLM-5.2 capacity; it is keeping it available and priced at parity. Do not assume a legacy discount that does not exist.
