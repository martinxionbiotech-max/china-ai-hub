#!/usr/bin/env python3
"""B2-b: Answer Blocks 标准化 (What is uncertain + Sources) + Where this model fits 负载表.
Incremental insertion only — never rewrites existing content."""
import re, sys

ROOT = "src/content"

# ---- workload table data (8 core model pages) ----
# relevance values only from page-documented facts
workload = {
    "deepseek-v4-pro": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "High",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "deepseek-v4-1-flash": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "High",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "kimi-k3": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "High",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "qwen3.8-max": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "High",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "No evidence",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "High",
    },
    "glm-5.3": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "No evidence",
        "Agent orchestration": "Moderate",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "minimax-m3": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "Moderate",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "doubao-seed-2-1-pro": {
        "Long-context analysis": "High",
        "Coding": "Moderate",
        "Structured API workflows": "High",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "No evidence",
        "GUI automation": "High",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
    "glm-5.2": {
        "Long-context analysis": "High",
        "Coding": "High",
        "Structured API workflows": "Moderate",
        "Agent orchestration": "High",
        "Local self-hosted deployment": "High",
        "GUI automation": "No evidence",
        "Video generation": "No evidence",
        "Enterprise cloud": "Moderate",
    },
}

WORKLOAD_ORDER = [
    "Long-context analysis",
    "Coding",
    "Structured API workflows",
    "Agent orchestration",
    "Local self-hosted deployment",
    "GUI automation",
    "Video generation",
    "Enterprise cloud",
]

def workload_table(slug):
    rows = "\n".join(
        f"| {w} | {workload[slug][w]} |" for w in WORKLOAD_ORDER
    )
    return (
        "## Where this model fits\n\n"
        "| Workload | Relevance |\n|---|---|\n"
        f"{rows}\n\n"
        "Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.\n"
    )

# ---- answer block data ----
# each: (what_is_uncertain bullets, sources list of (name, url))
answer = {}

