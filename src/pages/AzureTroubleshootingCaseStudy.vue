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
            An anonymized troubleshooting case study involving long database reconnection
            times after SQL mirror failover for an ASP.NET Framework application on Azure
            App Service.
          </p>
        </div>

        <div class="summary-grid">
          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Environment</span>
              <strong>Azure App Service, ASP.NET Framework 4.8, SQL Server, SQL mirroring</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Focus</span>
              <strong>Reproduction testing, comparative analysis, and platform isolation</strong>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="summary-card">
            <q-card-section>
              <span>Outcome</span>
              <strong>Evidence showed the delay was not caused by Azure App Service itself</strong>
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

        <aside class="case-study-sidebar" aria-label="Azure troubleshooting case study details">
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
              <h2>Tools and Techniques</h2>
              <q-list dense>
                <q-item v-for="tool in toolsAndTechniques" :key="tool">
                  <q-item-section avatar>
                    <q-icon name="manage_search" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ tool }}</q-item-section>
                </q-item>
              </q-list>
            </q-card-section>
          </q-card>

          <q-card flat bordered class="detail-card">
            <q-card-section>
              <h2>Findings</h2>
              <q-list dense>
                <q-item v-for="finding in findings" :key="finding">
                  <q-item-section avatar>
                    <q-icon name="fact_check" color="primary" />
                  </q-item-section>
                  <q-item-section>{{ finding }}</q-item-section>
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

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/azure-troubleshooting')

const environment = [
  'Azure App Service',
  'ASP.NET Framework 4.8',
  'SQL Server',
  'SQL mirroring',
]

const toolsAndTechniques = [
  'Azure App Service diagnostics',
  'Reproduction testing',
  'Platform analysis',
  'Comparative testing between environments',
]

const findings = [
  'The behavior was reproducible',
  'The delay was not caused by Azure App Service itself',
  'Evidence supported further investigation outside the App Service platform',
]

const lessonsLearned = [
  'Importance of reproduction testing',
  'Importance of comparative testing',
  'Avoiding assumptions during troubleshooting',
  'Using evidence to isolate root cause',
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
    title: 'Separate platform behavior from application and database behavior',
    paragraphs: [
      'The investigation started with a deliberately narrow question: was Azure App Service introducing the reconnect delay, or was the difference caused by behavior elsewhere in the application, database, or failover path?',
      'That hypothesis required comparing environments, reproducing the behavior, and avoiding assumptions based only on where the symptom appeared.',
    ],
  },
  {
    eyebrow: 'Investigation',
    title: 'Build a reproducible comparison',
    paragraphs: [
      'The troubleshooting process included reviewing the application architecture, comparing behavior between Azure App Service and VM environments, and working with engineering resources to create a reproducible test environment.',
      'Reproduction testing made it possible to observe the behavior consistently instead of relying on isolated reports. Comparative testing provided a way to evaluate what differed between hosting environments.',
    ],
  },
  {
    eyebrow: 'Resolution',
    title: 'Narrow the platform boundary with evidence',
    paragraphs: [
      'The issue was reproduced consistently, but the investigation demonstrated that Azure App Service itself was not the cause of the long reconnect behavior.',
      'That finding shifted the troubleshooting path away from App Service remediation and toward further investigation outside the App Service platform.',
    ],
  },
  {
    eyebrow: 'Outcome',
    title: 'Clarify responsibility and avoid unnecessary remediation',
    paragraphs: [
      'The investigation provided clarity about platform responsibility and helped prevent unnecessary platform-focused remediation efforts.',
      'The main value was diagnostic: the work narrowed the issue, documented the evidence, and gave the customer a clearer path for continued investigation.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Use evidence before assigning cause',
    paragraphs: [
      'This scenario reinforced the importance of reproduction testing and comparative testing when symptoms differ across environments.',
      'It also showed why effective troubleshooting depends on resisting early assumptions and using evidence to isolate where a root cause is most likely to live.',
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
