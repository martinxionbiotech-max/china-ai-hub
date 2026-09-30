---
image: "/images/ai/agents-autoglm.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: autoglm
agent_name: AutoGLM
company: zhipu-ai
description: "Zhipu AI's open-source phone-use autonomous agent (repo Open-AutoGLM). The VLM sees the phone screen, plans a chain-of-thought action sequence, and executes it via ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). First phone agent with true Phone Use capabilities (2024-10-25); AutoGLM 2.0 commercial product runs agents in cloud virtual phones. Research/learning use."
agent_type: autonomous
underlying_models: []
framework: "Python framework (PhoneAgent API + CLI); model AutoGLM-Phone-9B built on the GLM-4.1V-9B family"
tool_calling: true
computer_use: true
memory: false
planning: true
api: true
pricing: "Open-source framework free. AutoGLM-Phone API (BigModel model id autoglm-phone) limited-time free as of 2026-09-20; paid price after promotion not publicly disclosed."
deployment: both
open_source: true
license: "Apache-2.0 (code); MIT (models)"
github: https://github.com/zai-org/Open-AutoGLM
documentation: https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md
use_cases:
  - Food delivery ordering and reordering
  - Product purchase and cross-platform price comparison
  - Travel planning (routes, flights/trains, hotels)
  - News, music, video playback and social interactions
  - Cloud-phone batch operations - notifications, likes, customer-service and attendance workflows
  - AI-native phone research and GUI agent development
limitations:
  - Research/learning use only; prohibited for illegal information gathering
  - Sensitive pages (payment, password, banking) cannot be screenshotted - agent auto-detects and requests human takeover
  - Android 7.0+ with developer mode + USB debugging required; ADB Keyboard needed for Android text input
  - iOS support requires separate WebDriverAgent setup
  - Local deployment needs ~24GB+ VRAM GPU
  - No persistent-memory feature documented in the README
last_verified: "2026-09-20"
sources:
  - source_name: Open-AutoGLM GitHub repository
    source_url: https://github.com/zai-org/Open-AutoGLM
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: AutoGLM Goes Open Source blog
    source_url: https://autoglm.z.ai/blog
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: AutoGLM-Phone model card (Hugging Face)
    source_url: https://huggingface.co/zai-org/AutoGLM-Phone-9B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: BigModel AutoGLM-Phone API docs
    source_url: https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**Short answer.** AutoGLM is Zhipu AI's open-source phone-use agent: a vision-language model (AutoGLM-Phone-9B, from the GLM-4.1V-9B family) reads the phone screen, plans a chain-of-thought action sequence, and executes it over ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). It was the first phone agent with true Phone Use capabilities (2024-10-25) and is research/learning-licensed.

**Key facts.**

- Ships as a Python framework (PhoneAgent API + CLI) built around AutoGLM-Phone-9B; the commercial AutoGLM 2.0 product runs the same approach on cloud virtual phones.
- Execution spans ADB (Android), HDC (HarmonyOS NEXT) and WebDriverAgent (iOS), with remote ADB over Wi-Fi/network for flexible control.
- Free framework under Apache-2.0 (code) and MIT (models); the hosted `autoglm-phone` API on BigModel was limited-time free as of 2026-09-20.
- Auto-detects sensitive screens (payment, password, banking) and requests human takeover; login and CAPTCHA scenarios support manual takeover.
- Local deployment needs roughly 24GB+ VRAM; Android use requires developer mode + USB debugging (plus ADB Keyboard for text input).

**What this means.** AutoGLM makes phone-level computer use an *open, inspectable* capability in China's ecosystem — the same GUI-operation primitive that ByteDance's Doubao "Work" mode and Butterfly Effect's Manus productize, but shipped as a model-plus-framework anyone can run locally or license for research.

**What is uncertain.** The paid price of the AutoGLM-Phone API after its promotional period is not publicly disclosed, and no persistent-memory feature is documented in the README. Independent evaluation of its task-completion reliability across the three OS backends (ADB/HDC/WebDriverAgent) is not recorded in this database.

**Sources.**

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-agents-autoglm-1 | Open-AutoGLM GitHub repository | https://github.com/zai-org/Open-AutoGLM | Official documentation | — | 2026-09-20 | high | — |
| src-agents-autoglm-2 | AutoGLM Goes Open Source blog | https://autoglm.z.ai/blog | Official | — | 2026-09-20 | high | — |
| src-agents-autoglm-3 | AutoGLM-Phone model card (Hugging Face) | https://huggingface.co/zai-org/AutoGLM-Phone-9B | Model card | — | 2026-09-20 | high | — |
| src-agents-autoglm-4 | BigModel AutoGLM-Phone API docs | https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md | Official documentation | — | 2026-09-20 | high | — |

## Why it matters

AutoGLM is the purest demonstration of [computer use](/technology/computer-use/) as a *model capability* rather than a wrapper product. Its entire function — reading a screen, planning an action sequence, tapping — is downstream of the AutoGLM-Phone-9B VLM's grounding and planning quality; there is no separate tool registry or orchestration layer doing the work. That makes it the reference case for how GUI automation depends on vision-model grounding, a relationship the database captures by binding the agent to Zhipu AI while the GLM-4.1V-9B lineage itself sits outside the tracked flagship models.

