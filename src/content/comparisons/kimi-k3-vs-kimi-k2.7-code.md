---
title: "Kimi K3 vs Kimi K2.7 Code: Moonshot's Flagship Against Its Coding Specialist"
author: "SinoAI Hub Research Team"
description: "Evidence-based comparison of Kimi K3 and Kimi K2.7 Code: API pricing, context window, output length, capabilities, licensing and benchmark records from the China AI Hub database."
entities:
  - kimi-k3
  - kimi-k2.7-code
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
  - source_name: "Moonshot AI — Kimi K3 (GitHub)"
    source_url: "https://github.com/MoonshotAI/Kimi-K3"
    source_type: official
  - source_name: "Kimi platform — Models documentation"
    source_url: "https://platform.kimi.ai/docs/models.md"
    source_type: official
  - source_name: "Kimi API — pricing (chat)"
    source_url: "https://platform.kimi.ai/docs/pricing/chat"
    source_type: official
---

All figures below are from the China AI Hub database, last verified 2026-09-20 (K2.7 Code last verified 2026-09-27). Where a field is not publicly disclosed, we say so rather than estimating.

## At a glance

| Dimension | Kimi K3 | Kimi K2.7 Code |
|---|---|---|
| Status (database) | active | active |
| Context window | 1,048,576 tokens | 262,144 tokens |
| Maximum output | 1,048,576 tokens | Not stated |
| Input price (per 1M) | $3.00 | $0.95 |
| Output price (per 1M) | $15.00 | $4.00 |
| Open weights | Yes (Kimi K3 License) | Not confirmed |
| API available | Yes | Yes |
| Reasoning | Yes | Yes |
| Coding | Yes | Yes |
| Vision / Video | Yes / Yes | Not listed |
| Tool calling | Yes | Not listed |
| Structured output | Yes | Not listed |
| Agent capability | Yes | Not listed |
| Benchmark records in DB | 6 | 0 |

## Pricing

Kimi K3 lists $3.00 input / $15.00 output per 1M tokens; Kimi K2.7 Code lists $0.95 input / $4.00 output — roughly a third of the input price and just over a quarter of the output price. A highspeed K2.7 Code variant (same model, higher throughput) is billed at 2x ($1.90 / $8.00). The K2.7 Code tier is the lower-cost coding-specific option in Moonshot's lineup.

## Context and output

Kimi K3 lists a 1,048,576-token context with a full-window 1,048,576-token maximum output. Kimi K2.7 Code lists a 262,144-token context and does not state a maximum-output ceiling in the fetched docs. For very long repository-scale work, K3's 1M-input/1M-output pairing is the distinguishing listed difference.

## Architecture and parameters

Kimi K3 publishes the fullest architecture card in the database: a 2.8T-total / 104B-activated MoE with 93 layers (1 dense), 896 experts (16 selected + 2 shared per token), a 69 KDA + 24 Gated MLA attention split, hidden dim 7168, SiTU-GLU, a 401M-parameter MoonViT-V2 vision encoder, and MXFP4 weights / MXFP8 activations. Moonshot does not disclose architecture or parameter counts for the K2.7 series — the K2.7 Code model is API-only with that information not publicly documented.

## Coding

Both list coding. Kimi K3 publishes vendor-reported DeepSWE (67.5) and Terminal-Bench 2.1 (88.3); Kimi K2.7 Code has no benchmark records in the database. The K2.7 Code model is positioned by Moonshot as a dedicated coding model (with always-on thinking and fixed sampling parameters), but its coding performance is not benchmark-documented in the database — the flagship K3 is the benchmark-backed coding model on record.

## Vision

Kimi K3 lists vision and video input; Kimi K2.7 Code lists neither. For multimodal coding (e.g., screen-recording-to-code workflows), only K3 lists the capability. Note K3's modality documentation is itself inconsistent across Moonshot's sources.

## Agent capabilities

Kimi K3 lists agent capability, tool calling and structured output; Kimi K2.7 Code lists none of these in its recorded set (its frontmatter records only reasoning and coding). For a documented tool/agent surface, the database records a clear difference.

## License and openness

Kimi K3 is open weight under the Kimi K3 License (MIT-style with revenue-triggered obligations above $20M / 100M MAU). Kimi K2.7 Code has no confirmed open-weight release — the K2.7 series is API-only, and Moonshot does not disclose architecture or parameter counts for it. For self-hosting, only K3 has a documented option.

## Deployment

