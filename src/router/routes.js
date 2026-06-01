const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
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