China AI Hub analysis indicates AutoGLM matters less as a production tool (it is research/learning-licensed, with sensitive-screen handoff by design) and more as the clearest evidence that phone-level computer use is technically mature in China's *open* ecosystem — a capability ByteDance's Doubao and Butterfly Effect's Manus keep behind closed surfaces. The open release lowers the cost for any team to study or build GUI agents on the GLM VLM stack.

## How it differs from Manus

AutoGLM and [Manus](/agents/manus/) both "operate a screen," but they are opposite bets on the same primitive.

- **Manus** is a closed, cloud-only general agent — a subscription product that does whole tasks (slides, websites, research, email/Slack) across a browser and files, with its underlying model orchestration undisclosed.
- **AutoGLM** is an open, model-specific phone agent — a framework and 9B VLM you can run locally or license, scoped to phone GUI operation across three mobile OS backends, research/learning-only.

China AI Hub analysis: the difference is openness-versus-product and phone-versus-browser. Manus trades transparency for a polished, general, subscription surface; AutoGLM trades polish and generality for an open, inspectable, phone-specific substrate. A team wanting a deployable general assistant buys Manus; a team wanting to study or build phone automation on an open VLM starts from AutoGLM.

## Practical implications

**For researchers.** AutoGLM is the reference open implementation of a phone-use agent — screen perception → chain-of-thought planning → action execution over ADB/HDC/WebDriverAgent, with remote ADB for Wi-Fi/network control. The setup costs are ~24GB+ VRAM locally plus per-OS backend tooling (developer mode, USB debugging, ADB Keyboard; a separate WebDriverAgent setup for iOS).

**For product teams.** The commercial AutoGLM 2.0 runs the same approach on cloud virtual phones, so a team can validate phone-agent value without managing physical devices; the hosted `autoglm-phone` API was free during its promotional period as of 2026-09-20.

**For evaluators.** Sensitive-screen auto-detection and human takeover are a *safety* feature, not a capability gap — but they also mean AutoGLM's autonomy is deliberately bounded around payment/password/banking surfaces, so end-to-end "finish a purchase" tasks stop at the handoff rather than completing unattended.

## What the evidence shows

The evidence is strong on *what* AutoGLM is and thin on *how well* it generalizes. The GitHub repo and blog document the architecture (VLM screen perception + planning + ADB/HDC/WebDriverAgent execution), the first-Phone-Use claim (2024-10-25), the sensitive-screen handoff, and the research/learning license; the Hugging Face model card confirms AutoGLM-Phone-9B's GLM-4.1V-9B lineage. The repo has also expanded past the core framework — a WeChat community, a Zhipu AI input-method (Autotyper) product and a Midscene.js integration — showing the phone-agent surface growing beyond the README's original scope.

What is missing is independent reliability data. No third-party benchmark of AutoGLM's task-completion rate across the three OS backends is recorded here, and no persistent-memory feature is documented — a boundary the README leaves explicit. China AI Hub analysis indicates the honest reading is "capability demonstrated and open," not "reliability independently proven": the availability evidence (repo, model card, API) precedes any reliability evidence, and buyers should treat the sensitive-screen handoff as a fixed constraint rather than a setting they can turn off.

## Where this fits

| Workload | Relevance |
|---|---|
| Phone GUI automation research (screen → plan → action) | High |
| Cloud-phone batch operations (AutoGLM 2.0) | High |
| Local phone-agent deployment (ADB/HDC/WebDriverAgent) | High |
| Payment/password/banking flows | Low (auto human-takeover by design) |
| General-purpose, non-phone task execution | Low (phone-scoped, research-licensed) |
| Independent reliability evaluation | No evidence recorded |

*Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.*

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | AutoGLM-Phone-9B (GLM-4.1V-9B family) | Official |
| Target users | Researchers and developers (research/learning use) | Official |
| Platform | Python framework (PhoneAgent API + CLI); AutoGLM 2.0 cloud product | Official |
| OS | Android (ADB), HarmonyOS NEXT (HDC), iOS (WebDriverAgent) | Official |
| Browser / computer use | Phone GUI computer use | Vendor-reported |
| Coding | Not publicly documented | Not publicly documented |
| Autonomous task execution | Yes (chain-of-thought planning) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes | Official |
| Memory | No | Official |
| Workflow | Screen reading → chain-of-thought planning → action execution | Vendor-reported |
| API | Yes (BigModel `autoglm-phone`) | Official |
| Pricing | Framework free; API limited-time free as of 2026-09-20 | Vendor-reported |
| Region | China (BigModel) | Official |
| Open-source | Yes — Apache-2.0 (code), MIT (models) | Official |
| Deployment | Cloud and self-hosted | Official |
| Limitations | Research/learning only; ~24GB+ VRAM for local; sensitive screens need human takeover | Official |
| Source | [Open-AutoGLM GitHub](https://github.com/zai-org/Open-AutoGLM) | Official |
| Last verified | 2026-09-20 | Official |

See the [Zhipu AI](/companies/zhipu-ai/) company profile, the [Manus](/agents/manus/) general agent, the [choosing-an-agent guide](/guides/choosing-an-agent/), and the site's [computer use](/technology/computer-use/) and [AI agents](/technology/ai-agents/) technology pages.

*Labels used above: **Official fact** (from the Open-AutoGLM GitHub repo, AutoGLM blog and model card), **Vendor-reported claim** (capability and pricing statements by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such). No independent evaluation of AutoGLM's phone-task reliability is currently recorded.*
