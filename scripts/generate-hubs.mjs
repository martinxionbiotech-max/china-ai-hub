#!/usr/bin/env node
/**
 * generate-hubs.mjs — build-time generator for the six dimension hub pages.
 *
 * Reads the hub definitions in scripts/hub-rules.json (single source of truth
 * for slugs, titles, editorial text and the per-dimension filtering rule),
 * evaluates each rule against the frontmatter of every model in
 * src/content/models/*.md, and writes src/data/hubs.json with the resulting
 * member model_ids. No counts or member lists are written by hand anywhere:
 * the count is always `members.length`, derived from frontmatter.
 *
 * The rendered hub pages (src/pages/models/<slug>.astro -> ModelHub.astro)
 * read hubs.json, so the build never re-evaluates the rule and can't drift
 * from this generator. scripts/check-entity-counts.py independently re-reads
 * the frontmatter and re-applies the same rules to verify 0 discrepancies.
 *
 * Usage:
 *   node scripts/generate-hubs.mjs
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const MODELS_DIR = path.join(ROOT, 'src', 'content', 'models');
const RULES_PATH = path.join(ROOT, 'scripts', 'hub-rules.json');
const OUT_PATH = path.join(ROOT, 'src', 'data', 'hubs.json');

/* ----------------------------- rule engine ----------------------------- */

function resolvePath(obj, dotted) {
  let cur = obj;
  for (const key of dotted.split('.')) {
    if (cur == null || typeof cur !== 'object') return undefined;
    cur = cur[key];
  }
  return cur;
}

function evalRule(data, rule) {
  switch (rule.op) {
    case 'eq':
      return resolvePath(data, rule.path) === rule.value;
    case 'gte': {
      const v = resolvePath(data, rule.path);
      return typeof v === 'number' && v >= rule.value;
    }
    case 'contains_ci': {
      const v = resolvePath(data, rule.path);
      return typeof v === 'string' && v.toLowerCase().includes(String(rule.value).toLowerCase());
    }
    case 'present': {
      const v = resolvePath(data, rule.path);
      return v != null && v !== '';
    }
    case 'any':
      return rule.rules.some((r) => evalRule(data, r));
    default:
      throw new Error(`Unknown rule op: ${rule.op}`);
  }
}

/* --------------------------- frontmatter load --------------------------- */

function readFrontmatter(filePath) {
  const text = fs.readFileSync(filePath, 'utf8');
  const m = text.match(/^---\s*\r?\n([\s\S]*?)\r?\n---/);
  if (!m) throw new Error(`No frontmatter found in ${filePath}`);
  return yaml.load(m[1]);
}

/* ------------------------------- generate ------------------------------- */

const rulesDoc = JSON.parse(fs.readFileSync(RULES_PATH, 'utf8'));
const modelFiles = fs
  .readdirSync(MODELS_DIR)
  .filter((f) => f.endsWith('.md'))
  .sort();

const models = modelFiles.map((f) => ({
  file: f,
  data: readFrontmatter(path.join(MODELS_DIR, f)),
}));

const hubs = rulesDoc.hubs.map((hub) => {
  const members = models
    .filter(({ data }) => evalRule(data, hub.rule))
    .map(({ data }) => data.model_id)
    .sort();
  // Editorial text and link lists are copied from the rule config verbatim;
  // only `members` (and therefore the count) is computed here.
  return {
    slug: hub.slug,
    title: hub.title,
    description: hub.description,
    short_answer: hub.short_answer,
    why_it_matters: hub.why_it_matters,
    rule_description: hub.rule_description,
    guides: hub.guides,
    research: hub.research,
    technology: hub.technology,
    members,
  };
});

fs.mkdirSync(path.dirname(OUT_PATH), { recursive: true });
fs.writeFileSync(OUT_PATH, JSON.stringify({ hubs }, null, 2) + '\n');

/* -------------------------------- report -------------------------------- */

console.log('Dimension hub generation complete.');
console.log(`  models read : ${models.length}`);
console.log(`  rules       : ${rulesDoc.hubs.length}`);
console.log(`  output      : ${path.relative(ROOT, OUT_PATH)}`);
console.log('');
console.log('| hub          | count | rule');
console.log('| ------------ | ----- | ----');
for (const hub of hubs) {
  console.log(`| ${hub.slug.padEnd(12)} | ${String(hub.members.length).padStart(5)} | ${hub.rule_description}`);
}