# models
answer["deepseek-v4-pro"] = (
    [
        "The deprecation status is conflicting: the news page says V4-Pro routes to V4.1-Flash after 2026-09-14, but the same-day change log says the API continues unchanged.",
        "Whether the Hugging Face checkpoint (last modified 2026-06-22) matches the 0813 GA checkpoint is not documented.",
        "Serving regions are not disclosed.",
        "All four benchmark scores are vendor-reported; no independent third-party measurement is recorded.",
    ],
    [
        ("DeepSeek API docs — Models & Pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek API Change Log", "https://api-docs.deepseek.com/updates"),
        ("DeepSeek-V4 Preview release", "https://www.deepseek.com/en/news/v4-preview/"),
        ("Hugging Face model card — DeepSeek-V4-Pro", "https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"),
    ],
)
answer["deepseek-v4-1-flash"] = (
    [
        "Benchmark scores are vendor-reported via the DeepSeek Harness and not independently verified.",
        "The HLE score differs between the full set (36.8) and the pure-text subset (39.1).",
        "Serving regions are not disclosed.",
    ],
    [
        ("DeepSeek API docs — Models & Pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek API Change Log", "https://api-docs.deepseek.com/updates"),
        ("DeepSeek-V4.1-Flash release announcement", "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"),
        ("Hugging Face model card — DeepSeek-V4.1-Flash", "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"),
    ],
)
answer["kimi-k3"] = (
    [
        "The input-modality boundary is inconsistent across official sources: the architecture table says Text+Image, while the README, launch blog and API guide also list video input.",
        "Some comparison benchmark scores are cited from Artificial Analysis (third-party); the K3-specific rows here are vendor-reported.",
        "Sampling is fixed (temperature 1.0, top_p 0.95) and cannot be changed through the API.",
    ],
    [
        ("Kimi K3 GitHub README", "https://github.com/MoonshotAI/Kimi-K3"),
        ("Kimi API platform — model list", "https://platform.kimi.ai/docs/models.md"),
        ("Kimi API — Chat Completions spec", "https://platform.kimi.ai/docs/api/chat.md"),
        ("Kimi K3 launch blog", "https://www.kimi.com/blog/kimi-k3"),
    ],
)
answer["qwen3.8-max"] = (
    [
        "The exact API release date is not stated; only the 0902 snapshot date (2026-09-02) is known.",
        "Benchmark scores come from the vendor model card and are not independently verified.",
        "The open Qwen3.8-2.4T-A95B weights are a different product (text-only, thinking-only), not this model.",
    ],
    [
        ("Model Studio — qwen3.8-max model detail", "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"),
        ("Model Studio — model pricing", "https://www.alibabacloud.com/help/en/model-studio/model-pricing"),
        ("Hugging Face model card — Qwen3.8-2.4T-A95B", "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"),
    ],
)
answer["glm-5.3"] = (
    [
        "The headline \"50% coding improvement\" is measured on Z.ai Code Bench, a private in-house benchmark that cannot be independently reproduced.",
        "The Apache-2.0 label comes from GitHub metadata; the README has no separate weights-license section, so per-model Hugging Face cards should be verified before reuse.",
        "Terminal-Bench 3.0 scores are not comparable to other vendors' 2.1 scores.",
    ],
    [
        ("Z.ai docs — GLM-5.3 model page", "https://docs.z.ai/guides/llm/glm-5.3"),
        ("Z.ai pricing", "https://docs.z.ai/guides/overview/pricing"),
        ("GLM-5 GitHub repository", "https://github.com/zai-org/GLM-5"),
    ],
)
answer["minimax-m3"] = (
    [
        "Maximum output tokens are not publicly disclosed; the 131,072 figure is derived from the official card's evaluation config.",
        "The MSA speedup claims (9x prefill / 15x decode) are vendor claims, not independently measured.",
        "Benchmark scores are vendor-reported and not independently verified.",
    ],
    [
        ("MiniMax API platform — model overview (CN)", "https://platform.minimaxi.com/docs/guides/models-intro"),
        ("MiniMax official M3 model page", "https://www.minimax.cn/models/text/m3"),
        ("MiniMax M3 official blog post", "https://www.minimax.cn/blog/minimax-m3"),
        ("Hugging Face model card — MiniMax-M3", "https://huggingface.co/MiniMaxAI/MiniMax-M3"),
    ],
)
answer["doubao-seed-2-1-pro"] = (
    [
        "Architecture and parameter counts are not publicly disclosed for the Seed 2.1 series.",
        "Only one benchmark (Code Arena Frontend, a preview-version score) is recorded; no GA benchmark evidence exists.",
        "The exact release day of the 260915 version is not stated (month 2026-09 only).",
        "No international endpoint was verified — the API is cn-beijing only.",
    ],
    [
        ("Ark official model list", "https://docs.volcengine.com/docs/ark/model-list?lang=zh"),
        ("Ark official model pricing", "https://docs.volcengine.com/docs/ark/model-pricing?lang=zh"),
        ("Ark model release announcements", "https://docs.volcengine.com/docs/ark/model-release-announcement"),
        ("ByteDance Seed official blog — Seed 2.1 release", "https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity"),
    ],
)
answer["glm-5.2"] = (
    [
        "It is superseded by GLM-5.3 but remains billable at the same price — a deprecation without retirement.",
        "Benchmark scores are vendor-reported and predate the GLM-5.3 successor.",
        "GLM-5.3's claimed gains rest on the private Z.ai Code Bench and cannot be independently reproduced.",
    ],
    [
        ("Z.ai docs — GLM-5.3 model page", "https://docs.z.ai/guides/llm/glm-5.3"),
        ("Z.ai pricing", "https://docs.z.ai/guides/overview/pricing"),
        ("Z.ai release notes", "https://docs.z.ai/release-notes/new-released"),
        ("Hugging Face model card — GLM-5.2", "https://huggingface.co/zai-org/GLM-5.2"),
    ],
)

