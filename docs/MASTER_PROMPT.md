# CHINA AI HUB — MASTER PROJECT PROMPT

## Project Name

China AI Hub

## Primary Domain

https://chinaaihub.com

## Recommended Positioning

China AI Models, Agents, APIs & AI Technology

Alternative positioning:

An Independent Database of China's AI Models, Agents, APIs and AI Companies.

---

# 0. ROLE

You are the lead product architect, senior developer, SEO/AIO strategist, data architect, AI researcher, technical writer and editorial analyst responsible for building China AI Hub.

You must think about this project as a long-term information infrastructure product, not as a normal content website.

The final product should become:

China AI Knowledge Graph
+
AI Model Database
+
AI Agent Database
+
AI Company Database
+
AI API Database
+
AI Pricing Database
+
AI Benchmark Database
+
AI Technology Knowledge Base
+
Comparison Engine
+
Original Research Platform

The website is intended primarily for an international English-speaking audience interested in understanding China's AI ecosystem.

---

# 1. CORE PRODUCT VISION

China AI Hub is NOT:

- a generic AI news website
- a Chinese AI news translation site
- a model ranking website
- a "Top 10 Chinese AI models" blog
- a collection of rewritten official documentation
- a mass-generated programmatic SEO website

China AI Hub IS:

> An independent English-language knowledge and intelligence platform for understanding China's AI models, agents, APIs, companies, technologies, pricing and ecosystem.

The central question the platform should help users answer is:

> Which Chinese AI model, agent or API is suitable for which task, at what cost, with what capabilities and under what deployment conditions?

Do not attempt to declare one universal "best" Chinese AI model.

Instead provide structured evidence so users can make their own decisions.

---

# 2. PRIMARY AUDIENCE

Prioritize:

1. AI developers
2. Software engineers
3. AI researchers
4. Enterprise technology buyers
5. AI startups
6. Developers evaluating Chinese APIs
7. Researchers studying China's AI industry
8. International businesses interested in Chinese AI
9. Journalists and analysts
10. Technical decision makers

Secondary audience:

- AI enthusiasts
- students
- technology investors
- consultants
- journalists

Content must assume an intelligent international reader who may know AI but does not necessarily understand China's AI ecosystem.

---

# 3. CORE DIFFERENTIATION

The main competitive advantage must NOT be "more articles".

The advantage should be:

## Structured Data + Evidence + Original Analysis

Other websites may provide:

- model lists
- news
- price tables
- reviews

China AI Hub should connect:

Model
→ Company
→ API
→ Pricing
→ Benchmark
→ Agent
→ Technology
→ Comparison
→ Original Research

This creates a China AI Knowledge Graph.

---

# 4. WEBSITE ARCHITECTURE

Phase 1 should use one primary domain.

Primary domain:

chinaaihub.com

Core URL structure:

/
/models
/agents
/companies
/api
/pricing
/benchmarks
/technology
/comparisons
/guides
/research
/news
/about

Do NOT create multiple subdomains during Phase 1 unless there is a strong technical reason.

Future data layer (ONE data subdomain only):

data.chinaaihub.com

Repo: `martinxionbiotech-max/china-ai-hub-data` (created 2026-09-21, public, main branch; agent access authorized).

No other subdomains are planned. models./agents./pricing. subdomains are cancelled — the main site routes `/models`, `/agents`, `/pricing` remain the canonical locations. The data subdomain should only be introduced after the main site's information architecture and authority are established.

---

# 5. INFORMATION ARCHITECTURE

The website has three major layers.

## Layer A — Structured Data

Contains:

- Models
- Companies
- Agents
- APIs
- Pricing
- Benchmarks
- Technologies

## Layer B — Knowledge

Contains:

- Guides
- Explainers
- Technology articles
- Entity explanations
- Comparison pages

## Layer C — Original Intelligence

Contains:

- Original Research
- Original Analysis
- Industry Reports
- China AI Hub View
- Historical analysis
- Market structure analysis

Do not mix these layers carelessly.

Database pages answer:

> What is known?

Editorial pages answer:

> What does it mean?

---

# 6. AI MODEL DATABASE

Create:

/models

The Model Database is one of the most important assets of the entire website.

Each model should have a stable unique ID.

Do not use display names as primary identifiers.

## Required Model Schema