Both are served through the Moonshot AI Platform API. Kimi K3 is self-hostable open weight; Kimi K2.7 Code is API-only with no confirmed open weights. K3's temperature is fixed at 1.0 and top_p at 0.95; K2.7 Code's thinking is always on with temperature/top_p/n/penalties fixed and must not be passed.

## Benchmarks

The database holds 6 benchmark records for Kimi K3 (GPQA Diamond, HLE-Full, DeepSWE, Terminal-Bench 2.1, MMMU-Pro, Video-MME) and 0 for Kimi K2.7 Code. All K3 rows are vendor-reported.

**Benchmark comparability is limited**: Kimi K2.7 Code has no benchmark records, so no head-to-head score comparison is possible.

## Why each difference matters

China AI Hub analysis indicates the following per-dimension implications, drawn from the listed facts above.

- **Pricing**: [Kimi K2.7 Code](/models/kimi-k27-code/) has an advantage at roughly a third of K3's input and just over a quarter of its output price — relevant for high-volume coding at lower cost.
- **Context**: [Kimi K3](/models/kimi-k3/) has an advantage in long-context work at 1M input with a 1M output ceiling, versus K2.7 Code's 262,144 input and unstated output.
- **Coding**: both list coding, but K3 is the benchmark-backed coding model on record (DeepSWE 67.5, Terminal-Bench 2.1 88.3) while K2.7 Code has no benchmark records.
- **Vision / media**: K3 is more relevant when vision/video input is required — it lists both where K2.7 Code lists neither.
- **Agent**: K3 is more relevant when a documented tool/agent/structured-output surface is core — it lists these where K2.7 Code lists none.
- **License**: K3 is open weight (Kimi K3 License); K2.7 Code has no confirmed open-weight release — only K3 offers a self-hosting option.
- **Deployment**: both API-available; K3 is self-hostable, K2.7 Code is API-only.
- **Benchmark**: K3 records 6 and K2.7 Code records 0; the evidence base is not comparable.

## Trade-off summary

- Price: Kimi K2.7 Code lists roughly a third of K3's input and a quarter of its output price.
- Context and output: Kimi K3 lists 1M-in/1M-out; K2.7 Code lists 262,144 in and no stated output ceiling.
- Capabilities: Kimi K3 lists vision, video, tool calling, structured output and agent capability; K2.7 Code lists none of these.
- Openness: K3 is open weight; K2.7 Code is API-only.

Choose by workload and budget: cost-sensitive coding favors K2.7 Code's price; long-context, multimodal, agent-heavy and self-hosting needs favor K3's listed capabilities. Verify current prices on the official pages before committing.

## Decision context

China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.

**For API developers.** Kimi K2.7 Code lists a lower price for a dedicated coding model, but has no benchmark records; Kimi K3 lists benchmarks plus a wider capability surface at a higher price. Both have fixed sampling parameters (K3: temperature 1.0/top_p 0.95; K2.7 Code: always-on thinking with fixed params). Latency is not publicly documented on this page.

**For self-hosting.** Kimi K3 is open weight (Kimi K3 License, revenue-triggered obligations); Kimi K2.7 Code has no confirmed open-weight release and is API-only. Hardware requirements and quantization are Not publicly documented on this page.

**For coding agents.** Both list coding. K3 is the benchmark-backed model (DeepSWE 67.5, Terminal-Bench 2.1 88.3) with a 1M output ceiling for long-horizon whole-repo work; K2.7 Code is the lower-cost coding specialist with no benchmark records.

**For enterprise.** Region, SLA, data-residency and compliance terms are not publicly documented — confirm with the vendor. Deployment differs: K3 offers self-hosting under a conditional license; K2.7 Code is API-only.

## What is uncertain

- Kimi K2.7 Code has no benchmark records and no documented maximum-output ceiling.
- Kimi K2.7 Code's architecture and parameter counts are not publicly disclosed.
- Kimi K3's input-modality boundary is inconsistent across Moonshot's official sources.

## Sources

- [Moonshot AI — Kimi K3 (GitHub)](https://github.com/MoonshotAI/Kimi-K3)
- [Kimi platform — Models documentation](https://platform.kimi.ai/docs/models.md)
- [Kimi API — pricing (chat)](https://platform.kimi.ai/docs/pricing/chat)

*Labels used above: **Official fact** (prices, context windows, capabilities and license terms from primary provider sources), **Vendor-reported claim** (benchmark scores), and **China AI Hub analysis** (the "why each difference matters" reasoning, introduced as analysis). No third-party benchmark evidence is currently recorded for these models.*
