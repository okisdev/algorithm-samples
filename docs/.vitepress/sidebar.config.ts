import { type DefaultTheme } from 'vitepress';

export function SortingSidebar(): DefaultTheme.SidebarItem[] {
    return [
        {
            text: 'Intro',
            link: '/sorting/index',
        },
        {
            text: 'Bubble Sort',
            link: '/sorting/bubble-sort',
        },
        {
            text: 'Quick Sort',
            link: '/sorting/quick-sort',
        },
    ];
}
