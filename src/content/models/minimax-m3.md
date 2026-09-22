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

MiniMax-M3 (2026-06-01) is MiniMax's flagship model: a ~428B-total / ~23B-activated MoE with MiniMax
Sparse Attention, a 1M-token context window (at least 512K guaranteed usable), and native multimodal
input - text, image (JPEG/PNG/GIF/WEBP up to 10MB) and video (up to 50MB direct, 512MB via Files API) -
with text output. It targets agentic reasoning, tool use, coding and long-context work.

Open weights (MXFP8, ~171k downloads) are on Hugging Face/GitHub under the MiniMax Community License.
International pay-as-you-go pricing (standard tier, permanent 50% off vs list): $0.30 input / $1.20
output per 1M tokens up to 512K input (double above 512K), cache reads at $0.06; priority tier costs
1.5x (as of 2026-09-20). Max output tokens are not publicly disclosed.
