---
title: "DeepSeek-V4-Pro vs DeepSeek-V4.1-Flash: Deprecated Flagship to the Current Flash"
author: "SinoAI Hub Research Team"
description: "Evidence-based comparison of DeepSeek-V4-Pro and DeepSeek-V4.1-Flash: API pricing, context window, capabilities, licenses, deployment and benchmark records from the China AI Hub database."
entities:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
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
  - source_name: "DeepSeek API docs — Models & Pricing"
    source_url: "https://api-docs.deepseek.com/quick_start/pricing"
    source_type: official
  - source_name: "DeepSeek API Change Log"
    source_url: "https://api-docs.deepseek.com/updates"
    source_type: official
  - source_name: "DeepSeek V4 Preview announcement"
    source_url: "https://www.deepseek.com/en/news/v4-preview/"
    source_type: official
  - source_name: "DeepSeek V4.1-Flash announcement"
    source_url: "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"
    source_type: official
  - source_name: "Hugging Face model card — DeepSeek-V4.1-Flash"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-20. Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | DeepSeek-V4-Pro | DeepSeek-V4.1-Flash |
|---|---|---|
| Status (database) | deprecated | active |
| Context window | 1,048,576 tokens | 1,048,576 tokens |
| Maximum output | 393,216 tokens | 393,216 tokens |
| Input price (per 1M, off-peak) | $0.66 | $0.15 |
| Output price (per 1M, off-peak) | $1.98 | $0.60 |
| Open weights | Yes (MIT) | Yes (MIT) |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Yes |
| Vision | No | Yes |
| Tool calling | Yes | Yes |
| Function calling | Yes | Yes |
| Structured output | Yes | Yes |
| Agent capability | Not listed | Not listed |
| Benchmark records in DB | 4 | 5 |

## Pricing

DeepSeek-V4-Pro lists $0.66 input / $1.98 output per 1M tokens; DeepSeek-V4.1-Flash lists $0.15 input / $0.60 output — roughly a quarter of the input price and under a third of the output price. Both are off-peak list prices; DeepSeek bills a 2x rate during documented peak windows, so both models carry the same peak/off-peak structure. Because the output-token gap (roughly 3.3x) exceeds the input-token gap (4.4x on paper, but output dominates reasoning workloads), the practical cost difference is largest on generation-heavy tasks.

## Context and output

The two models list an identical context window (1,048,576 tokens) and identical maximum output (393,216 tokens). On paper this axis does not differentiate them. The difference is architectural: V4-Pro activates 49B of a 1.6T-parameter MoE, while V4.1-Flash activates only 8B on input and 16B on output of a 552B MoE — a much sparser design that is what enables the flash-tier price at the same window size.

## Coding

