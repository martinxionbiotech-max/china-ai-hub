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

Baidu (百度) is a publicly listed Chinese technology company headquartered in Beijing, and the provider of the ERNIE (文心) model family through Baidu AI Cloud's Qianfan (千帆) platform. The Qianfan family includes the "Qianfan model service and agent development platform" and the AppBuilder agent-development surface. The [Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/) is described in its documentation as "an enterprise-grade large-model application development and management platform" with an out-of-the-box toolchain of RAG, Agent, workflow and UI Builder, plus pre-built Baidu AI Search and iRAG components.

## Why it matters

China AI Hub analysis indicates Baidu's structural role is enterprise application delivery on its own ERNIE stack. Where Tencent's agent platform fuses to WeChat ([Yuanqi](/agents/yuanqi/)) and ByteDance's to Doubao ([Coze](/agents/coze/)), Baidu's AppBuilder is aimed at the enterprise team that wants a deployed agent without assembling an LLM stack — a managed, single-vendor integration rather than a neutral tool.

China AI Hub analysis indicates Baidu competes on pre-integration rather than model choice: AppBuilder bundles RAG, agent orchestration and UI building into one managed platform, with components pre-integrated to Baidu's own ERNIE models and search infrastructure. That puts it in direct competition with the open self-hosted platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) for the same enterprise builders, but on the opposite side of the trade-off — AppBuilder sells deployment speed and pre-integration in exchange for model choice.

China AI Hub analysis indicates AppBuilder is the most explicitly "enterprise toolchain" of the three bound platforms: it names RAG, workflow and UI Builder as first-class components and exposes a full-code exit (OpenAPI/SDK), which [Coze](/agents/coze/) and [Yuanqi](/agents/yuanqi/) de-emphasize in favor of channel publishing. A developer who needs code-level control but stays within a managed Baidu stack is the exact buyer AppBuilder is shaped for, whereas Coze and Yuanqi are shaped for operators who never want to see code.

## How it differs from Coze, Yuanqi and the open platforms

The three big-lab platforms share a managed-builder shape but optimize for different buyers and channels; the open platforms differ on openness.

- **[Coze](/agents/coze/)** (ByteDance) optimizes for consumer/SMB reach across WeChat, Feishu and Douyin on Doubao, plus a Volcengine enterprise tier.
- **[Yuanqi](/agents/yuanqi/)** (Tencent) optimizes for the WeChat official-account channel on Hunyuan, with customer-service and IP-persona categories.
- **[Dify](/agents/dify/)** and **[FastGPT](/agents/fastgpt/)** are open, self-hostable, model-agnostic — the neutral alternative to a managed single-vendor stack.
- **AppBuilder** (Baidu) optimizes for enterprise application delivery on ERNIE, with an explicit RAG/Agent/workflow/UI Builder toolchain and full-code OpenAPI/SDK paths.

China AI Hub analysis: the practical consequence is that the three bound platforms are rarely in direct substitution — a brand wanting a Douyin assistant picks Coze, a publisher wanting an agent inside WeChat reaches for Yuanqi, and an enterprise wanting RAG delivery on a managed stack weighs AppBuilder. The model underneath is decided by the channel, not the other way around; the neutral platforms are the exit when the model must be chosen by the buyer.

## Practical implications and limitations

**For enterprises on Baidu AI Cloud.** AppBuilder is the native managed path to RAG and agent applications on ERNIE, with pre-integrated search (Baidu AI Search) and image-generation RAG (iRAG) — a tighter default experience than assembling the same stack on a neutral platform.

**For full-code developers.** The visual builder is the front door, but the OpenAPI/SDK layer is the exit: developers who outgrow zero/low-code must move to the API surface, which is documented but not the platform's emphasis.

**For multi-model buyers.** AppBuilder is single-vendor (ERNIE), cloud-only and proprietary. Teams that need to swap models or self-host must weigh [Dify](/agents/dify/) or [FastGPT](/agents/fastgpt/) instead. The ERNIE model version behind a given agent and the consolidated pricing are not stated on public pages — a transparency gap teams should flag before committing.

## Entity hub

### Products

- [Baidu Qianfan AppBuilder (千帆 AppBuilder)](/agents/baidu-appbuilder/)

### Agents

- [Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [MCP](/technology/mcp/)
- [RAG](/technology/rag/)
- [Agent ecosystem structure and gaps](/research/china-ai-agent-ecosystem-structure-and-gaps/)

## What is uncertain

- The specific ERNIE model version behind a given AppBuilder agent is not stated on the platform overview.
- AppBuilder pricing is split across a billing page and the Qianfan console rather than a single public price list.
- ERNIE models are not yet tracked as standalone model records in this database.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-baidu-1 | Baidu Qianfan AppBuilder documentation | https://cloud.baidu.com/doc/AppBuilder/index.html | Official documentation | — | 2026-09-29 | high | — |
| src-companies-baidu-2 | Baidu Qianfan model service and agent development platform | https://cloud.baidu.com/doc/WENXINWORKSHOP/s/7ltgucw50 | Official documentation | — | 2026-09-29 | high | — |
| src-companies-baidu-3 | Baidu ERNIE (文心) model product page | https://cloud.baidu.com/product/model.html | Official | — | 2026-09-29 | high | — |

*Labels used above: **Official fact** (from Baidu Qianfan AppBuilder and ERNIE documentation), **Vendor-reported claim** (platform and model-family statements by Baidu), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for AppBuilder agents.*
