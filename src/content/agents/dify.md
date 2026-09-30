---
agent_id: dify
agent_name: Dify
company: langgenius
description: "Dify is an open-source LLM application development platform by LangGenius. Its interface combines AI workflow, RAG pipeline, agent capabilities, model management and observability (Opik, Langfuse, Arize Phoenix) to move teams from prototype to production. Model-agnostic: integrates hundreds of proprietary and open-source LLMs, including any OpenAI API-compatible model. Deployable on Dify Cloud, VPC, or self-hosted via Docker Compose."
agent_type: platform
underlying_models: []
framework: "Visual workflow canvas plus RAG pipeline, agent and model-management layers; Docker Compose self-hosting; backend API for integration."
tool_calling: true
mcp: true
memory: true
planning: true
api: true
pricing: "Open source (free self-hosted); Dify Cloud is a paid SaaS with free and paid tiers (dify.ai/pricing); commercial licensing required for multi-tenant SaaS redistribution under the Dify Open Source License."
deployment: both
open_source: true
license: "Dify Open Source License (Apache-2.0 based with additional conditions)"
github: https://github.com/langgenius/dify
documentation: https://docs.dify.ai/
use_cases:
  - Building agentic workflows and RAG pipelines
  - Prototyping and shipping LLM applications
  - Model management across multiple providers
  - Observability and evaluation of LLM apps
  - Self-hosted or VPC deployment for data control
limitations:
  - License is not pure Apache-2.0 — a commercial license is required for multi-tenant SaaS-style redistribution
  - Minimum system requirements (2-core CPU, 4 GiB RAM) mean heavier self-hosting than a CLI tool
  - Model neutrality means the operator must configure and pay for their own model providers
  - MCP is exposed via a published MCP Server URL that carries authentication credentials
last_verified: "2026-09-30"
sources:
  - source_name: Dify GitHub repository
    source_url: https://github.com/langgenius/dify
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Dify official website
    source_url: https://dify.ai/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Dify documentation
    source_url: https://docs.dify.ai/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Dify LICENSE
    source_url: https://github.com/langgenius/dify/blob/main/LICENSE
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Dify MCP Server documentation
    source_url: https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Dify pricing
    source_url: https://dify.ai/pricing
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** Dify is an open-source LLM application development platform by LangGenius that combines AI workflow, RAG pipeline, agent capabilities, model management and observability in one workspace — the leading model-neutral, self-hostable alternative to vendor-bound agent builders.

**Key facts.**

- Visual workflow canvas plus a RAG pipeline, agent layer and model-management layer, with observability integrations (Opik, Langfuse, Arize Phoenix).
- Model-agnostic: integrates hundreds of proprietary and open-source LLMs, including any OpenAI API-compatible model.
- Three deployment modes: Dify Cloud (managed SaaS), VPC, and self-hosted via Docker Compose (`docker compose up -d`).
- Open source under the "Dify Open Source License" — Apache-2.0 based with additional conditions; a commercial license is required for multi-tenant SaaS-style redistribution.
- Backend API for integration, and MCP support via a published MCP Server URL (which carries authentication credentials).
- Free self-hosted; Dify Cloud is a paid SaaS with free and paid tiers.

**What this means.** Dify is the neutral counterweight in a vendor-bound ecosystem: a platform with no model of its own, whose entire value is orchestrating other vendors' models behind a consistent workflow and RAG layer.

**What is uncertain.** The exact boundary of "multi-tenant SaaS redistribution" that triggers a commercial license, the company's funding, production sizing beyond the 2-core/4 GiB minimum, and the independent output-quality of Dify-built applications are not recorded in this database.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-dify-1 | Dify GitHub repository | https://github.com/langgenius/dify | Official documentation | — | 2026-09-30 | high | — |
| src-agents-dify-2 | Dify official website | https://dify.ai/ | Official | — | 2026-09-30 | high | — |
| src-agents-dify-3 | Dify documentation | https://docs.dify.ai/ | Official documentation | — | 2026-09-30 | high | — |
| src-agents-dify-4 | Dify LICENSE | https://github.com/langgenius/dify/blob/main/LICENSE | Official documentation | — | 2026-09-30 | high | — |
| src-agents-dify-5 | Dify MCP Server documentation | https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp | Official documentation | — | 2026-09-30 | high | — |
| src-agents-dify-6 | Dify pricing | https://dify.ai/pricing | Official | — | 2026-09-30 | high | — |

## Why it matters

Dify matters as the reference implementation of model-neutrality as a product. Where [Coze](/agents/coze/) defaults to Doubao, [Baidu AppBuilder](/agents/baidu-appbuilder/) to ERNIE and [Yuanqi](/agents/yuanqi/) to Hunyuan, Dify has no default at all — it orchestrates hundreds of models behind one workflow and RAG layer.

China AI Hub analysis indicates Dify's structural role is orchestration-without-a-model: it sells the *workflow*, *retrieval* and *observability* layers, not any model, which is both its strength (no lock-in) and its cost (the operator must assemble and pay for model access themselves). That positions it as the escape hatch from the bound platforms, and the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) records exactly this contrast — most Chinese agents are bound to their vendor's models; Dify is the opposite.

China AI Hub analysis: Dify's openness is more consequential than a bound lab agent's, but it narrows in one specific place — the license. It stays free to run but not free to resell as a competing multi-tenant SaaS, a boundary that protects the Dify Cloud business model. That is the open-core pattern in miniature: the self-hosted core is free, and the commercial boundary is drawn exactly where a reseller could undercut the managed service.

