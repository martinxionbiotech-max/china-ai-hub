# Doubao app research (fetched 2026-09-20)

Entity: Doubao (豆包) consumer AI assistant app — ByteDance. All facts below come from pages actually fetched on 2026-09-20; nothing is from memory.

## Sources used

1. https://www.doubao.com/ — web title + region-ban page (via browser; JS-rendered)
2. https://www.doubao.com/download/desktop — official desktop/web download & features page (browser)
3. https://www.doubao.com/download/mobile — official mobile download page (browser)
4. https://www.doubao.com/legal/ey01 — "豆包付费服务协议" (paid-service agreement, updated 2026-08-15, effective 2026-08-22)
5. https://itunes.apple.com/search?term=豆包&country=cn&entity=software — Apple App Store CN listing (trackId 6459478672)
6. https://www.volcengine.com/product/doubao — Volcengine (火山引擎) Doubao LLM platform page
7. https://seed.bytedance.com/en/ (and /en/seed2_1) — ByteDance Seed site
8. https://www.dola.com/security/region-restricted — Dola region page (reached via Doubao ban page)
9. https://docs.volcengine.com/docs/82379 — Ark docs home (B2B platform context)

Note: tavily_extract / tavily_search were out of quota and web_search was disabled during this run; browser + web_fetch were used instead.

## Product facts

