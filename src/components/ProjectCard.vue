<template>
  <q-card flat bordered class="project-card">
    <q-img
      v-if="project.image"
      :src="project.image.src"
      :alt="project.image.alt"
      :ratio="16 / 9"
      fit="cover"
      loading="lazy"
      class="project-card__image"
    />

    <q-card-section>
      <div class="project-card__body">
        <div class="project-card__title-row">
          <div class="project-card__title-main">
            <q-icon
              :name="project.icon"
              size="34px"
              class="project-card__icon"
              :style="{ color: project.iconColor }"
            />
            <component :is="titleTag" class="project-card__title">
              {{ project.title }}
            </component>
          </div>

          <q-chip
            v-if="project.status"
            outline
            square
            dense
            color="primary"
            class="project-card__status"
          >
            {{ project.status }}
          </q-chip>
        </div>

        <p>{{ project.description }}</p>
      </div>

      <div class="project-card__actions">
        <div class="tag-list" aria-label="Project tags">
          <q-chip v-for="tag in project.tags" :key="tag" outline square dense>
            {{ tag }}
          </q-chip>
        </div>

        <div class="project-card__link-row">
          <q-btn
            v-if="project.url"
            outline
            no-caps
            color="primary"
            icon-right="open_in_new"
            :label="projectLabel"
            :href="project.url"
            target="_blank"
            rel="noopener noreferrer"
            class="project-card__link"
          />
          <q-btn
            v-else-if="showUnavailableAction"
            outline
            no-caps
            color="primary"
            icon="schedule"
            :label="unavailableLabel"
            disable
            class="project-card__link"
          />
          <q-btn
            v-if="project.caseStudyPath"
            flat
            no-caps
            color="primary"
            icon-right="arrow_forward"
            :label="caseStudyLabel"
            :to="project.caseStudyPath"
            class="project-card__link"
          />
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
defineProps({
  project: {
    type: Object,
    required: true,
  },
  titleTag: {
    type: String,
    default: 'h3',
  },
  projectLabel: {
    type: String,
    default: 'Project',
  },
  caseStudyLabel: {
    type: String,
    default: 'Case study',
  },
  unavailableLabel: {
    type: String,
    default: 'Coming soon',
  },
  showUnavailableAction: {
    type: Boolean,
    default: false,
  },
})
</script>

<style lang="scss" scoped>
.project-card {
  display: flex;
  flex-direction: column;
  min-height: 0;
  height: 100%;
  padding: 10px;
  background: var(--ck-surface-bg);
  border-color: var(--ck-border);
  border-radius: 8px;
  box-shadow: var(--ck-card-shadow);
  overflow: hidden;
}

.project-card__image {
  background: var(--ck-surface-subtle);
  border: 1px solid var(--ck-border);
  border-radius: 6px;
  overflow: hidden;
}

.project-card__image :deep(.q-img__image) {
  transform: scale(1.01);
}

.project-card :deep(.q-card__section) {
  display: grid;
  align-content: start;
  gap: 16px;
  flex: 1;
  padding: 16px 6px 6px;
}

.project-card__body,
.project-card__actions {
  display: grid;
}

.project-card__body {
  gap: 10px;
}

.project-card__actions {
  align-self: end;
  gap: 12px;
  margin-top: auto;
}

.project-card__title-row {
  display: flex;
  align-items: center;
  gap: 12px;
  justify-content: space-between;
}

.project-card__title-main {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: center;
  gap: 12px;
  min-width: 0;
}

.project-card__title {
  margin: 0;
  color: var(--ck-text-primary);
  font-size: 1.08rem;
  font-weight: 800;
  line-height: 1.25;
}

.project-card__icon {
  color: var(--ck-link);
}

.project-card__status {
  width: fit-content;
  flex: 0 0 auto;
  min-height: 22px;
  margin: 0;
  padding: 0 8px;
  border-radius: 5px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.02em;
}

.project-card p {
  margin: 0;
  color: var(--ck-text-secondary);
  font-size: 0.92rem;
  line-height: 1.58;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag-list :deep(.q-chip) {
  min-height: 24px;
  padding: 0 9px;
  background: rgba(8, 12, 17, 0.045);
  border: 1px solid rgba(8, 12, 17, 0.08);
  border-radius: 5px;
  color: var(--ck-text-secondary);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0;
  margin: 0;
}

body.body--dark .tag-list :deep(.q-chip) {
  background: rgba(255, 255, 255, 0.055);
  border-color: rgba(255, 255, 255, 0.08);
  color: #c8d0da;
}

.project-card__link-row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 8px 10px;
}

.project-card__link {
  flex: 0 1 auto;
  min-height: 34px;
  padding: 0 10px;
  font-weight: 700;
}

@media (max-width: 640px) {
  .project-card__link-row {
    justify-content: flex-start;
  }
}
</style>