model_id
model_name
provider
model_family
version
aliases
release_date
status
architecture
parameter_information
context_window
maximum_output
reasoning
coding
math
chinese
english
multilingual
vision
audio
video
tool_calling
function_calling
structured_output
agent_capability
open_weight
license
self_hosting
api_available
input_price
output_price
cached_input_price
batch_price
official_api
cloud_providers
regions
benchmark_results
known_limitations
last_verified
sources

Where data is unavailable:

Use:

null
unknown
not publicly disclosed

Never invent values.

---

# 7. MODEL CAPABILITY SYSTEM

Capabilities must NOT simply be described with arbitrary scores.

Prefer documented facts and clearly defined evaluation data.

Capability categories:

Reasoning
Coding
Mathematics
Chinese
English
Multilingual
Long Context
Vision
Audio
Video
Tool Calling
Function Calling
Structured Output
Agent
RAG
Computer Use

Where scores are used:

Clearly identify:

- benchmark
- benchmark version
- evaluation method
- model version
- score
- source
- date

Never turn one benchmark into a universal quality ranking.

---

# 8. AI AGENT DATABASE

Create:

/agents

This is a strategic pillar of China AI Hub.

Categories:

Coding Agents
Research Agents
Browser Agents
Computer Use Agents
Enterprise Agents
Customer Service Agents
Marketing Agents
Data Agents
Multi-Agent Systems
Autonomous Agents

## Agent Schema

agent_id
agent_name
company
description
underlying_models
framework
tool_calling
browser_use
computer_use
mcp
memory
planning
multi_agent
api
pricing
deployment
open_source
license
github
documentation
use_cases
limitations
last_verified
sources

Clearly distinguish:

AI model
AI assistant
AI agent
agent framework
agent platform

Do not treat every chatbot as an "agent".

---

# 9. COMPANY DATABASE

Create:

/companies

Initial research universe should include major organizations such as:

DeepSeek
Alibaba / Qwen
Moonshot AI / Kimi
Z.ai / GLM
MiniMax
ByteDance / Doubao
Baidu / ERNIE
Tencent / Hunyuan
iFlytek / Spark
StepFun
Baichuan
01.AI
Huawei
Xiaomi

This list is not exhaustive.

Research additional significant Chinese AI companies.

## Company Schema

company_id
company_name
aliases
founded
headquarters
ownership_information_where_relevant
ai_products
foundation_models
agents
api
open_models
cloud_distribution
major_releases
open_source_projects
official_documentation
official_website
related_entities
sources
last_verified

Do not add controversial corporate information without reliable sourcing.

---

# 10. API DATABASE

Create:

/api

Track:

API availability
API endpoint
authentication
streaming
function calling
tool calling
structured output
vision
audio
context limits
rate limits
regions
cloud providers
pricing
documentation
last verified

Where possible distinguish:

official API
cloud-hosted API
third-party API
self-hosted endpoint

---

# 11. PRICING DATABASE

Create:

/pricing

Pricing is dynamic and must be treated as time-sensitive data.

## Required Fields

provider
model
input_price_per_1m_tokens
output_price_per_1m_tokens
cached_input_price
cached_output_price
batch_price
subscription_price
pay_as_you_go_price
currency
region
billing_mode
standard_or_high_speed
effective_date
last_verified
official_source

Always preserve the original source.

Never compare prices without checking:

- currency
- region
- billing model
- token unit
- input/output distinction
- cache pricing
- batch pricing

When prices change:

preserve historical data when practical.

Record:

old value
new value
effective date
source

---

# 12. BENCHMARK DATABASE

Create:

/benchmarks

Schema:

benchmark_id
benchmark_name
version
model
model_version
score
evaluation_method
dataset
date
source
source_type
vendor_reported
independent_evaluation
limitations

Distinguish:

Vendor-reported
Independent
Academic
Community

Do not present benchmark scores as universal rankings.

Do not create "best model" claims from a single benchmark.

---

# 13. TECHNOLOGY KNOWLEDGE BASE

Create:

/technology

Initial topics:

Reasoning Models
Mixture of Experts
Long Context
RAG
AI Agents
MCP
A2A
Tool Calling
Function Calling
Computer Use
Multimodal AI
Deep Research
Synthetic Data
Distillation
Quantization
Inference
AI Chips
AI Infrastructure

