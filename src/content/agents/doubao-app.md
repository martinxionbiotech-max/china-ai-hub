---
image: "/images/ai/agents-doubao-app.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: doubao-app
agent_name: Doubao
company: bytedance
description: "ByteDance's consumer AI assistant app (豆包) for life and work: Q&A and explanations, study help, office automation (documents, spreadsheets, PPT, data analysis, code), image and video creation (Seedream/Seedance models), voice calls, photo recognition and web search. 'Doubao Work' mode runs an autonomous planning/executing agent that operates a virtual desktop on the local computer to complete complex tasks, with real-time watching, pause and takeover; integrates with Feishu for enterprise context. Mainland-China-focused; overseas users are redirected to Dola."
agent_type: autonomous
underlying_models: []
tool_calling: true
computer_use: true
planning: true
pricing: "App Store CN: Basic free; Standard 68 CNY/month (688 CNY/yr); Enhanced 200 CNY/month (2,048 CNY/yr); Professional 500 CNY/month (5,088 CNY/yr). Quota-based; creation packs and cloud-storage expansion sold separately."
deployment: cloud
open_source: false
license: proprietary
documentation: https://www.doubao.com/
use_cases:
  - Daily Q&A, cooking help, concept learning, inspiration
  - Study help - explaining problems, grading homework, summarizing materials
  - Office automation - docs, spreadsheets, PPTs, data analysis, code generation
  - Agentic desktop automation (Doubao Work virtual desktop)
  - Voice-driven image editing (豆包 P 图) and image/video creation
  - Enterprise work via Feishu integration
limitations:
  - Chat LLM powering the consumer app is not named in fetched official pages (only creation models Seedream/Seedance are)
  - Region restriction - web access requires login outside mainland China; overseas users pointed to Dola (itself geo-restricted)
  - Membership is quota-based; creation packs expire and do not roll over
  - Android store listing not directly verified this run (iOS CN listing fetched)
  - App Store disclaimer - as an AI it may misunderstand or mislead; users advised to cross-check
  - No public consumer API; developer access to Doubao models is via Volcengine Ark
known_limitations:
  - "No public GitHub repository located as of 2026-09-27 (checked ByteDance org)"
last_verified: "2026-09-20"
sources:
  - source_name: Doubao official website
    source_url: https://www.doubao.com/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Doubao desktop download & features page
    source_url: https://www.doubao.com/download/desktop
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Apple App Store CN listing (Doubao)
    source_url: https://itunes.apple.com/search?term=%E8%B1%86%E5%8C%85&country=cn&entity=software
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Doubao paid-service agreement
    source_url: https://www.doubao.com/legal/ey01
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Volcengine Doubao LLM platform page
    source_url: https://www.volcengine.com/product/doubao
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**Short answer.** Doubao is ByteDance's consumer AI assistant app (豆包) — Q&A, study help, office automation, image/video creation via Seedream/Seedance — plus its "Doubao Work" autonomous desktop agent that operates a virtual desktop on the local computer. It is the demand-side complement to ByteDance's closed-API [Doubao Seed](/models/doubao-seed-2-1-pro/) models, mainland-China-focused and subscription-billed.

**Key facts.**

- Combines a consumer assistant (Q&A, study, office docs/spreadsheets/PPT/data/code) with creation models Seedream (image) and Seedance (video), plus voice calls, photo recognition and web search.
- "Doubao Work" mode runs a planning/executing agent on a local virtual desktop, with real-time watching, pause and takeover, and Feishu integration for enterprise context.
- Subscription tiers: Basic free; Standard 68 CNY/month (688/yr); Enhanced 200 CNY/month (2,048/yr); Professional 500 CNY/month (5,088/yr) — quota-based, with creation packs and cloud-storage sold separately.
- Mainland-China-focused; overseas users are redirected to Dola (itself geo-restricted), and web access outside mainland China requires login.
- No public consumer API — developer access to Doubao models is via [Volcengine Ark](/api/ark/) only.

**What this means.** Doubao is where ByteDance's closed model strategy meets consumers: the same Seed models Ark sells to developers are productized as a subscription the public pays for monthly, with the computer-use capability surfaced as a shipping desktop mode rather than a developer SDK.

**What is uncertain.** The chat LLM powering the consumer assistant is not named in official pages (only creation models Seedream/Seedance are), and the Android store listing was not directly verified this run. Exact quota math per tier and whether Doubao Work ships outside mainland China are not publicly documented.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-doubao-app-1 | Doubao official website | https://www.doubao.com/ | Official | — | 2026-09-20 | high | — |
| src-agents-doubao-app-2 | Doubao desktop download & features page | https://www.doubao.com/download/desktop | Official | — | 2026-09-20 | high | — |
| src-agents-doubao-app-3 | Apple App Store CN listing (Doubao) | https://itunes.apple.com/search?term=%E8%B1%86%E5%8C%85&country=cn&entity=software | Official | — | 2026-09-20 | high | — |
| src-agents-doubao-app-4 | Doubao paid-service agreement | https://www.doubao.com/legal/ey01 | Official | — | 2026-09-20 | high | — |
| src-agents-doubao-app-5 | Volcengine Doubao LLM platform page | https://www.volcengine.com/product/doubao | Official | — | 2026-09-20 | high | — |

## Why it matters

