// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sinoaihub.com',
  output: 'static',
  vite: {
    plugins: [tailwindcss()],
  },
  integrations: [
    sitemap({
      // Model variants (X-Highspeed, FlashX) canonicalise to a parent model.
      // They stay reachable for people following an old link, but they are
      // noindex and must not compete in the sitemap.
      filter: (page) =>
        !/\/(glm-53-flashx|minimax-m27-highspeed|kimi-k27-code-highspeed)\/$/.test(page),
    }),
  ],
});
