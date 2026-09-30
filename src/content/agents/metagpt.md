---
agent_id: metagpt
agent_name: MetaGPT
company: deepwisdom
description: "MetaGPT is an open-source multi-agent framework by DeepWisdom (now FoundationAgents). It assigns distinct roles — product managers, architects, project managers and engineers — to LLMs to form a collaborative 'software company' that turns a one-line requirement into user stories, requirements, data structures, APIs and code, under the philosophy 'Code = SOP(Team)'. Ships as a pip-installable Python framework and CLI; the natural-language-programming product MGX (MetaGPT X) is built on it. MIT-licensed."
agent_type: framework
underlying_models: []
framework: "Python framework (pip install metagpt) with a role-based multi-agent architecture; SOP (standard operating procedure) orchestration of a software-company team; configurable LLM backend (OpenAI, Azure, Ollama, Groq and other API-compatible providers)."
tool_calling: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "Free and open source (MIT). The commercial product MGX (MetaGPT X) at mgx.dev is separately offered; framework usage is free with self-supplied model API keys."
deployment: self_hosted
open_source: true
license: MIT
github: https://github.com/FoundationAgents/MetaGPT
documentation: https://docs.deepwisdom.ai/
use_cases:
  - Multi-agent software development from a single requirement
  - Role-based orchestration (PM / architect / engineer) of LLM teams
  - Data analysis via the Data Interpreter
  - Research prototyping of agentic workflows (SPO, AOT, AFlow)
  - Natural-language programming via MGX
limitations:
  - Requires Python 3.9–3.11 (3.12 not yet supported per the README)
  - Model-agnostic means the user must configure and pay for their own LLM API keys
  - The framework is a research-grade SDK, not a turnkey hosted product (MGX is the productized layer)
  - Repository recently moved from geekan/MetaGPT to FoundationAgents/MetaGPT
last_verified: "2026-09-30"
sources:
  - source_name: MetaGPT GitHub repository (FoundationAgents)
    source_url: https://github.com/FoundationAgents/MetaGPT
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: MetaGPT documentation (DeepWisdom)
    source_url: https://docs.deepwisdom.ai/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: MGX (MetaGPT X) product site
    source_url: https://mgx.dev/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: MetaGPT project page (Foundation Agents)
    source_url: https://foundationagents.deepwisdom.ai/projects/metagpt/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** MetaGPT is an open-source multi-agent framework by DeepWisdom (now FoundationAgents) that assigns the roles of a software company — product managers, architects, project managers and engineers — to LLMs, so a one-line requirement produces user stories, requirements, data structures, APIs and code under the philosophy "Code = SOP(Team)".

**Key facts.**

- Role-based multi-agent architecture: a simulated software company with PM, architect, project-manager and engineer agents, orchestrated by standard operating procedures.
- Consumed as a CLI (`metagpt "Create a 2048 game"`) or a Python library (`from metagpt.software_company import generate_repo`), with a Data Interpreter for code-and-data tasks.
- Model-agnostic: configurable backend (OpenAI, Azure, Ollama, Groq and other API-compatible providers), configured in `~/.metagpt/config2.yaml`.
- MIT-licensed and free; the user supplies their own model API keys.
- Targets Python 3.9–3.11 (3.12 not yet supported per the README).
- The productized natural-language-programming layer is MGX (MetaGPT X) at mgx.dev, described as "the world's first AI agent development team."
- Repository moved from geekan/MetaGPT to FoundationAgents/MetaGPT.

**What this means.** MetaGPT is the reference implementation of the "multi-agent company" idea — a *framework* that encodes a software team's SOPs into a multi-agent pipeline, whose commercial energy has shifted to a productized layer (MGX) rather than the SDK itself.

**What is uncertain.** The reason for the repo move, the company's headquarters and funding, Python 3.12 timing, the framework's production reliability, and the formal relationship between the open framework and MGX are not documented.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-metagpt-1 | MetaGPT GitHub repository (FoundationAgents) | https://github.com/FoundationAgents/MetaGPT | Official documentation | — | 2026-09-30 | high | — |
| src-agents-metagpt-2 | MetaGPT documentation (DeepWisdom) | https://docs.deepwisdom.ai/ | Official documentation | — | 2026-09-30 | high | — |
| src-agents-metagpt-3 | MGX (MetaGPT X) product site | https://mgx.dev/ | Official | — | 2026-09-30 | high | — |
| src-agents-metagpt-4 | MetaGPT project page (Foundation Agents) | https://foundationagents.deepwisdom.ai/projects/metagpt/ | Official | — | 2026-09-30 | high | — |

## Why it matters

MetaGPT matters as the framework-level contrast to the platform agents in this database. Where [Coze](/agents/coze/) and [Dify](/agents/dify/) are managed or self-hosted *platforms*, MetaGPT is a *library* — a research-grade multi-agent SDK that a developer composes into their own system.

China AI Hub analysis indicates MetaGPT's structural role is idea-source rather than deployment target: its "software company" SOP model and its research lineage (the SPO, AOT and AFlow papers) have shaped how the broader agent field thinks about role decomposition and self-optimizing workflows, even as its direct production use remains a developer's assembly job rather than an out-of-the-box product. That is why its commercial energy has moved to MGX, which productizes the same multi-agent idea behind a natural-language interface.

