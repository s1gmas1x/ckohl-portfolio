<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            An anonymized Azure App Service performance investigation case study focused
            on evidence-based diagnostics for production web applications.
          </p>
        </div>

        <div class="summary-grid">
          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Environment</span>
              <strong>Azure App Service, production web applications, enterprise workloads</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Symptoms</span>
              <strong>Slow response times, intermittent latency, and degradation under load</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Focus</span>
              <strong>Use telemetry and diagnostics to narrow possible causes</strong>
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

        <aside class="case-study-sidebar" aria-label="Azure performance case study details">
          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Environment</h2>
              <div class="tag-list" aria-label="Environment">
                <q-chip v-for="item in environment" :key="item" outline square>
                  {{ item }}
                </q-chip>
              </div>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Reported Symptoms</h2>
              <q-list dense>
                <q-item v-for="symptom in reportedSymptoms" :key="symptom">
                  <q-item-section avatar>
                    <q-icon name="speed" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ symptom }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Tools Used</h2>
              <q-list dense>
                <q-item v-for="tool in toolsUsed" :key="tool">
                  <q-item-section avatar>
                    <q-icon name="query_stats" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ tool }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Lessons Learned</h2>
              <q-list dense>
                <q-item v-for="lesson in lessonsLearned" :key="lesson">
                  <q-item-section avatar>
                    <q-icon name="lightbulb" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ lesson }}</q-item-section>
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
import { useMeta } from 'quasar'
import PageBackLink from 'src/components/PageBackLink.vue'
import { caseStudies } from 'src/data/caseStudies.js'
import { createPageMeta } from 'src/utils/seo.js'

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/azure-performance')

useMeta(
  createPageMeta({
    title: `${caseStudy.title} | Chad Kohl Case Study`,
    description: caseStudy.summary,
    path: caseStudy.path,
    socialTitle: `${caseStudy.title} | Chad Kohl`,
    socialDescription: caseStudy.summary,
  }),
)

const environment = [
  'Azure App Service',
  'Production web applications',
  'Enterprise customer workloads',
]

const reportedSymptoms = [
  'Slow response times',
  'Intermittent latency',
  'Performance degradation under load',
]

const toolsUsed = [
  'Azure App Service',
  'App Lens',
  'Performance telemetry',
  'Memory analysis',
  'Diagnostic logs',
]

const lessonsLearned = [
  'Performance issues rarely have a single obvious cause',
  'Telemetry is critical for diagnosis',
  'Evidence should drive conclusions',
  'Eliminating possibilities is often as valuable as confirming them',
  'Structured troubleshooting reduces time to resolution',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Production performance issues across App Service workloads',
    paragraphs: [
      'Customers reported Azure App Service performance issues including slow response times, intermittent latency, and performance degradation under load.',
      'The investigation needed to avoid assuming a single cause and instead determine whether the symptoms were more likely connected to application code, infrastructure, resource constraints, or external dependencies.',
    ],
  },
  {
    eyebrow: 'Investigation',
    title: 'Separate possible sources of latency',
    paragraphs: [
      'The investigation process focused on identifying where the issue might originate. That meant evaluating application behavior, infrastructure signals, resource usage, and dependency patterns together instead of treating any one layer as the presumed cause.',
      'This approach helped keep the troubleshooting process structured while preserving room for multiple possible explanations.',
    ],
  },
  {
    eyebrow: 'Diagnostic Approach',
    title: 'Use telemetry to narrow the field',
    paragraphs: [
      'Typical techniques included reviewing App Lens diagnostics, analyzing performance telemetry, reviewing memory and CPU usage, evaluating application behavior patterns, and comparing platform metrics with reported symptoms.',
      'The goal was to let evidence narrow the possible causes. In many cases, eliminating unlikely causes was as important as confirming a likely one.',
    ],
  },
  {
    eyebrow: 'Findings',
    title: 'Establish evidence-based conclusions',
    paragraphs: [
      'The primary value of the investigation was establishing evidence-based conclusions and narrowing the scope of potential causes.',
      'The troubleshooting process focused on identifying actionable next steps rather than making assumptions or claiming root causes that had not been definitively proven.',
    ],
  },
  {
    eyebrow: 'Outcome',
    title: 'Guide future remediation efforts',
    paragraphs: [
      'The investigations helped customers better understand the likely source of performance issues and guided future remediation efforts.',
      'The outcome was a clearer diagnostic picture: what evidence supported, what had been ruled out, and where follow-up work should focus.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Structured troubleshooting improves clarity',
    paragraphs: [
      'Performance issues rarely have a single obvious cause, especially in production systems where application behavior, hosting infrastructure, resource usage, and dependencies interact.',
      'Telemetry, diagnostic logs, and structured elimination helped drive conclusions while avoiding unsupported claims.',
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
