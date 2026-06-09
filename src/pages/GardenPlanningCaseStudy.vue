<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            A personal software project focused on helping gardeners plan, organize,
            and manage growing spaces throughout the season.
          </p>
        </div>

        <div class="summary-grid">
          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Product Focus</span>
              <strong>Garden planning, raised bed visualization, and seasonal workflows</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Stack</span>
              <strong>Laravel, Vue 3, Quasar, and PostgreSQL</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Architecture</span>
              <strong>API-backed product with database-driven plant information</strong>
            </q-card-section>
          </q-card>
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

        <aside class="case-study-sidebar" aria-label="Garden Planning App case study details">
          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Technology Stack</h2>
              <div class="tag-list" aria-label="Technology stack">
                <q-chip v-for="technology in technologyStack" :key="technology" outline square>
                  {{ technology }}
                </q-chip>
              </div>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Key Features</h2>
              <q-list dense>
                <q-item v-for="feature in keyFeatures" :key="feature">
                  <q-item-section avatar>
                    <q-icon name="check_circle" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ feature }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Technical Challenges</h2>
              <q-list dense>
                <q-item v-for="challenge in technicalChallenges" :key="challenge">
                  <q-item-section avatar>
                    <q-icon name="build_circle" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ challenge }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Future Roadmap</h2>
              <q-list dense>
                <q-item v-for="item in futureRoadmap" :key="item">
                  <q-item-section avatar>
                    <q-icon name="timeline" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ item }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>
        </aside>
      </div>
    </section>
  </q-page>
</template>

<script setup>
import PageBackLink from 'src/components/PageBackLink.vue'
import { caseStudies } from 'src/data/caseStudies.js'

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/garden-planning')

const technologyStack = ['Laravel', 'Vue 3', 'Quasar', 'PostgreSQL']

const keyFeatures = [
  'Interactive garden layout planning',
  'Raised bed management',
  'Plant information database',
  'Seasonal planning workflows',
  'Mobile-friendly experience',
]

const technicalChallenges = [
  'Designing a flexible garden layout system',
  'Managing plant information and spacing requirements',
  'Supporting different climates and growing conditions',
  'Balancing ease of use with advanced planning features',
]

const futureRoadmap = [
  'User accounts and synchronization',
  'Location-aware growing recommendations',
  'Weather integrations',
  'Frost date calculations',
  'Planting schedules',
  'Additional planning tools',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Organize seasonal garden planning in one product',
    paragraphs: [
      'The Garden Planning App is designed around a practical gardening workflow: planning growing spaces, managing raised beds, organizing seasonal activities, and keeping useful plant information in one application.',
      'The product needed to support both desktop planning sessions and mobile-friendly use while staying approachable for gardeners who may not want a complex planning tool.',
    ],
  },
  {
    eyebrow: 'Product Goals',
    title: 'Make planning clearer across the season',
    paragraphs: [
      'The goals are to simplify garden planning, visualize raised beds and growing areas, organize seasonal planting activities, provide useful gardening information in a single application, and support desktop and mobile workflows.',
      'Those goals shape the technical direction: the architecture needs enough structure for plant data and planning workflows while remaining flexible as product requirements evolve.',
    ],
  },
  {
    eyebrow: 'Architecture',
    title: 'API-backed product with responsive planning tools',
    paragraphs: [
      'The architecture uses a Laravel backend for API and business logic, with Vue 3 and Quasar powering a responsive frontend experience.',
      'PostgreSQL supports database-driven plant information, while modular feature development keeps the product easier to evolve as new planning tools are added.',
    ],
  },
  {
    eyebrow: 'Technical Decisions',
    title: 'Let product workflows drive implementation',
    paragraphs: [
      'The application follows a product-first design approach so technical decisions are grounded in garden planning workflows rather than abstract feature lists.',
      'Key decisions include database-backed plant information, modular feature development, and a frontend stack that can support interactive layouts, raised bed management, and mobile-friendly workflows.',
    ],
  },
  {
    eyebrow: 'Future Roadmap',
    title: 'Build toward more personalized planning',
    paragraphs: [
      'Future work includes user accounts and synchronization, location-aware growing recommendations, weather integrations, frost date calculations, planting schedules, and additional planning tools.',
      'These roadmap items influence the architecture because early data modeling and feature boundaries need to leave room for more personalized recommendations and scheduling capabilities.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Architecture has to leave room for product change',
    paragraphs: [
      'The project reinforced that product requirements evolve during development and that iterative development reduces risk.',
      'It also showed how early architecture decisions impact future flexibility, and why user workflows should drive technical decisions.',
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
.content-block h2,
.detail-card h2 {
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

.summary-card,
.detail-card {
  background: var(--ck-surface-bg);
  border-color: var(--ck-border);
  border-radius: 8px;
}

.summary-card :deep(.q-card__section) {
  display: grid;
  gap: 8px;
  padding: 22px;
}

.summary-card span {
  color: var(--ck-text-muted);
  font-size: 0.86rem;
  font-weight: 700;
}

.summary-card strong {
  color: var(--ck-text-primary);
  font-size: 1rem;
  line-height: 1.45;
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

.detail-card :deep(.q-card__section) {
  display: grid;
  gap: 16px;
  padding: 22px;
}

.detail-card h2 {
  font-size: 1.1rem;
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

.detail-card :deep(.q-item) {
  min-height: 36px;
  padding: 4px 0;
  color: var(--ck-text-secondary);
}

.detail-card :deep(.q-item__section--avatar) {
  min-width: 34px;
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
