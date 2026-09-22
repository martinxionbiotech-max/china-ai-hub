---
image: "/images/ai/comparisons-deepseek-v4-pro-vs-qwen3.8-max.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "DeepSeek-V4-Pro vs Qwen3.8-Max: Pricing, Reasoning, Coding and Deployment"
description: "Evidence-based comparison of DeepSeek-V4-Pro and Qwen3.8-Max: API pricing, context window, capabilities, open weights, licenses and benchmark records from the China AI Hub database."
entities:
  - deepseek-v4-pro
  - qwen3.8-max
dimensions:
  - pricing
  - context
  - reasoning
  - coding
  - vision
  - tool_calling
  - open_weight
  - license
  - api
  - deployment
published_date: "2026-09-22"
updated_date: "2026-09-22"
sources:
  - source_name: "DeepSeek API pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
  - source_name: "DeepSeek V4 Preview announcement"
    source_url: "https://www.deepseek.com/en/news/v4-preview/"
    source_type: official
  - source_name: "Alibaba Cloud Model Studio — Qwen3.8-Max"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"
    source_type: cloud_doc
  - source_name: "Alibaba Cloud Model Studio — Model pricing"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
    source_type: cloud_doc
---

All figures below are from the China AI Hub database, last verified 2026-09-22. Scores and capabilities are labeled by source type; where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | DeepSeek-V4-Pro | Qwen3.8-Max |
|---|---|---|
| Status (database) | deprecated | active |
| Context window | 1,048,576 tokens | 1,048,576 tokens |
| Maximum output | 393,216 tokens | 131,072 tokens |
| Input price (per 1M) | $0.66 | $2.00 |
| Output price (per 1M) | $1.98 | $6.00 |
| Open weights | Yes (MIT) | No (proprietary) |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Yes |
| Vision / Video | No | Yes / Yes |
| Tool calling | Yes | Yes |
| Structured output | Yes | Yes |
| Benchmark records in DB | 4 | 5 |

## Pricing

DeepSeek-V4-Pro lists input at $0.66 and output at $1.98 per 1M tokens; Qwen3.8-Max lists $2.00 input and $6.00 output — roughly three times the input price and three times the output price of the DeepSeek model. Both providers list their prices on official pages linked above. Price-per-token is only one axis: a model that needs fewer output tokens per task can cost less even at a higher per-token price.

## Context and output

Both list a 1,048,576-token context window. They differ on maximum output: 393,216 tokens listed for DeepSeek-V4-Pro versus 131,072 for Qwen3.8-Max. For very long generations (whole-document writing, long code synthesis), the listed output ceiling differs materially.

## Capabilities

Both list reasoning, coding, tool calling and structured output. The difference is in media: Qwen3.8-Max lists vision and video input; DeepSeek-V4-Pro lists neither. For document-image, chart and video workflows, only one of the two lists the capability.

## Openness and deployment

DeepSeek-V4-Pro is open weight under MIT; Qwen3.8-Max is proprietary with API access only. Self-hosting is an option for the DeepSeek model and not for Qwen3.8-Max. Note the database lists DeepSeek-V4-Pro's status as deprecated (preview 2026-04-24, GA 2026-08-13) — check the provider's current lineup before building on it.

## Benchmarks and verification

The database holds 4 benchmark records for DeepSeek-V4-Pro and 5 for Qwen3.8-Max, all labeled with source type (vendor-reported vs independent) and version. Different benchmarks cover different models, so counts are not comparable scores. We do not rank models on this page; the tables above state measured and vendor-listed facts, and the trade-offs below explain what to weigh.

## Trade-off summary

- Price: DeepSeek-V4-Pro lists substantially lower input/output prices.
- Media: Qwen3.8-Max lists vision and video; DeepSeek-V4-Pro lists neither.
- Output length: DeepSeek-V4-Pro lists a 3x longer maximum output.
- Openness: DeepSeek-V4-Pro is MIT open weight and self-hostable; Qwen3.8-Max is API-only.
- Status: DeepSeek-V4-Pro is listed as deprecated; Qwen3.8-Max as active.

The right choice depends on the workload — vision requirements, self-hosting needs, price sensitivity and how much output a task generates. Verify prices on the official pages before committing, as both change frequently.
