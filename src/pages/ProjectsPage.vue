<template>
  <q-page class="projects-page">
    <section class="projects-hero">
      <div class="projects-inner">
        <PageBackLink label="Back to home" />

        <div class="section-heading">
          <p class="eyebrow">Projects</p>
          <h1>Project portfolio</h1>
          <p>
            A fuller view of practical applications, experiments, and product ideas built around
            real workflows, maintainable code, and useful interfaces.
          </p>
        </div>
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
  font-weight: 800;
  letter-spacing: 0;
}

.section-heading h1 {
  font-size: 3.5rem;
  line-height: 1.05;
}

.section-heading p {
  color: var(--ck-text-secondary);
  line-height: 1.68;
}

.section-heading p {
  margin: 14px 0 0;
  font-size: 1.08rem;
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

  .section-heading h1 {
    font-size: 2.8rem;
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

  .section-heading h1 {
    font-size: 2.25rem;
  }
}
</style>
