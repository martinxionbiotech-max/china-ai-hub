---
slug: rag
title: RAG
definition: "Retrieval-Augmented Generation (RAG) is a pattern where a language model's answers are grounded in documents fetched by a retrieval system at query time, combining the fluency of generation with evidence from an external corpus."
related_models:
  - kimi-k3
  - qwen3.8-max
  - deepseek-v4-1-flash
related_companies:
  - moonshot-ai
  - alibaba-cloud
  - deepseek
related_technologies:
  - long-context
  - function-calling
related_guides: []
last_verified: "2026-09-22"
sources:
  - source_name: "Lewis et al. — Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    source_url: "https://arxiv.org/abs/2005.11401"
    source_type: academic
  - source_name: "Meta AI — RAG overview"
    source_url: "https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/"
    source_type: official
---

## Technical background

RAG was formalized by Lewis et al. (Facebook AI Research, 2020) as a way to give parametric models access to non-parametric knowledge. It became the default enterprise pattern for grounding LLM answers in private or current documents, and remains the mainstream answer to hallucination in production systems.

## How it works

A pipeline chunks a corpus, embeds the chunks, and indexes them in a vector store. At query time the query is embedded, similar chunks are retrieved (often with a reranker and sometimes hybrid lexical+vector search), and the top results are placed into the prompt with instructions to answer only from them. Citations can be generated when chunks carry IDs.

## Why it matters

RAG grounds answers in evidence that can be checked, updated and permissioned — properties a pretrained model alone cannot offer. It is the standard architecture for enterprise Q&A, customer support, and any system where correctness and source-ability matter more than pure fluency.

## Chinese adoption

RAG is widely deployed across Chinese enterprise AI offerings. In the China AI Hub ecosystem, the pattern is enabled by long-context APIs: models such as Kimi K3, Qwen3.8-Max and DeepSeek-V4.1-Flash list 1M-token context windows (last verified 2026-09-22), which lets pipelines load far more retrieved evidence per request than earlier generations. Embedding and reranking endpoints are offered by the same API providers.

## Major Chinese companies and models

- **Moonshot AI** — Kimi K3 (1M context) for evidence-heavy prompts.
- **Alibaba Cloud** — Qwen3.8-Max (1M context) with Model Studio tooling.
- **DeepSeek** — V4.1-Flash lists 1M context and function calling suitable for retrieval pipelines.

## Practical applications

Enterprise document Q&A with citations, customer-support bots over policy corpora, compliance and legal search, codebase question answering, and audit trails where every claim links to a source chunk.

## Limitations

Retrieval quality caps answer quality: chunking strategy, embedding model and reranking matter more than the generator. Multi-hop questions degrade without iterative retrieval. Long retrieved contexts increase latency and token cost. Grounding reduces but does not eliminate hallucination.

## Deployment considerations

Measure end-to-end retrieval accuracy on your own corpus, not public benchmarks; keep a reranking stage; store chunk provenance for citations; and consider agentic retrieval (multiple search steps) for multi-hop queries.

## Future development

RAG is converging with long-context models (fewer, bigger evidence blocks), agentic search loops, and memory systems that persist retrieved knowledge across sessions.
