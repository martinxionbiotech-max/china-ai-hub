---
agent_id: baidu-appbuilder
agent_name: Baidu Qianfan AppBuilder (千帆 AppBuilder)
company: baidu
description: "Baidu's agent development platform (百度千帆·Agent开发平台 / AppBuilder): an enterprise-grade large-model application development and management platform built on Baidu's ERNIE (文心) foundation models. Ships an out-of-the-box toolchain of RAG, Agent, workflow and UI Builder, pre-built Baidu AI Search and iRAG components, plus document/image understanding and speech recognition; supports zero-code, low-code and full-code development, with OpenAPI and SDK."
agent_type: platform
underlying_models: []
framework: "Enterprise application development and management platform with RAG / Agent / workflow / UI Builder toolchain; MCP service, knowledge-base and database management; OpenAPI and SDK for developers."
tool_calling: true
mcp: true
memory: true
planning: true
api: true
pricing: "Not publicly documented (billing published via a 计费说明 page; a 'Qianfan Token Plan' personal edition launched with first-purchase discounts; model usage billed through Baidu AI Cloud)."
deployment: cloud
open_source: false
license: proprietary
documentation: https://cloud.baidu.com/doc/AppBuilder/index.html
use_cases:
  - Enterprise AI-native application development
  - RAG document and table Q&A applications
  - Agent applications with reasoning and tool use
  - Zero-code application prototyping and low-code delivery
  - AI search and image-generation components
limitations:
  - Underlying ERNIE model version behind agents is not stated on the platform overview
  - Pricing is split across a billing page and the Qianfan console rather than a single public price list
  - Cloud-only platform; no self-hosted edition of the platform itself
  - Zero-code / low-code focus means full-code developers must use the OpenAPI/SDK layer
last_verified: "2026-09-30"
sources:
  - source_name: Baidu Qianfan AppBuilder documentation
    source_url: https://cloud.baidu.com/doc/AppBuilder/index.html
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Baidu Qianfan model service and agent development platform
    source_url: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/7ltgucw50
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Baidu ERNIE (文心) model product page
    source_url: https://cloud.baidu.com/product/model.html
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Baidu Qianfan AI application developer center pricing
    source_url: https://cloud.baidu.com/doc/qianfan-docs/s/Jm8r1826a
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** Baidu Qianfan AppBuilder (百度千帆·Agent开发平台) is Baidu's enterprise-grade agent and large-model application development platform, built on the ERNIE (文心) model family — an out-of-the-box RAG/Agent/workflow/UI Builder toolchain with pre-integrated Baidu AI Search and iRAG, spanning zero-code to full-code.

**Key facts.**

- Ships an out-of-the-box toolchain of RAG, Agent, workflow and UI Builder, plus document understanding, image understanding and speech recognition as traditional AI components.
- Pre-built application components include Baidu AI Search and iRAG (image-generation RAG).
- Supports zero-code, low-code and full-code development paths, with OpenAPI and SDK for developers who leave the visual builder.
- Enterprise application development and management platform: knowledge-base and database management, an MCP service, and an agent framework with reasoning and tool use.
- Built on Baidu's ERNIE foundation-model family; the platform overview does not name the exact ERNIE version behind a given agent.
- Cloud-only; no self-hosted edition.
- A "Qianfan Token Plan" personal edition launched with first-purchase discounts, pointing to credit-based personal pricing alongside enterprise contracts.

**What this means.** AppBuilder is Baidu's "last mile" from ERNIE models to deployed enterprise applications — the managed, single-vendor integration layer that Baidu sells through Baidu AI Cloud, as distinct from the consumer [文心一言](/companies/baidu/) surface and the Qianfan API.

**What is uncertain.** The specific ERNIE version behind each agent, the consolidated pricing (split across a billing page and the console), the scope of the MCP service, and whether agents can route to non-ERNIE models are all not stated on public pages.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-baidu-appbuilder-1 | Baidu Qianfan AppBuilder documentation | https://cloud.baidu.com/doc/AppBuilder/index.html | Official documentation | — | 2026-09-30 | high | — |
| src-agents-baidu-appbuilder-2 | Baidu Qianfan model service and agent development platform | https://cloud.baidu.com/doc/WENXINWORKSHOP/s/7ltgucw50 | Official documentation | — | 2026-09-30 | high | — |
| src-agents-baidu-appbuilder-3 | Baidu ERNIE (文心) model product page | https://cloud.baidu.com/product/model.html | Official | — | 2026-09-30 | high | — |
| src-agents-baidu-appbuilder-4 | Baidu Qianfan AI application developer center pricing | https://cloud.baidu.com/doc/qianfan-docs/s/Jm8r1826a | Official documentation | — | 2026-09-30 | high | — |

## Why it matters

AppBuilder matters because it is the enterprise leg of Baidu's ERNIE strategy. Baidu reaches consumers through the ERNIE Bot assistant, developers through the Qianfan API, and enterprise application teams through AppBuilder — the team that wants a deployed agent without assembling an LLM stack itself.

China AI Hub analysis indicates AppBuilder's structural role is enterprise application delivery. It bundles RAG, agent orchestration and UI building into one managed platform, and its components are pre-integrated with Baidu's own ERNIE models and search infrastructure — a managed, single-vendor integration rather than a neutral tool. That puts it in direct competition with the open self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) for the same enterprise builders, but on the opposite side of the trade-off: AppBuilder sells deployment speed and pre-integration in exchange for model choice.

