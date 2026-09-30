---
company_id: langgenius
company_name: LangGenius (Dify)
description: "LangGenius is the company behind Dify, the open-source LLM application development platform, and its managed cloud (Dify Cloud). Incorporated as DIFY PTE. LTD. in Singapore."
aliases:
  - Dify
  - Dify PTE. LTD.
headquarters: "Singapore"
funding: "Not publicly documented as of 2026-09-29."
ai_products:
  - Dify (open-source LLM application development platform)
  - Dify Cloud (managed SaaS)
foundation_models: []
agents:
  - dify
api: []
open_source_projects:
  - Dify (langgenius/dify)
official_documentation: https://docs.dify.ai/
official_website: https://dify.ai/
related_entities: []
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
---
**What it is.** LangGenius is the company behind [Dify](/agents/dify/), the open-source LLM application development platform, and its managed cloud (Dify Cloud); it is incorporated as DIFY PTE. LTD. in Singapore. **Why it matters.** It is the vendor of the most prominent model-neutral, self-hostable agent-building platform in this database — a company with no model of its own, whose product's entire value is orchestrating other vendors' models. **Key characteristics.** Dify combines AI workflow, RAG pipeline, agent capabilities, model management and observability; LangGenius also operates Dify Cloud. **What a professional should know.** Dify's license is Apache-2.0 based but not pure — a commercial license is required for multi-tenant SaaS redistribution — and the company's funding details are not publicly documented.

LangGenius is a Singapore-based company (incorporated as DIFY PTE. LTD. in 2018, per Singapore corporate records) behind Dify, an open-source LLM application development platform. The platform integrates "hundreds of proprietary / open-source LLMs," including any OpenAI API-compatible model, and is deployed via Dify Cloud, VPC or self-hosted Docker Compose. The company's product strategy is a classic open-core model: the open-source repository is free to self-host, while Dify Cloud is the managed, paid layer.

## Why it matters

China AI Hub analysis indicates LangGenius occupies the neutral-tool position that the six Chinese model labs do not. In an ecosystem the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) describes as largely vendor-bound — [Coze](/agents/coze/) defaults to Doubao, [Yuanqi](/agents/yuanqi/) to Hunyuan, [Baidu AppBuilder](/agents/baidu-appbuilder/) to ERNIE — Dify is the platform a buyer reaches for when it wants to swap models under one application rather than be locked to one vendor.

China AI Hub analysis indicates Dify's structural role is orchestration-without-a-model: it sells the workflow, retrieval and observability layers, not any model, which is both its strength (no lock-in) and its cost (the operator must assemble and pay for model access themselves). That positions LangGenius as the escape hatch from the bound platforms — it matters as much for what it is not (a model vendor) as for what it is (a neutral orchestrator).

China AI Hub analysis indicates LangGenius's openness is more consequential than a bound lab's, but it narrows in one specific place — the license. Dify stays free to run but not free to resell as a competing multi-tenant SaaS, a boundary that protects the Dify Cloud business model. That is the open-core pattern in miniature: the self-hosted core is free, and the commercial boundary is drawn exactly where a reseller could undercut the managed service.

## How it differs from FastGPT and MetaGPT

LangGenius (Dify), [Labring](/companies/labring/) (FastGPT) and [DeepWisdom](/companies/deepwisdom/) (MetaGPT) are all open-source and model-agnostic, but they sit in different cells of the ecosystem.

- **[FastGPT](/agents/fastgpt/)** (Labring) is knowledge-base-first — document ingestion, chunk management, hybrid retrieval and rerank are its primary surface, aimed at enterprise Q&A over internal corpora.
- **[MetaGPT](/agents/metagpt/)** (DeepWisdom) is a *framework*, not a platform — a pip-installable, role-based multi-agent SDK a developer composes into their own system, with a commercial product (MGX) layered on top.
- **Dify** (LangGenius) is a *platform* — a self-hostable application builder spanning workflow, RAG, agents and observability, oriented to prototype-to-production application shipping.

China AI Hub analysis: the three are complementary rather than competing in the same lane. A team choosing Dify is choosing breadth of application scope over depth in any single area — the reverse of FastGPT's retrieval-depth bet and distinct from MetaGPT's library-not-platform shape.

## Practical implications and limitations

**For teams escaping lock-in.** Dify is the documented, self-hostable path to run one workflow across many models — the strongest fit for a team that wants to swap models without rebuilding its application.

**For self-hosters.** The trade-off is real infrastructure: a 2-core CPU / 4 GiB RAM minimum, and the operator must configure and pay for every model provider. Dify gives data and routing control in exchange for operational responsibility.

**For those who might resell.** The non-OSI license is the key legal gate: self-hosting for internal use is free, but redistributing Dify as a multi-tenant SaaS requires a commercial license from LangGenius. Funding and the precise incorporation date are documented only through public corporate records, not the company's own site, so commercial independence rests on secondary evidence.

## Entity hub

### Products

- [Dify](/agents/dify/)

### Agents

- [Dify](/agents/dify/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [MCP](/technology/mcp/)
- [RAG](/technology/rag/)
- [Agent ecosystem structure and gaps](/research/china-ai-agent-ecosystem-structure-and-gaps/)

## What is uncertain

- Funding rounds are not publicly documented.
- The precise incorporation date (2018) comes from Singapore corporate records, not the company's own site.
- The exact boundary of "multi-tenant SaaS redistribution" that triggers a commercial license is defined by the Dify Open Source License, not a standard OSI license.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-langgenius-1 | Dify GitHub repository | https://github.com/langgenius/dify | Official documentation | — | 2026-09-29 | high | — |
| src-companies-langgenius-2 | Dify official website | https://dify.ai/ | Official | — | 2026-09-29 | high | — |
| src-companies-langgenius-3 | Dify documentation | https://docs.dify.ai/ | Official documentation | — | 2026-09-29 | high | — |

*Labels used above: **Official fact** (from the Dify GitHub repository and documentation), **Vendor-reported claim** (product statements by LangGenius), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Dify-built applications.*
