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
last_verified: "2026-09-30"
sources:
  - source_name: FastGPT GitHub repository
    source_url: https://github.com/labring/FastGPT
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: FastGPT documentation
    source_url: https://doc.fastgpt.io/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: FastGPT cloud service
    source_url: https://fastgpt.io/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: FastGPT Open Source License
    source_url: https://github.com/labring/FastGPT/blob/main/LICENSE
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: FastGPT home (labring.github.io)
    source_url: https://labring.github.io/fastgpt-home/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** FastGPT is an open-source, knowledge-base-first platform by Labring (环界云计算) for building LLM applications on top of RAG retrieval and visual workflow orchestration — China's most prominent self-hosted answer to enterprise knowledge Q&A, with a commercial edition and a managed cloud.

**Key facts.**

- Knowledge-base-first: data processing, RAG retrieval, chunk editing, hybrid retrieval with rerank, and TXT/MD/HTML/PDF/Docx ingestion.
- Visual workflow orchestration with Agent Skill editing, dialog and plugin workflows (including RPA nodes), and bidirectional MCP.
- Model-agnostic through Labring's AI Proxy — a model aggregation and load-balancing service.
- Three deployment modes: Docker Compose self-hosting, the managed cloud (fastgpt.io), or one-click deployment on Sealos Cloud.
- Open source under the "FastGPT Open Source License" — commercial use as a backend service is permitted, but a SaaS service or commercial redistribution requires authorization.
- A commercial edition adds deeper support; its pricing is documented separately from the repo.

**What this means.** FastGPT is the self-hosted knowledge-infrastructure play: it competes with the closed platforms' knowledge features ([Baidu AppBuilder](/agents/baidu-appbuilder/), [Coze](/agents/coze/)) on a bring-your-own-model, self-hosted basis — the segment of Chinese enterprises that cannot send internal documents to a managed cloud.

**What is uncertain.** The commercial edition's feature set and pricing (documented separately), the exact SaaS-restriction boundary, Labring's headquarters and funding, and independent retrieval-quality evaluation are not recorded in this database.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-fastgpt-1 | FastGPT GitHub repository | https://github.com/labring/FastGPT | Official documentation | — | 2026-09-30 | high | — |
| src-agents-fastgpt-2 | FastGPT documentation | https://doc.fastgpt.io/ | Official documentation | — | 2026-09-30 | high | — |
| src-agents-fastgpt-3 | FastGPT cloud service | https://fastgpt.io/ | Official | — | 2026-09-30 | high | — |
| src-agents-fastgpt-4 | FastGPT Open Source License | https://github.com/labring/FastGPT/blob/main/LICENSE | Official documentation | — | 2026-09-30 | high | — |
| src-agents-fastgpt-5 | FastGPT home (labring.github.io) | https://labring.github.io/fastgpt-home/ | Official | — | 2026-09-30 | high | — |

## Why it matters

FastGPT matters as the knowledge-base counterpoint to the workflow-first open platforms. Where [Dify](/agents/dify/) leads with general application workflows, FastGPT leads with document ingestion, chunk management, hybrid retrieval and rerank — the RAG plumbing that enterprise knowledge assistants are built on.

China AI Hub analysis indicates FastGPT's structural role is self-hosted knowledge infrastructure: it occupies the exact segment of Chinese enterprises that cannot send internal documents to a managed cloud, and it serves them on a bring-your-own-model basis. That is why its retrieval depth is the moat — chunk management, hybrid retrieval and rerank are treated as the primary surface, not a secondary feature, which is what clusters it with enterprise document-Q&A use cases rather than general agent-building.

China AI Hub analysis: FastGPT's non-OSI license locates it between two poles — more open than a closed platform (you can self-host the core) but less open than a pure-MIT framework (you cannot resell it as SaaS). That boundary, like [Dify](/agents/dify/)'s, protects a commercial business model; the difference is that FastGPT draws the line at "backend service use" rather than "multi-tenant SaaS redistribution," which is a stricter commercial gate for anyone wanting to wrap it into a product.

