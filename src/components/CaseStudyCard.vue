<template>
  <q-card flat bordered class="case-study-card">
    <q-card-section>
      <div class="case-study-card__body">
        <div class="case-study-card__header">
          <span>{{ caseStudy.category }}</span>
          <h3>{{ caseStudy.title }}</h3>
        </div>

        <p>{{ caseStudy.summary }}</p>
      </div>

      <div class="case-study-card__actions">
        <div class="tag-list" aria-label="Case study technologies">
          <q-chip
            v-for="technology in caseStudy.technologies"
            :key="technology"
            outline
            square
            dense
          >
            {{ technology }}
          </q-chip>
        </div>

        <q-btn
          outline
          no-caps
          color="primary"
          icon-right="arrow_forward"
          label="Read case study"
          :to="caseStudy.path"
          class="case-study-card__link"
        />
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
defineProps({
  caseStudy: {
    type: Object,
    required: true,
  },
})
</script>

<style lang="scss" scoped>
.case-study-card {
  position: relative;
  height: 100%;
  background: var(--card-bg);
  border-color: var(--card-border);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
  overflow: hidden;
}

.case-study-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 24px;
  width: 48px;
  height: 3px;
  background: var(--ck-orange);
  border-radius: 0 0 999px 999px;
}

.case-study-card :deep(.q-card__section) {
  display: grid;
  align-content: start;
  gap: 22px;
  height: 100%;
  padding: 24px;
}

.case-study-card__body,
.case-study-card__actions {
  display: grid;
}

.case-study-card__body {
  gap: 14px;
}

.case-study-card__actions {
  align-self: end;
  gap: 16px;
  margin-top: auto;
}

.case-study-card__header {
  display: grid;
  gap: 8px;
}

.case-study-card__header span {
  color: var(--ck-link);
  font-size: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.case-study-card h3 {
  margin: 0;
  color: var(--text-primary);
  font-size: 1.18rem;
  font-weight: 800;
  line-height: 1.25;
}

.case-study-card p {
  margin: 0;
  color: var(--text-secondary);
  line-height: 1.65;
}

.case-study-card__link {
  justify-self: start;
  font-weight: 700;
}

.tag-list :deep(.q-chip) {
  font-weight: 700;
  margin: 0;
}

@media (max-width: 640px) {
  .case-study-card :deep(.q-card__section) {
    padding: 22px;
  }
}
</style>
