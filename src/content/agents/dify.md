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
last_verified: "2026-09-29"
sources:
  - source_name: Dify GitHub repository
    source_url: https://github.com/langgenius/dify
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Dify official website
    source_url: https://dify.ai/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Dify documentation
    source_url: https://docs.dify.ai/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Dify LICENSE
    source_url: https://github.com/langgenius/dify/blob/main/LICENSE
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Dify MCP Server documentation
    source_url: https://docs.dify.ai/en/cloud/use-dify/publish/publish-mcp
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Dify is an open-source LLM application development platform by LangGenius that combines AI workflow, RAG pipeline, agent capabilities, model management and observability in one collaborative workspace. **Why it matters.** It is the leading model-neutral, self-hostable alternative to vendor-bound agent builders — the platform a team reaches for when it wants to orchestrate many models behind one application rather than be locked to one vendor. **Key characteristics.** A visual workflow canvas, hundreds of supported LLMs (including any OpenAI API-compatible model), observability integrations (Opik, Langfuse, Arize Phoenix), and deployment on Dify Cloud, VPC or self-hosted Docker. **What a professional should know.** The license is Apache-2.0 based but not pure — a commercial license is required for multi-tenant SaaS redistribution, and self-hosting has real system requirements (2-core CPU, 4 GiB RAM minimum).

Dify positions itself as a production path from prototype to deployment. Its README describes an intuitive interface combining "AI workflow, RAG pipeline, agent capabilities, model management, observability features (including Opik, Langfuse, and Arize Phoenix) and more." The model layer is deliberately broad: it integrates "hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted solutions, covering GPT, Mistral, Llama3, and any OpenAI API-compatible models."

Dify runs three ways: Dify Cloud (managed SaaS), a VPC deployment, and self-hosted via Docker Compose (the recommended path is `docker compose up -d` after copying `.env.example`). The self-hosting route means teams keep data and model routing under their own control, which is the core of its appeal versus the closed platforms.

See the [LangGenius](/companies/langgenius/) profile.

## Why it matters

Dify matters as the neutral counterweight in an otherwise vendor-bound agent ecosystem. The research page on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) records that most Chinese agents are bound to their vendor's own models; Dify is the opposite — a platform with no model of its own, whose entire value is orchestrating other vendors' models behind a consistent workflow and RAG layer. China AI Hub analysis indicates its structural role is model-neutrality as a product: where [Coze](/agents/coze/) defaults to Doubao and [Baidu AppBuilder](/agents/baidu-appbuilder/) defaults to ERNIE, Dify has no default at all, which is both its strength (no lock-in) and its cost (the operator must assemble and pay for model access themselves). China AI Hub analysis: this trade-off is the whole point of Dify — it sells the *orchestration* rather than any model, which is why its openness is more consequential than a bound lab agent's. The non-OSI license is the one place its "open" posture narrows: it stays free to run but not free to resell as a competing multi-tenant SaaS, a boundary that protects the Dify Cloud business model.

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
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The exact boundary of "multi-tenant SaaS redistribution" that triggers a commercial license is defined by the Dify Open Source License, not a standard OSI license.
- No independent benchmark of Dify-built applications' output quality is recorded in this database.
- The company's funding is not publicly documented.
- The minimum system requirements (2-core CPU, 4 GiB RAM) are a floor; production sizing is not specified.
- The database does not independently test how well a given cross-vendor model performs inside Dify's workflow engine.

*Labels used above: **Official fact** (from the Dify GitHub repository, LICENSE and documentation), **Vendor-reported claim** (feature and deployment statements by LangGenius), and **China AI Hub analysis** (our synthesis, always introduced as such).*