## How it differs from FastGPT and MetaGPT

Dify, FastGPT and MetaGPT are all open-source and model-agnostic, but they sit in different cells of the ecosystem.

- **[FastGPT](/agents/fastgpt/)** is knowledge-base-first: document ingestion, chunk management, hybrid retrieval and rerank are its primary surface, aimed at enterprise Q&A over internal corpora.
- **[MetaGPT](/agents/metagpt/)** is a *framework*, not a platform — a pip-installable, role-based multi-agent SDK that a developer composes into their own system, with a commercial product (MGX) layered on top.
- **Dify** is a *platform* — a self-hostable application builder spanning workflow, RAG, agents and observability, oriented to prototype-to-production application shipping.

China AI Hub analysis: the three are complementary rather than competing in the same lane. Dify is the general-purpose application platform; FastGPT is the specialist for retrieval-heavy knowledge work; MetaGPT is the idea-and-pattern source whose commercial energy has shifted to a productized layer. A team choosing Dify is choosing breadth of application scope over depth in any single area — the reverse of FastGPT's bet.

## Practical implications

**For teams escaping lock-in.** Dify is the documented, self-hostable path to run one workflow across many models — the strongest fit in the database for a team that wants to swap models without rebuilding its application.

**For self-hosters.** The trade-off is real infrastructure: a 2-core CPU / 4 GiB RAM minimum, and the operator must configure and pay for every model provider. Dify gives data and routing control in exchange for operational responsibility — the inverse of a bound platform's managed convenience.

**For MCP publishers.** Dify exposes applications as MCP Servers, but the published URL carries authentication credentials — a security consideration that bound platforms (whose MCP is internal) do not surface the same way.

**For those who might resell.** The non-OSI license is the key legal gate: self-hosting for internal use is free, but redistributing Dify as a multi-tenant SaaS requires a commercial license from LangGenius.

## What the evidence shows

The evidence for Dify is strong because it is a mature open-source project with a public repo, docs, LICENSE and a pricing page. The README's own framing — "AI workflow, RAG pipeline, agent capabilities, model management, observability features" — grounds the "orchestration-without-a-model" reading in the vendor's primary material, and the LICENSE text confirms the commercial-redistribution condition that the non-pure Apache-2.0 label flags.

The gaps are licensing precision and independent evaluation. The exact trigger for the commercial license is defined by the Dify Open Source License, not a standard OSI license, so the boundary is vendor-drawn; the company's funding is not public; and no independent benchmark of Dify-built application quality is recorded here. China AI Hub analysis indicates Dify's transparency is otherwise the highest among the agent platforms in this database, precisely because it is open — the repo and license are inspectable in a way the closed platforms' pricing and model routing are not.

## Where this fits

| Workload | Relevance |
|---|---|
| Agentic workflow + RAG application building | High |
| Prototype-to-production LLM application shipping | High |
| Cross-model orchestration (hundreds of providers) | High |
| Observability and evaluation of LLM apps | High |
| Self-hosted / VPC deployment for data control | High |
| Knowledge-base-first enterprise Q&A | Moderate (FastGPT is deeper) |
| Reselling as a multi-tenant SaaS | Restricted (commercial license) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Model-agnostic (hundreds of LLMs; any OpenAI API-compatible model) | Official |
| Target users | Developers, application teams, self-hosters | Official |
| Platform | Web app + Docker self-hosted; cloud SaaS | Official |
| OS | Cross-platform (Docker); Linux server | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Not a primary focus (application workflow, not a code agent) | Official |
| Autonomous task execution | Yes (agent capabilities, workflow) | Vendor-reported |
| MCP | Yes (MCP Server publish) | Official |
| Tool calling | Yes (workflow tools, agent tools) | Official |
| Memory | Yes (RAG, conversation memory) | Official |
| Workflow | Visual workflow canvas + RAG pipeline + agent layer | Official |
| API | Yes (backend service / API) | Official |
| Pricing | Open source (free); Dify Cloud paid SaaS tiers | Vendor-reported |
| Region | Global (Singapore company; cloud + self-hosted) | Official |
| Open-source | Yes — Apache-2.0 based (Dify Open Source License) | Official |
| Deployment | Both (cloud + self-hosted) | Official |
| Limitations | Non-pure Apache-2.0 (SaaS needs commercial license); 2-core/4GiB minimum | Official |
| Source | [GitHub](https://github.com/langgenius/dify) · [dify.ai](https://dify.ai/) · [docs](https://docs.dify.ai/) | Official |
| Last verified | 2026-09-30 | Official |

See the [LangGenius](/companies/langgenius/) company profile, the [self-hosting guide](/guides/self-hosting-chinese-open-weights/), the [open-weight vs API economics](/guides/open-weight-vs-api/), and the site's [AI agents](/technology/ai-agents/), [RAG](/technology/rag/) and [MCP](/technology/mcp/) technology pages. For the structural reading of Dify as the neutral counterweight to the bound platforms, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) and [the rise of Chinese AI agents](/research/rise-of-chinese-ai-agents/).

*Labels used above: **Official fact** (from the Dify GitHub repository, LICENSE, documentation and pricing page), **Vendor-reported claim** (feature and deployment statements by LangGenius), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Dify-built applications.*
