import { defineConfig } from 'vitepress';

import { SortingSidebar } from './sidebar.config';

// https://vitepress.dev/reference/site-config
export default defineConfig({
    lang: 'zh-HK',
    title: 'Algorithm Samples',
    description: 'A collection of algorithms.',

    lastUpdated: true,
    cleanUrls: true,

    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Basic', link: '/basic/index' },
            { text: 'Sorting', link: '/sorting/index' },
        ],

        sidebar: {
            '/sorting/': SortingSidebar(),
        },

        socialLinks: [{ icon: 'github', link: 'https://github.com/okisdev/algorithm-samples' }],

        footer: {
            message: 'MIT License.',
            copyright: 'Copyright © 2023 Harry Yep',
        },
    },
});