China AI Hub analysis: this split — an MIT framework that is free and self-hosted, plus a commercial product that wraps it — is the same open-core pattern that [Dify](/agents/dify/) and [FastGPT](/agents/fastgpt/) run, but applied to a *framework* rather than a *platform*. The difference is material: Dify and FastGPT are tools you run; MetaGPT is a library you import. Its influence therefore shows up less in deployments than in the design patterns (role-based SOPs, self-optimizing workflows) that the rest of the agent field has adopted.

## How it differs from the platforms and frameworks

MetaGPT sits in a distinct cell of the agent ecosystem.

- **[Dify](/agents/dify/)** and **[FastGPT](/agents/fastgpt/)** are platforms — self-hostable application builders (workflow/RAG/observability, or knowledge-base/RAG) that an operator runs to build applications.
- **[DeepSeek Harness](/agents/deepseek-harness/)** is a plugin-composed runtime whose agent loop is replaceable; it defaults toward a vendor's models.
- **MetaGPT** is a role-based multi-agent *library* — a pip-installable SDK whose core claim is not "run this to build apps" but "encode your team's SOPs as agents and compose them in Python."

China AI Hub analysis: the cleanest contrast is framework-versus-platform. A platform gives you a running system and a UI; a framework gives you building blocks and a loop. MetaGPT is the clearest example in this database of the latter — a developer-facing library whose most famous artifact is an idea (the software-company SOP) rather than a hosted surface, which is why it pairs naturally with a productized layer (MGX) rather than replacing one.

## Practical implications

**For researchers and framework builders.** MetaGPT is the reference to study role-based SOP orchestration — the SPO/AOT/AFlow lineage is a research asset in its own right, and the MIT license makes the code freely inspectable.

**For developers wanting multi-agent codegen.** The CLI and library paths are documented, but the developer must supply and pay for their own LLM keys and stay on Python 3.9–3.11 — a research-grade setup, not a turnkey product.

**For teams wanting a product.** MGX is the productized path; the framework itself is the SDK underneath. Anyone evaluating MetaGPT for production should be clear which layer they are actually adopting.

## What the evidence shows

The evidence is strong on the framework's conceptual design because it is explicit in primary material: "Assign different roles to GPTs to form a collaborative software entity for complex tasks," with the PM/architect/project-manager/engineer roles and the "Code = SOP(Team)" philosophy documented across the repo and docs. The model-agnostic backend (OpenAI, Azure, Ollama, Groq) and the config2.yaml mechanism are documented, and the MGX product is described as the natural-language-programming layer built on the framework.

The gaps are provenance and evaluation. The repo move from geekan/MetaGPT to FoundationAgents/MetaGPT is recorded but not explained; the company's headquarters and funding are not public; Python 3.12 timing is unstated; and the framework's production reliability is not independently benchmarked. China AI Hub analysis indicates MetaGPT is a case where conceptual influence clearly outruns measurable deployment — its ideas are widely cited in the agent field, but no independent production-evaluation evidence is recorded in this database.

## Where this fits

| Workload | Relevance |
|---|---|
| Multi-agent software development from one requirement | High |
| Role-based SOP orchestration (PM/architect/engineer) | High |
| Research prototyping (SPO, AOT, AFlow) | High |
| Data analysis via Data Interpreter | High |
| Natural-language programming via MGX | Moderate (separate product) |
| Turnkey hosted deployment | Low (framework, not a product) |
| Production multi-tenant SaaS on the framework | Low (research-grade SDK) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Model-agnostic (OpenAI, Azure, Ollama, Groq, API-compatible) | Official |
| Target users | Developers, researchers | Official |
| Platform | Python framework (pip install metagpt) + CLI | Official |
| OS | Cross-platform (Python 3.9–3.11) | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Yes (software-company code generation) | Vendor-reported |
| Autonomous task execution | Yes (multi-agent SOP orchestration) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes (Data Interpreter, tools) | Official |
| Memory | Yes (agent memory / workspace) | Official |
| Workflow | Role-based SOP: PM / architect / PM / engineer pipeline | Official |
| API | Yes (Python library API) | Official |
| Pricing | Free and open source (MIT); MGX offered separately | Vendor-reported |
| Region | Global (self-hosted) | Official |
| Open-source | Yes — MIT | Official |
| Deployment | Self-hosted | Official |
| Limitations | Python 3.9–3.11; user supplies model keys; research-grade SDK | Official |
| Source | [GitHub](https://github.com/FoundationAgents/MetaGPT) · [docs](https://docs.deepwisdom.ai/) | Official |
| Last verified | 2026-09-30 | Official |

See the [DeepWisdom](/companies/deepwisdom/) company profile, the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/) and [tool calling](/technology/tool-calling/) technology pages. For the structural reading of MetaGPT as framework-versus-platform, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/) and [the rise of Chinese AI agents](/research/rise-of-chinese-ai-agents/).

*Labels used above: **Official fact** (from the MetaGPT GitHub repository, DeepWisdom documentation and the Foundation Agents project page), **Vendor-reported claim** (capability statements by DeepWisdom), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for the MetaGPT framework.*
