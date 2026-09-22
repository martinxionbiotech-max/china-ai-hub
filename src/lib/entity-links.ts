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
  }
  return map;
}

export function modelHref(map: Map<string, string>, name: string): string {
  return `/models/${map.get(name) ?? name}/`;
}