# companies
answer["deepseek"] = (
    [
        "The founding date is not stated on the official pages fetched.",
        "V4-Pro's deprecation is conflicting across official pages (news page vs change log).",
    ],
    [
        ("DeepSeek API docs — Models & Pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek API Change Log", "https://api-docs.deepseek.com/updates"),
        ("DeepSeek official site (EN)", "https://www.deepseek.com/en/"),
        ("DeepSeek Transparency Center", "https://www.deepseek.com/en/transparency/"),
    ],
)
answer["bytedance"] = (
    [
        "Funding rounds are not officially disclosed.",
        "No Doubao LLM weights are public — every user routes through ByteDance's own infrastructure.",
    ],
    [
        ("Ark (Volcengine) official documentation", "https://docs.volcengine.com/docs/ark/product-overview?lang=zh"),
        ("Ark official model list", "https://docs.volcengine.com/docs/ark/model-list?lang=zh"),
        ("Ark model release announcements", "https://docs.volcengine.com/docs/ark/model-release-announcement"),
        ("ByteDance Seed official blog — Seed 2.1 release", "https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity"),
        ("ByteDance Seed GitHub organization", "https://github.com/ByteDance-Seed"),
    ],
)
answer["alibaba-cloud"] = (
    [
        "The older \"Tongyi Qianwen / 通义千问\" branding was not confirmed on the fetched English pages.",
        "The open A95B release carries a custom MIT-style license with scale-triggered obligations for large operators.",
    ],
    [
        ("Alibaba Cloud Model Studio — text generation model list", "https://www.alibabacloud.com/help/en/model-studio/text-generation-model"),
        ("Qwen3.8 open-model repository README", "https://github.com/QwenLM/Qwen3.8"),
        ("Hugging Face model card — Qwen3.8-2.4T-A95B", "https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B"),
    ],
)
answer["minimax"] = (
    [
        "Funding-round details are not listed on official pages.",
        "The user counts (230+ countries, 300M+ users) are vendor claims stated on the CN site.",
    ],
    [
        ("MiniMax official site (international)", "https://www.minimax.io/"),
        ("MiniMax official site (China)", "https://www.minimax.cn/about"),
        ("MiniMax API platform — model overview (CN)", "https://platform.minimaxi.com/docs/guides/models-intro"),
        ("MiniMax official release notes", "https://platform.minimaxi.com/docs/release-notes/models.md"),
    ],
)
answer["moonshot-ai"] = (
    [
        "No official funding disclosure located.",
        "The K3 license requires a separate agreement above $20M revenue and UI attribution above 100M MAU — conditioned at scale.",
    ],
    [
        ("Moonshot AI official site (EN)", "https://www.moonshot.ai/"),
        ("Moonshot AI company profile (CN)", "https://www.moonshot.cn/about"),
        ("Kimi API platform — model list", "https://platform.kimi.ai/docs/models.md"),
        ("Kimi K3 GitHub README", "https://github.com/MoonshotAI/Kimi-K3"),
    ],
)
answer["zhipu-ai"] = (
    [
        "No official funding disclosure located; IPO/funding reports are not confirmed on official channels.",
        "The founding date is not stated on the official pages fetched.",
        "The Apache-2.0 label comes from GitHub metadata; the README has no separate weights-license section.",
    ],
    [
        ("Z.ai docs — GLM-5.3 model page", "https://docs.z.ai/guides/llm/glm-5.3"),
        ("Z.ai docs — GLM-5.3-Flash model page", "https://docs.z.ai/guides/vlm/glm-5.3-flash"),
        ("Z.ai release notes", "https://docs.z.ai/release-notes/new-released"),
        ("GLM-5 GitHub repository", "https://github.com/zai-org/GLM-5"),
    ],
)

# comparisons
answer["deepseek-v4-pro-vs-kimi-k3"] = (
    [
        "Benchmark scores are vendor-reported and not independently re-measured.",
        "DeepSeek-V4-Pro is listed deprecated with conflicting official pages on its post-2026-09-14 status.",
        "No third-party benchmark evidence is recorded for either model.",
    ],
    [
        ("DeepSeek API pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek V4 Preview announcement", "https://www.deepseek.com/en/news/v4-preview/"),
        ("Moonshot AI — Kimi K3 (GitHub)", "https://github.com/MoonshotAI/Kimi-K3"),
        ("Kimi platform — Models documentation", "https://platform.kimi.ai/docs/models.md"),
    ],
)
answer["deepseek-v4-pro-vs-qwen3.8-max"] = (
    [
        "Benchmark comparability is limited — different versions, harnesses and partial coverage.",
        "DeepSeek-V4-Pro is listed deprecated (preview 2026-04-24, GA 2026-08-13); verify the current lineup.",
        "No third-party benchmark evidence is recorded for either model.",
    ],
    [
        ("DeepSeek API pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek V4 Preview announcement", "https://www.deepseek.com/en/news/v4-preview/"),
        ("Alibaba Cloud Model Studio — Qwen3.8-Max", "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"),
        ("Alibaba Cloud Model Studio — Model pricing", "https://www.alibabacloud.com/help/en/model-studio/model-pricing"),
    ],
)
answer["deepseek-v4-1-flash-vs-glm-5.3-flash"] = (
    [
        "Benchmark comparability is limited — different versions, harnesses and partial coverage.",
        "GLM-5.3-Flash lists tool calling, function calling and structured output as \"Not listed\" — an absence of documentation, not a verified lack of capability.",
    ],
    [
        ("DeepSeek API pricing", "https://api-docs.deepseek.com/quick_start/pricing"),
        ("DeepSeek — V4.1-Flash announcement", "https://www.deepseek.com/en/news/deepseek-v4-1-flash/"),
        ("Z.ai — GLM-5.3-Flash documentation", "https://docs.z.ai/guides/vlm/glm-5.3-flash"),
        ("Z.ai — Pricing overview", "https://docs.z.ai/guides/overview/pricing"),
    ],
)
answer["doubao-seed-2-1-pro-vs-minimax-m3"] = (
    [
        "The single Doubao benchmark record makes head-to-head comparison unreliable.",
        "MiniMax M3 does not publicly disclose a maximum output figure.",
    ],
    [
        ("Volcengine Ark — Model list", "https://docs.volcengine.com/docs/ark/model-list?lang=zh"),
        ("Volcengine Ark — Model pricing", "https://docs.volcengine.com/docs/ark/model-pricing?lang=zh"),
        ("MiniMax — Models introduction", "https://platform.minimaxi.com/docs/guides/models-intro"),
        ("MiniMax — MiniMax M3 announcement", "https://www.minimax.cn/blog/minimax-m3"),
    ],
)
answer["kimi-k3-vs-minimax-m3"] = (
    [
        "MiniMax M3 does not publicly disclose a maximum output figure.",
        "Benchmark comparability is limited — different versions, harnesses and partial coverage.",
    ],
    [
        ("Moonshot AI — Kimi K3 (GitHub)", "https://github.com/MoonshotAI/Kimi-K3"),
        ("Kimi platform — Models documentation", "https://platform.kimi.ai/docs/models.md"),
        ("MiniMax — Models introduction", "https://platform.minimaxi.com/docs/guides/models-intro"),
        ("MiniMax — MiniMax M3 announcement", "https://www.minimax.cn/blog/minimax-m3"),
    ],
)
answer["qwen3.8-max-vs-glm-5.3"] = (
    [
        "Benchmark comparability is limited — different versions, harnesses and partial coverage.",
        "GLM-5.3 lists no tool calling or structured output — an absence of documentation, not a verified lack of capability.",
    ],
    [
        ("Alibaba Cloud Model Studio — Qwen3.8-Max", "https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max"),
        ("Alibaba Cloud Model Studio — Model pricing", "https://www.alibabacloud.com/help/en/model-studio/model-pricing"),
        ("Z.ai — GLM-5.3 documentation", "https://docs.z.ai/guides/llm/glm-5.3"),
        ("Z.ai — Pricing overview", "https://docs.z.ai/guides/overview/pricing"),
        ("Z.ai — GLM-5 (GitHub)", "https://github.com/zai-org/GLM-5"),
    ],
)

