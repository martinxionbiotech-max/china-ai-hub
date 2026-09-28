---
image: "/images/ai/models-minimax-m3.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: minimax-m3
model_name: MiniMax-M3
provider: minimax
model_family: MiniMax M-series
release_date: "2026-06-01"
status: active
architecture: "Mixture-of-Experts: ~428B total / ~23B activated; MiniMax Sparse Attention (MSA) with claimed 9x prefill and 15x decode speedup vs M2 at 1M context"
parameter_information:
  total_parameters: "~428B"
  active_parameters: "~23B"
context_window: 1048576
maximum_output: 131072
capabilities:
  reasoning: true
  coding: true
  vision: true
  video: true
  tool_calling: true
  agent_capability: true
open_weight: true
license: "MiniMax Community License (custom): free for non-commercial use; commercial use requires prominent attribution 'Built with MiniMax M3' plus written authorization from MiniMax if yearly revenue exceeds US$20M (otherwise a one-time notice to api@minimax.io)"
self_hosting: true
api_available: true
pricing:
  input_price_per_1m: 0.3
  output_price_per_1m: 1.2
  currency: USD
  pricing_ref: minimax
official_api: true
cloud_providers:
  - MiniMax Platform
regions:
  - china
  - international
benchmark_results:
  - benchmark: BrowseComp
    score: 83.5
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/models/text/m3
  - benchmark: PostTrainBench
    score: 37.1
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/models/text/m3
  - benchmark: SWE-bench Pro
    score: 59.0
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/blog/minimax-m3
  - benchmark: Terminal-Bench 2.1
    score: 66.0
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/blog/minimax-m3
  - benchmark: MCP Atlas
    score: 74.2
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/blog/minimax-m3
known_limitations:
  - "Maximum output of 131,072 tokens derived from official card evaluation config (128K max output tokens); the standalone API max-output ceiling is not separately published"
  - "Max output tokens not publicly disclosed in official docs"
  - "1M context with at least 512K guaranteed usable; pricing splits at the 512K input boundary"
  - "Thinking is disabled by default (thinking=adaptive enables it)"
  - "Benchmarks vendor-reported; not independently verified"
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official M3 model page
    source_url: https://www.minimax.cn/models/text/m3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax M3 official blog post
    source_url: https://www.minimax.cn/blog/minimax-m3
    source_type: official
    published_date: "2026-06-01"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — MiniMax-M3
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** MiniMax-M3 (2026-06-01) is MiniMax's flagship model: a ~428B-total / ~23B-activated MoE with MiniMax Sparse Attention, a 1M-token context window, and native multimodal input. **Why it matters.** It targets agentic reasoning, tool use, coding and long-context work at one of the lowest flagship prices in the database ($0.30 input). **Key characteristics.** Text, image (up to 10MB) and video (up to 50MB direct, 512MB via Files API) input with text output; thinking disabled by default with a `thinking=adaptive` toggle. **What a professional should know.** Maximum output tokens are not publicly disclosed — the 131,072 figure is derived from the official card's evaluation config, not a published API ceiling — and pricing doubles above the 512K input boundary.

## Architecture and parameters

MiniMax-M3 is a ~428B-total / ~23B-activated MoE (~5.4% activation) built around MiniMax Sparse Attention (MSA), which MiniMax claims delivers 9x prefill and 15x decode speedup vs M2 at 1M context. That speedup is a vendor claim, not an independent measurement, but the architectural direction — linear/sparse attention to make long context affordable — matches the market-wide pattern (Qwen's DeltaNet, Kimi's KDA). See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

The 1M-token window comes with a practical qualifier: at least 512K is guaranteed usable, and pricing splits at the 512K boundary (double above). This is honest tiering — the full 1M is advertised, but the economics and the guarantee both live at 512K. Treat M3 as a 512K-usable, 1M-capable model. See the [context-window research](/research/chinese-ai-context-windows/).

## Pricing implications

