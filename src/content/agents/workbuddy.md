---
agent_id: workbuddy
agent_name: WorkBuddy
company: tencent
description: "WorkBuddy is Tencent's all-scenario AI office agent — a desktop workbench launched 9 March 2026 on the CodeBuddy architecture. It plans and executes multi-step tasks, operates local files with permission, and delivers finished documents, spreadsheets and slides. It is model-neutral by design (Hunyuan, GLM, Kimi, MiniMax and DeepSeek are all built in), compatible with the OpenClaw skill format, and connected to WeChat, WeCom, QQ, Feishu and DingTalk for remote control."
agent_type: enterprise
underlying_models:
  - Hunyuan Hy4 preview
  - GLM-5.3
  - GLM-5.3-Flash
  - GLM-5.2
  - MiniMax-M3
  - MiniMax-M2.7
  - Kimi K3
  - Kimi K2.7 Code
  - Kimi K2.6
  - DeepSeek-V4-Pro
framework: "Desktop agent client for Windows, macOS, HarmonyOS PC and Linux (UOS/Kylin), built on Tencent's CodeBuddy architecture. Task execution runs locally in a sandbox; models are routed either to built-in cloud models or to a user-configured OpenAI-compatible endpoint. Extensible through Buddy apps, experts, skills (OpenClaw-compatible), connectors and MCP."
tool_calling: true
browser_use: null
computer_use: false
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "Free tier: 500 credits/month. Standard ¥99/month (2,000 base + 2,000 bonus credits). Advanced ¥199/month (4,000 + 5,000). Flagship ¥999/month (20,000 + 30,000). Buddy One VIP ¥999–1,399/month with a 50,000-credit pool shared across WorkBuddy, Tencent Docs, ima and Tencent Drive. Enterprise pricing quoted separately."
deployment: cloud
open_source: false
license: proprietary
github: null
documentation: https://www.workbuddy.cn/docs/workbuddy/Overview
use_cases:
  - Multi-step office work that ends in a finished file — documents, spreadsheets, slide decks, formatted data
  - Batch reading and processing of local files after folder authorisation
  - Deep research with cross-source checking and structured report output
  - Scheduled and recurring tasks (daily briefs, report generation)
  - Remote task dispatch from WeChat, WeCom, QQ, Feishu or DingTalk
  - Enterprise agent deployment through the WorkBuddy Managed Agents API, with versioned agents and A/B routing
  - Reuse of OpenClaw-format skills and community skill packages
limitations:
  - No built-in GUI or browser control — browser work depends on the Agent Browser skill, not a core operator
  - Desktop-first; the mobile app can dispatch tasks but cannot operate desktop files
  - Cloud-delivered service — no open-source or self-hosted edition, though a VPC edition is offered to enterprises
  - With the built-in models, inputs and outputs are processed in the cloud; only a custom-model configuration keeps content off Tencent's side
  - Hy3 ships as a built-in model but is not yet tracked in this database's model index (Hy4 preview is)
  - No independent evaluation of task-completion quality is recorded
  - Skill quality is uneven at the platform's 200,000-listing scale; skill-scanner reduces but does not eliminate the risk of a malicious package
last_verified: "2026-10-31"
sources:
  - source_name: WorkBuddy official site (China)
    source_url: https://www.workbuddy.cn/
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: WorkBuddy product documentation
    source_url: https://www.workbuddy.cn/docs/workbuddy/Overview
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: WorkBuddy model configuration documentation
    source_url: https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: WorkBuddy pricing
    source_url: https://www.workbuddy.cn/pricing/
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: WorkBuddy Enterprise — Managed Agents API (Tencent Cloud documentation)
    source_url: https://cloud.tencent.com/document/product/1831/138581
    source_type: cloud_doc
    published_date: "2026-09-23"
    last_verified: "2026-10-31"
    confidence: high
  - source_name: WorkBuddy open platform
    source_url: https://open.workbuddy.cn/
    source_type: official
    last_verified: "2026-10-31"
    confidence: high
  - source_name: 央广网 — 腾讯汤道生：以开放生态打造全场景Agent生产力系统 (Tencent Digital Ecosystem Summit, 29 Oct 2026)
    source_url: https://tech.cnr.cn/techgd/20261029/t20261029_527856346.shtml
    source_type: industry_media
    published_date: "2026-10-29"
    last_verified: "2026-10-31"
    confidence: high
  - source_name: 极目新闻 — 腾讯版"小龙虾"来了！WorkBuddy正式上线 (launch report, 10 Mar 2026)
    source_url: https://www.ctdsb.net/c1476_202603/2681903.html
    source_type: industry_media
    published_date: "2026-03-10"
    last_verified: "2026-10-31"
    confidence: medium
---

**Short answer.** WorkBuddy is Tencent's desktop AI workbench: you describe a task, it plans and executes the steps on your own machine, and it hands back a finished file. It launched on 9 March 2026, runs on the CodeBuddy architecture, and is unusual in two respects — it ships with models from five different Chinese labs rather than only Tencent's own, and it was built to accept the OpenClaw skill format from day one.