## How it differs from Dify and the closed platforms

FastGPT's differentiation is its depth in one area against breadth elsewhere.

- **[Dify](/agents/dify/)** is the general application platform — workflow, RAG, agents, observability — for prototype-to-production shipping across many model providers.
- **[Baidu AppBuilder](/agents/baidu-appbuilder/)** and **[Coze](/agents/coze/)** are closed, single-vendor managed platforms with knowledge features, but cloud-only and bound to ERNIE and Doubao respectively.
- **FastGPT** is the knowledge-base specialist: open-source, self-hostable, model-agnostic via AI Proxy, with hybrid retrieval and rerank as first-class — and a bidirectional MCP that the closed platforms' internal MCP does not mirror.

China AI Hub analysis: for an enterprise whose primary need is answering questions over an internal document corpus, FastGPT's self-hosted retrieval stack is the closest direct match among the platforms tracked here — the reverse of Dify's breadth-first bet. The two are complementary: FastGPT for retrieval-heavy knowledge work, Dify for general application scope.

## Practical implications

**For enterprises with sensitive documents.** FastGPT is the documented self-hosted path to keep a document corpus inside the firewall while still getting RAG, rerank and workflow orchestration. The cost is operational: Docker Compose self-hosting or the paid cloud, plus supplying and paying for your own model via AI Proxy.

**For knowledge-base teams.** The retrieval depth (chunk editing, hybrid retrieval, rerank, multi-format ingestion) is the reason to choose FastGPT over a general platform — it is the primary surface, not an add-on.

**For those who might resell.** The license permits commercial use as a backend service but requires authorization for a SaaS offering or commercial redistribution — a stricter gate than MIT, and a material consideration for anyone building a product on top of it.

## What the evidence shows

The evidence is strong on FastGPT's retrieval depth because the capability list is explicit in primary material: application orchestration (Agent Skill editing, dialog and plugin workflows with RPA nodes, bidirectional MCP), application debugging (knowledge-base search testing, full call-chain logs, evaluation), knowledge-base management (multi-library reuse, chunk editing, hybrid retrieval and rerank, multi-format ingestion), plugins, and operations. The AI Proxy model-aggregation layer is documented as the mechanism of its model neutrality.

The gaps are commercial and evaluative. The commercial edition's features and pricing are documented separately from the open-source repo; the SaaS-restriction boundary is drawn by a non-OSI license; Labring's corporate details and funding are not on official channels; and there is no independent evaluation of retrieval quality across the supported formats and rerank models. China AI Hub analysis indicates the retrieval claims are well-documented as *capabilities* but unverified as *measured results* — the same vendor-reported-versus-independent gap that runs across the open agent platforms.

## Where this fits

| Workload | Relevance |
|---|---|
| Knowledge-base Q&A over an internal document corpus | High |
| Enterprise knowledge management / AI customer service | High |
| Hybrid retrieval + rerank pipelines | High |
| Visual agent and plugin workflow orchestration | High |
| Self-hosted deployment (Docker Compose / Sealos) | High |
| General prototype-to-production application building | Moderate (Dify is broader) |
| Reselling as a SaaS | Restricted (authorization required) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

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
| Last verified | 2026-09-30 | Official |

See the [Labring](/companies/labring/) company profile, the [self-hosting guide](/guides/self-hosting-chinese-open-weights/), the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/), [RAG](/technology/rag/) and [MCP](/technology/mcp/) technology pages. For the structural reading of FastGPT as the self-hosted counterpoint to Dify and the closed platforms, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/).

*Labels used above: **Official fact** (from the FastGPT GitHub repository, LICENSE, documentation and cloud site), **Vendor-reported claim** (feature and deployment statements by Labring), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for FastGPT-built applications.*
