<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <q-btn
          flat
          no-caps
          color="primary"
          icon="arrow_back"
          label="Back to portfolio"
          to="/"
          class="back-link"
        />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            KitchenRatio is a baking and recipe scaling platform focused on baker's
            percentages and dough hydration calculations.
          </p>

          <div class="hero-actions">
            <q-btn
              unelevated
              no-caps
              color="primary"
              icon-right="open_in_new"
              label="View live application"
              :href="liveApplicationUrl"
              target="_blank"
              rel="noopener noreferrer"
            />
          </div>
        </div>

        <div class="summary-grid">
          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Focus</span>
              <strong>Baker's math, hydration, recipe scaling, and baking education</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Stack</span>
              <strong>Vue 3, Vite, Pinia, VitePress, Netlify, and Cloudflare</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Deployment</span>
              <strong>Frontend hosted on Netlify with Cloudflare for DNS and traffic</strong>
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

        <aside class="case-study-sidebar" aria-label="KitchenRatio case study details">
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
              <h2>Engineering Challenges</h2>
              <q-list dense>
                <q-item v-for="challenge in engineeringChallenges" :key="challenge">
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
              <h2>SEO Work</h2>
              <q-list dense>
                <q-item v-for="item in seoWork" :key="item">
                  <q-item-section avatar>
                    <q-icon name="trending_up" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ item }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Project Links</h2>
              <q-btn
                outline
                no-caps
                color="primary"
                icon-right="open_in_new"
                label="KitchenRatio calculator"
                :href="liveApplicationUrl"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link"
              />
              <q-btn
                outline
                no-caps
                color="primary"
                icon-right="open_in_new"
                label="Educational content"
                :href="educationalContentUrl"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link"
              />
            </q-card-section>
          </q-card>
        </aside>
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { caseStudies } from 'src/data/caseStudies.js'
import { projects } from 'src/data/projects.js'

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/kitchenratio')
const kitchenRatioProject = projects.find((project) => project.title.includes('KitchenRatio'))
const liveApplicationUrl = kitchenRatioProject?.url ?? 'https://kitchenratio.com/calculator'
const educationalContentUrl = 'https://kitchenratio.com'

const technologyStack = ['Vue 3', 'Vite', 'Pinia', 'VitePress', 'Netlify', 'Cloudflare']

const keyFeatures = [
  "Baker's percentage calculations",
  'Dough hydration calculations',
  'Recipe scaling',
  'Saved recipes (planned)',
  'Educational baking guides',
]

const seoWork = [
  'Added sitemap',
  'Added robots.txt',
  'Added Open Graph metadata',
  'Added route-based meta tags',
  'Submitted site to Google Search Console',
  'Added Google Analytics',
  'Optimized content structure for search indexing',
]

const engineeringChallenges = [
  "Designing a flexible baker's math calculation engine",
  'Balancing simplicity and advanced baking concepts',
  'Integrating documentation and calculator experiences',
  'Maintaining responsive design for mobile users',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Making baker\'s math easier to understand',
    paragraphs: [
      "KitchenRatio addresses a practical challenge for bakers: baker's percentages and hydration calculations are powerful, but they can be hard to apply consistently when scaling recipes or learning dough formulas.",
      'The platform needed to support accurate calculation workflows while also making the underlying concepts approachable through educational baking content.',
    ],
  },
  {
    eyebrow: 'Solution',
    title: 'A focused calculator and learning platform',
    paragraphs: [
      'The solution centers on recipe scaling, hydration percentages, and clear calculator flows for common baking decisions. Planned saved recipes extend that workflow by giving bakers a path to return to formulas over time.',
      'VitePress supports the documentation and guide experience, while the Vue 3 application provides the interactive calculator interface.',
    ],
  },
  {
    eyebrow: 'Implementation',
    title: 'Flexible calculations with responsive delivery',
    paragraphs: [
      "The engineering work focused on designing a flexible baker's math calculation engine that could support simple recipe scaling and more advanced baking concepts without making the interface feel overly complex.",
      'The frontend uses Vue 3, Vite, and Pinia. VitePress supports the educational content experience, Netlify hosts the frontend, and Cloudflare handles DNS and traffic management.',
      'SEO and analytics work included sitemap and robots.txt setup, Open Graph metadata, route-based meta tags, Google Search Console submission, Google Analytics, and search-friendly content structure.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Balance precision with clarity',
    paragraphs: [
      'KitchenRatio reinforced the importance of pairing accurate domain logic with clear user-facing language. Baking calculations require precision, but the experience also needs to guide users who are still learning the concepts.',
      'The project also highlighted the value of integrating documentation and calculator experiences so educational content can support the tool rather than live separately from it.',
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

.back-link {
  margin-bottom: 40px;
  font-weight: 700;
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

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
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

.project-link {
  justify-self: start;
  font-weight: 700;
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

  .back-link {
    margin-bottom: 28px;
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
