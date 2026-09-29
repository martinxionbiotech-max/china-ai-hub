---
company_id: deepwisdom
company_name: DeepWisdom (FoundationAgents)
description: "DeepWisdom is the company behind MetaGPT, the open-source multi-agent framework (now under the FoundationAgents GitHub organization), and MGX (MetaGPT X), a natural-language-programming product."
aliases:
  - FoundationAgents
  - MetaGPT
headquarters: "Not publicly documented as of 2026-09-29."
funding: "Not publicly documented as of 2026-09-29."
ai_products:
  - MetaGPT (open-source multi-agent framework)
  - MGX (MetaGPT X) natural-language programming product
foundation_models: []
agents:
  - metagpt
api: []
open_source_projects:
  - MetaGPT (FoundationAgents/MetaGPT)
official_documentation: https://docs.deepwisdom.ai/
official_website: https://deepwisdom.ai/
related_entities: []
last_verified: "2026-09-29"
sources:
  - source_name: MetaGPT GitHub repository (FoundationAgents)
    source_url: https://github.com/FoundationAgents/MetaGPT
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: MetaGPT documentation (DeepWisdom)
    source_url: https://docs.deepwisdom.ai/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: MGX (MetaGPT X) product site
    source_url: https://mgx.dev/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** DeepWisdom is the company behind [MetaGPT](/agents/metagpt/), the open-source multi-agent framework, and MGX (MetaGPT X), a natural-language-programming product; the MetaGPT repository now lives under the FoundationAgents GitHub organization. **Why it matters.** It is the source of the "software company as multi-agent team" idea — assigning PM, architect and engineer roles to LLMs under the "Code = SOP(Team)" philosophy — which has shaped how the broader agent field thinks about role decomposition. **Key characteristics.** A pip-installable, MIT-licensed Python framework; a research lineage producing the SPO, AOT and AFlow papers; and the MGX product at mgx.dev. **What a professional should know.** The framework is model-agnostic (users supply their own model keys), targets Python 3.9–3.11, and the company's headquarters and funding are not publicly documented.

DeepWisdom develops MetaGPT, an open-source multi-agent framework that "assigns different roles to GPTs to form a collaborative entity for complex tasks," simulating a software company with product managers, architects, project managers and engineers. The repository recently moved from `geekan/MetaGPT` to `FoundationAgents/MetaGPT`.

The team also ships MGX (MetaGPT X), launched February 2025 and described as "the world's first AI agent development team," a natural-language-programming product that productizes the same multi-agent idea behind a consumer-facing interface.

## Why it matters

China AI Hub analysis: DeepWisdom matters as the idea-source of the multi-agent paradigm rather than a deployment target. Its "software company" SOP model and its papers have influenced how the field decomposes work across specialized agent roles, even as its direct production use remains a developer's assembly job. The shift of its commercial energy to MGX reflects the broader pattern in this ecosystem: open-source frameworks establish the idea, and a productized layer captures the demand.

## Entity hub

### Products

- [MetaGPT](/agents/metagpt/)

### Agents

- [MetaGPT](/agents/metagpt/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)

## What is uncertain

- Headquarters and funding are not publicly documented.
- The repository's move from `geekan/MetaGPT` to `FoundationAgents/MetaGPT` is documented in the redirect but not explained on the company site.

## Sources

- [MetaGPT GitHub repository](https://github.com/FoundationAgents/MetaGPT)
- [MetaGPT documentation](https://docs.deepwisdom.ai/)
- [MGX product site](https://mgx.dev/)

*Labels used above: **Official fact** (from the MetaGPT GitHub repository and DeepWisdom documentation), **Vendor-reported claim** (product statements by DeepWisdom), and **China AI Hub analysis** (our synthesis, always introduced as such).*
