<template>
  <q-page class="about-page">
    <section class="about-hero">
      <div class="about-inner hero-grid">
        <div class="hero-copy">
          <p class="eyebrow">{{ aboutHero.eyebrow }}</p>
          <h1>{{ aboutHero.name }}</h1>
          <p class="professional-title">{{ aboutHero.title }}</p>
          <h2>{{ aboutHero.headline }}</h2>
          <p class="hero-intro">{{ aboutHero.intro }}</p>
          <p class="hero-summary">{{ aboutHero.summary }}</p>

          <div class="hero-actions">
            <q-btn
              unelevated
              no-caps
              color="primary"
              label="View projects"
              @click="scrollToHomeSection('projects')"
            />
            <q-btn
              outline
              no-caps
              color="primary"
              label="Contact"
              class="q-ml-md"
              style="margin-left: 20px"
              @click="scrollToHomeSection('contact')"
            />
          </div>
        </div>

        <q-card flat bordered class="profile-card">
          <q-card-section>
            <div class="profile-mark" aria-label="Chad Kohl profile mark">CK</div>
            <q-icon name="psychology" color="primary" size="32px" />
            <p>How does this system work, and how can I make it better?</p>
          </q-card-section>
        </q-card>
      </div>
    </section>

    <section class="about-section">
      <div class="about-inner content-grid">
        <article class="story-column">
          <section v-for="section in aboutStorySections" :key="section.title" class="story-block">
            <p class="eyebrow">{{ section.eyebrow }}</p>
            <h2>{{ section.title }}</h2>
            <p v-for="paragraph in section.paragraphs" :key="paragraph">
              {{ paragraph }}
            </p>
          </section>
        </article>

        <aside class="timeline-column" aria-label="Major milestones">
          <q-card flat bordered class="timeline-card">
            <q-card-section>
              <h2>Major milestones</h2>
              <q-timeline color="primary" layout="dense">
                <q-timeline-entry
                  v-for="milestone in aboutTimeline"
                  :key="milestone.title"
                  :title="milestone.title"
                  :subtitle="milestone.subtitle"
                >
                  <p>{{ milestone.body }}</p>
                </q-timeline-entry>
              </q-timeline>
            </q-card-section>
          </q-card>
        </aside>
      </div>
    </section>

    <section class="about-section alternate-section">
      <div class="about-inner">
        <div class="section-heading">
          <p class="eyebrow">Experience</p>
          <h2>Highlights from the path</h2>
        </div>

        <div class="highlight-grid">
          <q-card
            v-for="highlight in experienceHighlights"
            :key="highlight.title"
            flat
            bordered
            class="highlight-card"
          >
            <q-card-section>
              <q-icon :name="highlight.icon" color="primary" size="28px" />
              <h3>{{ highlight.title }}</h3>
              <p>{{ highlight.description }}</p>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </section>

    <section class="about-section">
      <div class="about-inner interests-grid">
        <div class="section-heading">
          <p class="eyebrow">Beyond technology</p>
          <h2>Systems worth understanding</h2>
          <p>
            Many of my interests share the same qualities that drew me to technology:
            experimentation, observation, problem-solving, and continuous improvement.
          </p>
        </div>

        <q-card flat bordered class="interests-card">
          <q-card-section>
            <div class="interest-list" aria-label="Interests">
              <q-chip v-for="interest in interests" :key="interest" outline square>
                {{ interest }}
              </q-chip>
            </div>
            <q-separator />
            <p>{{ closingThought }}</p>
          </q-card-section>
        </q-card>
      </div>
    </section>
  </q-page>
</template>

<script setup>
import { useMeta } from 'quasar'
import { nextTick } from 'vue'
import { useRouter } from 'vue-router'
import {
  aboutHero,
  aboutStorySections,
  aboutTimeline,
  closingThought,
  experienceHighlights,
  interests,
} from 'src/data/about.js'

const router = useRouter()

useMeta({
  title: 'About Chad Kohl | Software Developer',
  meta: {
    description: {
      name: 'description',
      content:
        "Learn about Chad Kohl's background in software development, Azure support engineering, leadership, creative work, and practical project building.",
    },
    ogTitle: {
      property: 'og:title',
      content: 'About Chad Kohl | Software Developer',
    },
    ogDescription: {
      property: 'og:description',
      content:
        "A professional narrative about Chad Kohl's path through technology, leadership, creativity, cloud support, and software development.",
    },
  },
})

async function scrollToHomeSection(sectionId) {
  await router.push({ path: '/', hash: `#${sectionId}` })
  await nextTick()

  document.getElementById(sectionId)?.scrollIntoView({
    behavior: 'smooth',
    block: 'start',
  })
}
</script>

<style lang="scss" scoped>
.about-page {
  background: var(--ck-page-bg);
  color: var(--ck-text-primary);
}