def build_answer_block(uncertain, sources):
    u = "\n".join(f"- {x}" for x in uncertain)
    s = "\n".join(f"- [{name}]({url})" for name, url in sources)
    return f"## What is uncertain\n\n{u}\n\n## Sources\n\n{s}\n"

# map file paths
def model_path(slug):
    return f"{ROOT}/models/{slug}.md"

def company_path(slug):
    return f"{ROOT}/companies/{slug}.md"

def comparison_path(slug):
    return f"{ROOT}/comparisons/{slug}.md"

def patch(path, anchor, insert_before_anchor, insert_text):
    with open(path) as f:
        t = f.read()
    if anchor not in t:
        print(f"  !! anchor not found in {path}: {anchor!r}")
        return False
    if t.count(anchor) != 1:
        print(f"  !! anchor not unique ({t.count(anchor)}x) in {path}: {anchor!r}")
        return False
    new = insert_text + "\n" + anchor if insert_before_anchor else anchor + "\n" + insert_text
    t = t.replace(anchor, new, 1)
    with open(path, "w") as f:
        f.write(t)
    return True

errors = []

# 1) model pages: workload table (before "## China AI Hub analysis") + answer block (before "*Labels used above:")
for slug in workload:
    p = model_path(slug)
    ok1 = patch(p, "## China AI Hub analysis", True, workload_table(slug))
    if not ok1:
        errors.append(p + " :: workload")
    unc, src = answer[slug]
    ok2 = patch(p, "*Labels used above:", True, build_answer_block(unc, src))
    if not ok2:
        errors.append(p + " :: answer")

# 2) company pages: answer block only
for slug in ["deepseek", "bytedance", "alibaba-cloud", "minimax", "moonshot-ai", "zhipu-ai"]:
    p = company_path(slug)
    unc, src = answer[slug]
    if not patch(p, "*Labels used above:", True, build_answer_block(unc, src)):
        errors.append(p + " :: answer")

# 3) comparison pages: answer block only
for slug in ["deepseek-v4-pro-vs-kimi-k3", "deepseek-v4-pro-vs-qwen3.8-max",
             "deepseek-v4-1-flash-vs-glm-5.3-flash", "doubao-seed-2-1-pro-vs-minimax-m3",
             "kimi-k3-vs-minimax-m3", "qwen3.8-max-vs-glm-5.3"]:
    p = comparison_path(slug)
    unc, src = answer[slug]
    if not patch(p, "*Labels used above:", True, build_answer_block(unc, src)):
        errors.append(p + " :: answer")

if errors:
    print("ERRORS:")
    for e in errors:
        print("  " + e)
    sys.exit(1)

print("All 20 pages patched OK (8 workload tables + 20 answer blocks).")
