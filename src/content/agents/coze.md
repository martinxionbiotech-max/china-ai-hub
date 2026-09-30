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
last_verified: "2026-09-30"
sources:
  - source_name: Coze China official site
    source_url: https://www.coze.cn/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Coze China documentation
    source_url: https://docs.coze.cn/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Coze Pro (Volcengine enterprise product page)
    source_url: https://www.volcengine.com/product/coze-pro
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Coze international site
    source_url: https://www.coze.com/
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
  - source_name: Coze MCP documentation
    source_url: https://docs.coze.cn/mcp
    source_type: official
    last_verified: "2026-09-30"
    confidence: high
---
**Short answer.** Coze (扣子) is ByteDance's no-code and low-code agent development platform: a visual workflow builder built around a "large-model node" that routes work to the [Doubao Seed 2.1](/models/doubao-seed-2-1-pro/) family by default, with one-click publishing to WeChat, Feishu and Douyin, and an enterprise tier ("Coze Pro") sold through Volcengine.

**Key facts.**

- A zero-code agent builder plus low-code workflow orchestration; the documented core of any workflow is the "large-model node" (大模型节点), where a workflow selects its model, tunes parameters and attaches plugins, workflow calls and knowledge bases.
- Fully integrated the Doubao 2.1 model family on 2026-06-23, announced at Volcengine's FORCE conference.
- The model node can also route to third-party models such as DeepSeek and Kimi — the platform is Doubao-default, not Doubao-exclusive.
- Enterprise offering "Coze Pro" runs on Volcengine as an out-of-the-box AI productivity platform.
- Publishes agents to ByteDance and Tencent channels: WeChat, Feishu and Douyin.
- Cloud-only and proprietary; no self-hosted edition.
- Pricing is free-tier plus paid individual/team/enterprise tiers on a credit/points basis, with exact tiers published on the logged-in console rather than static pages.

**What this means.** Coze is ByteDance's distribution layer for its closed model stack: the same company that sells [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) weights through the [Ark](/api/ark/) API also sells a no-code surface where those models are the default and the app reaches consumer channels directly.

**What is uncertain.** The specific Doubao model version behind a given agent (beyond the "Doubao 2.1" family naming) is not spelled out on public pages; exact tier pricing requires the logged-in console; and whether the cross-model routing delivers parity with the Doubao default has not been independently evaluated.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-coze-1 | Coze China official site | https://www.coze.cn/ | Official | — | 2026-09-30 | high | — |
| src-agents-coze-2 | Coze China documentation | https://docs.coze.cn/ | Official documentation | — | 2026-09-30 | high | — |
| src-agents-coze-3 | Coze Pro (Volcengine enterprise product page) | https://www.volcengine.com/product/coze-pro | Official | — | 2026-09-30 | high | — |
| src-agents-coze-4 | Coze MCP documentation | https://docs.coze.cn/mcp | Official documentation | — | 2026-09-30 | high | — |
| src-agents-coze-5 | Coze international site | https://www.coze.com/ | Official | — | 2026-09-30 | high | — |

## Why it matters

Coze matters because it is the consumer-and-SMB arm of ByteDance's closed-model strategy — the no-code complement to the developer-facing [Ark](/api/ark/) API and the consumer-facing [Doubao App](/agents/doubao-app/). Where ByteDance reaches developers through an API and consumers through an assistant, Coze reaches the middle: operators who want a working agent in a WeChat or Douyin channel without writing code.

China AI Hub analysis indicates Coze's structural role is downstream distribution rather than tooling neutrality. It extends ByteDance's closed-API posture one layer up — from model weights, through the Ark API, to a no-code agent surface — and it is the clearest example in the database of a platform whose default model is its own vendor's model. The June 2026 "full integration" of Doubao 2.1 is the signal event: it converted the platform from a general builder into a distribution channel for the Doubao family, mirroring how [Yuanqi](/agents/yuanqi/) routes Tencent's Hunyuan into WeChat and how [Baidu AppBuilder](/agents/baidu-appbuilder/) routes ERNIE into enterprise apps.

China AI Hub analysis: the fact that the model node *can* route to DeepSeek and Kimi but *defaults* to Doubao is a strategic choice, not a technical ceiling. Keeping cross-model routing available defends against lock-in criticism and captures users who need a specific third-party model, while the default nudges the whole base toward Doubao spend — the same economics as the Ark API, but at a higher abstraction level where the buyer is an operator, not an engineer.