.about-inner {
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.about-hero {
  padding: 96px 0 80px;
  background: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
}

body.body--dark .about-hero {
  background: linear-gradient(135deg, var(--ck-charcoal), var(--ck-surface-dark));
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(300px, 0.85fr);
  gap: 48px;
  align-items: center;
}

.hero-copy h1,
.hero-copy h2,
.section-heading h2,
.story-block h2,
.timeline-card h2,
.highlight-card h3 {
  margin: 0;
  color: var(--ck-text-strong);
  font-weight: 800;
  letter-spacing: 0;
}

.hero-copy h1 {
  max-width: 820px;
  font-size: 4rem;
  line-height: 1;
}

.hero-copy h2 {
  max-width: 820px;
  margin-top: 20px;
  font-size: 2.4rem;
  line-height: 1.08;
}

.professional-title {
  margin: 14px 0 0;
  color: var(--ck-link);
  font-size: 1rem;
  font-weight: 800;
}

.eyebrow {
  margin: 0 0 14px;
  color: var(--ck-link);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.hero-intro,
.hero-summary,
.section-heading p,
.story-block p:not(.eyebrow),
.highlight-card p,
.interests-card p,
.timeline-card :deep(.q-timeline__content p) {
  color: var(--ck-text-secondary);
  line-height: 1.7;
}

.hero-intro {
  max-width: 720px;
  margin: 24px 0 0;
  font-size: 1.18rem;
}

.hero-summary {
  max-width: 720px;
  margin: 18px 0 0;
  font-size: 1rem;
}

.profile-card,
.timeline-card,
.highlight-card,
.interests-card {
  background: var(--ck-surface-bg);
  border-color: var(--ck-border);
  border-radius: 8px;
}

.profile-card {
  box-shadow: var(--ck-card-shadow);
}

.profile-card :deep(.q-card__section) {
  display: grid;
  gap: 18px;
  padding: 28px;
}

.profile-mark {
  display: grid;
  place-items: center;
  width: 76px;
  aspect-ratio: 1;
  border-radius: 8px;
  background: var(--ck-charcoal);
  color: var(--ck-accent-orange);
  font-size: 1.4rem;
  font-weight: 800;
}

body.body--dark .profile-mark {
  background: var(--ck-accent-orange);
  color: var(--ck-charcoal);
}

.profile-card p {
  margin: 0;
  color: var(--ck-text-primary);
  font-size: 1.35rem;
  font-weight: 800;
  line-height: 1.35;
}

.about-section {
  padding: 80px 0;
}

.alternate-section {
  background: var(--ck-section-bg);
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 360px;
  gap: 48px;
  align-items: start;
}

.story-column {
  display: grid;
  gap: 48px;
}

.story-block h2,
.section-heading h2 {
  font-size: 2.2rem;
  line-height: 1.15;
}

.story-block p:not(.eyebrow) {
  margin: 18px 0 0;
  font-size: 1rem;
}

.timeline-column {
  position: sticky;
  top: 96px;
}

.timeline-card :deep(.q-card__section),
.interests-card :deep(.q-card__section),
.highlight-card :deep(.q-card__section) {
  display: grid;
  gap: 16px;
  padding: 24px;
}

.timeline-card h2 {
  font-size: 1.2rem;
}

.timeline-card :deep(.q-timeline) {
  margin: 0;
}

.timeline-card :deep(.q-timeline__title) {
  color: var(--ck-text-primary);
  font-size: 0.98rem;
  font-weight: 800;
}

.timeline-card :deep(.q-timeline__subtitle) {
  color: var(--ck-link);
  font-size: 0.78rem;
  font-weight: 700;
  opacity: 1;
  text-transform: none;
}

.timeline-card :deep(.q-timeline__content p) {
  margin: 6px 0 0;
  font-size: 0.92rem;
}

.section-heading {
  max-width: 720px;
  margin-bottom: 32px;
}

.section-heading p {
  margin: 14px 0 0;
}

.highlight-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.highlight-card h3 {
  font-size: 1.16rem;
}

.highlight-card p,
.interests-card p {
  margin: 0;
}

.interests-grid {
  display: grid;
  grid-template-columns: minmax(260px, 0.8fr) 1fr;
  gap: 48px;
  align-items: start;
}

.interest-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.interest-list :deep(.q-chip) {
  background: var(--ck-surface-subtle);
  border-color: var(--ck-border);
  color: var(--ck-text-primary);
}

@media (max-width: 900px) {
  .hero-grid,
  .content-grid,
  .interests-grid,
  .highlight-grid {
    grid-template-columns: 1fr;
  }

  .hero-copy h1 {
    font-size: 3.3rem;
  }

  .hero-copy h2 {
    font-size: 2rem;
  }

  .timeline-column {
    position: static;
  }
}

@media (max-width: 640px) {
  .about-inner {
    width: min(100% - 24px, 1120px);
  }

  .about-hero {
    padding: 64px 0 56px;
  }

  .hero-copy h1 {
    font-size: 2.35rem;
    line-height: 1.04;
  }

  .hero-copy h2 {
    font-size: 1.7rem;
  }

  .hero-intro {
    font-size: 1rem;
  }

  .about-section {
    padding: 64px 0;
  }

  .story-block h2,
  .section-heading h2 {
    font-size: 1.85rem;
  }

  .profile-card :deep(.q-card__section),
  .timeline-card :deep(.q-card__section),
  .interests-card :deep(.q-card__section),
  .highlight-card :deep(.q-card__section) {
    padding: 22px;
  }
}
</style>
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 30px;
}
