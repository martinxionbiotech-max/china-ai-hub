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
**Short answer.** MiniMax Agent is MiniMax's cloud agent platform at agent.minimax.io — a web app with Skills, Schedules, Websites, Research and AI PPT capability areas, plus always-on cloud agents MaxClaw and MaxHermes. It is the closed, subscription-facing counterpart to the open-source [MiniMax Code](/agents/minimax-code/), built on the same [MiniMax-M3](/models/minimax-m3/) / [M2.7](/models/minimax-m27/) models.

**Key facts.**

- A managed web-app platform (Skills, Schedules, Websites, Research, AI PPT) with persistent memory and evolving skills — a *product* layer over MiniMax's M-series models, not a new model capability.
- Two always-on cloud agents: MaxClaw (a 24/7 personal assistant reachable from daily apps including Telegram) and MaxHermes (Beta, a self-evolving agent that unlocks new skills from completed complex tasks).
- Billed via MiniMax Token Plan subscriptions: Plus $22 / Max $55 / Ultra $132 per month, with 5-hour rolling and weekly quota windows; overflow credits at 1,000 credits = $1.
- Cloud-hosted only; no self-host option documented, and no public GitHub repository (verified against MiniMax-AI on 2026-09-27).
- Web-app plan and pricing details require sign-in and were not retrievable from fetched sources.

**What this means.** MiniMax runs a two-sided agent strategy on one model family: the open CLI ([MiniMax Code](/agents/minimax-code/)) captures developers, while MiniMax Agent captures non-developers through subscriptions and always-on assistants — using subscription pricing rather than API pricing to monetize the same M-series capability.

**What is uncertain.** The first release date is not publicly disclosed, MaxHermes is in Beta, and the relationship between the web app, MaxClaw/MaxHermes and MiniMax Code is not explained in any single fetched document. Web-app plan details sit behind sign-in.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-minimax-agent-1 | MiniMax Agent homepage | https://agent.minimax.io/ | Official | — | 2026-09-20 | high | — |
| src-agents-minimax-agent-2 | MiniMax Agent docs index (llms.txt) | https://agent.minimax.io/docs/llms.txt | Official documentation | — | 2026-09-20 | high | — |
| src-agents-minimax-agent-3 | MiniMax Token Plan pricing guide | https://platform.minimax.io/docs/guides/pricing-token-plan | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

MiniMax Agent is the managed-consumption side of MiniMax's dual strategy, and the clearest case in the database of a vendor splitting one model family across an open CLI and a closed cloud platform. Its value proposition — persistent memory, evolving skills, always-on assistants — is a *product* layer on top of MiniMax-M3's capability, monetized by subscription rather than tokens.

China AI Hub analysis indicates MiniMax Agent matters as evidence of how a Chinese lab productizes one model family across two surfaces: [MiniMax Code](/agents/minimax-code/) is the open, developer-facing front-end, while MiniMax Agent is the closed, subscription-facing front-end for the same underlying M-series models. The self-evolving MaxHermes (Beta) is the forward-looking bet — an agent that grows capabilities from completed tasks — but its Beta status means the "evolving" claim is aspirational rather than independently verified.

## How it differs from MiniMax Code

The two MiniMax agents are complementary surfaces over one model family, not competitors.

- **[MiniMax Code](/agents/minimax-code/)** is the open-source (MIT) developer surface — a desktop app and CLI (mcode) for coding, everyday workflows, automation and remote collaboration, with MCP, memory, Agent Team and a terminal coding agent.
- **MiniMax Agent** is the closed cloud surface — a web app of capability areas (Skills, Schedules, Websites, Research, AI PPT) plus always-on assistants MaxClaw/MaxHermes, targeting non-developers and daily users.

China AI Hub analysis: MiniMax Code is where MiniMax earns developer credibility (open code, MCP, ACP), and MiniMax Agent is where it captures non-developer demand (subscription, memory, always-on assistants). The two are the same company answering "how do we monetize M3/M2.7" twice — once with an open CLI and once with a closed product — and the split itself is the strategy: no single surface has to serve both audiences.

