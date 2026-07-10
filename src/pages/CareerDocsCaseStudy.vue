<template>
  <q-page class="case-study-page">
    <section class="case-study-hero">
      <div class="case-study-inner">
        <PageBackLink />

        <div class="case-study-heading">
          <p class="eyebrow">{{ caseStudy.category }}</p>
          <h1>{{ caseStudy.title }}</h1>
          <p>
            A career document workflow that keeps Markdown as the source of truth while
            CareerDocs handles structured rendering, review, and export-ready output.
          </p>
        </div>

        <div class="summary-grid">
          <CaseStudySummaryCard
            label="Source of Truth"
            value="Markdown career content, resume instructions, and reusable project narratives"
          />
          <CaseStudySummaryCard
            label="Rendering Layer"
            value="CareerDocs structures the content into readable resume and career documents"
          />
          <CaseStudySummaryCard
            label="Boundary"
            value="Static portfolio case study with no claims about automated hiring outcomes"
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

        <aside class="case-study-sidebar" aria-label="CareerDocs case study details">
          <CaseStudyDetailCard title="Workflow Stack">
            <div class="tag-list" aria-label="Workflow stack">
              <q-chip v-for="technology in technologyStack" :key="technology" outline square>
                {{ technology }}
              </q-chip>
            </div>
          </CaseStudyDetailCard>

          <CaseStudyDetailCard title="Pipeline Stages">
            <q-list dense>
              <q-item v-for="stage in pipelineStages" :key="stage">
                <q-item-section avatar>
                  <q-icon name="schema" color="primary" />
                </q-item-section>
                <q-item-section>{{ stage }}</q-item-section>
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

const caseStudy = caseStudies.find((item) => item.path === '/case-studies/careerdocs')

useMeta(
  createPageMeta({
    title: `${caseStudy.title} | Chad Kohl Case Study`,
    description: caseStudy.summary,
    path: caseStudy.path,
    socialTitle: `${caseStudy.title} | Chad Kohl`,
    socialDescription: caseStudy.summary,
  }),
)

const technologyStack = ['Markdown', 'CareerDocs', 'Vue 3', 'Quasar', 'Document workflow']

const pipelineStages = [
  'Capture career content in Markdown',
  'Maintain resume generation instructions separately',
  'Transform source material into structured document views',
  'Review content before export',
  'Produce consistent resume and career document outputs',
]

const designConstraints = [
  'Keep Markdown as the source of truth',
  'Treat CareerDocs as the rendering and export layer',
  'Avoid implying automated hiring outcomes',
  'Make content review explicit before documents are reused',
]

const lessonsLearned = [
  'Career content is easier to maintain when source and presentation are separate',
  'Reusable narratives reduce rewriting across resume and portfolio contexts',
  'Document tooling should support judgment rather than replace it',
  'Clear instructions make generated drafts easier to review and improve',
]

const narrativeSections = [
  {
    eyebrow: 'Problem',
    title: 'Career documents need consistency without becoming locked to one format',
    paragraphs: [
      'Resume content, project summaries, and career narratives often need to appear in more than one format. Editing each document directly creates drift, because the same experience can be phrased differently across resumes, profiles, and portfolio material.',
      'The CareerDocs workflow addresses that maintenance problem by separating durable source material from the rendered documents people eventually read.',
    ],
  },
  {
    eyebrow: 'Source Workflow',
    title: 'Use Markdown as the source of truth',
    paragraphs: [
      'The content pipeline starts with Markdown notes for career material, project narratives, and resume generation instructions. Those files preserve the underlying context in a portable format that can be reviewed, revised, and reused over time.',
      'Keeping Markdown as the source of truth prevents the rendering layer from becoming the only place where career content exists. The source material stays editable even if the presentation format changes later.',
    ],
  },
  {
    eyebrow: 'Rendering Layer',
    title: 'Let CareerDocs structure and export the content',
    paragraphs: [
      'CareerDocs sits downstream from the Markdown source material. Its role is to organize the content into readable document views, support review, and produce export-ready career documents.',
      'That division is deliberate: Markdown owns the durable facts and reusable phrasing, while CareerDocs owns presentation, document structure, and export workflows.',
    ],
  },
  {
    eyebrow: 'Workflow Design',
    title: 'Keep human review in the loop',
    paragraphs: [
      'The pipeline supports drafting and formatting, but it does not imply automated hiring outcomes or promise that documents will produce interviews. The value is operational: reduce duplicated writing, make updates easier, and keep documents consistent.',
      'Human review remains part of the workflow because career documents need judgment, audience awareness, and careful editing before they are reused.',
    ],
  },
  {
    eyebrow: 'Implementation',
    title: 'Document the pipeline as static frontend content',
    paragraphs: [
      'This portfolio page is static frontend content. It documents the CareerDocs and career document pipeline without reading Markdown notes at runtime or adding backend calls.',
      'That keeps the public case study stable while the underlying source notes and CareerDocs workflow can continue to evolve privately.',
    ],
  },
  {
    eyebrow: 'Lessons Learned',
    title: 'Separate source content from output formatting',
    paragraphs: [
      'The project reinforced that document systems are easier to maintain when source material and rendering responsibilities are explicit. Markdown provides a portable editing layer; CareerDocs provides a focused document experience.',
      'That boundary makes the workflow easier to reason about and reduces the risk of treating any generated or rendered output as final without review.',
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
