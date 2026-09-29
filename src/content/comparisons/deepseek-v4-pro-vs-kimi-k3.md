---
image: "/images/ai/comparisons-deepseek-v4-pro-vs-kimi-k3.webp"
image_credit: "AI-generated illustration (Seedream)"
title: "DeepSeek-V4-Pro vs Kimi K3: Price, Output Length and Licensing"
author: "SinoAI Hub Research Team"
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

**Benchmark comparability is limited**: the two models' scores come from different test configurations — different benchmark versions, evaluation harnesses and tool setups — and several benchmarks cover only one of the two. Do not rank on headline scores alone.

## Why each difference matters

China AI Hub analysis indicates the following per-dimension implications, drawn from the listed facts above.

- **Cost**: [DeepSeek-V4-Pro](/models/deepseek-v4-pro/) has an advantage at ~4.5x lower input and ~7.5x lower output price. Because reasoning workloads multiply output tokens, the output-price gap has a larger real-world effect on per-task cost than the input gap alone suggests.
- **Long-context**: both list a 1M-token input window; [Kimi K3](/models/kimi-k3/) has an advantage in extreme-length generation because it lists the full-window 1M-token maximum output.
- **Reasoning**: both list reasoning, so neither has a listed advantage on this axis — the output-price differential, not capability, drives the reasoning-workload decision.
- **Coding**: both list coding and tool calling; DeepSeek-V4-Pro's price is more relevant for high-volume code generation, while Kimi K3 adds vision/video for multimodal coding.
- **Agent**: Kimi K3 is more relevant when agent orchestration is core — it lists agent capability where DeepSeek-V4-Pro does not.
- **Deployment / license**: both are open-weight and self-hostable, but the licenses differ materially. MIT (DeepSeek) is permissive with no thresholds; the Kimi K3 License has a limitation for large operators — Model-as-a-Service above $20M revenue needs a separate agreement, and products above 100M MAU / $20M monthly revenue must display attribution.
- **API**: both expose an API; DeepSeek-V4-Pro is listed deprecated, which is the operational limitation to verify before committing.

## Trade-off summary

- Price: DeepSeek-V4-Pro lists substantially lower prices on both input and output.
- Output length: Kimi K3 lists a 1M-token maximum output, the highest in our database.
- Media and agent: Kimi K3 lists vision, video and agent capability; DeepSeek-V4-Pro does not.
- License: MIT (DeepSeek) versus Kimi K3 License with revenue-triggered obligations.
- Status: DeepSeek-V4-Pro is listed as deprecated; Kimi K3 as active.

Choose by workload: long-form generation and media favor Kimi K3's listed capabilities; price-sensitive text workloads favor the DeepSeek pricing, with the caveat of its deprecated status. Verify current prices and status on the official pages before committing.

## Decision context

China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.

**For API developers.** Price is the sharpest split: DeepSeek-V4-Pro lists ~4.5x lower input and ~7.5x lower output price, which compounds on reasoning workloads that multiply output tokens. Both list tool calling; Kimi K3 additionally lists structured output. DeepSeek-V4-Pro is listed deprecated, which is the operational caveat to verify before committing. Latency is not publicly documented for either model on this page.

**For self-hosting.** Both are open weight but under different licenses — MIT (DeepSeek-V4-Pro, no revenue thresholds) versus the Kimi K3 License (a separate agreement above $20M revenue, and UI attribution above 100M MAU / $20M monthly revenue). Hardware requirements and quantization are Not publicly documented on this page.

**For coding agents.** Both list coding and tool calling. Kimi K3 lists agent capability where DeepSeek-V4-Pro does not, and adds vision/video for multimodal coding. Both list a 1M-token context. SWE-benchmark and terminal scores are not broken out on this page (aggregate counts 4 vs 6).

**For enterprise.** Region, SLA, data-residency and compliance terms are not publicly documented — confirm with the vendor. Deployment and license differ materially: MIT has no revenue thresholds, while the Kimi K3 License imposes obligations for large operators, which may matter in enterprise legal review. DeepSeek-V4-Pro's deprecated status is the other operational risk to verify.

## What is uncertain

- Benchmark scores are vendor-reported and not independently re-measured.
- DeepSeek-V4-Pro is listed deprecated with conflicting official pages on its post-2026-09-14 status.
- No third-party benchmark evidence is recorded for either model.

## Sources

- [DeepSeek API pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek V4 Preview announcement](https://www.deepseek.com/en/news/v4-preview/)
- [Moonshot AI — Kimi K3 (GitHub)](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi platform — Models documentation](https://platform.kimi.ai/docs/models.md)

*Labels used above: **Official fact** (prices, context windows, capabilities and license terms from primary provider sources), **Vendor-reported claim** (benchmark scores), and **China AI Hub analysis** (the "why each difference matters" reasoning, introduced as analysis). No third-party benchmark evidence is currently recorded for these models.*
