/* ------------------------------------------------------------------ */
/* Shared JSON-LD and FAQ builders for entity pages (main site).       */
/* Rules: no fabricated ratings/reviews/authors; only include fields   */
/* that exist in the data; dates only when full ISO dates are known.   */
/* ------------------------------------------------------------------ */

export type Faq = { q: string; a: string };

const isoDate = (s?: string) => (s && /^\d{4}-\d{2}-\d{2}$/.test(s) ? s : undefined);

const sentence = (s: string) => {
  const t = s.trim().replace(/[.。]+$/, '');
  return `${t}.`;
};

/* ------------------------------- JSON-LD --------------------------- */

export function breadcrumbJsonLd(items: { name: string; url: string }[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      item: it.url,
    })),
  };
}

export function softwareApplicationJsonLd(o: {
  id: string;
  name: string;
  description: string;
  provider?: string;
  providerUrl?: string;
  datePublished?: string;
}) {
  const out: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'SoftwareApplication',
    '@id': o.id,
    name: o.name,
    url: o.id,
    description: o.description,
    applicationCategory: 'AIApplication',
  };
  if (o.provider) {
    out.provider = o.providerUrl
      ? { '@type': 'Organization', name: o.provider, url: o.providerUrl }
      : { '@type': 'Organization', name: o.provider };
  }
  const dp = isoDate(o.datePublished);
  if (dp) out.datePublished = dp;
  return out;
}

export function organizationJsonLd(o: {
  id: string;
  name: string;
  description: string;
  sameAs?: string[];
  alternateName?: string[];
}) {
  const out: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    '@id': o.id,
    name: o.name,
    url: o.id,
    description: o.description,
  };
  if (o.sameAs && o.sameAs.length) out.sameAs = o.sameAs;
  if (o.alternateName && o.alternateName.length) out.alternateName = o.alternateName;
  return out;
}

export function apiReferenceJsonLd(o: {
  id: string;
  name: string;
  description: string;
  provider?: string;
  providerUrl?: string;
  documentation?: string;
}) {
  const out: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'APIReference',
    '@id': o.id,
    name: o.name,
    url: o.id,
    description: o.description,
  };
  if (o.provider) {
    out.provider = o.providerUrl
      ? { '@type': 'Organization', name: o.provider, url: o.providerUrl }
      : { '@type': 'Organization', name: o.provider };
  }
  if (o.documentation) out.documentation = o.documentation;
  return out;
}

export function offerCatalogJsonLd(o: {
  id: string;
  name: string;
  description: string;
  offers: {
    model: string;
    modelUrl?: string;
    input?: number | null;
    output?: number | null;
    currency: string;
  }[];
}) {
  return {
    '@context': 'https://schema.org',
    '@type': 'OfferCatalog',
    '@id': o.id,
    name: o.name,
    url: o.id,
    description: o.description,
    itemListElement: o.offers.map((m) => {
      const offer: Record<string, unknown> = {
        '@type': 'Offer',
        itemOffered: m.modelUrl
          ? { '@type': 'SoftwareApplication', name: m.model, url: m.modelUrl }
          : { '@type': 'SoftwareApplication', name: m.model },
        priceCurrency: m.currency,
      };
      if (m.input != null) offer.price = m.input;
      if (m.output != null) offer.description = `Output: $${m.output} per 1M tokens`;
      return offer;
    }),
  };
}

export function datasetJsonLd(o: {
  id: string;
  name: string;
  description: string;
  dateModified?: string;
}) {
  const out: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'Dataset',
    '@id': o.id,
    name: o.name,
    url: o.id,
    description: o.description,
  };
  const dm = isoDate(o.dateModified);
  if (dm) out.dateModified = dm;
  return out;
}

/* ----------------------------- FAQ builders ------------------------ */
/* All answers are derived from the entity's own verified fields.      */

/* eslint-disable @typescript-eslint/no-explicit-any */

