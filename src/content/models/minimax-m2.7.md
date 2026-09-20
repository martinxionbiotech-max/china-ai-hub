---
model_id: minimax-m2.7
model_name: MiniMax-M2.7
provider: minimax
model_family: MiniMax M2.7
release_date: "2026-03-18"
status: active
context_window: 204800
capabilities:
  reasoning: true
  tool_calling: true
  vision: false
open_weight: true
license: "Custom NON-COMMERCIAL license (MIT-style terms for non-commercial use only; any commercial use requires prior written authorization from MiniMax at api@minimax.io; attribution 'Built with MiniMax M2.7' required)"
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
  - benchmark: GDPval-AA ELO
    score: 1495
    metric: ELO
    date: "2026-03-18"
    source_type: vendor_reported
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
  - benchmark: MM Claw end-to-end benchmark
    score: 62.7
    metric: accuracy
    date: "2026-03-18"
    source_type: vendor_reported
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
known_limitations:
  - "Text-only input; interleaved thinking always on (cannot be disabled via API)"
  - "Parameter count and max output tokens not publicly disclosed"
  - "Must echo full assistant content (thinking blocks) back in multi-turn history"
  - "Benchmarks vendor-reported; not independently verified"
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax API platform — model overview (CN)
    source_url: https://platform.minimaxi.com/docs/guides/models-intro
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official release notes
    source_url: https://platform.minimaxi.com/docs/release-notes/models.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Hugging Face model card — MiniMax-M2.7
    source_url: https://huggingface.co/MiniMaxAI/MiniMax-M2.7
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

MiniMax-M2.7 (2026-03-18) is MiniMax's "self-evolving" model: the first model MiniMax says deeply
participates in its own evolution, with recursive self-improvement, agent teams, complex skills and tool
search. It has a 204,800-token context, text-only input, and interleaved thinking that is always on.
Output speed is ~60 tokens/s; the highspeed variant serves ~100 TPS at 2x price.

Open weights (~1.46M downloads) are on Hugging Face under a custom non-commercial license. International
pricing: $0.30 input / $1.20 output per 1M tokens, cache reads $0.06, cache writes $0.375 (as of
2026-09-20). Parameter count and max output are not publicly disclosed.
