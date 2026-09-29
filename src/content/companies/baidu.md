---
company_id: baidu
company_name: Baidu
description: "Baidu (百度): Chinese internet and AI company behind the ERNIE (文心) foundation-model family and the Baidu Qianfan (千帆) AppBuilder agent development platform, sold through Baidu AI Cloud."
aliases:
  - 百度
  - 百度智能云
  - Baidu AI Cloud
  - 文心
headquarters: "Beijing, China"
funding: "Publicly listed (NASDAQ: BIDU; SEHK: 9888)."
ai_products:
  - ERNIE (文心) foundation model family
  - Baidu Qianfan AppBuilder (千帆 AppBuilder) agent platform
  - 文心一言 (ERNIE Bot)
  - Baidu AI Search
  - iRAG
foundation_models: []
agents:
  - baidu-appbuilder
api: []
open_source_projects: []
official_documentation: https://cloud.baidu.com/doc/AppBuilder/index.html
official_website: https://cloud.baidu.com/
related_entities: []
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
**What it is.** Baidu is the Chinese internet and AI company behind the ERNIE (文心) foundation-model family and the [Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/) agent development platform. **Why it matters.** It is China's longest-running AI-lab-plus-search combination: its agent platform bundles RAG, agent orchestration and UI building on top of ERNIE, competing for enterprise application delivery. **Key characteristics.** ERNIE spans multimodal foundation models; AppBuilder ships pre-built Baidu AI Search and iRAG components plus zero-code, low-code and full-code paths. **What a professional should know.** The AppBuilder platform is enterprise-focused and cloud-only, its public overview does not name the exact ERNIE version behind a given agent, and its pricing is distributed across a billing page and the Qianfan console.

Baidu (百度) is a publicly listed Chinese technology company headquartered in Beijing, and the provider of the ERNIE (文心) model family through Baidu AI Cloud's Qianfan (千帆) platform. The Qianfan family includes the "Qianfan model service and agent development platform" and the AppBuilder agent-development surface.

The [Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/) is described in its documentation as "an enterprise-grade large-model application development and management platform" with an out-of-the-box toolchain of RAG, Agent, workflow and UI Builder, plus pre-built Baidu AI Search and iRAG components.

## Why it matters

China AI Hub analysis: Baidu's structural role is enterprise application delivery on its own ERNIE stack. Where Tencent's agent platform fuses to WeChat ([Yuanqi](/agents/yuanqi/)) and ByteDance's to Doubao ([Coze](/agents/coze/)), Baidu's AppBuilder is aimed at the enterprise team that wants a deployed agent without assembling an LLM stack — a managed, single-vendor integration rather than a neutral tool, competing with the open self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) on a bring-your-own-model basis.

## Entity hub

### Products

- [Baidu Qianfan AppBuilder (千帆 AppBuilder)](/agents/baidu-appbuilder/)

### Agents

- [Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [MCP](/technology/mcp/)

## What is uncertain

- The specific ERNIE model version behind a given AppBuilder agent is not stated on the platform overview.
- AppBuilder pricing is split across a billing page and the Qianfan console rather than a single public price list.
- ERNIE models are not yet tracked as standalone model records in this database.

## Sources

- [Baidu Qianfan AppBuilder documentation](https://cloud.baidu.com/doc/AppBuilder/index.html)
- [Baidu Qianfan model service and agent development platform](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/7ltgucw50)
- [Baidu ERNIE model product page](https://cloud.baidu.com/product/model.html)

*Labels used above: **Official fact** (from Baidu Qianfan AppBuilder and ERNIE documentation), **Vendor-reported claim** (platform and model-family statements by Baidu), and **China AI Hub analysis** (our synthesis, always introduced as such).*
