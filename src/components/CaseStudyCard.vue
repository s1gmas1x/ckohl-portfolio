<template>
  <q-card flat bordered class="case-study-card">
    <q-card-section>
      <div class="case-study-card__header">
        <span>{{ caseStudy.category }}</span>
        <h3>{{ caseStudy.title }}</h3>
      </div>

      <p>{{ caseStudy.summary }}</p>

      <div class="tag-list" aria-label="Case study technologies">
        <q-chip v-for="technology in caseStudy.technologies" :key="technology" outline square dense>
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
  height: 100%;
  background: var(--card-bg);
  border-color: var(--card-border);
  border-radius: 8px;
}

.case-study-card :deep(.q-card__section) {
  display: grid;
  gap: 14px;
  height: 100%;
  padding: 24px;
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
  font-size: 1.16rem;
  font-weight: 800;
}

.case-study-card p {
  margin: 0;
  color: var(--text-secondary);
  line-height: 1.65;
}

.case-study-card__link {
  justify-self: start;
  align-self: end;
  margin-top: 4px;
  font-weight: 700;
}

@media (max-width: 640px) {
  .case-study-card :deep(.q-card__section) {
    padding: 22px;
  }
}
</style>
