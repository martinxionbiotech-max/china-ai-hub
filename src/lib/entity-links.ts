import { getCollection } from 'astro:content';

/* ------------------------------------------------------------------ */
/* Astro's glob loader slugifies entry ids (dots removed:             */
/* "qwen3.8-max" -> "qwen38-max"), but entity data fields keep the    */
/* original dotted names. This resolver maps both forms to the real   */
/* entry id so every internal link points at a built URL.             */
/* ------------------------------------------------------------------ */

export async function getModelIdMap(): Promise<Map<string, string>> {
  const models = await getCollection('models');
  const map = new Map<string, string>();
  for (const m of models) {
    map.set(m.id, m.id);
    map.set(m.data.model_id, m.id);
    map.set(m.data.model_name, m.id);
    map.set(m.data.model_name.toLowerCase(), m.id);
    map.set(slugifyEntity(m.data.model_name), m.id);
    map.set(slugifyEntity(m.data.model_id), m.id);
  }
  return map;
}

/** Fallback slug for a display name: "Kimi K3" -> "kimi-k3", "GLM-5.3" -> "glm-53". */
export function slugifyEntity(name: string): string {
  return name
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

export function modelHref(map: Map<string, string>, name: string): string {
  const direct = map.get(name);
  if (direct) return `/models/${direct}/`;
  const slug = slugifyEntity(name);
  return `/models/${map.get(slug) ?? slug}/`;
}
