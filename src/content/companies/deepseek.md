---
company_id: deepseek
company_name: DeepSeek
aliases:
  - 深度求索
headquarters: "Hangzhou, Zhejiang, China (derived from the official footer company name 杭州深度求索人工智能基础技术研究有限公司 and Zhejiang ICP / Hangzhou public-security filings; the official pages fetched do not print a headquarters line verbatim)"
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

DeepSeek is a Chinese AI company (杭州深度求索人工智能基础技术研究有限公司) known for open-weight
models and low-cost APIs. Its current API lineup is the DeepSeek-V4.1 family: `deepseek-flash`
(DeepSeek-V4.1-Flash, released 2026-09-10, multimodal, MIT open weights) and `deepseek-v4-pro`
(DeepSeek-V4-Pro-0813), both with 1M-token context windows and 384K maximum output.

The API platform (platform.deepseek.com) offers OpenAI-compatible, Responses and Anthropic-compatible
endpoints with automatic KV caching and peak/off-peak pricing in USD. The founding date is not stated on
the official pages fetched.