## How it differs from Yuanqi and Baidu AppBuilder

The three big-lab agent platforms in this database share a shape — a managed builder on top of the vendor's own foundation model — but they attach to different distribution assets.

- **[Tencent Yuanqi](/agents/yuanqi/)** is channel-bound to WeChat: its defining asset is the WeChat official-account agent, and its categories skew to customer service, government service and IP personas. It competes on reach into the highest-value consumer channel.
- **[Baidu Qianfan AppBuilder](/agents/baidu-appbuilder/)** is the enterprise leg: an out-of-the-box RAG/Agent/workflow/UI Builder toolchain with pre-integrated Baidu AI Search and iRAG, plus full-code OpenAPI/SDK paths. It competes on enterprise application delivery on ERNIE.
- **Coze** sits between them: a broader consumer/SMB surface (publishing to WeChat, Feishu and Douyin, workplace productivity agents) plus an enterprise tier (Coze Pro on Volcengine). It competes on breadth of channel and on the Doubao model family, not on any single channel or enterprise toolchain.

China AI Hub analysis: the three platforms are not interchangeable — they are each a managed on-ramp to a different vendor's model and a different distribution asset. A buyer choosing among them is really choosing whose model and whose channel they want their agents bound to. Coze's distinguishing edge is that it spans the widest channel set (WeChat, Feishu, Douyin) while remaining Doubao-default underneath.

## Practical implications

**For SMB operators and non-developers.** Coze is the fastest documented path to a working agent in WeChat, Feishu or Douyin without code. The trade-off is lock-in: the default model is Doubao, and the platform is cloud-only, so there is no self-hosted exit.

**For enterprises.** Coze Pro on Volcengine is the managed path — an out-of-the-box productivity platform rather than a toolkit to assemble. Enterprises already on Volcengine's cloud get a tighter default experience; multi-model buyers must configure the model node to route elsewhere and accept that the default remains Doubao.

**For builders who want model freedom.** The model node's third-party routing (DeepSeek, Kimi) exists but is not the default, so Coze is a weaker fit than the neutral platforms ([Dify](/agents/dify/), [FastGPT](/agents/fastgpt/)) for teams whose core requirement is swapping models under one workflow. Coze is a distribution surface first and a neutral tool second.

## What the evidence shows

The evidence for Coze's architecture is strong at the concept level and thin at the transparency level. The official documentation is explicit that the "large-model node" is the core engine of a workflow — where model selection, parameter tuning, plugin attachment and knowledge-base wiring happen — which grounds the "Doubao-default" reading in primary documentation rather than inference. The June 2026 FORCE announcement of Doubao 2.1 full integration is documented across the official site and the international mirror.

The transparency gaps are structural, not cosmetic. Pricing tiers live behind a login, so the free-to-paid economics are not auditable from static pages; the model node's third-party routing is documented but the version-level model identity behind an agent is not; and there is no independent evaluation of Coze-built agent quality recorded in this database. China AI Hub analysis indicates these gaps are consistent with the platform's role — a distribution channel documents its reach and its default model more than it documents model choice, because model choice is the one thing a bound platform is structurally least interested in exposing.

## Where this fits

| Workload | Relevance |
|---|---|
| No-code chatbot / agent for WeChat, Feishu or Douyin | High |
| SMB workplace productivity agents (office, PPT, analysis) | High |
| Enterprise managed AI platform (Coze Pro on Volcengine) | High |
| Visual workflow orchestration with plugins and knowledge bases | High |
| Multi-model routing (DeepSeek, Kimi via model node) | Moderate (available, not default) |
| Self-hosted / on-premises deployment | None (cloud-only, proprietary) |
| Full-code SDK-first development | Low (zero/low-code surface; API exists) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

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
| Last verified | 2026-09-30 | Official |

See the [ByteDance](/companies/bytedance/) company profile, the [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) model page, the [Ark API](/api/ark/) platform, and the site's [choosing-an-agent guide](/guides/choosing-an-agent/), [AI agents](/technology/ai-agents/), [tool calling](/technology/tool-calling/) and [MCP](/technology/mcp/) technology pages. For the structural reading of where Coze sits relative to the other bound platforms, see the research on [the agent ecosystem structure](/research/china-ai-agent-ecosystem-structure-and-gaps/).

*Labels used above: **Official fact** (from the Coze China site, documentation and Volcengine product pages), **Vendor-reported claim** (capability and pricing statements by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such). No third-party evaluation evidence is currently recorded for Coze-built agents.*