Each technology page should cover:

Definition
Technical background
How it works
Why it matters
Chinese adoption
Major Chinese companies/models
Practical applications
Limitations
Deployment considerations
Future development
Sources

Where appropriate, distinguish:

global technology
Chinese implementation
company-specific implementation

Do not imply that a technology is uniquely Chinese when it is not.

---

# 14. COMPARISON SYSTEM

Create:

/comparisons

Examples:

/comparisons/deepseek-vs-qwen
/comparisons/deepseek-vs-kimi
/comparisons/qwen-vs-glm
/comparisons/kimi-vs-minimax

Comparison dimensions:

Pricing
Context
Reasoning
Coding
Chinese
English
Multilingual
Vision
Audio
Tool Calling
Agent
Open Weight
License
API
Deployment
Documentation
Use Cases
Availability

Avoid:

Best
Winner
#1
Worst

unless the statement refers to a clearly defined objective measurement.

Do not provide an overall ranking.

Comparison pages should explain trade-offs and differences.

---

# 15. MODEL EXPLORER

Build a searchable/filterable Model Explorer.

Filters:

Provider
Model Family
Reasoning
Coding
Vision
Audio
Video
Context
Open Weight
License
API
Self Hosting
Price Range
Model Type

The explorer must provide genuine utility.

Do not build a visual filter that does not correspond to real database fields.

---

# 16. PRICING EXPLORER

Build a pricing comparison tool.

Users should be able to compare:

Model
Provider
Input
Output
Cached Input
Context
Region
Billing Mode
Last Verified

Normalize units.

Display original source.

Show last verification date.

---

# 17. ENTITY GRAPH

Build a strong internal entity graph.

Example:

DeepSeek V4 Pro
↓
DeepSeek
↓
DeepSeek API
↓
DeepSeek Pricing
↓
DeepSeek Benchmarks
↓
DeepSeek vs Qwen
↓
Reasoning Models
↓
AI Agents

Relationships should include:

model → company
model → API
model → pricing
model → benchmark
model → agent
model → technology
company → models
company → agents
agent → models
agent → company
technology → models
technology → companies
comparison → entities
research → entities

Internal linking should be semantic, not keyword-stuffed.

---

# 18. SOURCE / EVIDENCE SYSTEM

This is a core product feature.

Every important factual data point should support:

value
source
source_type
published_date
last_verified
confidence

Preferred source hierarchy:

## Level 1 — Primary Sources

Official documentation
Official model cards
Official API pricing
Official technical papers
Official GitHub
Official announcements

## Level 2 — High Quality Technical Sources

Academic papers
Benchmark organizations
Cloud documentation
Independent technical research

## Level 3 — Major Industry Media

Reuters
Bloomberg
Financial Times
TechCrunch
Specialist publications

## Level 4 — Community

GitHub discussions
Hugging Face
Reddit
Developer communities

Community sources should not be the sole source for critical facts.

---

# 19. SOURCE CONFLICT HANDLING

When sources disagree:

1. Do not silently select one.
2. Identify the conflicting claims.
3. Identify the source of each claim.
4. Check source dates.
5. Check model versions.
6. Check region and pricing conditions.
7. Explain possible reasons for the difference.
8. Preserve uncertainty when necessary.

Do not manufacture certainty.

---

# 20. DATA FRESHNESS

Dynamic information should display:

Last updated
Last verified

Especially:

Model version
Pricing
API availability
Context window
Benchmark results
Product availability
License
Documentation

For important entities, maintain change history when practical.

---

# 21. DATA PIPELINE

Design the architecture for:

Official Sources
↓
Crawler / Firecrawl
↓
Change Detection
↓
Structured Extraction
↓
Source Attribution
↓
Validation
↓
Database
↓
Page Rendering
↓
SEO / Schema
↓
QA
↓
Publication

Agents should assist with:

- discovery
- extraction
- normalization
- change detection
- source comparison
- update proposals

Agents must NOT automatically overwrite critical data without validation.

---

# 22. ORIGINAL CONTENT STRATEGY

This is one of the most important requirements.

The website must contain substantial original content.

Original content must NOT be:

- translated Chinese articles
- rewritten company documentation
- AI-generated summaries
- content assembled from five articles
- keyword-expanded articles
- generic "what is AI" content

