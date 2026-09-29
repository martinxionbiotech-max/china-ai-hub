---
title: "Qwen3.8-Max vs Qwen3.8-2.4T-A95B: Closed API Flagship Against Its Open-Weight Sibling"
author: "SinoAI Hub Research Team"
description: "Evidence-based comparison of Qwen3.8-Max and Qwen3.8-2.4T-A95B: API availability, context window, capabilities, licensing, deployment and benchmark records from the China AI Hub database."
entities:
  - qwen3.8-max
  - qwen3.8-2.4t-a95b
dimensions:
  - pricing
  - context
  - coding
  - vision
  - agent
  - license
  - deployment
  - benchmark
published_date: "2026-09-29"
updated_date: "2026-09-29"
sources:
  - source_name: "Alibaba Cloud Model Studio — Qwen3.8-Max"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"
    source_type: cloud_doc
  - source_name: "Alibaba Cloud Model Studio — Model pricing"
    source_url: "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
    source_type: cloud_doc
  - source_name: "Hugging Face model card — Qwen3.8-2.4T-A95B"
    source_url: "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"
    source_type: official
  - source_name: "Qwen3.8 repository README"
    source_url: "https://github.com/QwenLM/Qwen3.8"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-20. Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | Qwen3.8-Max | Qwen3.8-2.4T-A95B |
|---|---|---|
| Status (database) | active | active |
| Context window | 1,048,576 tokens | 262,144 tokens (extensible to 1,010,000) |
| Maximum output | 131,072 tokens | Not stated |
| Input price (per 1M) | $2.00 (Singapore) | N/A (no API) |
| Output price (per 1M) | $6.00 (Singapore) | N/A (no API) |
| Open weights | No (proprietary) | Yes (Qwen3.8-Max License) |
| API available | Yes | No |
| Reasoning | Yes | Yes |
| Coding | Yes | Not listed |
| Vision / Video | Yes / Yes | No / No |
| Tool calling | Yes | Not listed |
| Structured output | Yes | Not listed |
| Benchmark records in DB | 5 | 0 |

## Pricing and API availability

This is the sharpest split. Qwen3.8-Max is an API model billed at $2.00 input / $6.00 output per 1M tokens (Singapore region). Qwen3.8-2.4T-A95B has no API and no API pricing — it is an open-weight release with `api_available: false` and `official_api: false`. One is paid-by-the-token; the other is free to download but you run it yourself.

## Context and output

Qwen3.8-Max lists a 1,048,576-token context (991,808 max input) and 131,072 maximum output. Qwen3.8-2.4T-A95B lists a native 262,144-token context, extensible to 1,010,000, with no stated maximum output. For long-input analysis out of the box, the API flagship lists the larger default window.

## Architecture and parameters

The two share the same published architecture: a 2.4T-parameter MoE with 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, and a Gated DeltaNet + Gated Attention hybrid. The difference is packaging, not design — Qwen3.8-Max is the closed API product with multimodal input and non-thinking mode, while Qwen3.8-2.4T-A95B is the text-only, thinking-only open-weight release. Alibaba's own documentation states the two are "not the same product" despite the shared architecture.

## Coding

Qwen3.8-Max lists coding and publishes vendor-reported Terminal-Bench 2.1 (86.6) and SWE-bench Pro (67.7). Qwen3.8-2.4T-A95B does not list coding in its recorded capability set (reasoning only) and has no benchmark records. For coding workloads the database records a clear difference in listed capability.

## Vision

Qwen3.8-Max lists vision and video input; Qwen3.8-2.4T-A95B is text-only (vision listed as false). For multimodal input only the API flagship lists the capability. This is the documented reason Alibaba describes the open weights as "not the same product" as the API model.

## Agent capabilities

Qwen3.8-Max lists tool calling, structured output, function calling and web search — a full agent substrate. Qwen3.8-2.4T-A95B lists none of these in its recorded set. For tool-driven agent pipelines, only the API flagship lists the relevant surface.

## License and openness

Qwen3.8-Max is proprietary, closed weight. Qwen3.8-2.4T-A95B is open weight under the "Qwen3.8-Max License" — a custom MIT-style license: unrestricted use/copy/modify/sell, but products with >100M MAU or >$20M monthly revenue must display the model name, and Model-as-a-Service or AI Work Assistant businesses with >$50M/12-month revenue need a separate license. This is conditional-open, not plain MIT.

## Deployment

