<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            A shared Laravel backend and internal platform layer for ckohl.com, designed
            to centralize site capabilities without turning the work into a public SaaS product.
          </p>
        </div>

        <div class="summary-grid">
          <CaseStudySummaryCard
            label="Platform Role"
            value="Shared backend services for ckohl.com portfolio and content workflows"
          />
          <CaseStudySummaryCard
            label="Stack"
            value="Laravel, API design, internal services, and structured content data"
          />
          <CaseStudySummaryCard
            label="Delivery"
            value="Static portfolio case study with no live backend calls from this page"
          />
        </div>
      </div>
    </section>

    <section class="case-study-content">
      <div class="case-study-inner content-grid">
        <article class="case-study-main">
          <section v-for="section in narrativeSections" :key="section.title" class="content-block">
            <p class="eyebrow">{{ section.eyebrow }}</p>
            <h2>{{ section.title }}</h2>
            <p v-for="paragraph in section.paragraphs" :key="paragraph">
              {{ paragraph }}
            </p>
          </section>
        </article>

        <aside class="case-study-sidebar" aria-label="ckohl.com shared backend case study details">
          <CaseStudyDetailCard title="Technology Stack">
            <div class="tag-list" aria-label="Technology stack">
              <q-chip v-for="technology in technologyStack" :key="technology" outline square>
                {{ technology }}
              </q-chip>
            </div>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Backend Responsibilities">
            <q-list dense>
              <q-item v-for="responsibility in backendResponsibilities" :key="responsibility">
                <q-item-section avatar>
                  <q-icon name="hub" color="primary" />
                </q-item-section>
                <q-item-section>{{ responsibility }}</q-item-section>
              </q-item>
            </q-list>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Design Constraints">
            <q-list dense>
              <q-item v-for="constraint in designConstraints" :key="constraint">
                <q-item-section avatar>
                  <q-icon name="rule" color="primary" />
                </q-item-section>
                <q-item-section>{{ constraint }}</q-item-section>
              </q-item>
            </q-list>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Lessons Learned">
            <q-list dense>
              <q-item v-for="lesson in lessonsLearned" :key="lesson">
                <q-item-section avatar>
                  <q-icon name="lightbulb" color="primary" />
                </q-item-section>
                <q-item-section>{{ lesson }}</q-item-section>
              </q-item>
            </q-list>
          </CaseStudyDetailCard>
        </aside>
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { useMeta } from 'quasar'
import CaseStudyDetailCard from 'src/components/CaseStudyDetailCard.vue'
import CaseStudySummaryCard from 'src/components/CaseStudySummaryCard.vue'
import PageBackLink from 'src/components/PageBackLink.vue'
import { caseStudies } from 'src/data/caseStudies.js'
import { createPageMeta } from 'src/utils/seo.js'

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/shared-backend')

useMeta(
  createPageMeta({
    title: `${caseStudy.title} | Chad Kohl Case Study`,
    description: caseStudy.summary,
    path: caseStudy.path,
    socialTitle: `${caseStudy.title} | Chad Kohl`,
    socialDescription: caseStudy.summary,
  }),
)

const technologyStack = ['Laravel', 'PHP', 'API design', 'Internal platform', 'Content workflows']

const backendResponsibilities = [
  'Centralize shared portfolio backend capabilities',
  'Support internal content and project workflows',
  'Keep frontend case studies static and independently deployable',
  'Provide a foundation for future ckohl.com services',
]

const designConstraints = [
  'Present the backend as internal infrastructure, not a public SaaS product',
  'Avoid live backend calls from static case study pages',
  'Keep the public portfolio resilient if backend services change',
  'Separate platform architecture from user-facing portfolio content',
]

