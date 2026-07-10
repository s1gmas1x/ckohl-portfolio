<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            A production app slowed down soon after a reported platform update. The work
            was to check that timing without pretending timing alone proved the cause.
          </p>
        </div>

        <div class="summary-grid">
          <CaseStudySummaryCard
            label="Environment"
            value="Azure App Service, enterprise workload, production web application"
          />
          <CaseStudySummaryCard
            label="Method"
            value="Telemetry review, platform comparison, and one controlled infrastructure move"
          />
          <CaseStudySummaryCard
            label="Outcome"
            value="Evidence associated the issue with hosting environment behavior"
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

        <aside class="case-study-sidebar" aria-label="Azure platform update case study details">
          <CaseStudyDetailCard title="Environment">
            <div class="tag-list" aria-label="Environment">
              <q-chip v-for="item in environment" :key="item" outline square>
                {{ item }}
              </q-chip>
            </div>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Tools Used">
            <q-list dense>
              <q-item v-for="tool in toolsUsed" :key="tool">
                <q-item-section avatar>
                  <q-icon name="query_stats" color="primary" />
                </q-item-section>
                <q-item-section>{{ tool }}</q-item-section>
              </q-item>
            </q-list>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Investigation Focus">
            <q-list dense>
              <q-item v-for="item in investigationFocus" :key="item">
                <q-item-section avatar>
                  <q-icon name="manage_search" color="primary" />
                </q-item-section>
                <q-item-section>{{ item }}</q-item-section>
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

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/azure-platform-update')

useMeta(
  createPageMeta({
    title: `${caseStudy.title} | Chad Kohl Case Study`,
    description: caseStudy.summary,
    path: caseStudy.path,
    socialTitle: `${caseStudy.title} | Chad Kohl`,
    socialDescription: caseStudy.summary,
  }),
)

const environment = ['Azure App Service', 'Enterprise customer workload', 'Production web application']

const toolsUsed = [
  'Azure App Service diagnostics',
  'App Service platform telemetry',
  'Instance Allocations',
  'Symptom and timing comparison',
]

const investigationFocus = [
  'Compared symptoms with available platform data',
  'Checked whether timing matched the reported platform change',
  'Investigated instance allocation data',
  'Used a controlled move to test whether behavior changed with the hosting environment',
]

const lessonsLearned = [
  'Correlation does not automatically establish causation',
  'A controlled infrastructure move can be a useful test',
  'Platform telemetry is useful when it is tied back to observed symptoms',
  'Do not overstate the conclusion when the evidence only narrows the field',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Performance degradation after a reported platform update',
    paragraphs: [
      'A customer reported performance degradation in a production web application hosted on Azure App Service.',
      'The timing made the platform update a reasonable suspect. It was not enough, by itself, to prove that the update caused the slowdown.',
    ],
  },
  {
    eyebrow: 'Investigation',
    title: 'Evaluate correlation before assigning cause',
    paragraphs: [
      'The investigation reviewed available diagnostics, platform information, and instance allocation data.',
      'The goal was to compare the customer\'s symptoms with platform signals while keeping another possibility open: the workload might be affected by the specific hosting environment underneath it.',
    ],
  },
  {
    eyebrow: 'Hypothesis',
    title: 'Use movement across infrastructure as a diagnostic signal',
    paragraphs: [
      'The working hypothesis was intentionally limited: if the issue was related to the underlying hosting environment rather than application code, moving the workload to a different App Service stamp could give the investigation a useful signal.',
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
      'The useful part was not a dramatic root-cause claim. It was a narrower problem space built from observed behavior, platform telemetry, and one controlled change.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Controlled changes help isolate complex platform issues',
    paragraphs: [
      'This case reinforced that correlation does not automatically establish causation, especially when symptoms appear near a platform event.',
      'It also showed how a small, controlled infrastructure change can make a messy production issue less vague.',
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