Qwen3.8-Max is API-only, served through Alibaba Cloud Model Studio across six regions (Beijing, Singapore, Hong Kong, Frankfurt, US-Virginia, Tokyo). Qwen3.8-2.4T-A95B is self-hostable open weight (no API). The deployment decision is essentially: managed multi-region API versus run-your-own open weights.

## Benchmarks

The database holds 5 benchmark records for Qwen3.8-Max — Terminal-Bench 2.1 (86.6), SWE-bench Pro (67.7), GPQA Diamond (92.6), HLE (43.6, 56.2 with tools) and MRCR v2 256K (92.9) — and 0 for Qwen3.8-2.4T-A95B. All Qwen3.8-Max rows are vendor-reported from the model card.

**Benchmark comparability is limited**: Qwen3.8-2.4T-A95B has no benchmark records, so no head-to-head score comparison is possible.

## Why each difference matters

China AI Hub analysis indicates the following per-dimension implications, drawn from the listed facts above.

- **Pricing**: [Qwen3.8-Max](/models/qwen38-max/) is paid per token via API; [Qwen3.8-2.4T-A95B](/models/qwen38-24t-a95b/) has no API pricing — its cost is your own inference hardware, not a per-token rate.
- **Context**: Qwen3.8-Max lists a larger default context (1M) versus the open model's 262,144 native (extensible to 1,010,000).
- **Coding**: Qwen3.8-Max is more relevant for coding workloads — it lists coding and coding benchmarks where the open model lists neither.
- **Vision / media**: Qwen3.8-Max is more relevant for multimodal input — it lists vision/video where the open model is text-only.
- **Agent**: Qwen3.8-Max is more relevant for tool-driven agent pipelines — it lists tool calling and structured output where the open model lists none.
- **License**: Qwen3.8-Max is proprietary; the open model is conditional-open (custom MIT-style with attribution and revenue thresholds).
- **Deployment**: Qwen3.8-Max is a managed six-region API; the open model is self-hosted — the choice is managed service versus run-your-own.
- **Benchmark**: Qwen3.8-Max records 5 and the open model records 0; the evidence base is not comparable.

## Trade-off summary

- API vs self-host: Qwen3.8-Max is a paid API; Qwen3.8-2.4T-A95B is a downloadable open weight with no API.
- Capabilities: Qwen3.8-Max lists coding, vision/video, tool calling and structured output; the open model is text-only, reasoning-only.
- Context: Max lists 1M default; the open model lists 262,144 native (extensible to 1,010,000).
- License: proprietary (Max) versus conditional-open custom MIT-style (A95B).

These are the same 2.4T/95B architecture marketed as two different products, not two interchangeable editions: Qwen3.8-Max is the managed multimodal flagship; Qwen3.8-2.4T-A95B is the text-only, thinking-only open-weight release. Choose by which constraint binds — managed convenience and modality, or open-weight self-hosting. Verify current prices on the official pages before committing.

## Decision context

China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.

**For API developers.** Only Qwen3.8-Max has an API. It lists coding, tool calling, structured output and vision/video. The open model has no API, so API developers have one option here, not two.

**For self-hosting.** Only Qwen3.8-2.4T-A95B is self-hostable. Its license is conditional-open: display the model name above 100M MAU / $20M monthly revenue, and a separate license for Model-as-a-Service above $50M/12-month revenue. Hardware requirements and quantization are Not publicly documented on this page.

**For coding agents.** Qwen3.8-Max lists coding, tool calling and structured output plus coding benchmarks (Terminal-Bench 2.1 86.6, SWE-bench Pro 67.7); the open model lists none of these and is text-only, so the API model is the documented coding-agent substrate.

**For enterprise.** The deployment split is fundamental: managed six-region API (Max) versus self-hosted open weights (A95B) under a conditional license. Region, SLA, data-residency and compliance terms for the API are not publicly documented — confirm with the vendor.

## What is uncertain

- Qwen3.8-2.4T-A95B has no benchmark records and no documented coding capability.
- The open model's maximum output is not stated.
- No third-party benchmark evidence is recorded for either model.

## Sources

- [Alibaba Cloud Model Studio — Qwen3.8-Max](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- [Alibaba Cloud Model Studio — Model pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)
- [Hugging Face model card — Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Qwen3.8 repository README](https://github.com/QwenLM/Qwen3.8)

*Labels used above: **Official fact** (prices, context windows, capabilities and license terms from primary provider sources), **Vendor-reported claim** (benchmark scores), and **China AI Hub analysis** (the "why each difference matters" reasoning, introduced as analysis). No third-party benchmark evidence is currently recorded for these models.*
