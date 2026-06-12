<template>
  <q-page class="home-page" :class="{ 'home-page--dark': isDarkMode }">
    <section class="hero-section">
      <div class="section-inner hero-grid">
        <div class="hero-copy">
          <p class="hero-badge">
            <q-icon name="code" size="14px" aria-hidden="true" />
            <span>Full-stack Developer</span>
          </p>
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
              icon="work"
              label="View Projects"
              @click="scrollToProjects"
            />
            <q-btn
              outline
              no-caps
              color="primary"
              icon="mail"
              label="Contact"
              @click="scrollToContact"
            />
          </div>
        </div>

        <div class="hero-code-card" aria-label="Developer profile code sample">
          <div class="code-window-bar" aria-hidden="true">
            <span></span>
            <span></span>
            <span></span>
          </div>

          <div class="code-card-mark" aria-hidden="true">&lt;/&gt;</div>
          <div class="code-brace-mark" aria-hidden="true">{</div>

          <div class="code-content">
            <div v-for="line in codeLines" :key="line.number" class="code-line">
              <span class="line-number">{{ line.number }}</span>
              <code v-html="line.html"></code>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="projects" class="content-section">
      <div class="section-inner">
        <div class="section-heading section-heading--with-action">
          <div class="section-heading__top">
            <p class="eyebrow">Projects</p>
            <q-btn
              flat
              no-caps
              color="primary"
              icon-right="arrow_forward"
              label="View all projects"
              to="/projects"
              class="section-heading__link"
            />
          </div>
          <h2>Selected projects</h2>
          <p>Small, practical applications built around real workflows, clear interfaces, and maintainable application code.</p>
        </div>

        <div class="card-grid projects-grid">
          <ProjectCard
            v-for="project in featuredProjects"
            :key="project.title"
            :project="project"
          />
        </div>
      </div>
    </section>

    <section id="case-studies" class="content-section alternate-section">
      <div class="section-inner">
        <div class="section-heading section-heading--with-action">
          <div class="section-heading__top">
            <p class="eyebrow">Case Studies</p>
            <q-btn
              flat
              no-caps
              color="primary"
              icon-right="arrow_forward"
              label="View all case studies"
              to="/case-studies"
              class="section-heading__link"
            />
          </div>
          <h2>Engineering case studies</h2>
          <p>Short writeups on product decisions, debugging work, and the technical reasoning behind selected projects.</p>
        </div>

        <div class="card-grid case-studies-grid">
          <CaseStudyCard
            v-for="caseStudy in featuredCaseStudies"
            :key="caseStudy.title"
            :case-study="caseStudy"
          />
        </div>
      </div>
    </section>

    <section id="about" class="content-section">
      <div class="section-inner about-preview">
        <div class="section-heading section-heading--with-action">
          <div class="section-heading__top">
            <p class="eyebrow">{{ aboutHero.eyebrow }}</p>
            <q-btn
              flat
              no-caps
              color="primary"
              icon-right="arrow_forward"
              label="View more about me"
              to="/about"
              class="section-heading__link"
            />
          </div>
          <h2>{{ aboutHero.headline }}</h2>
          <p>{{ aboutHero.summary }}</p>
        </div>

        <div class="about-highlight-grid">
          <q-card
            v-for="highlight in homepageHighlights"
            :key="highlight.title"
            flat
            bordered
            class="about-highlight-card"
          >
            <q-card-section>
              <q-icon :name="highlight.icon" size="28px" />
              <h3>{{ highlight.title }}</h3>
              <p>{{ highlight.description }}</p>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </section>

    <section id="skills" class="content-section">
      <div class="section-inner skills-section">
        <div class="section-heading">
          <p class="eyebrow">Skills</p>
          <h2>Skills & technologies</h2>
          <p>Frontend implementation, Laravel-backed application structure, diagnostics, and steady delivery across modern web projects.</p>
        </div>

        <div class="skill-groups">
          <div
            v-for="group in skillGroups"
            :key="group.title"
            class="skill-group"
          >
            <div class="skill-group__header">
              <q-icon :name="group.icon" size="24px" />
              <h3>{{ group.title }}</h3>
            </div>

            <div class="skill-list">
              <a
                v-for="skill in group.skills"
                :key="skill.label"
                :href="skill.url"
                target="_blank"
                rel="noopener noreferrer"
                class="skill-item"
              >
                <q-icon
                  :name="skill.icon"
                  size="28px"
                  class="skill-item__icon"
                  :style="{ color: skill.iconColor }"
                />
                <span>
                  <strong>{{ skill.label }}</strong>
                  <small>{{ skill.description }}</small>
                </span>
              </a>
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

    <footer class="site-footer">
      <div class="section-inner footer-grid">
        <div>
          <img :src="ckLogo" alt="CK." class="footer-logo" />
          <p>Building web applications that make practical workflows easier to manage.</p>
        </div>

        <div class="footer-links" aria-label="Footer navigation">
          <span>Navigation</span>
          <button type="button" @click="scrollToProjects">Projects</button>
          <button type="button" @click="scrollToContact">Contact</button>
        </div>
      </div>
    </footer>
  </q-page>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'
import {
  mdiApi,
  mdiDatabase,
  mdiDocker,
  mdiGithub,
  mdiLaravel,
  mdiLinux,
  mdiMicrosoftAzure,
  mdiSass,
  mdiVuejs,
  mdiLanguageJavascript,
  mdiLanguagePhp,
} from '@quasar/extras/mdi-v7'
import CaseStudyCard from 'src/components/CaseStudyCard.vue'
import ProjectCard from 'src/components/ProjectCard.vue'
import quasarMark from 'src/assets/svg/quasar-mark.svg'
import ckLogo from 'src/assets/svg/logo/ck-logo.svg'
import { aboutHero, experienceHighlights } from 'src/data/about.js'
import { caseStudies } from 'src/data/caseStudies.js'
import { featuredProjects } from 'src/data/projects.js'

const $q = useQuasar()

const isDarkMode = computed(() => $q.dark.isActive)

const homepageHighlights = experienceHighlights.slice(0, 3)
const featuredCaseStudies = caseStudies.slice(0, 3)

const codeLines = [
  {
    number: 1,
    html: '<span class="code-keyword">const</span> <span class="code-variable">developer</span> = {',
  },
  { number: 2, html: '  <span class="code-property">name</span>: <span class="code-string">"Chad Kohl"</span>,' },
  {
    number: 3,
    html: '  <span class="code-property">role</span>: <span class="code-string">"Full-Stack Developer"</span>,',
  },
  {
    number: 4,
    html: '  <span class="code-property">focus</span>: [<span class="code-string">"Web Apps"</span>, <span class="code-string">"APIs"</span>, <span class="code-string">"UI/UX"</span>],',
  },
  {
    number: 5,
    html: '  <span class="code-property">passion</span>: <span class="code-string">"Building solutions that make a difference"</span>,',
  },
  {
    number: 6,
    html: '  <span class="code-property">technologies</span>: [<span class="code-string">"Vue"</span>, <span class="code-string">"Quasar"</span>, <span class="code-string">"Laravel"</span>],',
  },
  { number: 7, html: '};' },
  { number: 8, html: '' },
  {
    number: 9,
    html: '<span class="code-keyword">function</span> <span class="code-function">buildSomethingGreat</span>() {',
  },
  {
    number: 10,
    html: `  <span class="code-keyword">return</span> <span class="code-string">"Let's work together"</span>;`,
  },
  { number: 11, html: '}' },
]

const skillGroups = [
  {
    title: 'Frontend',
    icon: 'view_quilt',
    skills: [
      {
        label: 'Vue 3',
        description: 'Component-driven application UI',
        icon: mdiVuejs,
        iconColor: '#42b883',
        url: 'https://vuejs.org/',
      },
      {
        label: 'Quasar',
        description: 'Responsive Vue application framework',
        icon: `img:${quasarMark}`,
        iconColor: '#00b4ff',
        url: 'https://quasar.dev/',
      },
      {
        label: 'JavaScript',
        description: 'Core browser application language',
        icon: mdiLanguageJavascript,
        iconColor: '#d6a700',
        url: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
      },
      {
        label: 'SCSS',
        description: 'Structured styling for responsive UI',
        icon: mdiSass,
        iconColor: '#cc6699',
        url: 'https://sass-lang.com/',
      },
    ],
  },
  {
    title: 'Backend',
    icon: 'dns',
    skills: [
      {
        label: 'Laravel',
        description: 'PHP application framework',
        icon: mdiLaravel,
        iconColor: '#ff2d20',
        url: 'https://laravel.com/',
      },
      {
        label: 'PHP',
        description: 'Server-side application development',
        icon: mdiLanguagePhp,
        iconColor: '#777bb4',
        url: 'https://www.php.net/',
      },
      {
        label: 'PostgreSQL',
        description: 'Relational application data',
        icon: mdiDatabase,
        iconColor: '#336791',
        url: 'https://www.postgresql.org/',
      },
      {
        label: 'REST APIs',
        description: 'HTTP-based service integration',
        icon: mdiApi,
        iconColor: 'var(--ck-link)',
        url: 'https://developer.mozilla.org/en-US/docs/Glossary/REST',
      },
    ],
  },
  {
    title: 'Cloud & DevOps',
    icon: 'cloud_queue',
    skills: [
      {
        label: 'Azure App Service',
        description: 'Cloud app hosting and diagnostics',
        icon: mdiMicrosoftAzure,
        iconColor: '#0078d4',
        url: 'https://azure.microsoft.com/en-us/products/app-service',
      },
      {
        label: 'Git / GitHub',
        description: 'Version control and issue-driven delivery',
        icon: mdiGithub,
        iconColor: 'var(--ck-text-primary)',
        url: 'https://github.com/',
      },
      {
        label: 'Docker',
        description: 'Containerized local and deployment workflows',
        icon: mdiDocker,
        iconColor: '#2496ed',
        url: 'https://www.docker.com/',
      },
      {
        label: 'Linux',
        description: 'Server environments and command-line work',
        icon: mdiLinux,
        iconColor: '#f5b800',
        url: 'https://www.kernel.org/',
      },
    ],
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
  --code-text: #334155;
  --code-line-number: #8a99a8;
  --code-keyword: #a85b00;
  --code-string: #087f8c;
  --code-variable: #1e2a30;
  --code-property: #287a3e;
  --code-function: #8a5a00;
  --code-header-bg: rgba(8, 12, 17, 0.05);

  background: var(--page-bg);
  color: var(--text-primary);
}

.section-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.hero-section {
  min-height: auto;
  display: flex;
  align-items: center;
  padding: 52px 0 28px;
  background: var(--hero-bg);
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(360px, 0.82fr);
  gap: 56px;
  align-items: stretch;
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
  max-width: 660px;
  font-size: 3.35rem;
  line-height: 1.08;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  width: fit-content;
  margin: 0 0 22px;
  padding: 6px 12px;
  background: rgba(249, 156, 30, 0.1);
  border: 1px solid rgba(249, 156, 30, 0.24);
  border-radius: 999px;
  color: var(--eyebrow-color);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
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
  max-width: 620px;
  margin: 26px 0 0;
  color: var(--text-secondary);
  font-size: 1.16rem;
  line-height: 1.72;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 22px;
}

.hero-code-card,
.contact-panel {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
}

.hero-code-card {
  position: relative;
  display: grid;
  align-self: stretch;
  gap: 18px;
  min-height: 400px;
  padding: 0 0 26px;
  background: var(--card-bg);
  overflow: visible;
}

.hero-code-card::after {
  content: none;
}

.code-window-bar {
  display: flex;
  align-items: center;
  gap: 7px;
  min-height: 38px;
  padding: 0 18px;
  background: var(--code-header-bg);
  border-bottom: 1px solid var(--card-border);
  border-radius: 8px 8px 0 0;
}

.code-window-bar span {
  width: 9px;
  aspect-ratio: 1;
  border-radius: 999px;
}

.code-window-bar span:nth-child(1) {
  background: #ef6b5a;
}

.code-window-bar span:nth-child(2) {
  background: #f4bf4f;
}

.code-window-bar span:nth-child(3) {
  background: #61c554;
}

.code-card-mark {
  position: absolute;
  top: -5px;
  right: -4px;
  color: var(--ck-orange);
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace;
  font-size: 4.15rem;
  font-weight: 800;
  letter-spacing: -0.12em;
  line-height: 1;
  opacity: 0.95;
}

.code-brace-mark {
  position: absolute;
  right: calc(100% - 10px);
  bottom: 0;
  z-index: 1;
  color: var(--ck-orange);
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace;
  font-size: 4.6rem;
  font-weight: 500;
  line-height: 1;
  opacity: 0.95;
}

.code-content {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 8px;
  padding: 18px 24px 0 22px;
  overflow: hidden;
}

.code-line {
  display: grid;
  grid-template-columns: 24px minmax(0, 1fr);
  gap: 8px;
  min-height: 18px;
  color: var(--code-text);
  font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace;
  font-size: clamp(0.7rem, 0.76vw, 0.82rem);
  line-height: 1.55;
}

.code-line code {
  min-width: 0;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}

.line-number {
  color: var(--code-line-number);
  text-align: right;
  user-select: none;
}

.code-line :deep(.code-keyword) {
  color: var(--code-keyword);
}

.code-line :deep(.code-string) {
  color: var(--code-string);
}

.code-line :deep(.code-variable) {
  color: var(--code-variable);
}

.code-line :deep(.code-property) {
  color: var(--code-property);
}

.code-line :deep(.code-function) {
  color: var(--code-function);
}

.content-section {
  scroll-margin-top: 88px;
  padding: 76px 0 88px;
}

.hero-section + .content-section {
  padding-top: 48px;
}

.alternate-section {
  background: var(--section-bg);
}

.section-heading {
  max-width: 720px;
  margin-bottom: 40px;
}

.section-heading--with-action {
  margin-bottom: 14px;
  max-width: none;
}

.section-heading--with-action > h2,
.section-heading--with-action > p {
  max-width: 720px;
}

.section-heading__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
}

.section-heading__link {
  margin-top: -8px;
  min-height: 34px;
  padding: 0;
  font-weight: 800;
}

.section-heading h2,
.contact-panel h2 {
  font-size: 2.85rem;
  line-height: 1.1;
}

.section-heading p:last-child,
.contact-panel p:last-child,
.case-row p {
  color: var(--text-secondary);
  line-height: 1.68;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.projects-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.case-studies-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.about-highlight-card h3,
.case-row h3,
.skill-group h3 {
  margin: 0;
  color: var(--text-primary);
  font-size: 1.08rem;
  font-weight: 800;
  line-height: 1.25;
}

.about-highlight-card p {
  margin: 0;
}

.home-page--dark {
  --hero-bg:
    radial-gradient(circle at top left, rgba(249, 156, 30, 0.06), transparent 32%),
    linear-gradient(135deg, #070b10, #0b1016);
  --eyebrow-color: var(--ck-accent-orange);
  --mark-bg: var(--ck-accent-orange);
  --mark-color: var(--ck-charcoal);
  --code-text: #94a3b8;
  --code-line-number: #5f6c7d;
  --code-keyword: #f99c1e;
  --code-string: #7dd3fc;
  --code-variable: #f8fafc;
  --code-property: #86efac;
  --code-function: #facc15;
  --code-header-bg: rgba(255, 255, 255, 0.07);
}

.about-preview {
  display: grid;
}

.about-highlight-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.about-highlight-card {
  padding: 10px;
  background: var(--card-bg);
  border-color: var(--card-border);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
}

.about-highlight-card :deep(.q-card__section) {
  display: grid;
  align-content: start;
  gap: 10px;
  height: 100%;
  padding: 16px 6px 6px;
}

.about-highlight-card :deep(.q-icon) {
  color: var(--ck-link);
}

.about-highlight-card p {
  color: var(--text-secondary);
  line-height: 1.62;
}

.skills-section {
  display: grid;
}

.skills-section .section-heading {
  margin-bottom: 20px;
}

.skill-groups {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.skill-group {
  display: grid;
  align-content: start;
  gap: 16px;
  padding: 22px;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
}

.skill-group__header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.skill-group__header :deep(.q-icon) {
  color: var(--ck-link);
}

.skill-list {
  display: grid;
  gap: 8px;
}

.skill-item {
  display: grid;
  grid-template-columns: 32px minmax(0, 1fr);
  align-items: center;
  gap: 10px;
  min-height: 54px;
  padding: 9px 10px;
  background: rgba(8, 12, 17, 0.035);
  border: 1px solid rgba(8, 12, 17, 0.07);
  border-radius: 6px;
  color: var(--text-primary);
  text-decoration: none;
  transition:
    border-color 0.18s ease,
    color 0.18s ease,
    transform 0.18s ease;
}

.skill-item:hover,
.skill-item:focus {
  border-color: color-mix(in srgb, var(--ck-link) 44%, transparent);
  color: var(--ck-link);
  transform: translateY(-1px);
}

.skill-item__icon {
  color: var(--ck-link);
}

.skill-item span {
  display: grid;
  gap: 2px;
  min-width: 0;
}

.skill-item strong {
  font-size: 0.9rem;
  line-height: 1.25;
}

.skill-item small {
  color: var(--text-secondary);
  font-size: 0.76rem;
  line-height: 1.35;
}

.home-page--dark .skill-item {
  background: rgba(255, 255, 255, 0.045);
  border-color: rgba(255, 255, 255, 0.08);
}

.contact-section {
  padding-top: 40px;
}

.contact-panel {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  padding: 32px;
  overflow: hidden;
}

.contact-panel::after {
  content: '';
  position: absolute;
  right: 0;
  bottom: 0;
  width: 180px;
  height: 100%;
  background-image: radial-gradient(rgba(249, 156, 30, 0.32) 1px, transparent 1px);
  background-size: 10px 10px;
  mask-image: linear-gradient(90deg, transparent, #000);
  pointer-events: none;
}

.site-footer {
  padding: 36px 0 44px;
  border-top: 1px solid var(--card-border);
  background: var(--page-bg);
}

.footer-grid {
  display: flex;
  justify-content: space-between;
  gap: 32px;
}

.footer-logo {
  display: block;
  width: 76px;
  height: auto;
  margin-bottom: 10px;
}

.site-footer p {
  max-width: 340px;
  margin: 0;
  color: var(--text-secondary);
  line-height: 1.6;
}

.footer-links {
  display: grid;
  gap: 8px;
  min-width: 160px;
}

.footer-links span {
  color: var(--text-strong);
  font-weight: 800;
}

.footer-links button {
  width: fit-content;
  padding: 0;
  background: transparent;
  border: 0;
  color: var(--text-secondary);
  cursor: pointer;
  font: inherit;
  text-align: left;
}

.footer-links button:hover,
.footer-links button:focus {
  color: var(--ck-link);
}

@media (max-width: 900px) {
  .section-inner {
    width: min(100% - 48px, 1120px);
  }

  .hero-grid,
  .card-grid,
  .about-highlight-grid {
    grid-template-columns: 1fr;
  }

  .hero-code-card {
    max-width: 640px;
    width: calc(100% - 24px);
    margin-left: 24px;
    min-height: 360px;
  }

  .card-grid {
    gap: 20px;
  }

  .projects-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .case-studies-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .about-highlight-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .skill-groups {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .hero-copy h1 {
    font-size: 2.85rem;
  }

  .section-heading h2,
  .contact-panel h2 {
    font-size: 2.4rem;
  }

  .section-heading--with-action {
    margin-bottom: 20px;
  }

  .section-heading__link {
    margin-top: -8px;
  }
}

@media (max-width: 640px) {
  .section-inner {
    width: min(100% - 48px, 1120px);
  }

  .hero-section {
    min-height: auto;
    padding: 38px 0 28px;
  }

  .hero-copy h1 {
    font-size: 2.15rem;
    line-height: 1.08;
  }

  .hero-summary {
    font-size: 1rem;
  }

  .hero-code-card,
  .contact-panel {
    padding: 22px;
  }

  .hero-code-card {
    min-height: auto;
    padding: 0 0 22px;
  }

  .code-content {
    padding: 8px 16px 0 16px;
  }

  .code-line {
    font-size: 0.7rem;
    grid-template-columns: 22px minmax(0, 1fr);
    gap: 7px;
  }

  .code-brace-mark {
    right: calc(100% - 8px);
    bottom: 0;
    font-size: 3.6rem;
  }

  .code-card-mark {
    top: -3px;
    right: -3px;
    font-size: 3.2rem;
  }

  .content-section {
    padding: 56px 0 64px;
  }

  .projects-grid {
    grid-template-columns: 1fr;
  }

  .case-studies-grid {
    grid-template-columns: 1fr;
  }

  .about-highlight-grid {
    grid-template-columns: 1fr;
  }

  .skill-groups {
    grid-template-columns: 1fr;
  }

  .contact-panel {
    align-items: stretch;
    flex-direction: column;
  }

  .footer-grid {
    flex-direction: column;
  }
}

@media (max-width: 380px) {
  .section-inner {
    width: min(100% - 36px, 1120px);
  }

  .hero-code-card {
    width: calc(100% - 20px);
    margin-left: 20px;
  }
}
</style>
