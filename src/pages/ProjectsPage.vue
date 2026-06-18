<template>
  <q-page class="projects-page">
    <section class="projects-hero">
      <div class="projects-inner">
        <PageBackLink label="Back to home" />

        <SectionHeader
          eyebrow="Projects"
          title="Project portfolio"
          title-tag="h1"
          description="A fuller view of practical applications, experiments, and product ideas built around real workflows, maintainable code, and useful interfaces."
          max-width="760px"
        />
      </div>
    </section>

    <section class="projects-section">
      <div class="projects-inner project-card-grid">
        <ProjectCard
          v-for="project in projects"
          :key="project.title"
          :project="project"
          title-tag="h2"
          project-label="View project"
          case-study-label="Read case study"
          show-unavailable-action
        />
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { useMeta } from 'quasar'
import PageBackLink from 'src/components/PageBackLink.vue'
import ProjectCard from 'src/components/ProjectCard.vue'
import SectionHeader from 'src/components/SectionHeader.vue'
import { projects } from 'src/data/projects.js'
import { createPageMeta } from 'src/utils/seo.js'

useMeta(
  createPageMeta({
    title: 'Projects | Chad Kohl Full Stack Developer',
    description:
      'Explore projects by Chad Kohl, a full stack developer building practical web applications, product experiments, and workflow-focused tools.',
    path: '/projects',
    socialTitle: 'Projects by Chad Kohl | Full Stack Developer',
    socialDescription:
      'Browse portfolio projects from Chad Kohl, including practical web apps, product experiments, and CK-branded interface work.',
  })
)
</script>

<style lang="scss" scoped>
.projects-page {
  background: var(--ck-page-bg);
  color: var(--ck-text-primary);
}

.projects-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.projects-hero {
  padding: 48px 0 40px;
  background: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
}

body.body--dark .projects-hero {
  background:
    radial-gradient(circle at top left, rgba(249, 156, 30, 0.06), transparent 32%),
    linear-gradient(135deg, #070b10, #0b1016);
}

.projects-section {
  padding: 52px 0 64px;
}

.project-card-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

@media (max-width: 900px) {
  .projects-inner {
    width: min(100% - 48px, 1120px);
  }

  .project-card-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

}

@media (max-width: 640px) {
  .projects-hero {
    padding: 34px 0 36px;
  }

  .projects-section {
    padding: 38px 0 48px;
  }

  .project-card-grid {
    grid-template-columns: 1fr;
  }

}
</style>
