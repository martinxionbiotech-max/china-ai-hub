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
Doubao is ByteDance's consumer AI assistant app: Q&A and explanations, study help, office automation (documents, spreadsheets, PPT, data analysis, code), and image and video creation backed by the Seedream and Seedance models. It also supports voice calls, photo recognition and web search.

"Doubao Work" mode runs an autonomous planning-and-executing agent that operates a virtual desktop on the local computer, with real-time watching, pause and takeover, plus Feishu integration for enterprise context.

Doubao is mainland-China-focused (overseas users are redirected to Dola) and billed by subscription: Basic is free; paid tiers are 68 / 200 / 500 CNY per month with quota-based usage and separately sold creation packs. See the [ByteDance](/companies/bytedance/) profile.
