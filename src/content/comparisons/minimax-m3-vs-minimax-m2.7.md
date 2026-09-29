---
title: "MiniMax-M3 vs MiniMax-M2.7: Flagship Against the Self-Evolving Model"
author: "SinoAI Hub Research Team"
description: "Evidence-based comparison of MiniMax-M3 and MiniMax-M2.7: API pricing, context window, capabilities, licenses, deployment and benchmark records from the China AI Hub database."
entities:
  - minimax-m3
  - minimax-m2.7
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
  - source_name: "MiniMax API platform — model overview (CN)"
    source_url: "https://platform.minimaxi.com/docs/guides/models-intro"
    source_type: official
  - source_name: "MiniMax M3 official blog post"
    source_url: "https://www.minimax.cn/blog/minimax-m3"
    source_type: official
  - source_name: "Hugging Face model card — MiniMax-M3"
    source_url: "https://huggingface.co/MiniMaxAI/MiniMax-M3"
    source_type: official
  - source_name: "Hugging Face model card — MiniMax-M2.7"
    source_url: "https://huggingface.co/MiniMaxAI/MiniMax-M2.7"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-20 (M2.7 last verified 2026-09-27). Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | MiniMax-M3 | MiniMax-M2.7 |
|---|---|---|
| Status (database) | active | active |
| Context window | 1,048,576 tokens | 204,800 tokens |
| Maximum output | Not publicly disclosed | Not publicly disclosed |
| Input price (per 1M) | $0.30 | $0.30 |
| Output price (per 1M) | $1.20 | $1.20 |
| Open weights | Yes (MiniMax Community License) | Yes (custom non-commercial) |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Not listed |
| Vision / Video | Yes / Yes | No / No |
| Tool calling | Yes | Yes |
| Agent capability | Yes | Not listed |
| Benchmark records in DB | 5 | 2 |

## Pricing

Both list the identical price — $0.30 input / $1.20 output per 1M tokens — with cache reads at $0.06. MiniMax-M3's pricing splits at the 512K input boundary (double above), and it offers a priority tier at 1.5x with a permanent 50%-off list. On price the two are equivalent per the database, which makes the capability differences the deciding factors.

## Context and output

MiniMax-M3 lists a 1,048,576-token context window (with at least 512K guaranteed usable and pricing split at 512K). MiniMax-M2.7 lists a 204,800-token context. Neither publicly discloses a standalone maximum-output ceiling (M3's 131,072 is derived from the official card's evaluation config). For long-context work the difference is a 5x listed input window.

## Architecture and parameters

MiniMax-M3 is a ~428B-total / ~23B-activated MoE built around MiniMax Sparse Attention (MSA), which MiniMax claims delivers 9x prefill and 15x decode speedup versus M2 at 1M context — a vendor claim, not an independent measurement. MiniMax-M2.7 does not disclose its parameter count; it is positioned as MiniMax's "self-evolving" model and, unlike M3, is not documented with a sparse-attention architecture card. The architecture disclosure gradient between the two is itself a recorded difference.

## Coding

MiniMax-M3 lists coding and publishes vendor-reported SWE-bench Pro (59.0) and Terminal-Bench 2.1 (66.0). MiniMax-M2.7 does not list coding in its recorded capability set (reasoning and tool calling only). For coding workloads the database records a clear difference in listed capability.

## Vision

MiniMax-M3 lists vision and video input; MiniMax-M2.7 is text-only input. For multimodal understanding only M3 lists the capability.

## Agent capabilities

MiniMax-M3 lists agent capability and tool calling, and publishes a vendor-reported MCP Atlas score (74.2) measuring MCP-connected tool use — the pattern agent builders rely on. MiniMax-M2.7 lists tool calling but not agent capability. Thinking is disabled by default on M3 (`thinking=adaptive` enables it); on M2.7 interleaved thinking is always on and cannot be disabled via API.

## License and openness

Both are open weight, but the licenses differ materially. MiniMax-M3 uses the MiniMax Community License: free for non-commercial use; commercial use requires "Built with MiniMax M3" attribution and, above $20M yearly revenue, written authorization (otherwise a one-time notice). MiniMax-M2.7 uses a custom NON-COMMERCIAL license: any commercial use requires prior written authorization from MiniMax, with attribution required. The M2.7 license is the stricter boundary — commercial self-hosting is effectively gated for both, but M3 allows commercial use below the revenue threshold with attribution.

## Deployment

Both are self-hostable open weight and served through the MiniMax Platform. Both list regions china and international. M3 is a ~428B-total / ~23B-active MoE; M2.7's parameter count is not publicly disclosed. Self-hosting hardware requirements and quantization are not publicly documented for either.