Original content must add independent value.

---

# 23. ORIGINAL CONTENT TYPES

Create five major types.

## A. Original Analysis

Examples:

Why Chinese AI Models Are Competing on Cost and Efficiency

How China's AI Model Market Is Changing

Why Open-Weight Models Matter in China's AI Ecosystem

## B. Original Comparisons

Example:

DeepSeek vs Qwen: Pricing, Reasoning, Coding and Deployment

## C. Original Explainers

Example:

What Is a Chinese Reasoning Model?

## D. Original Industry Research

Example:

The State of Chinese AI Agents in 2026

## E. China AI Hub View

Major research and analysis articles should include:

China AI Hub View

This is the author's independent interpretation of the evidence.

It must not simply repeat source material.

---

# 24. ORIGINAL WRITING SKILL

For all substantial editorial content, use the latest available original research / expert writing skill.

The writer's role:

Senior AI industry researcher
+
Technical analyst
+
Independent English-language author

The writer is NOT:

A summarizer
A translator
An SEO spinner
A content farm writer

---

# 25. ORIGINAL RESEARCH WORKFLOW

Every major research article must follow:

Research Question
↓
Primary Source Collection
↓
Evidence Extraction
↓
Cross-Source Verification
↓
Structured Data Collection
↓
Comparison
↓
Historical Context
↓
Pattern Identification
↓
Independent Analysis
↓
Original Synthesis
↓
Author View
↓
Conclusion
↓
Fact QA
↓
Originality QA

---

# 26. ORIGINAL ARTICLE FRAMEWORK

Recommended structure:

# H1

Executive Summary

## What We Know

## What the Data Shows

## What Has Changed

## Why It Matters

## Detailed Analysis

## Comparison / Evidence

## Limitations and Uncertainty

## China AI Hub View

## Conclusion

## Sources

This is a reasoning framework.

Do not mechanically force every heading into every article.

---

# 27. INFORMATION → ANALYSIS → CONCLUSION → ORIGINAL CONTENT → AUTHOR VIEW

Every major article should follow this logic:

Information
↓
Evidence
↓
Analysis
↓
Interpretation
↓
Conclusion
↓
Original Synthesis
↓
Author View

The article must clearly distinguish:

FACT
ANALYSIS
INTERPRETATION
UNCERTAINTY

Do not present interpretation as fact.

---

# 28. ORIGINALITY TEST

Before publishing any substantial article, answer:

1. What information was independently researched?
2. What data was collected?
3. What comparison was performed?
4. What analysis was performed?
5. What is genuinely new?
6. What is the author's independent interpretation?
7. Could this article exist without simply rewriting another source?

If the answer to the final question is "no":

DO NOT PUBLISH.

Revise the article.

---

# 29. WRITING STYLE

Write for intelligent international readers.

Style:

Clear
Direct
Analytical
Professional
Technical when necessary
Human
Evidence-driven

Avoid:

"AI is rapidly transforming..."
"In today's fast-paced world..."
"With the development of AI..."
"It is important to note that..."
"revolutionary"
"game-changing"
"unprecedented"

unless supported and genuinely necessary.

Avoid repetitive AI-generated phrasing.

Do not inflate word count.

The goal is:

SUBSTANCE

not:

LENGTH.

---

# 30. AUTHOR VIEW

The China AI Hub View should:

- synthesize evidence
- identify meaningful patterns
- explain trade-offs
- acknowledge uncertainty
- explain practical implications

It should NOT:

- promote a company
- blindly criticize a company
- declare universal winners
- pretend certainty where none exists

The author's viewpoint must be traceable to the evidence.

---

# 31. ORIGINAL RESEARCH TOPIC BACKLOG

Initial research topics:

1. The State of China's AI Models in 2026
2. How Chinese AI Model Pricing Has Changed
3. Chinese AI Models and the Shift Toward Task Efficiency
4. Open-Weight AI Models in China
5. The Rise of Chinese AI Agents
6. Chinese AI Coding Models
7. Chinese AI Models for Long-Context Applications
8. Chinese AI APIs Compared
9. Chinese AI Model Deployment Options
10. Chinese AI Infrastructure
11. Chinese AI Model Companies Explained
12. How DeepSeek Changed China's AI Market
13. Qwen's Role in China's Open Model Ecosystem
14. Kimi and Long-Context AI
15. GLM and Agent-Oriented AI
16. MiniMax and Multimodal AI
17. Chinese AI Models for Developers
18. Chinese AI Models for Enterprise
19. Chinese AI Model Licensing Explained
20. China AI Benchmark Landscape

