---
slug: reasoning-models
title: Reasoning Models
definition: "A reasoning model is a language model trained to produce explicit intermediate reasoning — typically chain-of-thought steps — before giving a final answer, usually via reinforcement learning on verifiable tasks rather than supervised imitation alone."
related_models:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - qwen3.8-max
  - glm-5.3
  - kimi-k3
  - minimax-m3
related_companies:
  - deepseek
  - alibaba-cloud
  - zhipu-ai
  - moonshot-ai
  - minimax
related_technologies:
  - mixture-of-experts
  - long-context
  - inference
related_guides: [how-to-read-vendor-reported-benchmarks]
last_verified: "2026-09-22"
sources:
  - source_name: "OpenAI — Introducing OpenAI o1"
    source_url: "https://openai.com/index/introducing-openai-o1-preview/"
    source_type: official
  - source_name: "DeepSeek-R1 (GitHub)"
    source_url: "https://github.com/deepseek-ai/DeepSeek-R1"
    source_type: official
  - source_name: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    source_url: "https://arxiv.org/abs/2501.12948"
    source_type: academic
---

## Technical background

Reasoning models emerged as a distinct category around 2024-2025. The core shift: instead of scaling pretraining data alone, labs added a training stage that optimizes the model for producing and verifying its own reasoning. The landmark open publication was DeepSeek-R1 (January 2025), which showed that reinforcement learning alone could induce reasoning behavior, without large supervised reasoning datasets.

## How it works

The dominant recipe has two stages. First, reinforcement learning with a rule- or model-based reward on verifiable tasks (math, code, logic), which teaches the model to allocate more compute to "thinking." Second, distillation or supervised fine-tuning transfers that behavior to smaller or production models. At inference time, the model emits a chain of thought — sometimes visible, sometimes hidden — before the final answer. Longer reasoning budgets generally improve hard-task accuracy at the cost of latency and tokens.

## Why it matters

Reasoning training is the main driver of post-2024 gains on hard benchmarks: competition math, competitive programming, and agentic tasks that require planning. It also changed cost curves — reasoning models bill for many more output tokens per request, so price-per-token is no longer a proxy for price-per-task.

## Chinese adoption

China adopted reasoning training at scale and, with DeepSeek-R1, was the first to publish the full recipe openly. In the China AI Hub database (last verified 2026-09-22), nearly every current flagship lists reasoning capability: DeepSeek-V4-Pro and V4.1-Flash, Qwen3.8-Max, GLM-5.3, Kimi K3, MiniMax M3, and the Doubao Seed 2.1 series all report reasoning support.

## Major Chinese companies and models

- **DeepSeek** — DeepSeek-R1 (MIT, the reference open reasoning release); current flagships DeepSeek-V4-Pro and V4.1-Flash list reasoning capability and 1M-token context.
- **Alibaba Cloud (Qwen)** — Qwen3.8-Max lists reasoning, coding and vision; the Qwen3 family includes open reasoning-tuned variants.
- **Zhipu AI** — GLM-5.3 and GLM-5.3-Flash (Apache-2.0, open weight) list reasoning capability.
- **Moonshot AI** — Kimi K3 lists reasoning, coding, vision and video.
- **MiniMax** — MiniMax M3 lists reasoning and coding at the low end of flagship pricing.

## Practical applications

Math and formal verification, competitive programming, debugging, multi-step agent planning, and research workflows where correctness outweighs latency. Reasoning models are also used as judges or verifiers inside agent pipelines.

## Limitations

High token consumption and latency; reasoning is not guaranteed to be faithful to the hidden computation; capability varies sharply by domain; and "reasoning" labels are vendor claims unless independently benchmarked. Our database labels benchmark scores by source type (vendor-reported vs independent) precisely because of this.

## Deployment considerations

Serving reasoning models multiplies output-token costs, so measure price-per-completed-task, not price-per-token. Off-peak discounts (e.g., DeepSeek's listed off-peak pricing) can matter for batch workloads. Hidden chains of thought are also a compliance consideration where auditability is required.

## Future development

Reasoning budgets are becoming controllable (low/medium/high modes), reasoning is merging with tool use and computer use inside agents, and cost per reasoning token keeps falling as efficiency techniques mature.