Doubao is the demand-side half of ByteDance's closed-model strategy, and the database's clearest case of a consumer surface built on models with no open weights. Where Ark sells Doubao Seed models to developers through an API, Doubao App sells their *output* to consumers through a subscription and a computer-use desktop mode — two routes to the same underlying models, one token-billed and one quota-billed.

China AI Hub analysis indicates Doubao's structural role is consumer distribution: it demonstrates that ByteDance's Seed models are productized for mainstream users, while [computer use](/technology/computer-use/) appears in a shipping consumer surface rather than only in a developer SDK. The un-named chat LLM is itself a signal — ByteDance is willing to document its *creation* models (Seedream, Seedance) but not the model behind the assistant's conversational core, reinforcing the closed posture that distinguishes it from open-weight rivals like DeepSeek and Qwen.

## How it differs from the other autonomous agents

Doubao occupies a different cell from the autonomous agents that ship to developers and teams.

- **[AutoGLM](/agents/autoglm/)** is an open phone-use agent — a framework and VLM anyone can run or license, research-only, with no consumer subscription.
- **[Manus](/agents/manus/)** is a closed cloud general agent sold as a subscription to do whole tasks, but is a *third-party product* with an undisclosed model supply chain.
- **Doubao** is a first-party consumer assistant plus a desktop agent, bound to ByteDance's own models end-to-end, distributed through the App Store and mainland-China web rather than a CLI or API.

China AI Hub analysis: Doubao is the only one of the three that is simultaneously a consumer app, a desktop agent, and a first-party model surface. AutoGLM and Manus compete on agent capability; Doubao competes on distribution — it inherits ByteDance's consumer reach and Feishu enterprise channel, which no open framework or independent agent can match.

## Practical implications

**For consumers.** Doubao is the "assistant plus creation suite" bundle — Q&A, study help, office automation, and Seedream/Seedance image/video generation under one quota-based subscription, with Doubao Work adding hands-off desktop automation. The quota system means heavy creation use exhausts a tier and requires top-ups; creation packs expire and do not roll over.

**For enterprises.** Feishu integration is the documented path for using Doubao in a work context; there is no consumer API to build against — teams needing programmatic access to the same models must go through [Volcengine Ark](/api/ark/), which is a separate, developer-facing channel.

**For evaluators.** The App Store's own disclaimer — the AI "may misunderstand or mislead" — is a vendor's explicit reliability caveat, and the un-named chat model means the assistant's conversational capability cannot be tied to a specific tracked model for comparison.

## What the evidence shows

The evidence is strongest on the product surface and weakest on the model internals. Official pages document the feature set (Q&A, study, office, creation, voice, photo, search), the Doubao Work desktop agent with real-time watch/pause/takeover, the Feishu integration, and the subscription tiers (68/200/500 CNY/month). The iOS App Store listing corroborates the pricing and adds the disclaimer that Doubao is geo-scoped to mainland China, with overseas users redirected to Dola.

The gap is the conversational core. The chat LLM behind the assistant is not named in any fetched official page — only the creation models (Seedream, Seedance) are — and there is no public GitHub repository (verified against ByteDance's org on 2026-09-27). China AI Hub analysis indicates this is a deliberate asymmetry: ByteDance discloses the models tied to *media generation* (where it wants to signal capability) while keeping the model behind the *assistant's reasoning* unnamed, which both protects the closed-API posture and makes Doubao's assistant quality impossible to benchmark against a named model.

## Where this fits

| Workload | Relevance |
|---|---|
| Consumer Q&A, study help, inspiration | High |
| Office automation (docs, spreadsheets, PPT, data, code) | High |
| Image / video creation (Seedream / Seedance) | High |
| Agentic desktop automation (Doubao Work) | High |
| Enterprise work via Feishu | High |
| Developer / programmatic access | Low (no consumer API; via Ark) |
| Overseas / non-mainland-China use | Low (redirected to Dola) |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | Not publicly documented (chat LLM unnamed; creation models Seedream/Seedance) | Official |
| Target users | Mainland-China consumers | Official |
| Platform | Mobile app, desktop app (Doubao Work virtual desktop), web | Official |
| OS | iOS, Android, desktop | Official |
| Browser / computer use | Computer use (Doubao Work virtual desktop) | Vendor-reported |
| Coding | Not publicly documented | Not publicly documented |
| Autonomous task execution | Yes (Doubao Work planning/executing agent) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes | Official |
| Memory | Not publicly documented | Not publicly documented |
| Workflow | Autonomous planning/executing on a virtual desktop with real-time watch/pause/takeover | Vendor-reported |
| API | No public consumer API (developer access via [Volcengine Ark](/api/ark/)) | Official |
| Pricing | Basic free; 68/200/500 CNY per month | Vendor-reported |
| Region | Mainland China (overseas redirected to Dola) | Official |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Region-restricted; quota-based membership; creation packs expire | Official |
| Source | [Doubao website](https://www.doubao.com/) | Official |
| Last verified | 2026-09-20 | Official |

See the [ByteDance](/companies/bytedance/) company profile, the [Volcengine Ark](/api/ark/) platform, the [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/) model, and the site's [computer use](/technology/computer-use/) and [multimodal AI](/technology/multimodal-ai/) technology pages.

*Labels used above: **Official fact** (from the Doubao website and App Store listing), **Vendor-reported claim** (capability and pricing statements by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such).*