Both list coding and tool calling, and both publish agentic-coding benchmarks. The distinction is in the numbers recorded: V4-Pro lists Terminal-Bench 2.1 at 87.9 and DeepSWE at 62.7; V4.1-Flash lists Terminal-Bench 2.1 at 90.6 and DeepSWE v1.1 at 74.2. The benchmark versions differ (DeepSWE vs DeepSWE v1.1), so the two are not directly comparable as a head-to-head score. What is documented is that DeepSeek positions V4.1-Flash as the current standard API coding model, with legacy names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` routing to it.

## Vision

This is a clear listed difference: DeepSeek-V4.1-Flash lists native vision; DeepSeek-V4-Pro lists no vision support. For image-input workflows (document images, charts, multimodal agent loops), only the flash model lists the capability. Neither model lists video input.

## Agent capabilities

Neither model lists an explicit `agent_capability` flag, but both list the tooling an agent needs — tool calling, function calling and structured output. DeepSeek's own [DeepSeek Harness](/agents/deepseek-harness/) product lists both models as underlying options. The operational difference is status: V4-Pro is deprecated, so a new agent integration would more naturally target V4.1-Flash unless a specific V4-Pro checkpoint is required.

## License and openness

Both are MIT-licensed open weight and self-hostable, so the license axis does not differentiate them. The same self-hosting caveat applies to both: a large sparse MoE requires substantial GPU memory even if activation is low, and the V4.1-Flash's Causal Encoder-Decoder design is non-trivial to serve efficiently outside DeepSeek's own stack.

## Deployment

Both are served through the DeepSeek Platform and both are open weight for self-hosting. The deployment-relevant difference is lifecycle: DeepSeek-V4-Pro is listed deprecated with conflicting official pages on whether its API continues unchanged after 2026-09-14 or routes requests to V4.1-Flash until V4.1-Pro launches. A production deployment on V4-Pro therefore carries an operational risk that a deployment on V4.1-Flash does not.

## Benchmarks

The database holds 4 benchmark records for DeepSeek-V4-Pro (HLE, Terminal-Bench 2.1, DeepSWE, Agents' Last Exam) and 5 for DeepSeek-V4.1-Flash (GPQA Diamond, HLE, Codeforces, Terminal-Bench 2.1, DeepSWE v1.1). All are vendor-reported. Counts are not scores, and the benchmark sets overlap only partially.

**Benchmark comparability is limited**: the two models' scores come from different test configurations — different benchmark versions (DeepSWE vs DeepSWE v1.1), evaluation harnesses and tool setups. Do not rank on headline scores alone.

## Why each difference matters

China AI Hub analysis indicates the following per-dimension implications, drawn from the listed facts above.

- **Pricing**: [DeepSeek-V4.1-Flash](/models/deepseek-v4-1-flash/) has an advantage at roughly a quarter of V4-Pro's input price and under a third of its output price; the output-token gap compounds on reasoning workloads.
- **Context**: identical 1M-token windows, so long-input analysis is equivalent; neither has a listed advantage on this axis.
- **Coding**: both list coding and tool calling; V4.1-Flash is the current API model and lists higher absolute terminal/coding scores, but the benchmark versions differ, so treat the numeric gap as non-comparable rather than as a verified lead.
- **Vision**: V4.1-Flash lists native vision where V4-Pro lists none — relevant when image input is required.
- **Agent**: neither lists an agent flag, and both list the tool/function/structured-output surface; the practical choice tracks status, not capability.
- **License**: both MIT open weight — this axis does not differentiate.
- **Deployment**: both self-hostable; V4-Pro's deprecated status is the operational caveat that V4.1-Flash does not carry.
- **Benchmark**: V4-Pro records 4 and V4.1-Flash records 5 vendor-reported rows, with only partial overlap and version mismatch; counts and scores are not directly comparable.

## Trade-off summary

- Price: DeepSeek-V4.1-Flash lists roughly a quarter of V4-Pro's input and under a third of its output price.
- Vision: DeepSeek-V4.1-Flash lists native vision; DeepSeek-V4-Pro does not.
- Context and output: identical (1M in / 393,216 out).
- Status: DeepSeek-V4-Pro is deprecated; DeepSeek-V4.1-Flash is active.
- License: both MIT open weight.

Choose by lifecycle and capability fit: for new, price-sensitive and multimodal workloads, DeepSeek-V4.1-Flash is the current standard model; DeepSeek-V4-Pro remains relevant only where a specific deprecated checkpoint or a 1.6T-total-parameter open weight is explicitly required. Verify current prices and the V4-Pro routing status on the official pages before committing.

## Decision context

China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.

**For API developers.** DeepSeek-V4.1-Flash lists ~4x lower input and ~3x lower output prices at the same 1M context and 393K output, so cost favors the flash model; the output-token gap compounds on reasoning workloads. Both list tool calling, function calling and structured output. V4.1-Flash adds native vision. Latency is not publicly documented for either model on this page.

**For self-hosting.** Both are MIT open weight and self-hostable, so the license axis does not differentiate. Hardware requirements and quantization are Not publicly documented on this page; the V4.1-Flash encoder-decoder design is a serving-complexity caveat. DeepSeek-V4-Pro's deprecated status is the operational risk to verify.

**For coding agents.** Both list coding, tool calling and structured output. V4.1-Flash lists higher absolute terminal/coding benchmark numbers, but the versions differ (DeepSWE vs DeepSWE v1.1), so the gap is not a verified lead. Both list a 1M context. V4.1-Flash is the current API model for new integrations.

**For enterprise.** Region, SLA, data-residency and compliance terms are not publicly documented — confirm with the vendor. Deployment and license are equivalent (MIT, self-hostable); the deciding factor is lifecycle — V4-Pro is deprecated, while V4.1-Flash is the active standard.

## What is uncertain

- Benchmark comparability is limited — different versions, harnesses and partial coverage.
- DeepSeek-V4-Pro's post-2026-09-14 API status is conflicting across official pages.
- Whether the V4-Pro Hugging Face checkpoint matches the 0813 GA checkpoint is not documented.
- Serving regions are not disclosed for either model.

## Sources

- [DeepSeek API docs — Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [DeepSeek API Change Log](https://api-docs.deepseek.com/updates)
- [DeepSeek V4 Preview announcement](https://www.deepseek.com/en/news/v4-preview/)
- [DeepSeek V4.1-Flash announcement](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)
- [Hugging Face model card — DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)

*Labels used above: **Official fact** (prices, context windows, capabilities and license terms from primary provider sources), **Vendor-reported claim** (benchmark scores), and **China AI Hub analysis** (the "why each difference matters" reasoning, introduced as analysis). No third-party benchmark evidence is currently recorded for these models.*
