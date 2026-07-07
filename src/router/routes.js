const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'projects', component: () => import('pages/ProjectsPage.vue') },
      { path: 'case-studies', component: () => import('pages/CaseStudiesPage.vue') },
      { path: 'about', component: () => import('pages/AboutPage.vue') },
      {
        path: 'case-studies/kitchenratio',
        component: () => import('pages/KitchenRatioCaseStudy.vue'),
      },
      {
        path: 'case-studies/azure-troubleshooting',
        component: () => import('pages/AzureTroubleshootingCaseStudy.vue'),
      },
      {
        path: 'case-studies/azure-platform-update',
        component: () => import('pages/AzurePlatformUpdateCaseStudy.vue'),
      },
      {
        path: 'case-studies/azure-performance',
        component: () => import('pages/AzurePerformanceCaseStudy.vue'),
      },
      {
        path: 'case-studies/garden-planning',
        component: () => import('pages/GardenPlanningCaseStudy.vue'),
      },
      {
        path: 'case-studies/obsidian-brain',
        component: () => import('pages/ObsidianBrainCaseStudy.vue'),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
