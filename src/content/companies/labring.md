---
company_id: labring
company_name: Labring (环界云计算)
description: "Labring (环界云计算) is a Chinese cloud-computing company founded in 2022, best known for Sealos (a Kubernetes-based cloud operating system) and the open-source FastGPT knowledge-base agent platform."
aliases:
  - 环界云计算
  - Sealos
  - 环界云
headquarters: "Not publicly documented as of 2026-09-29."
funding: "Media-reported Alibaba Cloud strategic investment (36Kr); not confirmed on official channels."
ai_products:
  - Sealos (cloud operating system)
  - FastGPT (knowledge-base agent platform)
  - AI Proxy (model aggregation service)
foundation_models: []
agents:
  - fastgpt
api: []
open_source_projects:
  - FastGPT (labring/FastGPT)
  - Sealos (labring/sealos)
  - AI Proxy (labring/aiproxy)
official_documentation: https://doc.fastgpt.io/
official_website: https://sealos.run/
related_entities: []
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
  - source_name: Sealos official site
    source_url: https://sealos.run/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Labring (环界云计算) is a Chinese cloud-computing company founded in 2022, best known for Sealos — a Kubernetes-based cloud operating system — and the open-source [FastGPT](/agents/fastgpt/) knowledge-base agent platform. **Why it matters.** It is the vendor of China's most prominent open-source knowledge-base agent platform, the self-hosted answer to RAG-heavy enterprise Q&A. **Key characteristics.** Sealos provides one-click cloud deployment; FastGPT offers data processing, RAG retrieval and visual AI workflow orchestration with bidirectional MCP. **What a professional should know.** FastGPT's license is not OSI-approved — commercial use is permitted as a backend service but a SaaS offering or redistribution requires authorization — and the company's Alibaba Cloud investment is media-reported rather than officially confirmed.

Labring (环界云计算) was founded in March 2022. Its core product, Sealos, is a cloud operating system built on Kubernetes, while FastGPT is its AI-knowledge-base platform; the company also operates AI Proxy, a model aggregation and load-balancing service that keeps FastGPT model-agnostic.

The company's open-source footprint is substantial: Sealos and FastGPT are both distributed on GitHub, with FastGPT offering a managed cloud (fastgpt.io), a Docker Compose self-hosted path, and one-click deployment on Sealos Cloud.

## Why it matters

China AI Hub analysis: Labring matters as the infrastructure-plus-knowledge combination in the agent ecosystem. Where [Dify](/agents/dify/) leads with general application workflows, FastGPT leads with document ingestion, chunk management and hybrid retrieval — the RAG plumbing for enterprise knowledge assistants — and it does so on a self-hosted, bring-your-own-model basis that suits Chinese enterprises which cannot send internal documents to a managed cloud. Its non-OSI license, however, means "open source" here comes with a commercial boundary that the pure-MIT frameworks do not have.

## Entity hub

### Products

- [FastGPT](/agents/fastgpt/)

### Agents

- [FastGPT](/agents/fastgpt/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [MCP](/technology/mcp/)

## What is uncertain

- Headquarters location is not published on official channels.
- The Alibaba Cloud strategic investment is media-reported (36Kr), not confirmed on official channels.
- Founding date (March 2022) is media-reported.

## Sources

- [FastGPT GitHub repository](https://github.com/labring/FastGPT)
- [FastGPT documentation](https://doc.fastgpt.io/)
- [Sealos official site](https://sealos.run/)

*Labels used above: **Official fact** (from the FastGPT GitHub repository, documentation and Sealos site), **Vendor-reported claim** (product statements by Labring), and **China AI Hub analysis** (our synthesis, always introduced as such).*
