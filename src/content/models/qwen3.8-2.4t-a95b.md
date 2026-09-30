---
image: "/images/ai/models-qwen3.8-2.4t-a95b.webp"
image_credit: "AI-generated illustration (Seedream)"
model_id: qwen3.8-2.4t-a95b
model_name: Qwen3.8-2.4T-A95B
provider: alibaba-cloud
model_family: Qwen3.8
release_date: "2026-08-12"
status: active
architecture: "2.4T-parameter MoE, 95B activated, 512 experts (10 routed + 1 shared per token), 92 layers, Gated DeltaNet + Gated Attention hybrid"
parameter_information:
  total_parameters: "2.4T"
  active_parameters: "95B"
context_window: 262144
capabilities:
  reasoning: true
  vision: false
open_weight: true
license: "Qwen3.8-Max License (custom MIT-style: unrestricted use/copy/modify/sell, but products with >100M MAU or >US$20M/month revenue must display the model name; Model-as-a-Service or AI Work Assistant businesses with >US$50M/12-month revenue need a separate license from Qwen)"
self_hosting: true
api_available: false
official_api: false
known_limitations:
  - "Text-only input; thinking cannot be disabled; reasoning_effort xhigh/medium/low"
  - "Native context 262,144 tokens, extensible to 1,010,000"
  - "Not the same product as the qwen3.8-max API model (which adds vision/video input, non-thinking mode and 1M default context)"
last_verified: "2026-09-20"
sources:
  - source_name: Hugging Face model card — Qwen3.8-2.4T-A95B
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen3.8 repository README
    source_url: https://github.com/QwenLM/Qwen3.8
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Qwen3.8-2.4T-A95B license file
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Qwen3.8-2.4T-A95B is Alibaba's first Qwen-Max-class open-weight release (2026-08-12): a 2.4T-parameter MoE with 95B activated parameters and a Gated DeltaNet + Gated Attention hybrid. **Why it matters.** It is the open-weight form of Qwen3.8-Max — one of the largest open-weight models in the collection — and the first time Alibaba has released Max-tier weights. **Key characteristics.** 512 experts (10 routed + 1 shared per token), 92 layers, text-only input, thinking that cannot be disabled, and a native 262,144-token context extensible to 1,010,000. **What a professional should know.** It is not the same product as the qwen3.8-max API model — the open weights are text-only and thinking-only, with no API endpoint — and the license is a custom MIT-style agreement with commercial attribution and revenue thresholds.

## Architecture and parameters

The 2.4T-total / 95B-activated (~3.9%) MoE routes each token to 10 of 512 experts plus one shared expert across 92 layers. The Gated DeltaNet + Gated Attention hybrid is Alibaba's long-context answer: linear-attention (DeltaNet) layers replace part of the quadratic attention stack so context stays economical, interleaved with full gated attention. China AI Hub analysis indicates this is the same hybrid the database records on the closed Qwen3.8-Max — the open release exposes the architecture that the API product keeps hidden. See [Mixture-of-Experts](/technology/mixture-of-experts/) and the [MoE architectures research](/research/chinese-ai-moe-architectures/).

## What the context window actually means

Native context is 262,144 tokens, extensible to 1,010,000. China AI Hub analysis indicates the native-vs-extensible split matters in practice: the model ships at 256K and only reaches 1M through extension, which is a different engineering proposition than a native 1M window and should be verified against the intended workload. See the [context-window research](/research/chinese-ai-context-windows/) and the [long-context hub](/models/long-context/).

## Pricing implications

There is no API — the model is open weights only, with no hosted endpoint and no per-token pricing. China AI Hub analysis indicates the cost model is therefore entirely self-hosting: hardware, serving and inference costs replace token pricing, which is why the 2.4T total footprint (a multi-GPU deployment) is the operative economic fact, not a token rate. See [self-hosting guide](/guides/self-hosting-chinese-open-weights/).

## API, coding, and agent implications

Text-only and thinking-only, with `reasoning_effort` at xhigh/medium/low. China AI Hub analysis indicates the absence of an API endpoint and of non-thinking mode means this model is a research-and-self-host artifact, not a drop-in agent substrate — teams wanting the Qwen3.8-Max capability with an API should use the [closed flagship](/models/qwen38-max/) instead. See the [Qwen3.8-Max vs A95B comparison](/comparisons/qwen38-max-vs-qwen38-24t-a95b/).

## Open weights and license

Open weight under the Qwen3.8-Max License: unrestricted use/copy/modify/sell, but products over 100M MAU or $20M/month revenue must display the model name, and Model-as-a-Service or AI Work Assistant businesses over $50M/12-month revenue need a separate license. China AI Hub analysis indicates this is a conditional-open license, not plain MIT — permissive for most self-hosters but with attribution and revenue-threshold obligations above the cutoffs. See [licensing explained](/research/chinese-ai-model-licensing-explained/) and the [open-weights hub](/models/open-weights/).

## Benchmark interpretation

No benchmark scores are recorded for Qwen3.8-2.4T-A95B in the database — its open release is positioned on architecture and scale rather than published benchmark results.

## What the benchmarks do not prove

With no recorded benchmarks, there is nothing with which to rank the open A95B weights independently, and its Max-class positioning rests on the Qwen3.8-Max model card rather than A95B-specific results. See [how to read vendor-reported benchmarks](/guides/how-to-read-vendor-reported-benchmarks/).

## Suitable and less suitable workloads

**Well-suited:** open-weight research and self-hosting, text-only reasoning at scale, and teams that need Max-class weights to fine-tune or deploy on their own hardware. **Less suited:** vision/video input (text-only), non-thinking/latency-sensitive use (thinking cannot be disabled), and anyone wanting a hosted API.

## Where this model fits

| Workload | Relevance |
|---|---|
| Long-context analysis | Moderate |
| Coding | Moderate |
| Structured API workflows | No evidence |
| Agent orchestration | No evidence |
| Local self-hosted deployment | High |
| GUI automation | No evidence |
| Video generation | No evidence |
| Enterprise cloud | Moderate |

Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.

## China AI Hub analysis

China AI Hub analysis indicates Qwen3.8-2.4T-A95B is Alibaba's strategic concession to the open-weight market: releasing Max-class weights for the first time lets Alibaba answer DeepSeek and Zhipu on open availability while deliberately withholding the multimodal, non-thinking API experience behind the closed Qwen3.8-Max. The text-only, thinking-only, no-API profile is the price of that openness, and it means the open weights are a different product, not a substitute for the flagship. Its Gated DeltaNet hybrid and 2.4T scale make it a significant research artifact, but the native 256K context (extensible to 1M) and absent benchmark record mean adopters inherit verification work. See the [state of China's AI models](/research/state-of-chinas-ai-models-2026/) research and the [MoE hub](/models/moe/).

## What is uncertain

- No benchmark scores are recorded for the open A95B weights.
- The model is text-only and thinking-only, so multimodal and non-thinking capabilities are absent rather than simply undocumented.
- The extensible 1M context is a different engineering proposition than a native 1M window.

## Sources

- [Hugging Face model card — Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)
- [Qwen3.8 repository README](https://github.com/QwenLM/Qwen3.8)
- [Qwen3.8-2.4T-A95B license file](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE)

*Labels used above: **Official fact** (architecture, parameters and license from Qwen's model card, README and license file) and **China AI Hub analysis** (our synthesis, always introduced as such). No benchmark evidence is currently recorded for this model.*
