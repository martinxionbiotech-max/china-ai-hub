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

DeepWisdom develops MetaGPT, an open-source multi-agent framework that "assigns different roles to GPTs to form a collaborative entity for complex tasks," simulating a software company with product managers, architects, project managers and engineers. The repository recently moved from `geekan/MetaGPT` to `FoundationAgents/MetaGPT`. The team also ships MGX (MetaGPT X), launched February 2025 and described as "the world's first AI agent development team," a natural-language-programming product that productizes the same multi-agent idea behind a consumer-facing interface.

## Why it matters

China AI Hub analysis indicates DeepWisdom matters as the idea-source of the multi-agent paradigm rather than a deployment target. Its "software company" SOP model and its papers have influenced how the field decomposes work across specialized agent roles, even as its direct production use remains a developer's assembly job.

China AI Hub analysis indicates DeepWisdom's structural role is framework-level idea-generation: where [Dify](/agents/dify/) and [FastGPT](/agents/fastgpt/) are tools an operator runs, MetaGPT is a library a developer imports, so its influence shows up less in deployments than in the design patterns — role-based SOPs and self-optimizing workflows — that the rest of the agent field has adopted. That is why its commercial energy has shifted to MGX, which productizes the same multi-agent idea behind a natural-language interface.

China AI Hub analysis indicates the company runs the open-core pattern in a *framework* shape rather than a *platform* shape: an MIT core that is free and self-hosted, plus a commercial layer (MGX) that wraps it. The contrast with Dify and FastGPT is material — their open cores are systems you run, while DeepWisdom's is a library you import — which explains why the repository's move to FoundationAgents matters less than the split between the free framework and the paid product it feeds.

## How it differs from Dify, FastGPT and the bound platforms

DeepWisdom sits in a distinct cell of the agent ecosystem from both the open platforms and the vendor-bound builders.

- **[Dify](/agents/dify/)** (LangGenius) and **[FastGPT](/agents/fastgpt/)** (Labring) are platforms — self-hostable application builders (workflow/RAG/observability, or knowledge-base/RAG) that an operator runs.
- **[Coze](/agents/coze/)** and **[Yuanqi](/agents/yuanqi/)** are vendor-bound managed builders — defaulting to Doubao and Hunyuan respectively — with no open weights and no self-hosted exit.
- **MetaGPT** (DeepWisdom) is a role-based multi-agent *library* — a pip-installable SDK whose core claim is not "run this to build apps" but "encode your team's SOPs as agents and compose them in Python."

China AI Hub analysis: the cleanest contrast is framework-versus-platform and framework-versus-vendor. A platform gives you a running system and a UI; a framework gives you building blocks and a loop. DeepWisdom is the clearest example in this database of the latter — a developer-facing library whose most famous artifact is an idea (the software-company SOP) rather than a hosted surface, which is why it pairs naturally with a productized layer (MGX) rather than replacing one.

## Practical implications and limitations

**For researchers and framework builders.** MetaGPT is the reference to study role-based SOP orchestration — the SPO/AOT/AFlow lineage is a research asset in its own right, and the MIT license makes the code freely inspectable.

**For developers wanting multi-agent codegen.** The CLI and library paths are documented, but the developer must supply and pay for their own LLM keys and stay on Python 3.9–3.11 — a research-grade setup, not a turnkey product. Python 3.12 is not yet supported per the README.

**For teams wanting a product.** MGX is the productized path; the framework itself is the SDK underneath. Anyone evaluating DeepWisdom for production should be clear which layer they are actually adopting — the free MIT framework or the paid MGX surface — because the two carry different support and stability expectations.

## Entity hub

### Products

- [MetaGPT](/agents/metagpt/)

### Agents

- [MetaGPT](/agents/metagpt/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [Tool Calling](/technology/tool-calling/)
- [Agent ecosystem structure and gaps](/research/china-ai-agent-ecosystem-structure-and-gaps/)

## What is uncertain

- Headquarters and funding are not publicly documented.
- The repository's move from `geekan/MetaGPT` to `FoundationAgents/MetaGPT` is documented in the redirect but not explained on the company site.
- Python 3.12 support timing and the formal relationship between the open framework and MGX are not documented.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-deepwisdom-1 | MetaGPT GitHub repository (FoundationAgents) | https://github.com/FoundationAgents/MetaGPT | Official documentation | — | 2026-09-29 | high | — |
| src-companies-deepwisdom-2 | MetaGPT documentation (DeepWisdom) | https://docs.deepwisdom.ai/ | Official documentation | — | 2026-09-29 | high | — |
| src-companies-deepwisdom-3 | MGX (MetaGPT X) product site | https://mgx.dev/ | Official | — | 2026-09-29 | high | — |

*Labels used above: **Official fact** (from the MetaGPT GitHub repository and DeepWisdom documentation), **Vendor-reported claim** (product statements by DeepWisdom), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for the MetaGPT framework.*