Before writing any topic:

Check whether the topic remains current.

Do not assume the title is still accurate.

---

# 32. SEO STRATEGY

Optimize for:

Google Search
Google AI Overviews
ChatGPT
Gemini
Perplexity
other AI search systems

Primary SEO concepts:

Entity SEO
Semantic SEO
Topical Authority
Structured Data
Original Research
Comparison Intent
Long-Tail Search
Data Utility
First-Party Evidence
Knowledge Graph

Do not keyword stuff.

Do not generate thin programmatic pages.

---

# 33. SEARCH INTENT CLUSTERS

Build content around:

## Model

DeepSeek V4 Pro
DeepSeek V4 Pro API
DeepSeek V4 Pro pricing
DeepSeek V4 Pro context window
DeepSeek V4 Pro benchmark

## Comparison

DeepSeek vs Qwen
DeepSeek vs Kimi
Qwen vs GLM
Kimi vs MiniMax

## Pricing

Chinese AI API pricing
DeepSeek API pricing
Qwen API pricing
Kimi API pricing
GLM API pricing

## Agent

Chinese AI agents
Chinese coding agents
Chinese AI browser agents
Chinese research agents

## Technology

Chinese reasoning models
Chinese open-weight models
China AI agent frameworks
Chinese AI infrastructure

---

# 34. PROGRAMMATIC SEO RULES

Programmatic pages are allowed only when:

1. The underlying data is real.
2. The page has genuine utility.
3. The entity is meaningful.
4. The page is sufficiently complete.
5. The page contains unique structured information.
6. The page has source attribution.
7. The page is internally linked.
8. The page is not just a template with one changed keyword.

Never generate thousands of low-value model pages.

---

# 35. GEO / AIO REQUIREMENTS

Important entity pages should contain:

Clear definition
Key facts
Structured tables
Source attribution
Last verified date
Entity relationships
Original analysis where appropriate

Make factual statements concise and independently understandable.

Use semantic HTML.

Use structured data.

Do not optimize for AI search by stuffing repetitive summaries.

---

# 36. SCHEMA.ORG

Use appropriate Schema.org types.

Companies:

Organization

Articles:

Article
TechArticle
NewsArticle when appropriate

Software/model entities:

Use Product / SoftwareApplication / appropriate types only where semantically justified.

Comparisons:

Article
ItemList where appropriate

Do not invent Schema.org properties.

Do not create fake ratings.

Do not create fake reviews.

Do not create unsupported aggregateRating data.

---

# 37. PAGE TYPES

Build reusable templates for:

ModelPage
CompanyPage
AgentPage
APIDetailPage
PricingPage
BenchmarkPage
TechnologyPage
ComparisonPage
GuidePage
ResearchPage
NewsPage

---

# 38. REUSABLE COMPONENTS

Build reusable components:

ModelCard
CompanyCard
AgentCard
PricingTable
BenchmarkTable
ComparisonTable
SourceBadge
LastVerified
EntityLinks
ModelExplorer
PricingExplorer
RelatedModels
RelatedAgents
RelatedCompanies
ResearchCard
DataUpdateHistory

---

# 39. HOMEPAGE STRUCTURE

Homepage should include:

Hero

China AI Models, Agents, APIs & AI Technology

Supporting copy:

Explore China's AI ecosystem through structured data, comparisons and original research.

Primary actions:

Explore Models
Compare Models

Then:

Latest Model Updates

Model Explorer

AI Pricing

AI Agents

Latest Comparisons

Original Research

China AI Landscape

Latest Data Updates

---

# 40. DESIGN SYSTEM

Visual direction:

Professional
Technical
Data-centric
Editorial
Research-oriented
Trustworthy

Avoid:

Generic AI gradients
Excessive neon
Robot illustrations
Stock AI imagery
Overly futuristic visuals
Consumer chatbot aesthetics

The site should feel closer to:

Professional industry intelligence
Technical research database
Data product

than:

AI startup landing page.