## Practical implications

**For non-developers.** MiniMax Agent is the subscription path to MiniMax's models without touching a CLI — Skills, Schedules, Websites, Research and AI PPT are pre-built capability areas, and MaxClaw is an always-on assistant reachable from Telegram. The cost is cloud lock-in and a quota system (5-hour rolling + weekly).

**For teams evaluating the ecosystem.** The docs do not explain in one place how the web app, MaxClaw, MaxHermes and MiniMax Code relate, so a buyer must assemble the picture from multiple pages. Web-app pricing sits behind sign-in — a friction point for pre-purchase evaluation.

**For evaluators.** There is no public GitHub repository and no documented self-host path, so independent inspection of how the "persistent memory" and "evolving skills" actually work is not possible from public sources.

## What the evidence shows

The evidence is strong on the product surface and the pricing, and weak on internals. The homepage and llms.txt index document the capability areas (Skills, Schedules, Websites, Research, AI PPT), the MaxClaw/MaxHermes assistants, and the "Minimize Effort, Maximize Intelligence" positioning; the Token Plan guide fixes the $22/$55/$132 tiers and the 1,000-credits=$1 overflow rate.

The gaps are structural opacity. No release date is disclosed, the web-app pricing is behind sign-in, MaxHermes is Beta, and the ecosystem's internal relationships are not explained in a single doc. China AI Hub analysis indicates this opacity is the honest cost of the closed-product strategy: unlike MiniMax Code (which anyone can inspect on GitHub), MiniMax Agent's "persistent memory" and "self-evolution" are vendor-reported claims that cannot be independently checked from public sources, so buyers must evaluate them on trial rather than documentation.

## Where this fits

| Workload | Relevance |
|---|---|
| Office / Finance / Coding Expert Collection areas | High |
| Deep research and website tasks | High |
| AI PPT and multimodal creation | High |
| 24/7 always-on assistant (MaxClaw, Telegram) | High |
| Self-evolving assistant (MaxHermes, Beta) | Moderate (Beta) |
| Self-hosted deployment | None (cloud-only) |
| Independent inspection of memory/evolution internals | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | [MiniMax-M3](/models/minimax-m3/), [MiniMax-M2.7](/models/minimax-m27/) | Official |
| Target users | Non-developers and daily users (web app) | Official |
| Platform | Web app (agent.minimax.io); always-on cloud agents MaxClaw/MaxHermes | Official |
| OS | Not publicly documented (cloud web app) | Not publicly documented |
| Browser / computer use | Not publicly documented | Not publicly documented |
| Coding | Not publicly documented | Not publicly documented |
| Autonomous task execution | Yes (always-on cloud agents; self-evolution) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes | Official |
| Memory | Yes (persistent memory) | Official |
| Workflow | Skills, Schedules, Websites, Research, AI PPT capability areas | Official |
| API | Not publicly documented | Not publicly documented |
| Pricing | Token Plan: Plus $22 / Max $55 / Ultra $132 per month | Vendor-reported |
| Region | Not publicly documented | Not publicly documented |
| Open-source | No — proprietary | Official |
| Deployment | Cloud | Official |
| Limitations | Cloud-hosted only; MaxHermes in Beta; web pricing needs sign-in | Official |
| Source | [MiniMax Agent homepage](https://agent.minimax.io/) | Official |
| Last verified | 2026-09-20 | Official |

See the [MiniMax](/companies/minimax/) company profile, the [MiniMax-M3](/models/minimax-m3/) model, the open-source [MiniMax Code](/agents/minimax-code/) counterpart, the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [AI agents](/technology/ai-agents/) technology page.

*Labels used above: **Official fact** (from the MiniMax Agent homepage and Token Plan pricing guide), **Vendor-reported claim** (capability and pricing statements by MiniMax), and **China AI Hub analysis** (our synthesis, always introduced as such).*