**Key facts.**

- Launched 9 March 2026; built on Tencent's CodeBuddy architecture; free to install, credits-based to use.
- Runs on Windows, macOS (Intel and ARM), HarmonyOS PC and Linux (UOS/Kylin), with iOS and Android clients that can dispatch tasks remotely.
- Task execution happens locally in a sandbox, after the user grants folder access; output is a document, spreadsheet, slide deck or dataset rather than a chat reply.
- Fourteen built-in models across five vendors: Hunyuan Hy4 preview and Hy3, five GLM variants, two MiniMax, three Kimi and two DeepSeek. Users can also attach any OpenAI-compatible endpoint as a custom model.
- Compatible with the OpenClaw skill system; the open platform lists five extensibility types (Buddy apps, experts, skills, connectors, hardware) and claims 200,000+ skills available.
- Remote control from WeChat, WeCom, QQ, Feishu and DingTalk — the WeCom path is documented as roughly a one-minute setup.
- Enterprise: a Managed Agents API (API 3.0, 2026-07-09) with versioned agents, weighted routing between versions, sessions, and A2A binding of external agents.
- As of 29 October 2026 Tencent reports the enterprise edition in 50+ industries, covering 50% of the China Top 500 and 60% of the Top 100.

**What this means.** Tencent built an agent that routes to its competitors' models and adopted a rival open-source skill format rather than inventing one. Both choices point the same way: the product is a distribution and governance layer, not a model bet.

**What is uncertain.** Enterprise pricing is not published. No independent evaluation of output quality exists. Whether the international edition (workbuddy.ai) carries the same model roster is unverified. The relative weight of Tencent's own Hunyuan models in default routing is not disclosed.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-workbuddy-1 | WorkBuddy official site (China) | https://www.workbuddy.cn/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-2 | WorkBuddy product documentation | https://www.workbuddy.cn/docs/workbuddy/Overview | Official documentation | — | 2026-10-31 | high | — |
| src-agents-workbuddy-3 | WorkBuddy model configuration documentation | https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model | Official documentation | — | 2026-10-31 | high | — |
| src-agents-workbuddy-4 | WorkBuddy pricing | https://www.workbuddy.cn/pricing/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-5 | WorkBuddy Enterprise Managed Agents API | https://cloud.tencent.com/document/product/1831/138581 | Cloud documentation | 2026-09-23 | 2026-10-31 | high | — |
| src-agents-workbuddy-6 | WorkBuddy open platform | https://open.workbuddy.cn/ | Official | — | 2026-10-31 | high | — |
| src-agents-workbuddy-7 | 央广网 — Tencent Digital Ecosystem Summit report | https://tech.cnr.cn/techgd/20261029/t20261029_527856346.shtml | Industry media | 2026-10-29 | 2026-10-31 | high | — |
| src-agents-workbuddy-8 | 极目新闻 — WorkBuddy launch report | https://www.ctdsb.net/c1476_202603/2681903.html | Industry media | 2026-03-10 | 2026-10-31 | medium | Launch-day details (2,000 internal users, 5,000 sign-up credits) differ from later official figures |

## Why it matters

WorkBuddy is the first entry in this database where a Chinese lab ships an agent that **runs on its competitors' models by default**. Tencent's own Hunyuan models are present — Hy4 preview and Hy3 sit at the top of the official list — but so do GLM-5.3, Kimi K3, MiniMax-M3 and DeepSeek-V4-Pro. A customer can buy Tencent's workbench and never touch Tencent's model.

That is not a concession. China AI Hub analysis indicates it is the correct move for a company whose real asset is distribution: Tencent owns WeChat and WeCom, and an agent that only ran Hunyuan would be competing on model quality against labs that are currently faster; an agent that runs anything can monetise every one of them through the same desktop and the same enterprise contract.

The second structural fact is the skill format. WorkBuddy accepts OpenClaw skills. Instead of building an ecosystem from an empty shelf, Tencent inherited one at launch, and by October the open platform was reporting 200,000+ skills. China AI Hub analysis indicates this is the single most consequential decision in the product: agent platforms usually die of cold start — no skills means no use, no use means no skills — and Tencent skipped the cold start by adopting an external standard.

## The two bets, stated plainly

**Bet one: the workbench, not the model.** The product's value proposition is the last mile — operating local files, producing a real .docx or .pptx, running a scheduled task — not a benchmark score. The model is a swappable component with a 200K default context, three speed tiers (fast / balanced / max) and an adjustable thinking budget. Even the accounting reflects this: users buy credits, not tokens.

**Bet two: governance as the enterprise moat.** The enterprise features that Tencent leads with are not intelligence features. They are allow/ask/deny rules over file, command and network access; local sandbox execution; a `skill-scanner` that inspects a skill before installation; skill auditing by a security team rather than community self-policing; SSO; audit trails; and a VPC edition for data sovereignty. For a Chinese enterprise buyer, that list is the purchase order — a startup cannot supply it, and a model lab has no reason to build it.