const lessonsLearned = [
  'Internal platforms still need clear product boundaries',
  'Static frontend pages reduce coupling to backend availability',
  'Shared backend work should make future features easier to add',
  'Architecture decisions are clearer when public and private surfaces stay separate',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Centralize backend capabilities without overexposing the platform',
    paragraphs: [
      'ckohl.com needs room for portfolio content, project metadata, internal workflows, and future site capabilities. Those needs benefit from a shared backend, but the backend itself is not the product being sold to users.',
      'The challenge was to think about the backend as internal platform infrastructure: useful for organizing and powering ckohl.com, but intentionally separate from the public portfolio pages that visitors read.',
    ],
  },
  {
    eyebrow: 'Platform Approach',
    title: 'Build a Laravel foundation for shared site services',
    paragraphs: [
      'The shared backend is framed as a Laravel-based platform layer for ckohl.com. Its job is to provide durable service boundaries for site data and internal workflows rather than creating a public multi-tenant SaaS application.',
      'That framing keeps implementation decisions grounded in the needs of the portfolio ecosystem: maintainability, clear APIs, content support, and future extensibility.',
    ],
  },
  {
    eyebrow: 'Frontend Boundary',
    title: 'Keep case study pages static and resilient',
    paragraphs: [
      'This case study page does not call the backend at runtime. It is static frontend content that documents the architecture and product thinking without adding a live dependency to the portfolio route.',
      'That boundary matters because the public portfolio should remain fast, cacheable, and reliable even as internal backend services evolve behind the scenes.',
    ],
  },
  {
    eyebrow: 'Architecture',
    title: 'Separate internal services from public presentation',
    paragraphs: [
      'The backend can act as a shared home for capabilities that should not be duplicated across future ckohl.com experiences. Examples include structured project data, workflow support, and service boundaries that can be reused by more than one frontend surface.',
      'The public website remains a presentation layer. That separation makes it easier to change internal APIs or workflows without forcing each portfolio page to become a backend integration point.',
    ],
  },
  {
    eyebrow: 'Implementation Decisions',
    title: 'Design for extensibility without premature product claims',
    paragraphs: [
      'The implementation direction emphasizes practical internal platform work: clear Laravel application boundaries, maintainable API design, and a backend model that can support future site capabilities.',
      'The page deliberately avoids describing the backend as a public SaaS product. The more accurate framing is a shared internal backend that supports ckohl.com and leaves space for future services.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Internal platform work needs explicit boundaries',
    paragraphs: [
      'A shared backend can make a portfolio ecosystem easier to evolve, but only when its responsibilities are named clearly. Otherwise internal infrastructure can be mistaken for a product surface it was never meant to be.',
      'The useful boundary is simple: Laravel can support shared services and future workflows, while static case study pages stay independent, readable, and deployable without live backend calls.',
    ],
  },
]
</script>

<style lang="scss" scoped>
.case-study-page {
  background: var(--ck-page-bg);
  color: var(--ck-text-primary);
}

.case-study-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.case-study-hero {
  padding: 56px 0 72px;
  background: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
}

body.body--dark .case-study-hero {
  background: linear-gradient(135deg, var(--ck-charcoal), var(--ck-surface-dark));
}

.case-study-heading {
  max-width: 820px;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--ck-link);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.case-study-heading h1,
.content-block h2 {
  margin: 0;
  color: var(--ck-text-strong);
  font-weight: 800;
  letter-spacing: 0;
}

.case-study-heading h1 {
  font-size: 4.2rem;
  line-height: 1;
}

.case-study-heading p {
  max-width: 720px;
  margin: 24px 0 0;
  color: var(--ck-text-secondary);
  font-size: 1.15rem;
  line-height: 1.7;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
  margin-top: 44px;
}

.case-study-content {
  padding: 80px 0;
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 340px;
  gap: 48px;
  align-items: start;
}

.case-study-main {
  display: grid;
  gap: 44px;
}

.content-block h2 {
  font-size: 2rem;
  line-height: 1.15;
}

.content-block p:not(.eyebrow) {
  margin: 18px 0 0;
  color: var(--ck-text-secondary);
  font-size: 1rem;
  line-height: 1.75;
}

.case-study-sidebar {
  display: grid;
  gap: 18px;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-list :deep(.q-chip) {
  background: var(--ck-surface-subtle);
  border-color: var(--ck-border);
  color: var(--ck-text-primary);
}

@media (max-width: 900px) {
  .summary-grid,
  .content-grid {
    grid-template-columns: 1fr;
  }

  .case-study-heading h1 {
    font-size: 3.3rem;
  }
}

@media (max-width: 640px) {
  .case-study-inner {
    width: min(100% - 24px, 1120px);
  }

  .case-study-hero {
    padding: 40px 0 56px;
  }

  .case-study-heading h1 {
    font-size: 2.35rem;
    line-height: 1.04;
  }

  .case-study-heading p {
    font-size: 1rem;
  }

  .case-study-content {
    padding: 64px 0;
  }
}
</style>
