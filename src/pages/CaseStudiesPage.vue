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
      <div class="case-studies-inner case-study-card-grid">
        <CaseStudyCard
          v-for="caseStudy in caseStudies"
          :key="caseStudy.title"
          :case-study="caseStudy"
        />
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

  .case-study-card-grid {
    grid-template-columns: 1fr;
  }

}
</style>
