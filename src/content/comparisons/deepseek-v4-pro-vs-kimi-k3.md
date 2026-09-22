---
title: "DeepSeek-V4-Pro vs Kimi K3: Price, Output Length and Licensing"
description: "Evidence-based comparison of DeepSeek-V4-Pro and Kimi K3: API pricing, context window, maximum output, capabilities, licenses and benchmark records from the China AI Hub database."
entities:
  - deepseek-v4-pro
  - kimi-k3
dimensions:
  - pricing
  - context
  - reasoning
  - coding
  - vision
  - agent
  - open_weight
  - license
  - api
published_date: "2026-09-22"
updated_date: "2026-09-22"
sources:
  - source_name: "DeepSeek API pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
  - source_name: "DeepSeek V4 Preview announcement"
    source_url: "https://www.deepseek.com/en/news/v4-preview/"
    source_type: official
  - source_name: "Moonshot AI — Kimi K3 (GitHub)"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
  - source_name: "Kimi platform — Models documentation"
    source_url: "https://platform.kimi.ai/docs/models.md"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-22. Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | DeepSeek-V4-Pro | Kimi K3 |
|---|---|---|
| Status (database) | deprecated | active |
| Context window | 1,048,576 tokens | 1,048,576 tokens |
| Maximum output | 393,216 tokens | 1,048,576 tokens |
| Input price (per 1M) | $0.66 | $3.00 |
| Output price (per 1M) | $1.98 | $15.00 |
| Open weights | Yes (MIT) | Yes (Kimi K3 License) |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Yes |
| Vision / Video | No | Yes / Yes |
| Tool calling | Yes | Yes |
| Agent capability | Not listed | Yes |
| Benchmark records in DB | 4 | 6 |

## Pricing

DeepSeek-V4-Pro lists $0.66 input / $1.98 output per 1M tokens. Kimi K3 lists $3.00 input / $15.00 output — roughly 4.5x the input price and 7.5x the output price. Both are pay-as-you-go API prices from official pages. Because output price dominates reasoning workloads, the per-task cost gap can be larger than the input-price gap suggests.

## Context and output

Both list a 1,048,576-token context window. Kimi K3 lists a 1,048,576-token maximum output — the full window — versus 393,216 for DeepSeek-V4-Pro. For extreme-length generation tasks this is the largest listed-output difference in our database.

## Capabilities

Both list reasoning, coding and tool calling. Kimi K3 additionally lists vision, video, structured output and agent capability. DeepSeek-V4-Pro lists function calling and structured output, and no vision/video. Agent capability is listed for Kimi K3 and not for DeepSeek-V4-Pro.

## Openness and licensing

Both are open weight, but the licenses differ materially. DeepSeek-V4-Pro is MIT. Kimi K3 uses the Kimi K3 License: permissive MIT-style terms, with additional obligations — Model-as-a-Service operators above $20M aggregate revenue must sign a separate agreement, and products above 100M MAU or $20M monthly revenue must display "Kimi K3" in the UI. Read the license text before commercial self-hosting.

## Benchmarks and verification

The database holds 4 benchmark records for DeepSeek-V4-Pro and 6 for Kimi K3, each labeled with source type and version. Different benchmarks cover different models; counts are not scores. We do not rank the two models on this page.

## Trade-off summary

- Price: DeepSeek-V4-Pro lists substantially lower prices on both input and output.
- Output length: Kimi K3 lists a 1M-token maximum output, the highest in our database.
- Media and agent: Kimi K3 lists vision, video and agent capability; DeepSeek-V4-Pro does not.
- License: MIT (DeepSeek) versus Kimi K3 License with revenue-triggered obligations.
- Status: DeepSeek-V4-Pro is listed as deprecated; Kimi K3 as active.

Choose by workload: long-form generation and media favor Kimi K3's listed capabilities; price-sensitive text workloads favor the DeepSeek pricing, with the caveat of its deprecated status. Verify current prices and status on the official pages before committing.