International pay-as-you-go standard tier is $0.30 input / $1.20 output per 1M tokens up to 512K input (double above 512K), cache reads $0.06, and a permanent 50% off list — the priority tier costs 1.5x. At $0.30, M3 is the cheapest flagship input price in the database, which is its clearest market position. The 4x input-to-output ratio is standard. See the [pricing-changed research](/research/chinese-ai-model-pricing-changed/).

## API, coding, and agent implications

Vendor-reported SWE-bench Pro (59.0), Terminal-Bench 2.1 (66.0), MCP Atlas (74.2), BrowseComp (83.5) and PostTrainBench (37.1) describe a capable agentic/coding profile with particular strength in MCP-based tool use and browsing. Agent capability is documented, and tool calling plus multimodal input make it a strong agent substrate. Thinking is off by default — unlike GLM-5.3's always-on — so you opt into reasoning per request via `thinking=adaptive`. See the [Doubao comparison](/comparisons/doubao-seed-2-1-pro-vs-minimax-m3/) and [Kimi comparison](/comparisons/kimi-k3-vs-minimax-m3/).

## Open weights and license

Open weight (MXFP8, ~171k downloads) on Hugging Face/GitHub under the MiniMax Community License — a custom license that is free for non-commercial use but requires prominent "Built with MiniMax M3" attribution for commercial use, and written authorization above $20M yearly revenue. This is conditional-open, not permissive. See [licensing explained](/research/chinese-ai-model-licensing-explained/).

## Benchmark interpretation

All five rows are vendor-reported. BrowseComp 83.5 and MCP Atlas 74.2 are agentic/browsing/tool-use signals; SWE-bench Pro 59.0 and Terminal-Bench 66.0 are coding; PostTrainBench 37.1 is a post-training quality metric. These describe a mid-to-strong coding profile at a low price, not a frontier-reasoning leader.

## What the benchmarks do not prove

The scores are vendor-reported and not independently verified; the MSA speedup claims (9x/15x) are unmeasured by any third party; and the maximum-output ceiling is unpublished. These gaps matter when M3's headline advantages — speed and price — are exactly what you'd want independently confirmed. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** cost-sensitive agentic work, MCP/tool-use applications, multimodal input (image/video) analysis, browsing agents, and long-context tasks within the 512K guaranteed band. **Less suited:** frontier-level deep reasoning, workloads requiring a documented output ceiling, and commercial self-hosting above the license thresholds.

## China AI Hub analysis

China AI Hub analysis indicates M3's competitive edge is price-per-capability in the agentic tier: it delivers multimodal input, MCP tool use and a 1M window at the lowest flagship input price tracked. The trade-offs are verification depth (vendor-only benchmarks, unpublished max output, unmeasured speed claims) and the 512K pricing split, which means the advertised 1M context costs 2x in the upper band. For budget-constrained agent deployments it is a strong candidate; for workloads where a hard, documented output ceiling or independently verified performance is required, the gaps are real.

## Market position and outlook

China AI Hub analysis indicates M3's edge is price-per-capability in the agentic tier: it delivers multimodal input (text plus JPEG/PNG/GIF/WEBP images up to 10MB and video up to 50MB direct or 512MB via the Files API), MCP tool use and a 1M window at the lowest flagship input price tracked ($0.30). The MCP Atlas score (74.2) is worth singling out because it measures the model's ability to drive MCP-connected tools, which is exactly the integration pattern agent builders use. The trade-offs are verification depth — vendor-only benchmarks, an unpublished maximum-output ceiling, and unmeasured 9x/15x speed claims — plus the 512K pricing split that doubles cost in the upper context band. For budget-constrained agent and multimodal deployments it is a strong candidate; for workloads needing a hard documented output ceiling or independent performance evidence, those gaps remain. See the [pricing-changed](/research/chinese-ai-model-pricing-changed/) and [multimodal capabilities](/research/chinese-ai-multimodal-capabilities/) research.

*Labels used above: **Official fact** (from primary sources), **Vendor-reported claim** (benchmark scores and MSA speedup claims published by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party benchmark evidence is currently recorded for this model.*