- Official name (web): 「豆包」, title "豆包 - 字节跳动旗下 AI 智能助手" (Doubao — ByteDance's AI intelligent assistant). Source 1.
- Official mobile-download tagline: "抖音旗下AI智能助手" (AI intelligent assistant under Douyin). Source 3.
- App Store CN product name: "豆包 - 生活工作 AI 助手" (Doubao — Life & Work AI Assistant). Source 5.
- Operator: 北京春田知韵科技有限公司 (Beijing Chuntian Zhiyun Technology Co., Ltd.) and/or its affiliates — stated in paid-service agreement (source 4) and Apple artist field (source 5). Operator's ICP on official site: 京ICP备2023020373号-1 (source 2).
- iOS CN App Store first release date: 2023-08-24 (releaseDate field). Source 5.
- iOS CN current version 15.1.0, released 2026-09-15; min iOS 15.0; bundle id com.bot.doubao; category Productivity. Source 5.
- iOS CN rating: 4.65 avg across 4,412,482 ratings (as fetched). Source 5.
- Positioning (App Store): an always-ready AI assistant — explains unfamiliar info, answers questions, gives quick clear answers, simplifies complex problems; study + work + creativity companion. Source 5.

## Features & capabilities

From official App Store description (source 5):
- Q&A / explanations; cooking help; concept learning; inspiration; research, trip planning, life organization.
- Study/work: explains problems, grades homework, breaks down knowledge points; summarizes materials, analyzes data, writes code, generates documents and PPTs.
- 工作任务模式 (Work Task Mode): automated office experience, built-in Office and professional skills, understands requirements, auto-executes, supports scheduled tasks ("复杂工作一键托管").
- 「豆包 P 图」: voice-driven image editing — background swap, style transfer, creative edits in one sentence.
- Image and video generation; video made "based on Seedance model" with cinematic quality.
- Voice input and voice calls: accurate recognition, natural responses; photo recognition (拍照识图); web search (联网搜索); human-like voice output.

From official desktop download page (source 2) — "豆包全面升级，集成 AI 自动化工作能力":
- Desktop app + web version ("下载豆包桌面版" / "使用网页版").
- 豆包工作 (Doubao Work / Work Mode): AI "干活搭子" (working partner) that can operate a virtual desktop on your local computer to complete complex tasks; user watches in real time, can pause or take over at any time.
- Delivery: documents, spreadsheets, PPTs, images, videos, webpages, systems.
- AI 编辑 (AI editing): point at a location in a document/PPT/webpage/app and Doubao edits precisely.
- 飞书联动 (Feishu integration): query meeting conclusions, summarize group chats, draft plans, generate weekly reports, using enterprise context; enterprise-grade agent governance/security based on Feishu platform.
- Promotion noted on page: limited-time free 30-day subscription; verified students get +2 months.
- Note: page is the paid-feature marketing page; free-tier specifics are not detailed here.

From paid-service agreement (source 4):
- Paid services covered: series memberships, member-exclusive AI creation quota packs (图片/视频生成, image/video generation), cloud storage expansion.
- Quota consumption order for creation: free quota → creation pack → membership quota.
- Membership tiers named in agreement: 标准套餐 / 加强套餐 / 高级套餐 (Standard / Enhanced / Advanced); consumption-based quotas; auto-renewal (monthly/annual) supported.
- Platform definition: "豆包" includes client applications (possibly multiple versions), browser extensions, mini-programs, official website www.doubao.com/chat/, plus SDKs and APIs for third-party websites/apps.

## Underlying models

- Desktop page (source 2) states the professional/paid tier's core creation models: "专业版 Seedream 5.0 生图，专业版 Seedance 2.5 生视频核心模型" (Seedream 5.0 for image generation, Seedance 2.5 for video generation), plus "内置自主规划执行的 Agent 智能体" (built-in autonomous planning/executing agent).
- App Store description (source 5) says video generation is based on the Seedance model (no version given there).
- The consumer chat LLM (e.g., which Doubao-Seed text model powers chat) is NOT explicitly named in any fetched page → `not publicly disclosed` in these sources.
- Related B2B model family on Volcengine Ark (source 6) — API-side names, not confirmed as app internals: Doubao-Seed-Evolving, Doubao-Seed-2.1-pro, Doubao-Seed-2.1-turbo, Doubao-Seed-Character, Doubao-Seedance-2.5/2.0/2.0-fast/2.0-mini, Doubao-Seedream-5.0-pro/5.0-lite, Doubao-Seed-RealtimeVoice, Doubao-Seed-ICL-2.0, Doubao-Seed-TTS-2.0, Doubao-Seed-Livelnterpret, Doubao-Seed-Audio, Doubao-Seed-Embedding.
- Volcengine page also states the Doubao model family powers ByteDance products 豆包爱学 / 飞书 / 即梦 / 豆包 / 抖音 / 猫箱 / TRAE (source 6).
- Seed site (source 7) describes Seed2.1 (Pro/Turbo) as an agent-focused model for productivity and code; no explicit Doubao-app linkage stated on that page.

## Pricing

Consumer app (App Store CN listing, source 5):
- 基础版 (Basic): free.
- 标准版 (Standard): 68 CNY/month (auto-renew monthly), 688 CNY/year (auto-renew annual).
- 加强版 (Enhanced): 200 CNY/month, 2048 CNY/year.
- 专业版 (Professional): 500 CNY/month, 5088 CNY/year.
- Auto-renewal charged via iTunes within 24h before period end. App download is free (price 0.0).
- Extra paid items per agreement (source 4): member-only creation quota packs (one-time purchase, fixed validity, not auto-renewing) and cloud-storage expansion; no prices listed on that page.
- Desktop page (source 2) mentions limited-time free 30-day subscription promotion (+2 months for verified students); no separate desktop pricing listed.

B2B API pricing on Volcengine Ark (source 6, yuan, not app pricing):
- Doubao-Seed-Evolving & 2.1-pro: 6 yuan/M input tokens, 30 yuan/M output; cache-hit 1.2 yuan/M tokens; 0.017 yuan/M tokens/hour cache. 2.1-turbo: 3/15/0.6. Character: from 0.8/M input, 2/M output.
- Video: Seedance-2.5 42 yuan/M tokens (with video input) / 70 (without); 2.0 from 28/46; fast 22/37; mini 14/23.
- Image: Seedream-5.0-pro from 0.30 yuan/image; 5.0-lite 0.22 yuan/image.
- Speech: voice clone 8 yuan/10k chars; TTS 5 yuan/10k chars; streaming ASR 4.5 yuan/hour; recording-file ASR 2.0: 0.8 yuan/hour.
- Embedding-vision: 0.7 yuan/M tokens (text), 1.8 yuan/M tokens (image).
- Platform-wide stat on that page: "180万亿 日均tokens使用量" (180 trillion daily tokens usage across the Doubao LLM platform; enterprise + consumer, not app-specific) and "0.15元起 百万输入tokens".

## Platforms & availability

- Web: www.doubao.com/chat/ (official site; source 1 & 4). Desktop: official desktop client download at doubao.com/download/desktop, /pc redirects there (sources 2, fetch checks). Mobile: doubao.com/download/mobile exists (source 3).
- iOS: App Store CN, since 2023-08-24, current 15.1.0 (source 5). Android page details not shown on the mobile page we fetched; agreement says client apps "may include different versions" (source 4) — Android-specific listing not verified this run → mark as not directly verified from fetched pages (Android not explicitly confirmed; do not claim without a source).
- Region behavior observed (fetched): www.doubao.com redirects a non-logged-in, non-mainland-China browser session to a ban page: "受区域限制，请先登录再使用豆包。你也可以选择使用 Dola。" (Regional restriction; log in first to use Doubao, or use Dola). Dola (www.dola.com) then shows "Dola is not available in this country or region" for our test IP. → Doubao consumer web/app is mainland-China-focused; overseas users are pointed to Dola (ByteDance's overseas assistant). Sources 1, 8.
- API: consumer app offers no public consumer API page; the legal agreement states the platform includes SDKs and APIs "for third-party websites and applications" (source 4). Developer/enterprise access to Doubao-family models is via Volcengine Ark (sources 6, 9).

## Use cases & limitations

Official use cases (sources 2, 5): daily Q&A and life help; study (tutoring, homework grading); office automation (docs, spreadsheets, PPT, data analysis, code); agentic desktop automation (Doubao Work); image/video creation; voice calls; web search; photo recognition; enterprise work via Feishu.
Official limitations:
- App Store disclaimer (source 5): as an AI it may still misunderstand or mislead; users advised to cross-check with other sources.
- Region restriction on web access without login (source 1); overseas users redirected to Dola, which itself is geo-restricted (source 8).
- Membership is quota-based (consumption counted in tokens converted to usage counts/durations); free tier has limited quotas; creation packs expire and don't roll over (source 4).
- Membership valid only while logged in; login device/terminal limits may apply (source 4).

## Conflicts / uncertainty notes

- Tier naming mismatch: App Store listing calls tiers 基础版/标准版/加强版/专业版 (source 5), while the official paid-service agreement (updated 2026-08-15) calls memberships 标准套餐/加强套餐/高级套餐 (source 4). Both official; treat as naming drift between the store listing and the legal doc.
- Video-generation model version: App Store text says "Seedance" generically (source 5); desktop page pins the professional tier to Seedance 2.5 + Seedream 5.0 (source 2). Older vs newer copy.
- User counts: no official user/MAU figure found in fetched sources → `not publicly disclosed` (as of these fetches).
- The chat LLM powering the consumer app is not named on fetched pages; only creation models (Seedream/Seedance) are. Do not assume Doubao-Seed-2.x powers the app without a source.
- Volcengine "180T daily tokens" and API prices describe the B2B Doubao LLM platform, not the consumer app subscription.
- Android availability was not directly verified from an official store page this run (only iOS CN listing fetched); desktop/web/mobile download pages exist on doubao.com.
- All Chinese quotes translated to English here; original text is in the cited pages.
