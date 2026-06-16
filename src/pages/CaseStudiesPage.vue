<template>
  <q-page class="case-studies-page">
    <section class="case-studies-hero">
      <div class="case-studies-inner">
        <PageBackLink label="Back to home" />

        <div class="section-heading">
          <p class="eyebrow">Case Studies</p>
          <h1>Engineering case studies</h1>
          <p>
            A fuller set of product, debugging, platform, and application design writeups from
            selected projects and technical investigations.
          </p>
        </div>
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
import { caseStudies } from 'src/data/caseStudies.js'
import { createPageMeta } from 'src/utils/seo.js'

useMeta(
  createPageMeta({
    title: 'Case Studies | Chad Kohl Developer Portfolio',
    description:
      'Read case studies from Chad Kohl covering product engineering, debugging, Azure platform diagnostics, and application design decisions.',
    path: '/case-studies',
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

.section-heading {
  max-width: 760px;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--ck-link);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.section-heading h1 {
  margin: 0;
  color: var(--ck-text-strong);
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: 0;
  line-height: 1.05;
}

.section-heading p {
  margin: 14px 0 0;
  color: var(--ck-text-secondary);
  font-size: 1.08rem;
  line-height: 1.68;
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

  .section-heading h1 {
    font-size: 2.8rem;
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

  .section-heading h1 {
    font-size: 2.25rem;
  }
}
</style>