export function modelFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  const name = d.model_name;
  if (d.context_window != null) {
    faqs.push({
      q: `What is the context window of ${name}?`,
      a: `${name} has a ${d.context_window.toLocaleString()}-token context window${
        d.maximum_output != null
          ? ` and a maximum output of ${d.maximum_output.toLocaleString()} tokens`
          : ''
      }.`,
    });
  } else {
    faqs.push({
      q: `What is the context window of ${name}?`,
      a: `The context window of ${name} has not been publicly disclosed.`,
    });
  }
  if (d.open_weight != null) {
    faqs.push({
      q: `Is ${name} open weight?`,
      a: d.open_weight
        ? `Yes — ${name} weights are openly available${d.license ? ` under the ${d.license} license` : ''}.`
        : `No — ${name} is not open weight.`,
    });
  }
  if (d.pricing?.input_price_per_1m != null) {
    faqs.push({
      q: `How much does ${name} cost through the API?`,
      a: `$${d.pricing.input_price_per_1m} per 1M input tokens and $${
        d.pricing.output_price_per_1m ?? '—'
      } per 1M output tokens (${d.pricing.currency}).`,
    });
  } else {
    faqs.push({
      q: `How much does ${name} cost through the API?`,
      a: `API pricing for ${name} is not currently listed in our database.`,
    });
  }
  faqs.push({
    q: `Where does China AI Hub get its ${name} data?`,
    a: `From ${d.sources.length} source${d.sources.length === 1 ? '' : 's'} (official pages first), last verified ${
      d.last_verified
    }. Benchmark scores are labeled by source type; see the sourcing policy for details.`,
  });
  return faqs;
}

export function agentFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  faqs.push({ q: `What is ${d.agent_name}?`, a: sentence(d.description) });
  if (d.underlying_models.length) {
    faqs.push({
      q: `Which models does ${d.agent_name} use?`,
      a: `${d.agent_name} uses ${d.underlying_models.join(', ')}.`,
    });
  }
  if (d.open_source != null) {
    faqs.push({
      q: `Is ${d.agent_name} open source?`,
      a: d.open_source
        ? `Yes${d.license ? ` — licensed under ${d.license}` : ''}.`
        : `No — ${d.agent_name} is not open source.`,
    });
  }
  if (d.pricing) {
    faqs.push({ q: `How much does ${d.agent_name} cost?`, a: sentence(d.pricing) });
  } else {
    faqs.push({
      q: `How much does ${d.agent_name} cost?`,
      a: `Pricing for ${d.agent_name} is not currently listed in our database.`,
    });
  }
  faqs.push({
    q: `Where does China AI Hub get its ${d.agent_name} data?`,
    a: `From ${d.sources.length} source${d.sources.length === 1 ? '' : 's'}, last verified ${d.last_verified}.`,
  });
  return faqs;
}

export function companyFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  const name = d.company_name;
  if (d.headquarters) {
    faqs.push({ q: `Where is ${name} based?`, a: sentence(d.headquarters) });
  }
  if (d.foundation_models.length) {
    faqs.push({
      q: `Which foundation models does ${name} offer?`,
      a: `${d.foundation_models.join(', ')}.`,
    });
  }
  if (d.api.length) {
    faqs.push({
      q: `Does ${name} provide an API?`,
      a: `Yes — ${name} operates the ${d.api.join(', ')} API${d.api.length === 1 ? '' : 's'}.`,
    });
  } else {
    faqs.push({
      q: `Does ${name} provide an API?`,
      a: `No API is currently listed for ${name} in our database.`,
    });
  }
  if (d.open_source_projects.length) {
    faqs.push({
      q: `What open-source projects does ${name} maintain?`,
      a: `${d.open_source_projects.join(', ')}.`,
    });
  }
  faqs.push({
    q: `Where does China AI Hub get its ${name} data?`,
    a: `From ${d.sources.length} source${d.sources.length === 1 ? '' : 's'}, last verified ${d.last_verified}.`,
  });
  return faqs;
}

