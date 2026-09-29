---
agent_id: coze
agent_name: Coze (扣子)
company: bytedance
description: "ByteDance's agent development platform (扣子/Coze): a one-stop AI development platform for building AI agents, workflows and applications with zero-code and low-code tools. Fully integrated the Doubao 2.1 model family (announced 2026-06-23 at Volcengine FORCE); the enterprise offering 'Coze Pro' runs on Volcengine. Supports publishing agents to WeChat, Feishu and Douyin channels, plus a model node that can also route to DeepSeek, Kimi and other models."
agent_type: platform
underlying_models:
  - doubao-seed-2-1-pro
framework: "Visual workflow builder with a 'large-model node' (大模型节点) as the core engine; zero-code agent configuration plus low-code workflow orchestration; plugins, knowledge bases and skill packs."
tool_calling: true
mcp: true
memory: true
planning: true
api: true
pricing: "Free tier plus paid subscription tiers (individual / team / enterprise); enterprise 'Coze Pro' is an out-of-the-box enterprise AI productivity platform on Volcengine; usage is credit/points-based with per-tier quotas."
deployment: cloud
open_source: false
license: proprietary
documentation: https://docs.coze.cn/
use_cases:
  - Building chatbots and AI agents without code
  - Workplace productivity agents (office, PPT, data analysis, web/app development)
  - Visual workflow orchestration with plugins and knowledge bases
  - Enterprise AI via Coze Pro on Volcengine
  - Publishing agents to WeChat, Feishu and Douyin
limitations:
  - Exact subscription pricing tiers are published on the logged-in console rather than static public pages
  - Underlying chat model naming beyond "Doubao 2.1" is not spelled out on the public overview pages
  - Platform is cloud-only; no self-hosted edition of the closed platform
  - Model node supports third-party models (DeepSeek, Kimi) but the platform defaults to Doubao
last_verified: "2026-09-29"
sources:
  - source_name: Coze China official site
    source_url: https://www.coze.cn/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Coze China documentation
    source_url: https://docs.coze.cn/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Coze Pro (Volcengine enterprise product page)
    source_url: https://www.volcengine.com/product/coze-pro
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Coze international site
    source_url: https://www.coze.com/
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
  - source_name: Coze MCP documentation
    source_url: https://docs.coze.cn/mcp
    source_type: official
    last_verified: "2026-09-29"
    confidence: high
---
**What it is.** Coze (扣子) is ByteDance's agent development platform — a one-stop, mostly zero-code environment for building AI agents, workflows and applications, positioned as a workplace and productivity surface rather than a developer framework. **Why it matters.** It is the consumer-and-SMB distribution arm of ByteDance's closed [Doubao Seed](/models/doubao-seed-2-1-pro/) models: users reach the models through the platform rather than through open weights, mirroring the [Doubao App](/agents/doubao-app/) on the development side. **Key characteristics.** A visual workflow builder whose core engine is a "large-model node," with plugins, knowledge bases and one-click publishing to WeChat, Feishu and Douyin; the enterprise tier, Coze Pro, runs on Volcengine. **What a professional should know.** Coze fully integrated the Doubao 2.1 model family in June 2026, but its model node can also route to DeepSeek and Kimi — so it is Doubao-default rather than Doubao-exclusive, and it is cloud-only with no self-hosted edition.

Coze is ByteDance's agent development platform (扣子/Coze): a one-stop AI development surface for building agents, workflows and applications, with zero-code configuration for non-developers and low-code workflow orchestration for builders. The core of any workflow is the "large-model node" (大模型节点), which the official documentation describes as the most powerful node in the system — it is where a workflow selects its model, tunes parameters, and attaches plugins, workflow calls and knowledge bases.

The platform is tightly coupled to ByteDance's model stack. Coze announced full integration of the Doubao 2.1 model family on 2026-06-23 at the Volcengine FORCE conference, which positioned the platform as a distribution channel for Doubao Seed models; the same model node can also route to third-party models such as DeepSeek and Kimi. The enterprise offering, "Coze Pro," is sold through Volcengine as an out-of-the-box enterprise AI productivity platform, and agents built in Coze can be published to WeChat, Feishu and Douyin.

See the [ByteDance](/companies/bytedance/) profile.

## Why it matters

Coze matters because it is ByteDance's answer to the question the rest of the agent ecosystem is also answering — how to convert model capability into a managed product — but on the consumer and small-business side rather than the developer side. Where [Qwen Code](/agents/qwen-code/) and [Dify](/agents/dify/) compete for developers and builders who want code-level or self-hosted control, Coze competes for operators who want a working agent in a WeChat channel without writing code. China AI Hub analysis indicates its structural role is downstream distribution: it extends ByteDance's closed-API posture one layer up, from the [Ark](/api/ark/) API to a no-code agent surface, and it is the clearest example in the database of a platform whose default model (Doubao) is the same vendor's own model, with cross-model routing available but not the default.

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Doubao 2.1 family ([Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/)); model node also routes DeepSeek, Kimi | Official |
| Target users | Non-developers, SMB operators, and low-code builders | Official |
| Platform | Web platform (coze.cn) + international (coze.com); enterprise Coze Pro on Volcengine | Official |
| OS | Browser-based (web platform) | Official |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Yes (web/app development via 扣子编程, code.coze.cn) | Vendor-reported |
| Autonomous task execution | Yes (agent + workflow orchestration) | Vendor-reported |
| MCP | Yes | Official |
| Tool calling | Yes (plugins, workflow calls, model node) | Official |
| Memory | Yes (knowledge base) | Official |
| Workflow | Visual workflow builder with large-model node, plugins, knowledge bases | Official |
| API | Yes (platform API; enterprise via [Volcengine Ark](/api/ark/)) | Official |
| Pricing | Free tier + paid individual/team/enterprise tiers; credit-based | Vendor-reported |
| Region | China (coze.cn); international (coze.com) | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Cloud-only; tier pricing on logged-in console; Doubao-default | Official |
| Source | [Coze China](https://www.coze.cn/) · [docs](https://docs.coze.cn/) · [Coze Pro](https://www.volcengine.com/product/coze-pro) | Official |
| Last verified | 2026-09-29 | Official |

## What is uncertain

- The exact subscription pricing tiers are not published on static public pages — they require the logged-in console.
- The specific Doubao model version behind a given agent, beyond the "Doubao 2.1" family naming, is not spelled out on the public overview pages.
- Whether the cross-model routing (DeepSeek, Kimi via the model node) delivers parity with the Doubao default is not independently evaluated.
- The platform's MCP support is documented in the docs, but its scope on the closed platform is not detailed on the overview pages.
- No independent third-party evaluation of Coze-built agents is recorded in this database.

*Labels used above: **Official fact** (from the Coze China site, documentation and Volcengine product pages), **Vendor-reported claim** (capability and pricing statements by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such).*
