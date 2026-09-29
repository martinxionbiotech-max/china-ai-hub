---
agent_id: fastgpt
agent_name: FastGPT
company: labring
description: "FastGPT is an open-source knowledge-based platform built on LLMs, by Labring (环界云计算). It offers out-of-the-box capabilities for data processing, RAG retrieval and visual AI workflow orchestration — including Agent Skill orchestration, bidirectional MCP, plugin workflows with RPA nodes, and hybrid retrieval with reranking. Deployable via Docker Compose, the managed cloud (fastgpt.io), or Sealos Cloud; a commercial edition adds deeper support."
agent_type: platform
underlying_models: []
framework: "Visual workflow orchestration with Agent Skill editing, dialog and plugin workflows (with RPA nodes), bidirectional MCP, and a knowledge-base layer with hybrid retrieval and rerank."
tool_calling: true
mcp: true
memory: true
planning: true
api: true
pricing: "Open source (free self-hosted); managed cloud (fastgpt.io) and a commercial edition are paid; commercial pricing via doc.fastgpt.io/guide/version/commercial."
deployment: both
open_source: true
license: "FastGPT Open Source License (commercial use as a backend service permitted; SaaS service and commercial redistribution require authorization)"
github: https://github.com/labring/FastGPT
documentation: https://doc.fastgpt.io/
use_cases:
  - Knowledge-base Q&A and RAG applications
  - AI customer service and enterprise knowledge management
  - Visual agent and plugin workflow orchestration
  - Self-hosted knowledge assistants on Sealos Cloud
  - Data processing and document ingestion pipelines
limitations:
  - License is not OSI-approved — commercial use is permitted only as a backend service, not as a SaaS offering, without authorization
  - Requires self-hosting (Docker Compose) or the paid cloud for production use
  - Model-agnostic means the operator supplies and pays for their own model via AI Proxy
  - Commercial edition features and pricing are documented separately from the open-source repo
last_verified: "2026-09-29"
sources:
  - source_name: FastGPT GitHub repository
    source_url: https://github.com/labring/FastGPT
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: FastGPT documentation
    source_url: https://doc.fastgpt.io/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: FastGPT cloud service
    source_url: https://fastgpt.io/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: FastGPT Open Source License
    source_url: https://github.com/labring/FastGPT/blob/main/LICENSE
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** FastGPT is an open-source, knowledge-base-first platform for building LLM applications, made by Labring (环界云计算) — the company behind the Sealos cloud OS. **Why it matters.** It is China's most prominent open-source knowledge-base agent platform, the self-hosted answer to RAG-heavy enterprise Q&A, with a visual workflow orchestrator and bidirectional MCP. **Key characteristics.** Out-of-the-box data processing and RAG retrieval, Agent Skill and plugin workflows (with RPA nodes), hybrid retrieval with reranking, and three deployment modes: Docker Compose, managed cloud (fastgpt.io) or Sealos Cloud. **What a professional should know.** The license is not OSI-approved — commercial use is permitted as a backend service but a SaaS offering or commercial redistribution requires authorization — and production use means self-hosting or the paid cloud.

FastGPT describes itself as "a knowledge-based platform built on the LLMs," offering data processing, RAG retrieval and visual AI workflow orchestration. Its capability list spans five areas: application orchestration (Agent Skill editing, dialog and plugin workflows with RPA nodes, bidirectional MCP), application debugging (knowledge-base search testing, full call-chain logs, evaluation), knowledge-base management (multi-library reuse, chunk editing, hybrid retrieval and rerank, TXT/MD/HTML/PDF/Docx ingestion), plugins (hot-reloadable system tools, RAG modules and agent loops) and operations (share windows, iframe embedding, conversation logs).

Deployment follows the open-source pattern: a one-line install script plus `docker compose up -d` for self-hosting, a managed cloud at fastgpt.io, or one-click deployment on Sealos Cloud. Model access is decoupled through Labring's AI Proxy — a model aggregation and load-balancing service — which is how the platform stays model-neutral.

See the [Labring](/companies/labring/) profile.

## Why it matters

FastGPT matters as the knowledge-base counterpoint to the workflow-first open platforms. Where [Dify](/agents/dify/) leads with general application workflows, FastGPT leads with document ingestion, chunk management, hybrid retrieval and rerank — the RAG plumbing that enterprise knowledge assistants are built on. China AI Hub analysis indicates its structural role is self-hosted knowledge infrastructure: it competes with the closed [Baidu AppBuilder](/agents/baidu-appbuilder/) and [Coze](/agents/coze/) knowledge features, but on a bring-your-own-model, self-hosted basis, which is exactly the segment of Chinese enterprises that cannot send internal documents to a managed cloud. Its non-OSI license, however, means the "open source" label comes with a commercial boundary that the pure-MIT frameworks ([MetaGPT](/agents/metagpt/)) do not have. China AI Hub analysis: that boundary locates FastGPT between two poles — more open than a closed platform (you can self-host the core) but less open than an MIT framework (you cannot resell it as SaaS). Its real moat is the knowledge-base depth — chunk management, hybrid retrieval and rerank — which is the RAG plumbing that generic workflow platforms treat as a secondary feature and FastGPT treats as the primary one. This is why it clusters with enterprise document-Q&A use cases rather than general agent-building. For an enterprise whose primary need is answering questions over an internal document corpus, FastGPT's self-hosted retrieval stack is the closest direct match among the platforms tracked here.

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Model-agnostic (via AI Proxy aggregation) | Official |
| Target users | Enterprises, knowledge-base builders, self-hosters | Official |
| Platform | Docker self-hosted; cloud (fastgpt.io); Sealos Cloud | Official |
| OS | Cross-platform (Docker); Linux server | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Not a primary focus | Official |
| Autonomous task execution | Yes (agent-loop, workflow orchestration) | Vendor-reported |
| MCP | Yes (bidirectional MCP) | Official |
| Tool calling | Yes (plugin workflow, RPA nodes) | Official |
| Memory | Yes (knowledge base, hybrid retrieval) | Official |
| Workflow | Visual workflow + Agent Skill + plugin workflow | Official |
| API | Yes (OpenAPI) | Official |
| Pricing | Open source (free); paid cloud and commercial edition | Vendor-reported |
| Region | China (with global self-hosting) | Official |
| Open-source | Yes — FastGPT Open Source License (non-OSI) | Official |
| Deployment | Both (self-hosted + cloud) | Official |
| Limitations | Non-OSI license; self-hosting or paid cloud for production | Official |
| Source | [GitHub](https://github.com/labring/FastGPT) · [docs](https://doc.fastgpt.io/) · [fastgpt.io](https://fastgpt.io/) | Official |
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The commercial edition's feature set and pricing are documented separately from the open-source repository.
- The exact boundary of the SaaS restriction is defined by the FastGPT Open Source License, not a standard OSI license.
- The company's headquarters and funding are not published on official channels.
- No independent third-party evaluation of FastGPT-built applications is recorded in this database.
- The database does not independently test retrieval quality across the supported file formats and rerank models.

*Labels used above: **Official fact** (from the FastGPT GitHub repository, LICENSE and documentation), **Vendor-reported claim** (feature and deployment statements by Labring), and **China AI Hub analysis** (our synthesis, always introduced as such).*
