---
image: "/images/ai/technologies-long-context.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: long-context
title: Long Context
definition: "Long context refers to a model's ability to accept very large inputs — hundreds of thousands to millions of tokens — in a single request, allowing whole codebases, document sets or conversation histories to be processed at once."
related_models:
  - kimi-k3
  - deepseek-v4-pro
  - glm-5.3
  - qwen3.8-max
  - minimax-m3
  - doubao-seed-2-1-pro
related_companies:
  - moonshot-ai
  - deepseek
  - zhipu-ai
  - alibaba-cloud
  - minimax
  - bytedance
related_technologies:
  - rag
  - inference
related_guides: [how-to-read-vendor-reported-benchmarks]
last_verified: "2026-09-22"
sources:
  - source_name: "Chen et al. — LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models"
    source_url: "https://arxiv.org/abs/2309.12307"
    source_type: academic
  - source_name: "Ding et al. — LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens"
    source_url: "https://arxiv.org/abs/2402.13753"
    source_type: academic
  - source_name: "Google — Gemini 1.5 announcement"
    source_url: "https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/"
    source_type: official
---

## Technical background

Context windows grew from 2K-8K tokens (2022-2023) to 128K-1M+ by 2024-2025. The enabling techniques were positional-encoding extensions (RoPE scaling), sparse or linear attention variants, and long-context fine-tuning methods such as LongLoRA. Frontier models now routinely advertise 1M-token windows.

## How it works

The context is the model's entire working memory: input text plus any retrieved documents plus the conversation so far. Positional encodings must generalize beyond training lengths, and attention must stay affordable — hence sparse attention (e.g., MiniMax's MSA) or hybrid designs. Long context also consumes KV-cache memory, which grows linearly with tokens.

## Why it matters

Long context changes system design: with a 1M-token window, many retrieval-augmented (RAG) pipelines can simply load the corpus into the prompt instead of chunking and ranking it. It also enables whole-repository code understanding and multi-document analysis in one pass.

## Chinese adoption

Chinese labs have been aggressive on context length. Per the China AI Hub database (last verified 2026-09-22), eleven current models list a 1,048,576-token context window: DeepSeek-V4-Pro and V4.1-Flash, Qwen3.8-Max and Qwen3.8-Flash, GLM-5.2/5.3/5.3-Flash, Kimi K3, MiniMax M3, and Doubao Seed 2.1 Pro/Evolving. Kimi K3 additionally lists a 1M-token maximum output.

## Major Chinese companies and models

- **Moonshot AI** — Kimi K3: 1M input and 1M output listed.
- **DeepSeek** — V4-Pro and V4.1-Flash: 1M input, 393K output.
- **Zhipu AI / Alibaba Cloud / MiniMax / ByteDance** — GLM-5.x, Qwen3.8, MiniMax M3 and Doubao Seed 2.1 Pro all list 1M input.

## Practical applications

Whole-codebase analysis and refactoring, long-document summarization and compliance review, multi-file log or legal discovery, and simplification of RAG pipelines (context stuffing as an alternative to retrieval).

## Limitations

Effective use of long context degrades with distance (middle-of-context loss); attention over 1M tokens is expensive and slow; KV-cache memory can dominate serving cost; and advertised lengths are not always usable lengths — test on real retrieval tasks.

## Deployment considerations

Budget for KV-cache memory, enable prefix caching for shared prompts, and benchmark attention quality at the lengths you actually use rather than trusting the advertised maximum.

## Future development

Long context is converging with agent memory architectures — persistent, searchable context stores rather than one giant prompt — and with hybrid retrieval-plus-context systems.
