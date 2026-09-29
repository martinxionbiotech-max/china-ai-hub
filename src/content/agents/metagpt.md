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
**What it is.** MetaGPT is an open-source multi-agent framework that assigns the roles of a software company — product managers, architects, project managers and engineers — to LLMs so that a one-line requirement produces user stories, requirements, data structures, APIs and code. **Why it matters.** It is the reference implementation of the "multi-agent company" idea: instead of a single agent prompting a single model, it encodes a software team's SOPs into a multi-agent pipeline under the philosophy "Code = SOP(Team)". **Key characteristics.** A pip-installable Python framework and CLI, a configurable LLM backend (OpenAI, Azure, Ollama, Groq and other API-compatible providers), and a research lineage that produced the SPO, AOT and AFlow papers. **What a professional should know.** It is MIT-licensed and model-agnostic (you supply your own model keys), it targets Python 3.9–3.11, and the productized natural-language-programming layer is MGX (MetaGPT X) at mgx.dev.

MetaGPT's core idea is role specialization: "Assign different roles to GPTs to form a collaborative entity for complex tasks." Internally it includes product managers, architects, project managers and engineers, and it "provides the entire process of a software company along with carefully orchestrated SOPs." The framework is consumed either as a CLI (`metagpt "Create a 2048 game"`) or as a library (`from metagpt.software_company import generate_repo`), with a Data Interpreter for code-and-data tasks.

The model backend is configured in `~/.metagpt/config2.yaml` and supports OpenAI, Azure, Ollama, Groq and other API-compatible providers — making the framework model-agnostic rather than bound to any vendor. The repository recently moved from `geekan/MetaGPT` to `FoundationAgents/MetaGPT`, and the DeepWisdom team also ships MGX, a natural-language-programming product described as "the world's first AI agent development team," which launched in February 2025.

See the [DeepWisdom](/companies/deepwisdom/) profile.

## Why it matters

MetaGPT matters as the framework-level contrast to the platform agents in this database. Where [Coze](/agents/coze/) and [Dify](/agents/dify/) are managed or self-hosted *platforms*, MetaGPT is a *library* — a research-grade multi-agent SDK that a developer composes into their own system. China AI Hub analysis indicates its structural role is idea-source rather than deployment target: its "software company" SOP model and its papers (SPO, AOT, AFlow) have shaped how the broader agent field thinks about role decomposition and self-optimizing workflows, even as its direct production use remains a developer's assembly job rather than an out-of-the-box product. That is why its commercial energy has shifted to MGX, which productizes the same multi-agent idea behind a natural-language interface. China AI Hub analysis: this split — an MIT framework that is free and self-hosted, plus a commercial product that wraps it — is the same open-core pattern that Dify and FastGPT run, but applied to a *framework* rather than a *platform*. Where Dify and FastGPT are tools you run, MetaGPT is a library you import; its influence therefore shows up less in deployments than in the design patterns (role-based SOPs, self-optimizing workflows) that the rest of the agent field has adopted.

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
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The repository's move from geekan/MetaGPT to FoundationAgents/MetaGPT is documented in the redirect but not explained on the company site.
- The company's headquarters and funding are not publicly documented.
- Python 3.12 support is not yet available, and no roadmap date is stated.
- The framework's production reliability is not independently benchmarked.
- The relationship between the open framework and the MGX product is not formally specified in the fetched documentation.

*Labels used above: **Official fact** (from the MetaGPT GitHub repository and DeepWisdom documentation), **Vendor-reported claim** (capability statements by DeepWisdom), and **China AI Hub analysis** (our synthesis, always introduced as such).*
