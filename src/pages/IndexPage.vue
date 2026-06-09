<template>
  <q-page class="home-page" :class="{ 'home-page--dark': isDarkMode }">
    <section class="hero-section">
      <div class="section-inner hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">Portfolio / Web Application Engineering</p>
          <h1>Building focused web tools with practical, reliable foundations.</h1>
          <p class="hero-summary">
            I am Chad Kohl, a developer who turns everyday workflows into useful web applications,
            from Vue and Quasar interfaces to Laravel backends and database-driven features.
          </p>

          <div class="hero-actions">
            <q-btn
              unelevated
              no-caps
              color="primary"
              label="View Projects"
              @click="scrollToProjects"
            />
            <q-btn outline no-caps color="primary" label="Contact" @click="scrollToContact" />
          </div>
        </div>

        <div class="hero-panel" aria-label="Portfolio snapshot">
          <div class="profile-mark">CK</div>
          <div>
            <p class="panel-label">Current focus</p>
            <h2>Product-minded interfaces, readable application structure, and evidence-based debugging.</h2>
          </div>
          <q-separator />
          <div class="stat-grid">
            <div v-for="stat in stats" :key="stat.label" class="stat-item">
              <strong>{{ stat.value }}</strong>
              <span>{{ stat.label }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="projects" class="content-section">
      <div class="section-inner">
        <div class="section-heading">
          <p class="eyebrow">Projects</p>
          <h2>Selected projects</h2>
          <p>Small, practical applications built around real workflows, clear interfaces, and maintainable application code.</p>
        </div>

        <div class="card-grid">
          <q-card
            v-for="project in projects"
            :key="project.title"
            flat
            bordered
            class="content-card"
          >
            <q-img
              v-if="project.image"
              :src="project.image.src"
              :alt="project.image.alt"
              :ratio="16 / 9"
              fit="cover"
              loading="lazy"
              class="content-card__image"
            />
            <q-card-section>
              <div class="content-card__body">
                <h3>{{ project.title }}</h3>
                <p>{{ project.description }}</p>
              </div>
              <div class="content-card__actions">
                <div class="tag-list" aria-label="Project tags">
                  <q-chip v-for="tag in project.tags" :key="tag" outline square dense>
                    {{ tag }}
                  </q-chip>
                </div>
                <q-btn
                  outline
                  no-caps
                  color="primary"
                  icon-right="open_in_new"
                  label="View project"
                  :href="project.url"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="project-link"
                />
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </section>

    <section id="case-studies" class="content-section alternate-section">
      <div class="section-inner">
        <div class="section-heading">
          <p class="eyebrow">Case Studies</p>
          <h2>Engineering case studies</h2>
          <p>Short writeups on product decisions, debugging work, and the technical reasoning behind selected projects.</p>
        </div>

        <div class="card-grid">
          <CaseStudyCard
            v-for="caseStudy in caseStudies"
            :key="caseStudy.title"
            :case-study="caseStudy"
          />
        </div>
      </div>
    </section>

    <section id="skills" class="content-section">
      <div class="section-inner split-section">
        <div class="section-heading">
          <p class="eyebrow">Skills</p>
          <h2>Core toolkit</h2>
          <p>Frontend implementation, Laravel-backed application structure, diagnostics, and steady delivery across modern web projects.</p>
        </div>

        <div class="skill-groups">
          <div v-for="group in skillGroups" :key="group.title" class="skill-group">
            <h3>{{ group.title }}</h3>
            <div class="skill-list">
              <q-chip v-for="skill in group.skills" :key="skill" outline square>{{ skill }}</q-chip>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="contact" class="content-section contact-section">
      <div class="section-inner contact-panel">
        <div>
          <p class="eyebrow">Contact</p>
          <h2>Have a project or technical problem to untangle?</h2>
          <p>Reach out for web application implementation, portfolio work, or practical debugging help.</p>
        </div>

        <q-btn
          unelevated
          no-caps
          color="primary"
          icon="mail"
          label="ckohl401@gmail.com"
          href="mailto:ckohl401@gmail.com"
        />
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'
import CaseStudyCard from 'src/components/CaseStudyCard.vue'
import { caseStudies } from 'src/data/caseStudies.js'
import { projects } from 'src/data/projects.js'

const $q = useQuasar()

const isDarkMode = computed(() => $q.dark.isActive)

const stats = [
  { value: 'Vue + Laravel', label: 'Application foundation' },
  { value: 'Quasar', label: 'Interface framework' },
  { value: 'Case studies', label: 'Technical reasoning' },
]

const skillGroups = [
  {
    title: 'Application UI',
    skills: ['Vue', 'Quasar', 'JavaScript', 'HTML', 'SCSS'],
  },
  {
    title: 'Backend and Data',
    skills: ['Laravel', 'PHP', 'PostgreSQL', 'Application design'],
  },
  {
    title: 'Engineering',
    skills: ['GitHub', 'Debugging', 'Code review', 'Build tooling'],
  },
]

function scrollToProjects() {
  document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

function scrollToContact() {
  document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
</script>

<style lang="scss" scoped>
.home-page {
  --page-bg: var(--ck-page-bg);
  --section-bg: var(--ck-section-bg);
  --hero-bg: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
  --text-strong: var(--ck-text-strong);
  --text-primary: var(--ck-text-primary);
  --text-secondary: var(--ck-text-secondary);
  --text-muted: var(--ck-text-muted);
  --eyebrow-color: var(--ck-orange-dark);
  --card-bg: var(--ck-surface-bg);
  --card-border: var(--ck-border);
  --row-border: var(--ck-row-border);
  --mark-bg: var(--ck-charcoal);
  --mark-color: var(--ck-accent-orange);
  --card-shadow: var(--ck-card-shadow);

  background: var(--page-bg);
  color: var(--text-primary);
}

.section-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.hero-section {
  min-height: calc(100vh - 72px);
  display: flex;
  align-items: center;
  padding: 96px 0 64px;
  background: var(--hero-bg);
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(320px, 0.85fr);
  gap: 48px;
  align-items: center;
}

.hero-copy h1,
.section-heading h2,
.contact-panel h2 {
  margin: 0;
  color: var(--text-strong);
  font-weight: 800;
  letter-spacing: 0;
}

.hero-copy h1 {
  max-width: 760px;
  font-size: 4.55rem;
  line-height: 1;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--eyebrow-color);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero-summary {
  max-width: 660px;
  margin: 26px 0 0;
  color: var(--text-secondary);
  font-size: 1.16rem;
  line-height: 1.68;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 32px;
}

.hero-panel,
.content-card,
.contact-panel {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 8px;
}

.hero-panel {
  display: grid;
  gap: 24px;
  padding: 28px;
  box-shadow: var(--card-shadow);
}

.profile-mark {
  display: grid;
  place-items: center;
  width: 72px;
  aspect-ratio: 1;
  border-radius: 8px;
  background: var(--mark-bg);
  color: var(--mark-color);
  font-weight: 800;
  font-size: 1.35rem;
}

.panel-label,
.stat-item span {
  margin: 0;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.hero-panel h2 {
  margin: 6px 0 0;
  color: var(--text-primary);
  font-size: 1.36rem;
  line-height: 1.36;
}

.stat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.stat-item {
  display: grid;
  gap: 4px;
}

.stat-item strong {
  color: var(--text-strong);
  font-size: 1.2rem;
}

.content-section {
  scroll-margin-top: 88px;
  padding: 92px 0;
}

.alternate-section {
  background: var(--section-bg);
}

.section-heading {
  max-width: 720px;
  margin-bottom: 36px;
}

.section-heading h2,
.contact-panel h2 {
  font-size: 2.85rem;
  line-height: 1.1;
}

.section-heading p:last-child,
.contact-panel p:last-child,
.content-card p,
.case-row p {
  color: var(--text-secondary);
  line-height: 1.68;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 22px;
}

.content-card {
  display: flex;
  flex-direction: column;
  min-height: 300px;
  overflow: hidden;
}

.content-card__image {
  border-bottom: 1px solid var(--card-border);
}

.content-card :deep(.q-card__section) {
  display: grid;
  align-content: start;
  gap: 20px;
  flex: 1;
  padding: 18px 24px 24px;
}

.content-card__body,
.content-card__actions {
  display: grid;
}

.content-card__body {
  gap: 6px;
}

.content-card__actions {
  align-self: end;
  gap: 16px;
  margin-top: auto;
}

.content-card h3,
.case-row h3,
.skill-group h3 {
  margin: 0;
  color: var(--text-primary);
  font-size: 1.16rem;
  font-weight: 800;
}

.content-card p {
  margin: 0;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.tag-list :deep(.q-chip) {
  background: var(--ck-surface-subtle);
  border-color: var(--ck-border);
  color: var(--text-primary);
  margin: 0;
}

.project-link {
  justify-self: start;
  font-weight: 700;
}

.home-page--dark {
  --hero-bg: linear-gradient(135deg, var(--ck-charcoal), var(--ck-surface-dark));
  --eyebrow-color: var(--ck-accent-orange);
  --mark-bg: var(--ck-accent-orange);
  --mark-color: var(--ck-charcoal);
}

.split-section {
  display: grid;
  grid-template-columns: minmax(260px, 0.7fr) 1fr;
  gap: 48px;
}

.skill-groups {
  display: grid;
  gap: 22px;
}

.skill-group {
  display: grid;
  gap: 12px;
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.contact-section {
  padding-top: 40px;
}

.contact-panel {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  padding: 32px;
}

@media (max-width: 900px) {
  .hero-grid,
  .split-section,
  .card-grid {
    grid-template-columns: 1fr;
  }

  .hero-panel {
    max-width: 640px;
  }

  .card-grid {
    gap: 16px;
  }

  .hero-copy h1 {
    font-size: 3.6rem;
  }

  .section-heading h2,
  .contact-panel h2 {
    font-size: 2.4rem;
  }
}

@media (max-width: 640px) {
  .section-inner {
    width: min(100% - 24px, 1120px);
  }

  .hero-section {
    min-height: auto;
    padding: 72px 0 48px;
  }

  .hero-copy h1 {
    font-size: 2.45rem;
    line-height: 1.02;
  }

  .hero-summary {
    font-size: 1rem;
  }

  .hero-panel,
  .contact-panel {
    padding: 22px;
  }

  .stat-grid {
    grid-template-columns: 1fr;
  }

  .content-section {
    padding: 68px 0;
  }

  .contact-panel {
    align-items: stretch;
    flex-direction: column;
  }
}
</style>
