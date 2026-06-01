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
            An anonymized Azure App Service investigation into production application
            performance degradation that appeared shortly after a platform update.
          </p>
        </div>

        <div class="summary-grid">
          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Environment</span>
              <strong>Azure App Service, enterprise workload, production web application</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Method</span>
              <strong>Telemetry review, platform analysis, and controlled infrastructure change</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Outcome</span>
              <strong>Evidence associated the issue with hosting environment behavior</strong>
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

        <aside class="case-study-sidebar" aria-label="Azure platform update case study details">
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
              <h2>Investigation Focus</h2>
              <q-list dense>
                <q-item v-for="item in investigationFocus" :key="item">
                  <q-item-section avatar>
                    <q-icon name="manage_search" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ item }}</q-item-section>
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
import { caseStudies } from 'src/data/caseStudies.js'

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/azure-platform-update')

const environment = ['Azure App Service', 'Enterprise customer workload', 'Production web application']

const toolsUsed = [
  'Azure App Service diagnostics',
  'App Service platform telemetry',
  'Instance Allocations',
  'Performance analysis techniques',
]

const investigationFocus = [
  'Reviewed available telemetry and diagnostics',
  'Analyzed platform information',
  'Investigated instance allocation data',
  'Evaluated correlation between symptoms and platform changes',
  'Considered the underlying infrastructure hosting environment',
]

const lessonsLearned = [
  'Correlation does not automatically establish causation',
  'Infrastructure changes can be useful diagnostic tools',
  'Platform telemetry can provide valuable evidence',
  'Controlled changes can help isolate complex issues',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Performance degradation after a reported platform update',
    paragraphs: [
      'A customer reported performance degradation in a production web application hosted on Azure App Service.',
      'The customer observed that the issue appeared shortly after a platform update and suspected the platform update was responsible.',
    ],
  },
  {
    eyebrow: 'Investigation',
    title: 'Evaluate correlation before assigning cause',
    paragraphs: [
      'The investigation reviewed available telemetry and diagnostics, analyzed platform information, and inspected instance allocation data.',
      'The goal was to evaluate whether the reported symptoms correlated with platform changes while also considering whether the workload might be affected by the underlying infrastructure hosting environment.',
    ],
  },
  {
    eyebrow: 'Hypothesis',
    title: 'Use movement across infrastructure as a diagnostic signal',
    paragraphs: [
      'The working hypothesis was intentionally limited: if the issue was related to the underlying hosting environment rather than application code, moving the workload to a different App Service stamp could provide useful evidence.',
      'This did not assume a definitive root cause. It created a controlled change that could help isolate whether the behavior followed the application or changed with the hosting environment.',
    ],
  },
  {
    eyebrow: 'Resolution',
    title: 'Recommend a scale-up to move stamps',
    paragraphs: [
      'A scale-up operation was recommended because it would move the application to a different App Service stamp.',
      'After the move, the reported issue no longer occurred. That result provided useful evidence for the investigation without overstating what had been proven.',
    ],
  },
  {
    eyebrow: 'Outcome',
    title: 'Narrow the scope with evidence',
    paragraphs: [
      'The investigation provided evidence that the issue was associated with the hosting environment rather than the application itself.',
      'The troubleshooting process helped narrow the scope of the problem and guided next steps through observed behavior, platform telemetry, and a controlled infrastructure change.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Controlled changes help isolate complex platform issues',
    paragraphs: [
      'This case reinforced that correlation does not automatically establish causation, especially when symptoms appear near a platform event.',
      'It also showed how platform telemetry and controlled infrastructure changes can provide evidence when troubleshooting complex production performance issues.',
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
