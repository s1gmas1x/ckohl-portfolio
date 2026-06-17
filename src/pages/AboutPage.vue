<template>
  <q-page class="about-page">
    <section class="about-hero">
      <div class="about-inner">
        <PageBackLink label="Back to home" />

        <div class="hero-grid">
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
                icon="work"
                label="View projects"
                @click="scrollToHomeSection('projects')"
              />
              <q-btn
                outline
                no-caps
                color="primary"
                icon="mail_outline"
                label="Contact"
                @click="scrollToHomeSection('contact')"
              />
            </div>
          </div>

          <q-card flat bordered class="profile-card">
            <q-card-section>
              <figure class="profile-photo-frame">
                <img
                  :src="aboutPortrait"
                  alt="Black-and-white professional portrait of Chad Kohl"
                  class="profile-photo"
                />
              </figure>

              <div class="profile-card__statement">
                <div class="profile-mark" aria-label="Chad Kohl profile mark">CK</div>
                <p>How does this system work, and how can I make it better?</p>
              </div>
            </q-card-section>
          </q-card>
        </div>
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
import PageBackLink from 'src/components/PageBackLink.vue'
import aboutPortrait from 'src/assets/images/about/a_studio_portrait_scene_black_and_white_photograp.webp'
import { createPageMeta } from 'src/utils/seo.js'
import {
  aboutHero,
  aboutStorySections,
  aboutTimeline,
  closingThought,
  experienceHighlights,
  interests,
} from 'src/data/about.js'

const router = useRouter()
const HEADER_SCROLL_OFFSET = 84
const SECTION_WAIT_TIMEOUT = 1000

useMeta(
  createPageMeta({
    title: 'About Chad Kohl | Full Stack Developer in Colorado Springs',
    description:
      "Learn about Chad Kohl's background in software development, Azure support engineering, leadership, and practical product building in Colorado Springs.",
    path: '/about',
    socialTitle: 'About Chad Kohl | Full Stack Developer in Colorado Springs',
    socialDescription:
      "Meet Chad Kohl, a Colorado Springs full stack developer with experience in software development, Azure support, and practical product building.",
    imagePath: '/chad-kohl-social-share.webp',
    imageAlt: 'Black-and-white portrait of Chad Kohl',
    imageWidth: '960',
    imageHeight: '1200',
    imageType: 'image/webp',
  })
)

async function scrollToHomeSection(sectionId) {
  await router.push('/')
  await nextTick()

  const section = await waitForSection(sectionId)

  if (!section) return

  const scrollTop = section.getBoundingClientRect().top + window.scrollY - HEADER_SCROLL_OFFSET

  window.scrollTo({
    top: Math.max(scrollTop, 0),
    behavior: 'smooth',
  })
}

function waitForSection(sectionId) {
  return new Promise((resolve) => {
    const startedAt = performance.now()

    function findSection() {
      const section = document.getElementById(sectionId)

      if (section || performance.now() - startedAt >= SECTION_WAIT_TIMEOUT) {
        resolve(section)
        return
      }

      window.requestAnimationFrame(findSection)
    }

    findSection()
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
  padding: 48px 0 60px;
  background: linear-gradient(135deg, var(--ck-surface-subtle), var(--ck-background-light));
}

body.body--dark .about-hero {
  background:
    radial-gradient(circle at top left, rgba(249, 156, 30, 0.12), transparent 36%),
    linear-gradient(135deg, var(--ck-page-bg), var(--ck-section-bg));
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(300px, 0.85fr);
  gap: 48px;
  align-items: start;
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

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 30px;
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
  max-width: 390px;
  justify-self: end;
}

.profile-card :deep(.q-card__section) {
  display: grid;
  gap: 16px;
  padding: 16px;
}

.profile-photo-frame {
  position: relative;
  margin: 0;
  overflow: hidden;
  border: 1px solid color-mix(in srgb, var(--ck-border) 76%, transparent);
  border-radius: 8px;
  background: var(--ck-charcoal);
  aspect-ratio: 1 / 1;
}

.profile-photo {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 52% 18%;
}

.profile-card__statement {
  display: grid;
  gap: 12px;
  padding: 4px 8px 8px;
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
  font-size: 1.18rem;
  font-weight: 800;
  line-height: 1.35;
}

.about-section {
  padding: 64px 0;
}

.alternate-section {
  background: var(--ck-section-bg);
}

.content-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 360px;
  gap: 40px;
  align-items: start;
}

.story-column {
  display: grid;
  gap: 38px;
}

.story-block h2,
.section-heading h2 {
  font-size: 2.2rem;
  line-height: 1.15;
}

.story-block p:not(.eyebrow) {
  margin: 14px 0 0;
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
  margin-bottom: 28px;
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
  gap: 40px;
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

  .profile-card {
    width: min(100%, 460px);
    justify-self: start;
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
    padding: 36px 0 48px;
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

  .hero-actions {
    display: grid;
    gap: 10px;
  }

  .hero-actions :deep(.q-btn) {
    width: 100%;
    min-height: 44px;
  }

  .profile-card {
    width: 100%;
  }

  .profile-card :deep(.q-card__section) {
    gap: 14px;
    padding: 12px;
  }

  .profile-photo-frame {
    aspect-ratio: 5 / 4;
  }

  .profile-photo {
    object-position: 50% 20%;
  }

  .profile-card__statement {
    gap: 12px;
    padding: 6px 8px 8px;
  }

  .about-section {
    padding: 48px 0;
  }

  .story-block h2,
  .section-heading h2 {
    font-size: 1.85rem;
  }

  .timeline-card :deep(.q-card__section),
  .interests-card :deep(.q-card__section),
  .highlight-card :deep(.q-card__section) {
    padding: 22px;
  }
}
</style>
