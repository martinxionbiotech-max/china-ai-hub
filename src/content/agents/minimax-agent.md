---
image: "/images/ai/agents-minimax-agent.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: minimax-agent
agent_name: MiniMax Agent
company: minimax
description: "MiniMax's cloud agent platform at agent.minimax.io ('Minimize Effort, Maximize Intelligence'). Web app with Skills, Schedules, Websites, Research and AI PPT capability areas, persistent memory and evolving skills; includes always-on cloud agents MaxClaw ('Your 24/7 personal assistant', accessible in daily apps incl. Telegram) and MaxHermes (Beta, 'An Agent That Grows With You', self-evolution via unlocked skills). Billed via MiniMax Token Plan."
agent_type: platform
underlying_models:
  - minimax-m3
  - minimax-m2.7
tool_calling: true
memory: true
planning: true
multi_agent: true
pricing: "Token Plan subscriptions: Plus $22/mo, Max $55/mo, Ultra $132/mo (5-hour rolling + weekly quota); credits 1,000 = $1. Web-app plan/pricing details require sign-in and are not publicly disclosed from fetched sources."
deployment: cloud
open_source: false
license: proprietary
documentation: https://agent.minimax.io/docs/llms.txt
use_cases:
  - Office, Finance and Coding 'Expert Collection' work areas
  - Deep research and website tasks
  - AI PPT and multimodal creation
  - 24/7 cloud assistant accessible in daily apps (MaxClaw, Telegram)
  - Self-evolving assistant that unlocks new skills from completed complex tasks (MaxHermes)
limitations:
  - Cloud-hosted only; no self-host option documented
  - First release date not publicly disclosed in fetched sources
  - Web-app plan/pricing details require sign-in (not retrievable)
  - MaxHermes is in Beta
  - Relationship between the web app, MaxClaw/MaxHermes and MiniMax Code is not explained in a single fetched doc (treated as an ecosystem of surfaces)
known_limitations:
  - "No public GitHub repository located as of 2026-09-27 (checked MiniMax-AI org)"
last_verified: "2026-09-20"
sources:
  - source_name: MiniMax Agent homepage
    source_url: https://agent.minimax.io/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Agent docs index (llms.txt)
    source_url: https://agent.minimax.io/docs/llms.txt
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax Token Plan pricing guide
    source_url: https://platform.minimax.io/docs/guides/pricing-token-plan
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**What it is.** MiniMax Agent is MiniMax's cloud agent platform at agent.minimax.io, with Skills, Schedules, Websites, Research and AI PPT capability areas plus always-on cloud agents. **Why it matters.** It is MiniMax's managed, closed-surface counterpart to its open-source [MiniMax Code](/agents/minimax-code/) — the subscription path to its [MiniMax-M3](/models/minimax-m3/) / M2.7 models for non-developers. **Key characteristics.** Persistent memory and evolving skills; the always-on MaxClaw (24/7 assistant, reachable via Telegram) and self-evolving MaxHermes (Beta). **What a professional should know.** Cloud-hosted only (no self-host option documented), billed via Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132 per month), and web-app pricing details require sign-in.

MiniMax Agent is MiniMax's cloud agent platform at agent.minimax.io ("Minimize Effort, Maximize Intelligence"). The web app provides Skills, Schedules, Websites, Research and AI PPT capability areas with persistent memory and evolving skills. It includes always-on cloud agents: MaxClaw, a 24/7 personal assistant reachable from daily apps including Telegram, and MaxHermes (Beta), an agent that grows with you by unlocking new skills.

Billing runs on MiniMax Token Plan subscriptions (Plus $22 / Max $55 / Ultra $132 per month) with 5-hour rolling and weekly quota windows; overflow credits cost 1,000 credits = $1.

See the [MiniMax](/companies/minimax/) profile and the [MiniMax-M3](/models/minimax-m3/) model page.

## Why it matters

MiniMax Agent represents the managed-consumption side of MiniMax's dual strategy: [MiniMax Code](/agents/minimax-code/) is the open, developer-facing surface, while MiniMax Agent is the closed, subscription-facing surface for the same underlying M-series models. Its value proposition — persistent memory, evolving skills, always-on assistants — is a *product* layer on top of MiniMax-M3's capability, not a new model capability itself. China AI Hub analysis indicates MiniMax Agent matters as evidence of how a Chinese lab productizes one model family across both an open CLI and a closed cloud platform, using subscriptions rather than API pricing to capture non-developer demand.

*Labels used above: **Official fact** (from the MiniMax Agent homepage and Token Plan pricing guide), **Vendor-reported claim** (capability and pricing statements by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such).*
