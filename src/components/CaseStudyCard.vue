<template>
  <q-card flat bordered class="case-study-card">
    <q-card-section>
      <div class="case-study-card__body">
        <div class="case-study-card__header">
          <q-chip
            outline
            square
            dense
            color="primary"
            class="case-study-card__category"
          >
            {{ caseStudy.category }}
          </q-chip>
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

.case-study-card :deep(.q-card__section) {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 16px;
  padding: 16px 6px 6px;
}

.case-study-card__body,
.case-study-card__actions {
  display: grid;
}

.case-study-card__body {
  gap: 10px;
}

.case-study-card__actions {
  align-self: stretch;
  gap: 12px;
  margin-top: auto;
}

.case-study-card__header {
  display: grid;
  align-content: start;
  gap: 10px;
}

.case-study-card__category {
  width: fit-content;
  min-height: 22px;
  margin: 0;
  padding: 0 8px;
  border-radius: 5px;
  font-size: 0.68rem;
  font-weight: 800;
  letter-spacing: 0.02em;
}

.case-study-card h3 {
  margin: 0;
  color: var(--ck-text-primary);
  font-size: 1.08rem;
  font-weight: 800;
  line-height: 1.25;
}

.case-study-card p {
  margin: 0;
  color: var(--ck-text-secondary);
  font-size: 0.92rem;
  line-height: 1.58;
}

.case-study-card__link {
  justify-self: start;
  min-height: 34px;
  padding: 0 10px;
  font-weight: 700;
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
</style>