## Benchmarks

The database holds 5 benchmark records for MiniMax-M3 (BrowseComp, PostTrainBench, SWE-bench Pro, Terminal-Bench 2.1, MCP Atlas) and 2 for MiniMax-M2.7 (GDPval-AA ELO, MM Claw end-to-end). The sets do not overlap. All are vendor-reported.

**Benchmark comparability is limited**: the two models' scores come from different benchmark sets and configurations, and the M2.7 rows (an ELO rating and a custom end-to-end benchmark) are not directly comparable to M3's accuracy scores. Do not rank on headline scores alone.

## Why each difference matters

China AI Hub analysis indicates the following per-dimension implications, drawn from the listed facts above.

- **Pricing**: identical listed prices ($0.30/$1.20), so this axis does not differentiate — capability fit decides.
- **Context**: [MiniMax-M3](/models/minimax-m3/) has an advantage in long-context work at 1,048,576 tokens versus M2.7's 204,800.
- **Coding**: MiniMax-M3 is more relevant for coding workloads — it lists coding and coding benchmarks where [MiniMax-M2.7](/models/minimax-m27/) lists none.
- **Vision / media**: MiniMax-M3 is more relevant when image or video input is required — it lists both where M2.7 is text-only.
- **Agent**: MiniMax-M3 is more relevant for agent/tool workloads — it lists agent capability and MCP tool use where M2.7 lists only tool calling.
- **License**: both conditional-open; M2.7 has a limitation in its strictly non-commercial boundary, while M3 allows commercial use with attribution below the revenue threshold.
- **Deployment**: both self-hostable; the footprint differs (M3 discloses ~428B/~23B; M2.7 does not disclose parameters).
- **Benchmark**: M3 records 5 and M2.7 records 2 vendor-reported rows with no overlap; not directly comparable.

## Trade-off summary

- Context: MiniMax-M3 lists a 1M-token window; M2.7 lists 204,800.
- Capabilities: MiniMax-M3 lists coding, vision, video and agent capability; M2.7 lists reasoning and tool calling only.
- Price: identical ($0.30/$1.20).
- License: M3 community license (commercial with attribution below threshold) versus M2.7 non-commercial-only.

Choose by workload: long-context, multimodal, coding and agent workloads favor MiniMax-M3's listed capabilities; M2.7's niche is its self-evolving positioning, and it is priced the same but with a stricter license. Verify current prices on the official pages before committing.

## Decision context

China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.

**For API developers.** The prices are identical, so the choice is capability-driven: MiniMax-M3 lists coding, vision/video and agent capability plus a 1M context; M2.7 lists only reasoning and tool calling with a 204,800 context. Thinking is off by default on M3 (`thinking=adaptive`); always-on on M2.7. Latency is not publicly documented on this page.

**For self-hosting.** Both are open weight with conditional licenses. M3's Community License allows commercial use with attribution below a $20M revenue threshold; M2.7's non-commercial license requires prior written authorization for any commercial use. Hardware requirements and quantization are Not publicly documented on this page.

**For coding agents.** MiniMax-M3 lists coding and publishes SWE-bench Pro (59.0) and Terminal-Bench 2.1 (66.0) plus MCP Atlas (74.2) for tool use; M2.7 lists no coding capability. M3 is more relevant for coding and agent workloads.

**For enterprise.** Region, SLA, data-residency and compliance terms are not publicly documented — confirm with the vendor. Deployment is comparable (both self-hostable), but the license obligations differ materially: M2.7's non-commercial boundary is stricter than M3's community license.

## What is uncertain

- Neither model publicly discloses a standalone maximum-output ceiling.
- M2.7's parameter count is not publicly disclosed.
- The MSA speedup claims (9x prefill / 15x decode) for M3 are vendor claims, not independently measured.
- Benchmark sets do not overlap, and M2.7's rows use different metrics (ELO, custom end-to-end).

## Sources

- [MiniMax API platform — model overview (CN)](https://platform.minimaxi.com/docs/guides/models-intro)
- [MiniMax M3 official blog post](https://www.minimax.cn/blog/minimax-m3)
- [Hugging Face model card — MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3)
- [Hugging Face model card — MiniMax-M2.7](https://huggingface.co/MiniMaxAI/MiniMax-M2.7)

*Labels used above: **Official fact** (prices, context windows, capabilities and license terms from primary provider sources), **Vendor-reported claim** (benchmark scores and the MSA speedup claims), and **China AI Hub analysis** (the "why each difference matters" reasoning, introduced as analysis). No third-party benchmark evidence is currently recorded for these models.*