China AI Hub analysis indicates these two bets are complementary rather than independent. A model-neutral agent needs governance to be trustworthy (you are routing corporate documents through five vendors' APIs); a governance story needs model neutrality to be credible (a procurement team will not accept a lock-in dressed as security). Each bet underwrites the other.

## How it differs from Manus, Yuanqi and the coding agents

- **[Manus](/agents/manus/)** is the general autonomous agent sold to consumers and teams, model-agnostic but explicitly opaque about which models it routes to, cloud-only, and with no enterprise governance layer. WorkBuddy is the same category of product with the opposite disclosure posture: the model list is published, and the governance layer is the sales pitch.
- **[Tencent Yuanqi](/agents/yuanqi/)** is Tencent's *other* agent product — no-code, Hunyuan-bound, distributed through WeChat official accounts. WorkBuddy and Yuanqi are a portfolio, not a replacement: Yuanqi sells reach inside WeChat, WorkBuddy sells a workbench on the desktop. China AI Hub analysis indicates Tencent is hedging the two plausible shapes of the agent market rather than committing to one.
- **[Kimi Code](/agents/kimi-code/)** and **[GLM Coding Plan](/agents/glm-coding-plan/)** are model-bound and coding-specific. WorkBuddy is broader (office, research, design, light development) and model-free, which is why it can list Kimi and GLM as components rather than competitors.
- **[Coze](/agents/coze/)** and **[Baidu AppBuilder](/agents/baidu-appbuilder/)** are build-a-bot platforms. WorkBuddy is a use-a-bot product with a platform attached — the platform (Buddy apps, experts, skills, connectors, hardware) exists to extend the desktop, not to replace it.

## Practical implications

**For buyers comparing it with Manus.** WorkBuddy is the enterprise-shaped option: published model roster, bring-your-own-model via an OpenAI-compatible endpoint, permission rules, audit, VPC, and an API for managed agents with version routing. The trade-offs are desktop-bound delivery and a China-first service posture.

**For teams that already run OpenClaw.** The skill compatibility is the reason to look. Existing skill packages can be reused, which lowers migration cost to near zero for the part of the stack that is hardest to rebuild.

**For developers.** The Managed Agents API is a genuine platform surface, not a thin wrapper: agents carry immutable versions, traffic is routed between versions by weight, manifests are capped at 256 KiB, and session message events are returned redacted — the reasoning trace is deliberately not exposed. That last detail matters for anyone planning to build evaluation on top of it.

**For anyone evaluating quality.** There is no independent benchmark. The vendor-reported enterprise numbers (50% of the China Top 500) measure adoption, not task success.

## What the evidence shows

The evidence is unusually strong for a product of this age, because Tencent documents it at three levels: the consumer product (site, pricing, help centre), the technical layer (model configuration, permission modes, sandbox), and the enterprise API (Tencent Cloud, API 3.0). The model roster, the pricing tiers, the credit mechanics, the permission model and the API shape are all primary-sourced.

Two claims rest on weaker ground. The "fully OpenClaw-compatible" statement comes from launch-day industry coverage rather than an official compatibility specification — no official page states the compatibility boundary, so what exactly carries over (skill manifest? tool schema? both?) is not documented. And the adoption figures are executive statements at a Tencent event, not audited disclosures.

China AI Hub analysis indicates the transparency itself is part of the strategy. A model-neutral workbench has to publish its model list to be credible; an enterprise governance product has to publish its permission model to be procurable. Where Manus's opacity follows from selling execution alone, WorkBuddy's disclosure follows from selling a layer that other companies' models and other companies' skills have to pass through.

## Where this fits

| Workload | Relevance |
|---|---|
| Multi-step office output (docx, xlsx, pptx) | High |
| Local file batch processing after authorisation | High |
| Scheduled / recurring report generation | High |
| Deep research with a written deliverable | High |
| Remote dispatch from Chinese IM platforms | High |
| Enterprise agent deployment with version routing | High |
| Whole-repo software development | Moderate (documented, but not the product's centre of gravity) |
| Browser or GUI automation as a core capability | Low (available as a skill, not built in) |
| Self-hosted deployment | Low (cloud service; VPC edition only) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## What this does not establish

- It does not establish that the OpenClaw skill format is fully portable in both directions; only that WorkBuddy accepts it.
- It does not establish output quality. No independent evaluation is recorded, and vendor adoption figures are not a quality measure.
- It does not establish that model neutrality improves results; it establishes that the choice is offered and documented.
- It does not establish that the international edition matches the China edition feature for feature.

See the [Tencent](/companies/tencent/) company profile, [Tencent Yuanqi](/agents/yuanqi/) for the group's other agent line, [Manus](/agents/manus/) for the consumer-facing alternative, and the site's [AI agents](/technology/ai-agents/) technology page.

*Labels used above: **Official fact** (WorkBuddy site, documentation, pricing, open platform, Tencent Cloud API docs), **Vendor-reported claim** (adoption and scale figures stated by Tencent executives), **Third-party** (launch-day industry coverage), and **China AI Hub analysis** (our synthesis, always introduced as such).*