export function apiFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  const name = `${d.api_id} API`;
  if (d.endpoint) {
    faqs.push({ q: `What is the ${name} endpoint?`, a: `The ${name} endpoint is ${d.endpoint}.` });
  }
  if (d.authentication) {
    faqs.push({ q: `How do you authenticate with the ${name}?`, a: sentence(d.authentication) });
  }
  if (d.context_limits.length) {
    const cl = d.context_limits
      .map(
        (c: any) =>
          `${c.model}: ${c.input_limit != null ? c.input_limit.toLocaleString() : '—'} in / ${
            c.output_limit != null ? c.output_limit.toLocaleString() : '—'
          } out`
      )
      .join('; ');
    faqs.push({ q: `What are the context limits of the ${name}?`, a: `${cl}.` });
  }
  if (d.function_calling != null) {
    faqs.push({
      q: `Does the ${name} support function calling?`,
      a: d.function_calling
        ? `Yes — the ${name} supports function calling.`
        : `No — the ${name} does not list function-calling support.`,
    });
  }
  faqs.push({
    q: `Where does China AI Hub get its ${name} data?`,
    a: `From ${d.sources.length} source${d.sources.length === 1 ? '' : 's'}, last verified ${d.last_verified}.`,
  });
  return faqs;
}

export function pricingFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  const inputs = d.models.map((m: any) => m.input_price_per_1m).filter((v: any) => v != null);
  if (inputs.length) {
    const min = Math.min(...inputs);
    faqs.push({
      q: `What does the ${d.provider_id} API cost?`,
      a: `Input prices start at $${min} per 1M tokens across ${d.models.length} listed model${
        d.models.length === 1 ? '' : 's'
      } (${d.currency}). See the table above for output and cached prices.`,
    });
  }
  const hasCached = d.models.some(
    (m: any) => m.cached_input_price_per_1m != null || m.cached_output_price_per_1m != null
  );
  if (hasCached) {
    faqs.push({
      q: `Does ${d.provider_id} offer cached pricing?`,
      a: `Yes — cached input/output prices are listed for some models in the table above.`,
    });
  }
  const hasBatch = d.models.some((m: any) => m.batch_price_per_1m != null);
  if (hasBatch) {
    faqs.push({
      q: `Does ${d.provider_id} offer batch pricing?`,
      a: `Yes — batch prices per 1M tokens are listed for some models in the table above.`,
    });
  }
  faqs.push({
    q: `When was ${d.provider_id} pricing last verified?`,
    a: `Last verified ${d.last_verified} against ${d.sources.length} official source${
      d.sources.length === 1 ? '' : 's'
    }. Prices change frequently — check the official pricing page before deciding.`,
  });
  return faqs;
}

export function benchmarkFaqs(d: any): Faq[] {
  const faqs: Faq[] = [];
  const name = d.benchmark_name;
  if (d.description) {
    faqs.push({ q: `What does ${name} measure?`, a: sentence(d.description) });
  }
  const models = [...new Set(d.evaluations.map((e: any) => e.model).filter(Boolean))] as string[];
  if (models.length) {
    faqs.push({
      q: `Which Chinese AI models have published ${name} results?`,
      a: `${models.join(', ')}.`,
    });
  }
  const types = [...new Set(d.evaluations.map((e: any) => e.source_type))] as string[];
  faqs.push({
    q: `Are ${name} scores independently verified?`,
    a: `Results on this page are labeled by source type (${types.join(', ')}). Vendor-reported scores are labeled as such, and scores from incompatible benchmark versions are never mixed.`,
  });
  faqs.push({
    q: `Where does China AI Hub get its ${name} data?`,
    a: `From ${d.sources.length} source${d.sources.length === 1 ? '' : 's'}, last verified ${d.last_verified}.`,
  });
  return faqs;
}
