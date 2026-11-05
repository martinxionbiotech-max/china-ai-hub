---
benchmark_id: agent-web-benchmarks
benchmark_name: "Agentic and Web Benchmarks"
description: "GAIA, BrowseComp, AutomationBench, CyberGym and IFEval: what each measures about agents, which Chinese models publish results, and why harness details decide the score."
task_type: "Multi-step assistant tasks, deep web research, business workflow automation, security testing and instruction following"
dataset_size: "GAIA 466 questions across 3 levels · BrowseComp 1,266 questions · AutomationBench workflow tasks · CyberGym vulnerability scenarios · IFEval ~541 prompts"
evaluation_method: "Agentic evaluation with tools, browsing and retries; IFEval by programmatic constraint checking"
scoring: "Accuracy or task success rate; IFEval reports strict and loose prompt-level accuracy"
caveat: "Every benchmark here scores a system, not a model: the tool set, search backend, time limit and retry policy change results more than model choice does. Two vendors reporting the same benchmark name may be measuring different agents. Treat cross-vendor comparisons without harness disclosure as indicative only."
contamination_notes: "GAIA and BrowseComp answers are public; the web itself changes between runs, so a score is a snapshot of the internet on the evaluation date. IFEval prompts are synthetic and cheap to optimise against."
limitations: "Results are recorded as published, with source type and date. Where a vendor reports only a task-completion percentage, this page does not reconstruct the harness."
member_ids: [gaia, browsecomp, automationbench, cybergym, ifeval]
last_verified: "2026-11-05"
evaluations:
  - benchmark: BrowseComp
    model: kimi-k3
    score: "91.2 (90.4 with full 1M context, no compaction)"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: BrowseComp
    model: kimi-k2.5
    score: "60.6 (74.9 with context management; 78.4 Agent Swarm)"
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: BrowseComp
    model: minimax-m3
    score: 83.5
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/models/text/m3
  - benchmark: AutomationBench
    model: deepseek-v4-1-flash
    score: 54.8
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: AutomationBench
    model: deepseek-v4-pro
    score: 31.8
    model_version: "Public"
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: AutomationBench
    model: qwen3.8-max
    score: 27.3
    model_version: "Pass@1"
    metric: accuracy
    date: "2026-08"
    source_type: vendor_reported
    source_url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
  - benchmark: AutomationBench
    model: glm-5.3-flash
    score: 48.8
    model_version: "GLM-5.2: 26.2"
    metric: accuracy
    date: "2026-08-26"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
  - benchmark: CyberGym
    model: deepseek-v4-1-flash
    score: 88.1
    metric: accuracy
    date: "2026-09-10"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: CyberGym
    model: deepseek-v4-pro
    score: 83.3
    metric: accuracy
    date: "2026-08-13"
    source_type: vendor_reported
    source_url: https://api-docs.deepseek.com/updates
  - benchmark: CyberGym
    model: glm-5.3
    score: 84.5
    model_version: "vuln discovery (GLM-5.2: 77.2)"
    metric: accuracy
    date: "2026-08-18"
    source_type: vendor_reported
    source_url: https://docs.z.ai/guides/llm/glm-5.3
sources:
  - source_name: "Mialon et al. — GAIA: a benchmark for General AI Assistants"
    source_url: https://arxiv.org/abs/2311.12983
    source_type: academic
    published_date: "2023-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "GAIA benchmark (Hugging Face)"
    source_url: https://huggingface.co/gaia-benchmark
    source_type: benchmark_org
    last_verified: "2026-09-29"
  - source_name: "OpenAI BrowseComp announcement"
    source_url: https://openai.com/index/browsecomp/
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official M3 model page
    source_url: https://www.minimax.cn/models/text/m3
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "AutomationBench official repository (Zapier)"
    source_url: https://github.com/zapier/AutomationBench
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: DeepSeek API Change Log
    source_url: https://api-docs.deepseek.com/updates
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3-Flash model page
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "CyberGym official repository (Sunblaze UC Berkeley)"
    source_url: https://github.com/sunblaze-ucb/cybergym
    source_type: official
    last_verified: "2026-09-22"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
  - source_name: "Zhou et al. — Instruction-Following Evaluation for Large Language Models (IFEval)"
    source_url: https://arxiv.org/abs/2311.07911
    source_type: academic
    published_date: "2023-11"
    last_verified: "2026-09-29"
    confidence: high
  - source_name: "IFEval — Google Research (instruction_following_eval)"
    source_url: https://github.com/google-research/google-research/tree/master/instruction_following_eval
    source_type: benchmark_org
    last_verified: "2026-09-29"