---

# 41. PERFORMANCE

Prioritize:

Fast loading
Static generation where appropriate
Semantic HTML
Minimal JavaScript
Responsive design
Excellent Core Web Vitals
Accessible tables
Crawlable content
AI-readable content
Clean URLs

Avoid unnecessary frontend complexity.

---

# 42. URL STRUCTURE

Use stable semantic URLs.

Examples:

/models/deepseek-v4-pro
/models/qwen3-max

/companies/deepseek
/companies/alibaba-qwen

/agents/example-agent

/pricing/deepseek
/pricing/qwen

/comparisons/deepseek-vs-qwen

/technology/mixture-of-experts

/guides/chinese-ai-models

/research/chinese-ai-agents-2026

Avoid:

/blog/post123
/article?id=123
/2026/09/random-title

unless technically required.

---

# 43. INTERNAL LINKING

Every entity should connect to related entities.

Example:

Model Page
→ Company
→ API
→ Pricing
→ Benchmark
→ Agent
→ Technology
→ Comparisons
→ Research

Use contextual links.

Do not repeat the same anchor unnaturally.

---

# 44. DATA ARCHITECTURE

Separate:

content data
entity data
source data
pricing data
benchmark data
SEO metadata
rendering logic

Use stable IDs.

Never make display names the database primary key.

---

# 45. DATA VALIDATION

Before publishing or updating data:

Check:

Freshness
Completeness
Missingness
Duplicates
Entity identity
Version consistency
Source quality
Price normalization
Unit consistency
Date consistency
Schema consistency

Critical data should require stronger validation.

---

# 46. CONTENT QUALITY GATE

Before publication verify:

Factual accuracy
Source quality
Source freshness
Originality
Completeness
Entity consistency
Internal links
Schema
SEO title
Meta description
Canonical
Indexability
Table correctness
Pricing correctness
Benchmark correctness
No unsupported claims
No fabricated data

---

# 47. MODEL DATA QUALITY GATE

For each model:

Check model name
Check provider
Check version
Check release date
Check current status
Check context
Check pricing
Check capabilities
Check license
Check API
Check source
Check verification date

If information is uncertain:

Mark uncertainty.

Do not guess.

---

# 48. PRICING DATA QUALITY GATE

Before publishing a price:

Verify:

Currency
Region
Billing model
Input/output unit
Cache
Batch
Subscription
Pay-as-you-go
Effective date
Official source

Display:

Last verified

---

# 49. BENCHMARK DATA QUALITY GATE

Before publishing:

Verify benchmark name
Benchmark version
Model version
Score
Evaluation method
Source
Date

Never mix scores from incompatible benchmark versions without explaining the difference.

---

# 50. NEWS SECTION

News is secondary.

News should be used mainly to:

- track ecosystem changes
- identify new models
- identify price changes
- identify new agents
- identify company developments
- trigger database updates
- provide current context

Do not allow news aggregation to become the site's primary product.

---

# 51. HISTORICAL DATA

Where practical maintain:

Model version history
Pricing history
Benchmark history
Company release history
Agent version history

Historical information should not be destroyed simply because a newer version exists.

---

# 52. INITIAL CONTENT TARGET

Phase 1:

30–50 Model pages
20–30 Company pages
20–30 Agent pages
30–40 Technology pages
10–20 Pricing pages
20–30 Comparison pages
15–20 Guides
10–15 Original Research articles

Quality is more important than quantity.

Do not publish weak pages merely to meet numerical targets.

---

# 53. INITIAL MODEL UNIVERSE

Start research with major Chinese model families.

Examples:

DeepSeek
Qwen
Kimi
GLM
MiniMax
Doubao
ERNIE
Hunyuan
Spark
StepFun
Baichuan
Yi
InternLM
MiMo
and other significant models discovered through research.

Do not assume that this list is complete.

Verify current versions before creating pages.

---

# 54. INITIAL AGENT UNIVERSE

Research:

Coding Agents
Research Agents
Browser Agents
Computer Use Agents
Enterprise Agents
Agent Platforms
Agent Frameworks
Multi-Agent systems

Distinguish actual products from marketing terminology.

---

# 55. PHASED IMPLEMENTATION

## PHASE 0 — REPOSITORY AUDIT

Before changing anything:

Inspect:

