<template>
  <q-page class="case-studies-page">
    <section class="case-studies-hero">
      <div class="case-studies-inner">
        <PageBackLink label="Back to home" />

        <SectionHeader
          eyebrow="Case Studies"
          title="Engineering case studies"
          title-tag="h1"
          description="A fuller set of product, debugging, platform, and application design writeups from selected projects and technical investigations."
          max-width="760px"
        />
      </div>
    </section>

    <section class="case-studies-section">
      <div class="case-studies-inner case-study-groups">
        <section
          v-for="group in groupedCaseStudies"
          :key="group.title"
          class="case-study-group"
          :aria-labelledby="group.headingId"
        >
          <div class="case-study-group__header">
            <p>{{ group.eyebrow }}</p>
            <h2 :id="group.headingId">{{ group.title }}</h2>
            <span>{{ group.description }}</span>
          </div>

          <div class="case-study-card-grid">
            <CaseStudyCard
              v-for="caseStudy in group.caseStudies"
              :key="caseStudy.title"
              :case-study="caseStudy"
            />
          </div>
        </section>
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { useMeta } from 'quasar'
import CaseStudyCard from 'src/components/CaseStudyCard.vue'
import PageBackLink from 'src/components/PageBackLink.vue'
import SectionHeader from 'src/components/SectionHeader.vue'
import { caseStudies } from 'src/data/caseStudies.js'
import { createPageMeta } from 'src/utils/seo.js'

const caseStudyGroupDefinitions = [
  {
    title: 'Product and application work',
    headingId: 'product-application-work',
    eyebrow: 'Build',
    description: 'Tools, applications, and platform pieces shaped around real workflows.',
    paths: [
      '/case-studies/kitchenratio',
      '/case-studies/garden-planning',
      '/case-studies/shared-backend',
    ],
  },
  {
    title: 'Cloud diagnostics',
    headingId: 'cloud-diagnostics',
    eyebrow: 'Investigate',
    description: 'Azure support case studies focused on symptoms, evidence, and narrowing causes.',
    paths: [
      '/case-studies/azure-troubleshooting',
      '/case-studies/azure-platform-update',
      '/case-studies/azure-performance',
    ],
  },
  {
    title: 'Knowledge and document systems',
    headingId: 'knowledge-document-systems',
    eyebrow: 'Organize',
    description: 'Workflows for turning notes, career material, and project context into useful outputs.',
    paths: ['/case-studies/obsidian-brain', '/case-studies/careerdocs'],
  },
]

const caseStudyByPath = new Map(caseStudies.map((caseStudy) => [caseStudy.path, caseStudy]))
const groupedCaseStudies = caseStudyGroupDefinitions.map((group) => ({
  ...group,
  caseStudies: group.paths.map((path) => caseStudyByPath.get(path)).filter(Boolean),
}))

useMeta(
  createPageMeta({
    title: 'Case Studies | Chad Kohl Developer Portfolio',
    description:
      'Read case studies from Chad Kohl covering product engineering, debugging, Azure platform diagnostics, and application design decisions.',
    path: '/case-studies',
    socialTitle: 'Case Studies by Chad Kohl | Full Stack Developer',
    socialDescription:
      'Read engineering case studies from Chad Kohl covering product decisions, debugging, Azure diagnostics, and application design.',
  })
)
</script>

<style lang="scss" scoped>
.case-studies-page {
  background: var(--ck-page-bg);
  color: var(--ck-text-primary);
}

.case-studies-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.case-studies-hero {
  padding: 48px 0 40px;
  background: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
}

body.body--dark .case-studies-hero {
  background:
    radial-gradient(circle at top left, rgba(249, 156, 30, 0.06), transparent 32%),
    linear-gradient(135deg, #070b10, #0b1016);
}

.case-studies-section {
  padding: 52px 0 64px;
}

.case-study-groups,
.case-study-group {
  display: grid;
}

.case-study-groups {
  gap: 56px;
}

.case-study-group {
  gap: 20px;
}

.case-study-group__header {
  display: grid;
  max-width: 760px;
  gap: 8px;
}

.case-study-group__header p,
.case-study-group__header h2,
.case-study-group__header span {
  margin: 0;
}

.case-study-group__header p {
  color: var(--ck-link);
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.case-study-group__header h2 {
  color: var(--ck-text-strong);
  font-size: 1.55rem;
  font-weight: 800;
  letter-spacing: 0;
  line-height: 1.2;
}

.case-study-group__header span {
  color: var(--ck-text-secondary);
  font-size: 0.98rem;
  line-height: 1.6;
}

.case-study-card-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

@media (max-width: 900px) {
  .case-studies-inner {
    width: min(100% - 48px, 1120px);
  }

  .case-study-card-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

}

@media (max-width: 640px) {
  .case-studies-hero {
    padding: 34px 0 36px;
  }

  .case-studies-section {
    padding: 38px 0 48px;
  }

  .case-study-groups {
    gap: 44px;
  }

  .case-study-group__header h2 {
    font-size: 1.35rem;
  }

  .case-study-card-grid {
    grid-template-columns: 1fr;
  }

}
</style>