China AI Hub analysis: AppBuilder is the enterprise mirror of Tencent's consumer-channel play. Where [Yuanqi](/agents/yuanqi/) sells WeChat reach on Hunyuan, AppBuilder sells enterprise RAG-and-agent delivery on ERNIE — and both compete against the open self-hosted platforms by offering a managed, pre-integrated stack that trades model choice for deployment speed. The practical consequence is a hard split: an ERNIE-committed enterprise gets a tighter default experience, while a multi-model buyer must look to Dify or FastGPT.

## How it differs from Coze and Yuanqi

The three big-lab platforms share a managed-builder shape but optimize for different buyers and channels.

- **[Coze](/agents/coze/)** (ByteDance) optimizes for consumer/SMB reach across WeChat, Feishu and Douyin on Doubao, plus a Volcengine enterprise tier. Its categories are workplace-productivity and channel publishing.
- **[Yuanqi](/agents/yuanqi/)** (Tencent) optimizes for the WeChat official-account channel on Hunyuan, with customer-service and IP-persona categories.
- **AppBuilder** (Baidu) optimizes for enterprise application delivery on ERNIE, with an explicit RAG/Agent/workflow/UI Builder toolchain, pre-built Baidu AI Search and iRAG components, and full-code OpenAPI/SDK paths.

China AI Hub analysis: AppBuilder is the most explicitly "enterprise toolchain" of the three — it names RAG, workflow and UI Builder as first-class components and exposes a full-code exit (OpenAPI/SDK), which Coze and Yuanqi de-emphasize in favor of channel publishing. A developer who needs code-level control but stays within a managed Baidu stack is the exact buyer AppBuilder is shaped for, whereas Coze and Yuanqi are shaped for operators who never want to see code.

## Practical implications

**For enterprises on Baidu AI Cloud.** AppBuilder is the native managed path to RAG and agent applications on ERNIE, with pre-integrated search (Baidu AI Search) and image-generation RAG (iRAG) — a tighter default experience than assembling the same stack on a neutral platform.

**For full-code developers.** The visual builder is the front door, but the OpenAPI/SDK layer is the exit: developers who outgrow zero/low-code must move to the API surface, which is documented but not the platform's emphasis.

**For multi-model buyers.** AppBuilder is single-vendor (ERNIE), cloud-only and proprietary. Teams that need to swap models or self-host must weigh [Dify](/agents/dify/) or [FastGPT](/agents/fastgpt/) instead — the neutral platforms that compete for the same builders on a bring-your-own-model basis.

## What the evidence shows

The evidence is strong on AppBuilder's component depth and weak on its model and pricing transparency. The official documentation describes it as "an enterprise-grade large-model application development and management platform" with an out-of-the-box RAG/Agent/workflow/UI Builder toolchain and pre-built Baidu AI Search and iRAG components — the richest named component list of the three bound platforms, which grounds the "enterprise toolchain" reading in primary material.

The gaps mirror the pattern: the ERNIE model version behind a given agent is unnamed on the overview, pricing is distributed across a billing page and the console, and the MCP service appears in the navigation without a detailed scope. China AI Hub analysis indicates this is the same asymmetry the other bound platforms show — the platform documents what it sells (the toolchain) more than what it routes (the specific model), because on a single-vendor stack the model is a default, not a choice to advertise.

## Where this fits

| Workload | Relevance |
|---|---|
| Enterprise RAG document/table Q&A application | High |
| Agent application with reasoning and tool use | High |
| Zero-code prototyping + low-code delivery | High |
| Full-code development via OpenAPI/SDK | Moderate (exit path, not emphasis) |
| AI search and image-generation components | High (Baidu AI Search, iRAG) |
| Multi-model routing / non-ERNIE models | Not documented |
| Self-hosted / on-premises deployment | None (cloud-only, proprietary) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Baidu ERNIE (文心) family — specific version not stated on overview | Official |
| Target users | Enterprise application teams, developers, SMBs | Official |
| Platform | Web platform (console.bce.baidu.com) | Official |
| OS | Browser-based (web platform) | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Yes (full-code path via OpenAPI/SDK) | Official |
| Autonomous task execution | Yes (Agent application framework) | Vendor-reported |
| MCP | Yes (MCP service) | Official |
| Tool calling | Yes (Agent framework, components) | Official |
| Memory | Yes (knowledge base, database management) | Official |
| Workflow | RAG / Agent / workflow / UI Builder toolchain | Official |
| API | Yes (OpenAPI, SDK) | Official |
| Pricing | Not publicly documented (billing page + Token Plan) | Not publicly documented |
| Region | China | Official |
| Open-source | No — proprietary (OpenAPI/SDK for developers) | Official |
| Deployment | Cloud | Official |
| Limitations | ERNIE version unnamed; pricing split; cloud-only | Official |
| Source | [AppBuilder docs](https://cloud.baidu.com/doc/AppBuilder/index.html) · [ERNIE](https://cloud.baidu.com/product/model.html) | Official |
| Last verified | 2026-09-30 | Official |

See the [Baidu](/companies/baidu/) company profile, the [choosing-an-agent guide](/guides/choosing-an-agent/), the [enterprise-deployment guide](/guides/enterprise-deployment/), and the site's [AI agents](/technology/ai-agents/), [RAG](/technology/rag/) and [MCP](/technology/mcp/) technology pages. For the structural reading of the three bound platforms, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/).

*Labels used above: **Official fact** (from Baidu Qianfan AppBuilder documentation and ERNIE product pages), **Vendor-reported claim** (capability statements by Baidu), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for AppBuilder agents.*
