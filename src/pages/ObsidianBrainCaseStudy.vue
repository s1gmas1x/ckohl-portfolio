<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            A personal knowledge system built in Obsidian to organize project context,
            career material, navigation rules, and dashboard-driven planning.
          </p>
        </div>

        <div class="summary-grid">
          <CaseStudySummaryCard
            label="System Focus"
            value="Project notes, career content, navigation patterns, and planning dashboards"
          />
          <CaseStudySummaryCard
            label="Stack"
            value="Obsidian, Markdown, linked notes, and structured dashboards"
          />
          <CaseStudySummaryCard
            label="Delivery"
            value="Static portfolio content derived from the local knowledge base"
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

        <aside class="case-study-sidebar" aria-label="Obsidian Brain case study details">
          <CaseStudyDetailCard title="Knowledge Stack">
            <div class="tag-list" aria-label="Knowledge stack">
              <q-chip v-for="technology in technologyStack" :key="technology" outline square>
                {{ technology }}
              </q-chip>
            </div>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="System Areas">
            <q-list dense>
              <q-item v-for="area in systemAreas" :key="area">
                <q-item-section avatar>
                  <q-icon name="account_tree" color="primary" />
                </q-item-section>
                <q-item-section>{{ area }}</q-item-section>
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

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/obsidian-brain')

useMeta(
  createPageMeta({
    title: `${caseStudy.title} | Chad Kohl Case Study`,
    description: caseStudy.summary,
    path: caseStudy.path,
    socialTitle: `${caseStudy.title} | Chad Kohl`,
    socialDescription: caseStudy.summary,
  }),
)

const technologyStack = ['Obsidian', 'Markdown', 'Linked notes', 'Dashboards', 'Content workflow']

const systemAreas = [
  'Project source notes',
  'Career content planning',
  'Navigation guidelines',
  'Executive dashboard views',
  'Portfolio content pipeline',
]

const designConstraints = [
  'Keep source notes easy to navigate',
  'Separate planning notes from publishable copy',
  'Make dashboards useful without adding process overhead',
  'Preserve enough context for future case study writing',
]

const lessonsLearned = [
  'A knowledge system is more useful when navigation rules are explicit',
  'Dashboards work best when they summarize decisions and next actions',
  'Project notes should preserve context without becoming final copy too early',
  'Static portfolio content benefits from a clear source-of-truth workflow',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Keep project knowledge usable after the work moves on',
    paragraphs: [
      'The Obsidian Brain project addresses a recurring portfolio and career problem: technical work creates useful context, but that context is easy to lose when notes, plans, and project details are scattered across different places.',
      'The system needed to support active project work, longer-term career content, and future portfolio writing without turning the knowledge base into another maintenance-heavy application.',
    ],
  },
  {
    eyebrow: 'Approach',
    title: 'Use linked notes as the operating layer',
    paragraphs: [
      'The core approach is a structured Obsidian vault organized around project notes, career content, navigation guidelines, and dashboard views. Markdown keeps the system portable, while links and indexes help connect related decisions across projects.',
      'Navigation guidelines give the vault a predictable shape, so the system can grow without relying on memory or one-off folder decisions.',
    ],
  },
  {
    eyebrow: 'Workflow',
    title: 'Separate thinking space from publishable output',
    paragraphs: [
      'Project notes can capture rough context, working decisions, implementation details, and follow-up ideas. Career content notes then translate that raw context into clearer positioning for portfolio pages, case studies, and professional summaries.',
      'That separation keeps the writing workflow useful: source notes can stay practical and incomplete, while published content can be edited for audience, structure, and accuracy.',
    ],
  },
  {
    eyebrow: 'Dashboard Design',
    title: 'Make the system navigable from durable entry points',
    paragraphs: [
      'Dashboard views act as stable entry points for current work and executive-level planning. Instead of depending on search alone, the dashboard gives the knowledge base a front door for priorities, projects, and content work.',
      'This keeps the system useful during repeated visits because important paths are visible before the user has to remember exact note names or folder locations.',
    ],
  },
  {
    eyebrow: 'Implementation',
    title: 'Keep the portfolio integration static',
    paragraphs: [
      'For the portfolio, the Obsidian Brain case study is implemented as static frontend content. The site does not read from the vault at runtime and does not add shared-backend calls.',
      'This keeps the public case study stable while the underlying knowledge base can continue evolving privately.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Structure matters most when notes become source material',
    paragraphs: [
      'The project reinforced that personal knowledge systems need just enough structure to make future reuse possible. Too little structure makes notes hard to recover, while too much structure slows down capture.',
      'The useful middle ground is a vault with clear navigation rules, durable dashboards, and a workflow that treats notes as source material rather than finished content.',
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
