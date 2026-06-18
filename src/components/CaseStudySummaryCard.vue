<template>
  <q-card flat bordered class="summary-card">
    <q-card-section>
      <span>{{ label }}</span>
      <strong>{{ value }}</strong>
    </q-card-section>
  </q-card>
</template>

<script setup>
defineProps({
  label: {
    type: String,
    required: true,
  },
  value: {
    type: String,
    required: true,
  },
})
</script>

<style lang="scss" scoped>
.summary-card {
  background: var(--ck-surface-bg);
  border-color: var(--ck-border);
  border-radius: 8px;
}

.summary-card :deep(.q-card__section) {
  display: grid;
  gap: 8px;
  padding: 22px;
}

.summary-card span {
  color: var(--ck-text-muted);
  font-size: 0.86rem;
  font-weight: 700;
}

.summary-card strong {
  color: var(--ck-text-primary);
  font-size: 1rem;
  line-height: 1.45;
}
</style>