repository
framework
dependencies
existing routes
content structure
build system
deployment configuration
SEO configuration
current components

Do not overwrite existing architecture blindly.

Produce:

ARCHITECTURE_AUDIT.md

---

# PHASE 1 — ARCHITECTURE

Build:

routing
content schemas
entity schemas
source schemas
SEO framework
Schema.org framework
internal linking framework
design system
reusable components

Do not mass-create content yet.

---

# PHASE 2 — DATABASE

Implement:

Models
Companies
Agents
Technology
Pricing
Benchmarks
API

Start with a controlled number of high-quality records.

---

# PHASE 3 — ENTITY GRAPH

Implement relationships between:

Models
Companies
Agents
APIs
Pricing
Benchmarks
Technology
Comparisons
Research

---

# PHASE 4 — EXPLORERS

Build:

Model Explorer
Pricing Explorer

Make them functional.

---

# PHASE 5 — CONTENT

Create:

Guides
Comparisons
Technology explainers
Original Research

Use the original research writing skill.

---

# PHASE 6 — SEO / GEO / AIO

Audit:

Indexability
Canonical
Titles
Descriptions
Headings
Internal links
Schema
Sitemaps
Robots
Semantic HTML
AI readability
Entity relationships

---

# PHASE 7 — AUTOMATION

Integrate:

Firecrawl
Source discovery
Change detection
Structured extraction
Validation
Update proposals

Agents may prepare updates.

Critical facts should pass validation before publication.

---

# PHASE 8 — CONTINUOUS INTELLIGENCE

Create a recurring update system.

Monitor:

Official model documentation
Official pricing
Official announcements
Official GitHub
Major benchmark updates
Major company releases
Agent product changes

Generate update candidates.

Do not blindly auto-publish.

---

# 56. AGENT OPERATING PRINCIPLES

When researching:

Think first.

Do not immediately write.

First establish:

What is the question?
What entities are involved?
What facts are needed?
What sources are authoritative?
What data has changed?
What conflicts exist?

Then write.

---

# 57. NEVER INVENT DATA

Never fabricate:

Prices
Benchmarks
Model parameters
Context windows
Capabilities
Licenses
Release dates
Company information
API availability
Performance results
Customer numbers
Market share

If unknown:

Say unknown.

If estimated:

Clearly label as estimate.

If vendor-reported:

Clearly label vendor-reported.

---

# 58. CLAIM CLASSIFICATION

Classify major claims internally as:

FACT
VENDOR CLAIM
INDEPENDENT FINDING
ANALYSIS
INTERPRETATION
ESTIMATE
UNCERTAINTY

The final article should not blur these categories.

---

# 59. COMPARISON PHILOSOPHY

Comparisons should explain:

What differs?
Why does it differ?
For which workloads does the difference matter?
What are the trade-offs?
What evidence supports the difference?

Do not simply produce:

A > B

unless referring to a specific measurable metric.

---

# 60. "CHINA AI HUB VIEW"

For major analytical pages:

Include a clearly identified:

China AI Hub View

This section should answer:

What does the evidence suggest?

What is changing?

What is likely to matter?

What remains uncertain?

What should technical readers pay attention to?

This is original editorial analysis.

It must never be fabricated.

---

# 61. CONTENT DEPTH

Do not define quality by word count.

A 1,500-word article with original analysis is better than a 4,000-word article filled with repetition.

Prefer:

Evidence
Specificity
Originality
Useful comparison
Technical clarity
Practical implications

over:

Length.

---

# 62. FAQ POLICY

Do not add generic FAQ sections to every page.

Use FAQ only when:

- genuine user questions exist
- the questions add search utility
- answers are not duplicates of the main content

---

# 63. IMAGES

Do not fill pages with stock AI images.

Prefer:

Charts
Data visualizations
Architecture diagrams
Model relationship diagrams
Original explanatory graphics

Only use images when they improve understanding.

---

# 64. AI SEARCH READABILITY

Important pages should have:

Clear H1
Concise definition
Fact table
Detailed explanation
Source attribution
Related entities
Last verified
Original analysis

Use clean semantic HTML.

---

# 65. FUTURE DATA PRODUCT

Design the database so future features can include:

JSON export
CSV export
Public datasets
API access
Historical pricing
Model change history
Benchmark datasets
Enterprise intelligence reports

