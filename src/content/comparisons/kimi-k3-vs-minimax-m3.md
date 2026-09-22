---
title: "Kimi K3 vs MiniMax M3: Price, Output Length and Media"
description: "Evidence-based comparison of Kimi K3 and MiniMax M3: API pricing, context window, maximum output, capabilities, licenses and benchmark records from the China AI Hub database."
entities:
  - kimi-k3
  - minimax-m3
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
  - source_name: "Moonshot AI — Kimi K3 (GitHub)"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
  - source_name: "Kimi platform — Models documentation"
    source_url: "https://platform.kimi.ai/docs/models.md"
    source_type: official
  - source_name: "MiniMax — Models introduction"
    source_url: "https://platform.minimaxi.com/docs/guides/models-intro"
    source_type: official
  - source_name: "MiniMax — MiniMax M3 announcement"
    source_url: "https://www.minimax.cn/blog/minimax-m3"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-22. Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | Kimi K3 | MiniMax M3 |
|---|---|---|
| Context window | 1,048,576 tokens | 1,048,576 tokens |
| Maximum output | 1,048,576 tokens | Not publicly disclosed |
| Input price (per 1M) | $3.00 | $0.30 |
| Output price (per 1M) | $15.00 | $1.20 |
| Open weights | Yes (Kimi K3 License) | Yes (MiniMax Community License) |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Yes |
| Vision / Video | Yes / Yes | Yes / Yes |
| Tool calling | Yes | Yes |
| Agent capability | Yes | Yes |
| Benchmark records in DB | 6 | 5 |

## Pricing

The widest price spread among our current flagship comparisons: Kimi K3 lists $3.00 input / $15.00 output per 1M tokens; MiniMax M3 lists $0.30 input / $1.20 output — one-tenth of Kimi K3's input price and one-twelfth of its output price. Both are official pay-as-you-go API prices. On long reasoning or generation workloads the per-task cost difference can be an order of magnitude.

## Context and output

Both list a 1,048,576-token context window. Kimi K3 lists a 1,048,576-token maximum output (the full window); MiniMax M3 does not publicly disclose a maximum output figure. For very long generations the listed difference is material.

## Capabilities

Capability profiles are close: both list reasoning, coding, vision, video, tool calling and agent capability. Neither lists structured output or function calling under those exact labels. Media coverage (vision and video) is listed for both.

## Openness and licensing

Both are open weight, with different obligations. Kimi K3 uses the Kimi K3 License: MIT-style terms, plus a separate agreement for Model-as-a-Service operators above $20M revenue and a UI attribution requirement above 100M MAU / $20M monthly revenue. MiniMax M3 uses the MiniMax Community License: free for non-commercial use; commercial use requires "Built with MiniMax M3" attribution and, above $20M yearly revenue, written authorization (otherwise a one-time notice to MiniMax). Read both texts before commercial self-hosting — the non-commercial restriction in the MiniMax license is the sharper boundary.

## Benchmarks and verification

The database holds 6 benchmark records for Kimi K3 and 5 for MiniMax M3, labeled by source type and version. Different benchmarks cover different models; we do not rank the two on this page. Check each benchmark page for score-by-score source labels.

## Trade-off summary

- Price: MiniMax M3 lists roughly one-tenth the input and one-twelfth the output price of Kimi K3.
- Output length: Kimi K3 lists a 1M-token maximum output; MiniMax M3 does not disclose one.
- Capabilities: closely matched on paper — reasoning, coding, vision, video, tools, agent.
- License: both custom; MiniMax's has a non-commercial boundary, Kimi's has revenue-triggered obligations.

Choose by cost profile and output-length needs, and by which license you can actually operate under. Verify current prices on the official pages before committing.
