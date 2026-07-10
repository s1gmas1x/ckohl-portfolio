<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            An anonymized troubleshooting case study involving long database reconnection
            times after SQL mirror failover for an ASP.NET Framework application on Azure
            App Service.
          </p>
        </div>

        <div class="summary-grid">
          <CaseStudySummaryCard
            label="Environment"
            value="Azure App Service, ASP.NET Framework 4.8, SQL Server, SQL mirroring"
          />
          <CaseStudySummaryCard
            label="Focus"
            value="Reproducing the delay and separating hosting behavior from app and database behavior"
          />
          <CaseStudySummaryCard
            label="Outcome"
            value="Evidence showed the delay was not caused by Azure App Service itself"
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

        <aside class="case-study-sidebar" aria-label="Azure troubleshooting case study details">
          <CaseStudyDetailCard title="Environment">
            <div class="tag-list" aria-label="Environment">
              <q-chip v-for="item in environment" :key="item" outline square>
                {{ item }}
              </q-chip>
            </div>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Tools and Techniques">
            <q-list dense>
              <q-item v-for="tool in toolsAndTechniques" :key="tool">
                <q-item-section avatar>
                  <q-icon name="manage_search" color="primary" />
                </q-item-section>
                <q-item-section>{{ tool }}</q-item-section>
              </q-item>
            </q-list>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Findings">
            <q-list dense>
              <q-item v-for="finding in findings" :key="finding">
                <q-item-section avatar>
                  <q-icon name="fact_check" color="primary" />
                </q-item-section>
                <q-item-section>{{ finding }}</q-item-section>
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

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/azure-troubleshooting')

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
  'ASP.NET Framework 4.8',
  'SQL Server',
  'SQL mirroring',
]

const toolsAndTechniques = [
  'Azure App Service diagnostics',
  'Reproduction testing',
  'Hosting environment comparison',
  'Application and database behavior review',
]

const findings = [
  'The delay could be reproduced consistently',
  'The App Service platform was not the source of the delay',
  'The next investigation needed to focus outside the hosting platform',
]

const lessonsLearned = [
  'Reproduce the behavior before debating the cause',
  'Compare environments carefully when the same app behaves differently',
  'Keep platform, app, and database assumptions separate until the data supports one',
  'Document what was ruled out so the next step is not guesswork',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Long reconnect times after SQL mirror failover',
    paragraphs: [
      'A customer reported that after a SQL mirror failover, an ASP.NET Framework 4.8 application running on Azure App Service experienced very long database reconnection times.',
      'The same application running on a virtual machine reconnected almost immediately, which led the customer to suspect that Azure App Service was causing the delay.',
    ],
  },
  {
    eyebrow: 'Hypothesis',
    title: 'Do not blame the host just because the symptom appears there',
    paragraphs: [
      'The investigation started with one question: was Azure App Service introducing the reconnect delay, or was the difference coming from the application, database, client connection behavior, or failover path?',
      'That required comparing environments and reproducing the behavior instead of assigning cause based only on where the symptom was easiest to see.',
    ],
  },
  {
    eyebrow: 'Investigation',
    title: 'Build a reproducible comparison',
    paragraphs: [
      'The work included reviewing the application architecture, comparing App Service and VM behavior, and working with engineering resources to create a repeatable test environment.',
      'That made it possible to watch the delay happen on demand. The comparison showed what changed between hosting environments and what stayed tied to the application and database path.',
    ],
  },
  {
    eyebrow: 'Resolution',
    title: 'Narrow the platform boundary with evidence',
    paragraphs: [
      'The issue was reproduced consistently, but the investigation showed that Azure App Service itself was not causing the long reconnect behavior.',
      'That shifted the work away from changing the hosting platform and toward the parts of the stack that still matched the evidence.',
    ],
  },
  {
    eyebrow: 'Outcome',
    title: 'Clarify responsibility and avoid unnecessary remediation',
    paragraphs: [
      'The investigation clarified platform responsibility and helped prevent unnecessary App Service changes.',
      'The main value was practical: the work narrowed the issue, documented the evidence, and gave the customer a better place to look next.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Make the evidence carry the conclusion',
    paragraphs: [
      'This scenario reinforced the importance of reproduction testing and comparative testing when symptoms differ across environments.',
      'It also showed why good support work depends on resisting early assumptions and being clear about what the evidence does and does not prove.',
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
