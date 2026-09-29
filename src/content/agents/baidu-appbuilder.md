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
last_verified: "2026-09-29"
sources:
  - source_name: Baidu Qianfan AppBuilder documentation
    source_url: https://cloud.baidu.com/doc/AppBuilder/index.html
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Baidu Qianfan model service and agent development platform
    source_url: https://cloud.baidu.com/doc/WENXINWORKSHOP/s/7ltgucw50
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Baidu ERNIE (文心) model product page
    source_url: https://cloud.baidu.com/product/model.html
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Baidu Qianfan AppBuilder (百度千帆·Agent开发平台) is Baidu's enterprise-grade agent and large-model application development platform, built on the ERNIE (文心) foundation model family. **Why it matters.** It is Baidu's toolchain for turning ERNIE models into deployed enterprise applications — the "last mile" from model to production that Baidu sells through Baidu AI Cloud. **Key characteristics.** An out-of-the-box toolchain of RAG, Agent, workflow and UI Builder; pre-built Baidu AI Search and iRAG components; zero-code, low-code and full-code development paths plus OpenAPI and SDK. **What a professional should know.** The platform is enterprise-focused and cloud-only, its public overview does not name the exact ERNIE model version behind a given agent, and its pricing is distributed across a billing page and the Qianfan console rather than a single public price list.

Baidu Qianfan AppBuilder is described in its official documentation as "an enterprise-grade large-model application development and management platform" that provides an out-of-the-box toolchain of RAG, Agent, workflow and UI Builder. It ships pre-built components — Baidu AI Search and iRAG as application-development features, plus document understanding, image understanding and speech recognition as traditional AI components — and it supports zero-code, low-code and full-code development paths to lower the barrier to shipping large-model applications.

The platform sits inside the larger Qianfan (千帆) family of Baidu AI Cloud, which also includes the "Qianfan model service and agent development platform" and the ERNIE model family. Agent development on the platform exposes a knowledge-base and database management layer, an MCP service, and OpenAPI and SDK interfaces for developers who want to leave the visual builder. A "Qianfan Token Plan" personal edition was recently launched with first-purchase discounts, indicating a move toward credit-based personal pricing alongside enterprise contracts.

See the [Baidu](/companies/baidu/) profile.

## Why it matters

Baidu AppBuilder matters because it is the enterprise leg of Baidu's ERNIE strategy: where [文心一言 (ERNIE Bot)](/companies/baidu/) reaches consumers and the Qianfan API reaches developers, AppBuilder reaches the enterprise application team that wants a deployed agent without assembling an LLM stack itself. China AI Hub analysis indicates its structural role is enterprise application delivery — it bundles RAG, agent orchestration and UI building into one managed platform, in contrast to the open-source self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) that compete for the same builders on a bring-your-own-model basis. The key differentiator is that AppBuilder's components are pre-integrated with Baidu's own ERNIE models and search infrastructure, which is a managed, single-vendor integration rather than a neutral tool. China AI Hub analysis: this positions AppBuilder as the enterprise mirror of Tencent's consumer-channel play — where Yuanqi sells WeChat reach, AppBuilder sells enterprise RAG-and-agent delivery on ERNIE — and both compete against the open self-hosted platforms by offering a managed, pre-integrated stack that trades model choice for deployment speed. The practical consequence is that an ERNIE-committed enterprise gets a tighter default experience, while a multi-model buyer must look to Dify or FastGPT.

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
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The specific ERNIE model version behind a given agent is not stated on the platform overview.
- Pricing is distributed across a billing page and the Qianfan console rather than a single public price list.
- The platform's MCP service scope is listed in the navigation but not detailed in the fetched overview.
- Whether AppBuilder agents can route to non-ERNIE models is not documented on the public pages.
- No independent third-party evaluation of AppBuilder agents is recorded in this database.

*Labels used above: **Official fact** (from Baidu Qianfan AppBuilder documentation and ERNIE product pages), **Vendor-reported claim** (capability statements by Baidu), and **China AI Hub analysis** (our synthesis, always introduced as such).*