---

**Short answer.** Agent benchmarks measure a model plus its tools, not the model alone. GAIA, BrowseComp, AutomationBench and CyberGym each test a different slice of agentic work, while IFEval tests the instruction-following baseline that everything else depends on. Scores move with the harness, so they are comparable across vendors only when the harness is published.

## What each one tests

| Benchmark | Task | Failure it exposes |
|---|---|---|
| GAIA | Real assistant tasks needing tools and planning | Gives up, or loops without progress |
| BrowseComp | Persistent multi-step web research | Loses the question across pages |
| AutomationBench | End-to-end business workflows | Completes steps, misses the goal |
| CyberGym | Vulnerability discovery and exploitation | Finds bugs, cannot exploit or report |
| IFEval | Format and constraint compliance | Ignores explicit instructions |

The progression is deliberate: IFEval is the floor, GAIA and BrowseComp are research competence, AutomationBench is business process, CyberGym is adversarial skill.

## GAIA

466 questions across three difficulty levels, designed so that a competent human with a browser can answer them and a model without tools cannot. It is the closest public proxy for "general assistant".

The score depends heavily on tool access and the time budget. A GAIA number without those two settings is not reproducible, and the benchmark's own authors describe it as measuring a system.

## BrowseComp

Deep research with a verifiable answer: the agent must browse, follow leads and return a specific fact. It rewards persistence and penalises premature answers.

This is the benchmark most sensitive to the search backend. The same model with a better search index scores higher, which makes cross-vendor BrowseComp comparisons unusually unreliable.

## AutomationBench

Business workflow tasks — forms, records, multi-step processes — where success means the end state is correct, not that each step ran. It is the closest to enterprise agent work and the least standardised in reporting.

## CyberGym

Security tasks in a sandbox: find and exploit vulnerabilities. It measures an adversarial capability that most enterprises do not want in production and do want to understand before deploying agents with tool access.

## IFEval

About 541 prompts testing verifiable constraints — length, format, casing, structure. It is cheap to optimise and correlates weakly with product quality, but a model that fails IFEval will fail agent pipelines for boring reasons: wrong JSON, ignored length limits, skipped format rules.

## The harness is the benchmark

For every one of these, the published score is a property of the evaluation system. Before comparing two vendors, establish: which tools, which search backend, what time limit, how many retries, and whether the agent could install software.

Most vendors publish none of these. That is the finding.

## Our read

**Agent benchmarks are the least comparable numbers in the market, and the most quoted in sales decks.** A GAIA percentage without tool and time settings is a demo result. Buyers should treat it as evidence that an agent exists, not that it works.

**IFEval deserves more attention than it gets.** It is unfashionable because it measures compliance rather than intelligence, but most production agent failures are compliance failures: malformed JSON, ignored constraints, wrong output shape. A model that scores well on GAIA and poorly on IFEval will be expensive to operate.

**AutomationBench is the one to watch for enterprise buyers.** It is the only benchmark here that scores the end state of a business process, which is what a customer actually experiences.

**CyberGym is a procurement input, not a marketing number.** If you plan to give an agent shell access, the relevant question is not the score but whether the vendor will describe its sandbox and permission model.