Do not implement all of these in Phase 1.

Design for extensibility.

---

# 66. FUTURE BUSINESS MODEL

Potential future products:

Free database
Premium data access
Historical pricing datasets
API access
Enterprise research
China AI market reports
Model monitoring
AI procurement intelligence
Developer API directory

Do not let monetization damage the information architecture.

---

# 67. FIRST 10 ORIGINAL RESEARCH ARTICLES

Prioritize research topics that demonstrate the site's unique value.

Suggested starting topics:

1. The State of China's AI Models in 2026
2. How Chinese AI Model Pricing Has Changed
3. The Rise of Chinese AI Agents
4. Chinese AI Models and Task Efficiency
5. Open-Weight AI Models in China
6. Chinese AI APIs Compared
7. Chinese AI Coding Models
8. China's Long-Context AI Models
9. Chinese AI Model Deployment Options
10. China AI Benchmark Landscape

Each article must be independently researched.

---

# 68. FINAL QUALITY STANDARD

Before declaring the website complete, ask:

## Product

Does the site provide real utility?

## Data

Are important facts structured?

## Evidence

Can users understand where important facts came from?

## Freshness

Can users see when information was verified?

## Entity Graph

Are models, companies, agents, technologies and APIs connected?

## Originality

Does the site produce original analysis?

## SEO

Are entity and search intents clearly covered?

## AI Search

Can AI systems understand the site's factual structure?

## Design

Does it look like a serious research/data product?

## Performance

Is it fast?

## Maintainability

Can agents update it without breaking the system?

If any answer is no, continue improving.

---

# 69. MOST IMPORTANT PRINCIPLE

Do not build:

"Another website about Chinese AI."

Build:

> "The English-language structured information layer for China's AI ecosystem."

The long-term product should become:

China AI Knowledge Graph
+
Structured Data
+
Evidence
+
Original Research
+
Comparison Tools
+
Continuously Updated Intelligence

The website should become more valuable as its structured data, historical records, entity relationships and original analysis accumulate.

---

# 70. EXECUTION RULE

Before implementation:

1. Audit the repository.
2. Create architecture plan.
3. Define schemas.
4. Define entity relationships.
5. Define source/evidence model.
6. Define content templates.
7. Define original research workflow.
8. Implement reusable components.
9. Implement database.
10. Create initial verified entities.
11. Create original content.
12. Implement SEO/GEO/AIO.
13. Validate everything.
14. Only then expand.

Do not skip architecture and immediately generate hundreds of pages.

Do not optimize for page count.

Optimize for:

Authority
Accuracy
Originality
Data Utility
Freshness
Entity Connectivity
Search Visibility
Long-Term Maintainability

---

# 71. FINAL DELIVERABLES

The completed Phase 1 system must include:

- Production-ready China AI Hub website
- Homepage
- Models database
- Companies database
- Agents database
- API database
- Pricing database
- Benchmark database
- Technology knowledge base
- Comparison system
- Model Explorer
- Pricing Explorer
- Evidence/source system
- Last Verified system
- Entity graph
- Internal linking system
- SEO infrastructure
- Schema.org infrastructure
- Sitemap
- Robots configuration
- AI-readable semantic content
- Original research framework
- Content quality gate
- Data quality gate
- Update architecture
- Documentation for future agents

Also create:

ARCHITECTURE.md
DATA_SCHEMA.md
CONTENT_GUIDELINES.md
ORIGINAL_RESEARCH_GUIDE.md
SOURCE_POLICY.md
SEO_GUIDE.md
UPDATE_PIPELINE.md

These documents should explain how future Codex/OpenClaw agents should maintain the project.

---

# 72. FINAL INSTRUCTION TO THE AGENT

Do not treat this as a one-time website generation task.

Treat China AI Hub as a long-term evolving information system.

Build the architecture so:

More models
+
More companies
+
More agents
+
More pricing data
+
More benchmarks
+
More technologies
+
More historical records
+
More original research

continually increase the value of the platform.

The final objective is not:

"Publish many AI articles."

The objective is:

> Build the most useful English-language structured knowledge platform for understanding China's AI ecosystem.

Proceed systematically.

Audit first.

Architect second.

Implement third.

Research fourth.

Publish fifth.

Validate continuously.