<template>
  <q-page class="home-page">
    <section class="hero-section">
      <div class="section-inner hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">Portfolio / Engineering Showcase</p>
          <h1>Building practical web experiences with a clear technical foundation.</h1>
          <p class="hero-summary">
            I am Chad Kohl, a developer focused on clean interfaces, reliable workflows, and
            thoughtful problem solving across modern web projects.
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
            <h2>Portfolio systems, technical case studies, and production-minded UI.</h2>
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
          <h2>Selected work</h2>
          <p>Current projects pulled into a reusable data source from the existing work page.</p>
        </div>

        <div class="card-grid">
          <q-card
            v-for="project in projects"
            :key="project.title"
            flat
            bordered
            class="content-card"
          >
            <q-card-section>
              <h3>{{ project.title }}</h3>
              <p>{{ project.description }}</p>
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
            </q-card-section>
          </q-card>
        </div>
      </div>
    </section>

    <section id="case-studies" class="content-section alternate-section">
      <div class="section-inner">
        <div class="section-heading">
          <p class="eyebrow">Case Studies</p>
          <h2>Problem-solving notes</h2>
          <p>Short-form technical writeups can live here as the portfolio grows.</p>
        </div>

        <div class="case-list">
          <article v-for="caseStudy in caseStudies" :key="caseStudy.title" class="case-row">
            <div>
              <span>{{ caseStudy.category }}</span>
              <h3>{{ caseStudy.title }}</h3>
            </div>
            <p>{{ caseStudy.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section id="skills" class="content-section">
      <div class="section-inner split-section">
        <div class="section-heading">
          <p class="eyebrow">Skills</p>
          <h2>Core toolkit</h2>
          <p>Frontend implementation, application structure, debugging, and iterative delivery.</p>
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
          <h2>Have a project or technical challenge?</h2>
          <p>Reach out for portfolio work, implementation help, or collaboration.</p>
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
import { projects } from 'src/data/projects.js'

const stats = [
  { value: '5', label: 'Homepage sections' },
  { value: 'Vue 3', label: 'Application base' },
  { value: 'Quasar', label: 'UI framework' },
]

const caseStudies = [
  {
    category: 'Workflow',
    title: 'Turning issues into incremental delivery',
    description: 'Document decisions, constraints, and build steps from idea through release.',
  },
  {
    category: 'Debugging',
    title: 'Tracing production-facing problems',
    description:
      'Capture symptoms, root cause, fix strategy, and verification in a reusable format.',
  },
  {
    category: 'Interface',
    title: 'Designing focused user flows',
    description: 'Show the tradeoffs behind layout, component structure, and responsive behavior.',
  },
]

const skillGroups = [
  {
    title: 'Frontend',
    skills: ['Vue', 'Quasar', 'JavaScript', 'HTML', 'SCSS'],
  },
  {
    title: 'Engineering',
    skills: ['GitHub', 'Debugging', 'Code review', 'Build tooling'],
  },
  {
    title: 'Delivery',
    skills: ['Responsive UI', 'Documentation', 'Issue workflows', 'Testing basics'],
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
  --page-bg: #f7f8fa;
  --section-bg: #ffffff;
  --hero-bg: linear-gradient(135deg, rgba(236, 241, 246, 0.86), rgba(255, 255, 255, 0.9));
  --text-strong: #101417;
  --text-primary: #161a1d;
  --text-secondary: #53606a;
  --text-muted: #69757d;
  --eyebrow-color: #37606a;
  --card-bg: #ffffff;
  --card-border: #e3e7eb;
  --row-border: #e4e8ec;
  --mark-bg: #101417;
  --mark-color: #ffffff;
  --card-shadow: 0 18px 50px rgba(15, 23, 42, 0.08);

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
  padding: 88px 0 56px;
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
  max-width: 780px;
  font-size: 4.8rem;
  line-height: 0.98;
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
  max-width: 640px;
  margin: 24px 0 0;
  color: var(--text-secondary);
  font-size: 1.16rem;
  line-height: 1.7;
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
  font-size: 1.45rem;
  line-height: 1.3;
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
  padding: 88px 0;
}

.alternate-section {
  background: var(--section-bg);
}

.section-heading {
  max-width: 680px;
  margin-bottom: 32px;
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
  line-height: 1.65;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.content-card {
  min-height: 300px;
}

.content-card :deep(.q-card__section) {
  display: grid;
  gap: 14px;
  height: 100%;
  padding: 24px;
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
  margin-top: auto;
}

.project-link {
  justify-self: start;
  margin-top: 4px;
}

.case-list {
  display: grid;
  gap: 14px;
}

.case-row {
  display: grid;
  grid-template-columns: minmax(220px, 0.8fr) 1fr;
  gap: 28px;
  align-items: start;
  padding: 22px 0;
  border-top: 1px solid var(--row-border);
}

.case-row span {
  display: block;
  margin-bottom: 8px;
  color: #1976d2;
  font-size: 0.8rem;
  font-weight: 800;
  text-transform: uppercase;
}

:global(.body--dark) .home-page {
  --page-bg: #10161c;
  --section-bg: #151d24;
  --hero-bg: linear-gradient(135deg, rgba(16, 22, 28, 0.96), rgba(25, 35, 44, 0.9));
  --text-strong: #f4f8fb;
  --text-primary: #dfe8ee;
  --text-secondary: #aebbc5;
  --text-muted: #90a0ab;
  --eyebrow-color: #8bc7d5;
  --card-bg: #17212a;
  --card-border: #2a3945;
  --row-border: #2a3945;
  --mark-bg: #f4f8fb;
  --mark-color: #10161c;
  --card-shadow: 0 18px 50px rgba(0, 0, 0, 0.28);
}

.case-row p {
  margin: 0;
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
    padding: 72px 0 40px;
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

  .stat-grid,
  .case-row {
    grid-template-columns: 1fr;
  }

  .case-row {
    gap: 10px;
  }

  .content-section {
    padding: 64px 0;
  }

  .contact-panel {
    align-items: stretch;
    flex-direction: column;
  }
}
</style>
