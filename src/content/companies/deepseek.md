---
image: "/images/ai/companies-deepseek.webp"
image_credit: "AI-generated illustration (Seedream)"
company_id: deepseek
company_name: DeepSeek
description: "DeepSeek (Hangzhou): DeepSeek Chat (web and mobile), DeepSeek API platform, and DeepSeek Harness developer preview. Foundation models DeepSeek-V4-Pro and V4.1-Flash; open model DeepSeek-V3-2."
aliases:
  - 深度求索
headquarters: "Hangzhou, Zhejiang, China (derived from the official footer company name 杭州深度求索人工智能基础技术研究有限公司 and Zhejiang ICP / Hangzhou public-security filings; the official pages fetched do not print a headquarters line verbatim)"
funding: "No external funding officially disclosed as of 2026-09-22 (media-reported rounds are not confirmed on official channels)."
ai_products:
  - DeepSeek Chat (web and mobile assistant)
  - DeepSeek API platform
  - DeepSeek Harness (developer preview)
foundation_models:
  - deepseek-v4-1-flash
  - deepseek-v4-pro
open_models:
  - deepseek-v3-2
major_releases:
  - name: DeepSeek-V4.1-Flash
    date: "2026-09-10"
    type: model_release
  - name: DeepSeek-V4-Pro GA (0813)
    date: "2026-08-13"
    type: model_release
  - name: DeepSeek-V4 Preview
    date: "2026-04-24"
    type: model_release
  - name: DeepSeek-V3.2
    date: "2025-12-01"
    type: model_release
open_source_projects:
  - DeepSeek-V4.1-Flash (MIT)
  - DeepSeek-V4-Pro (MIT)
  - DeepSeek-V4-Flash (MIT)
  - DeepSeek-V3.2 (MIT)
  - DeepSeek-R1 (MIT)
  - DeepSeek-OCR / DeepSeek-OCR-2
  - DeepEP
  - FlashMLA
  - DeepGEMM
  - 3FS
official_documentation: https://api-docs.deepseek.com/
official_website: https://www.deepseek.com/
related_entities: []
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
  - source_name: DeepSeek official site (EN)
    source_url: https://www.deepseek.com/en/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: DeepSeek Transparency Center
    source_url: https://www.deepseek.com/en/transparency/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** DeepSeek is the Chinese AI company behind the DeepSeek-V4 family of open-weight models and the low-cost DeepSeek API platform. **Why it matters.** DeepSeek set the price floor for the Chinese API market — its flash tier lists $0.15/1M input tokens — and publishes frontier models under MIT, the most permissive license in the ecosystem. **Key characteristics.** Current API lineup is [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) and [DeepSeek-V4-Pro](/models/deepseek-v4-pro/), both with 1M-token context; OpenAI-, Responses- and Anthropic-compatible endpoints; peak/off-peak pricing. **What a professional should know.** V4-Pro is marked deprecated with conflicting official pages on whether its API continues after 2026-09-14 — resolve that against the current change log before committing production workloads.

DeepSeek is a Chinese AI company (杭州深度求索人工智能基础技术研究有限公司) known for open-weight
models and low-cost APIs. Its current API lineup is the DeepSeek-V4.1 family: `deepseek-flash`
(DeepSeek-V4.1-Flash, released 2026-09-10, multimodal, MIT open weights) and `deepseek-v4-pro`
(DeepSeek-V4-Pro-0813), both with 1M-token context windows and 384K maximum output.

The API platform (platform.deepseek.com) offers OpenAI-compatible, Responses and Anthropic-compatible
endpoints with automatic KV caching and peak/off-peak pricing in USD. The founding date is not stated on
the official pages fetched.

## Why it matters

DeepSeek is the ecosystem's price-and-openness reference point: MIT open weights (V4.1-Flash, V4-Pro, V3.2) plus the lowest budget-tier pricing ($0.15/1M input) make it the default anchor against which every other vendor's cost and license are measured. Its open inference infrastructure (FlashMLA, DeepGEMM, DeepEP, 3FS) extends that influence below the model layer, as the [AI infrastructure](/technology/ai-infrastructure/) page details. China AI Hub analysis indicates DeepSeek's structural role is the cost-and-openness floor — its 49B-active MoE design and off-peak discounts shaped the market's pricing expectations, and its MIT releases shaped its licensing expectations, even as the V4-Pro deprecation ambiguity shows how quickly that frontier layer now turns over.

*Labels used above: **Official fact** (from DeepSeek API docs and the official site), **Vendor-reported claim** (pricing and model capabilities published by DeepSeek), and **China AI Hub analysis** (our synthesis, always introduced as such).*
