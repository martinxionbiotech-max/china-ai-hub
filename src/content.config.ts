import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/* ------------------------------------------------------------------ */
/* Shared schemas (see docs/DATA_SCHEMA.md for the full spec)          */
/* ------------------------------------------------------------------ */

const sourceSchema = z.object({
  source_name: z.string(),
  source_url: z.string().url(),
  source_type: z.enum([
    'official',
    'academic',
    'benchmark_org',
    'cloud_doc',
    'industry_media',
    'community',
    'independent',
  ]),
  published_date: z.string().optional(),
  last_verified: z.string().optional(),
  confidence: z.enum(['high', 'medium', 'low', 'estimate']).optional(),
});

const benchmarkResultSchema = z.object({
  benchmark: z.string(),
  model: z.string().optional(),
  benchmark_version: z.string().optional(),
  score: z.union([z.number(), z.string()]),
  metric: z.string().optional(),
  model_version: z.string().optional(),
  date: z.string().optional(),
  source_type: z.enum(['vendor_reported', 'independent', 'academic', 'community']),
  source_url: z.string().url().optional(),
});

/* ------------------------------------------------------------------ */
/* Collections                                                          */
/* ------------------------------------------------------------------ */

const models = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/models' }),
  schema: z.object({
    model_id: z.string(),
    model_name: z.string(),
    provider: z.string(),
    model_family: z.string().optional(),
    version: z.string().optional(),
    aliases: z.array(z.string()).default([]),
    release_date: z.string().optional(),
    status: z.enum(['active', 'preview', 'deprecated', 'discontinued']).default('active'),
    architecture: z.string().optional(),
    parameter_information: z
      .object({
        total_parameters: z.string().nullable().optional(),
        active_parameters: z.string().nullable().optional(),
        parameter_precision: z.string().nullable().optional(),
      })
      .optional(),
    context_window: z.number().nullable().optional(),
    maximum_output: z.number().nullable().optional(),
    capabilities: z
      .object({
        reasoning: z.boolean().nullable().optional(),
        coding: z.boolean().nullable().optional(),
        math: z.boolean().nullable().optional(),
        chinese: z.boolean().nullable().optional(),
        english: z.boolean().nullable().optional(),
        multilingual: z.boolean().nullable().optional(),
        vision: z.boolean().nullable().optional(),
        audio: z.boolean().nullable().optional(),
        video: z.boolean().nullable().optional(),
        tool_calling: z.boolean().nullable().optional(),
        function_calling: z.boolean().nullable().optional(),
        structured_output: z.boolean().nullable().optional(),
        agent_capability: z.boolean().nullable().optional(),
        rag: z.boolean().nullable().optional(),
        computer_use: z.boolean().nullable().optional(),
      })
      .default({}),
    open_weight: z.boolean().nullable().optional(),
    license: z.string().nullable().optional(),
    self_hosting: z.boolean().nullable().optional(),
    api_available: z.boolean().nullable().optional(),
    pricing: z
      .object({
        input_price_per_1m: z.number().nullable().optional(),
        output_price_per_1m: z.number().nullable().optional(),
        currency: z.string().default('USD'),
        effective_date: z.string().optional(),
        pricing_ref: z.string().optional(),
      })
      .optional(),
    official_api: z.boolean().nullable().optional(),
    cloud_providers: z.array(z.string()).default([]),
    regions: z.array(z.string()).default([]),
    benchmark_results: z.array(benchmarkResultSchema).default([]),
    known_limitations: z.array(z.string()).default([]),
    superseded_by: z.string().optional(),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const companies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/companies' }),
  schema: z.object({
    company_id: z.string(),
    company_name: z.string(),
    aliases: z.array(z.string()).default([]),
    founded: z.union([z.number(), z.string()]).optional(),
    headquarters: z.string().optional(),
    ownership_information: z.string().optional(),
    ai_products: z.array(z.string()).default([]),
    foundation_models: z.array(z.string()).default([]),
    agents: z.array(z.string()).default([]),
    api: z.array(z.string()).default([]),
    open_models: z.array(z.string()).default([]),
    cloud_distribution: z.array(z.string()).default([]),
    major_releases: z
      .array(z.object({ name: z.string(), date: z.string().optional(), type: z.string().optional() }))
      .default([]),
    open_source_projects: z.array(z.string()).default([]),
    official_documentation: z.string().url().optional(),
    official_website: z.string().url().optional(),
    related_entities: z.array(z.string()).default([]),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const agents = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/agents' }),
  schema: z.object({
    agent_id: z.string(),
    agent_name: z.string(),
    company: z.string(),
    description: z.string(),
    agent_type: z.enum([
      'coding',
      'research',
      'browser',
      'computer_use',
      'enterprise',
      'customer_service',
      'marketing',
      'data',
      'multi_agent',
      'autonomous',
      'framework',
      'platform',
    ]),
    underlying_models: z.array(z.string()).default([]),
    framework: z.string().nullable().optional(),
    tool_calling: z.boolean().nullable().optional(),
    browser_use: z.boolean().nullable().optional(),
    computer_use: z.boolean().nullable().optional(),
    mcp: z.boolean().nullable().optional(),
    memory: z.boolean().nullable().optional(),
    planning: z.boolean().nullable().optional(),
    multi_agent: z.boolean().nullable().optional(),
    api: z.boolean().nullable().optional(),
    pricing: z.string().nullable().optional(),
    deployment: z.enum(['cloud', 'self_hosted', 'both']).nullable().optional(),
    open_source: z.boolean().nullable().optional(),
    license: z.string().nullable().optional(),
    github: z.string().url().nullable().optional(),
    documentation: z.string().url().nullable().optional(),
    use_cases: z.array(z.string()).default([]),
    limitations: z.array(z.string()).default([]),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const apis = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/apis' }),
  schema: z.object({
    api_id: z.string(),
    provider: z.string(),
    api_type: z.enum(['official', 'cloud_hosted', 'third_party', 'self_hosted_endpoint']),
    endpoint: z.string().url().optional(),
    authentication: z.string().optional(),
    streaming: z.boolean().nullable().optional(),
    function_calling: z.boolean().nullable().optional(),
    tool_calling: z.boolean().nullable().optional(),
    structured_output: z.boolean().nullable().optional(),
    vision: z.boolean().nullable().optional(),
    audio: z.boolean().nullable().optional(),
    context_limits: z
      .array(z.object({ model: z.string(), input_limit: z.number().optional(), output_limit: z.number().optional() }))
      .default([]),
    rate_limits: z.string().optional(),
    regions: z.array(z.string()).default([]),
    cloud_providers: z.array(z.string()).default([]),
    pricing_ref: z.string().optional(),
    documentation: z.string().url().optional(),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const pricing = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pricing' }),
  schema: z.object({
    provider_id: z.string(),
    currency: z.string().default('USD'),
    region: z.string().optional(),
    billing_mode: z.string().default('pay_as_you_go'),
    models: z.array(
      z.object({
        model: z.string(),
        input_price_per_1m: z.number().nullable().optional(),
        output_price_per_1m: z.number().nullable().optional(),
        cached_input_price_per_1m: z.number().nullable().optional(),
        cached_output_price_per_1m: z.number().nullable().optional(),
        batch_price_per_1m: z.number().nullable().optional(),
        note: z.string().optional(),
        effective_date: z.string().optional(),
        official_source: z.string().url().optional(),
      })
    ),
    price_history: z
      .array(
        z.object({
          model: z.string(),
          field: z.string(),
          old_value: z.union([z.number(), z.string()]),
          new_value: z.union([z.number(), z.string()]),
          effective_date: z.string().optional(),
          source: z.string().url().optional(),
        })
      )
      .default([]),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const benchmarks = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/benchmarks' }),
  schema: z.object({
    benchmark_id: z.string(),
    benchmark_name: z.string(),
    version: z.string().optional(),
    description: z.string().optional(),
    evaluations: z.array(benchmarkResultSchema).default([]),
    limitations: z.string().optional(),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const technologies = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/technologies' }),
  schema: z.object({
    slug: z.string(),
    title: z.string(),
    definition: z.string(),
    related_models: z.array(z.string()).default([]),
    related_companies: z.array(z.string()).default([]),
    related_technologies: z.array(z.string()).default([]),
    related_guides: z.array(z.string()).default([]),
    last_verified: z.string(),
    sources: z.array(sourceSchema),
  }),
});

const comparisons = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/comparisons' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    entities: z.array(z.string()),
    dimensions: z.array(z.string()).default([]),
    published_date: z.string().optional(),
    updated_date: z.string().optional(),
    sources: z.array(sourceSchema).default([]),
  }),
});

const guides = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guides' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    published_date: z.string().optional(),
    updated_date: z.string().optional(),
    related_entities: z.array(z.string()).default([]),
    sources: z.array(sourceSchema).default([]),
  }),
});

const research = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/research' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    published_date: z.string().optional(),
    updated_date: z.string().optional(),
    research_question: z.string().optional(),
    related_entities: z.array(z.string()).default([]),
    author_view: z.boolean().default(true),
    sources: z.array(sourceSchema).default([]),
  }),
});

const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    published_date: z.string(),
    type: z.enum(['model_release', 'price_change', 'company', 'agent', 'other']),
    trigger_updates: z.array(z.string()).default([]),
    sources: z.array(sourceSchema).default([]),
  }),
});

export const collections = {
  models,
  companies,
  agents,
  apis,
  pricing,
  benchmarks,
  technologies,
  comparisons,
  guides,
  research,
  news,
};
