<template>
  <q-card flat bordered class="detail-card">
    <q-card-section>
      <h2>{{ title }}</h2>
      <slot />
    </q-card-section>
  </q-card>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
})
</script>

<style lang="scss" scoped>
.detail-card {
  background: var(--ck-surface-bg);
  border-color: var(--ck-border);
  border-radius: 8px;
}

.detail-card :deep(.q-card__section) {
  display: grid;
  gap: 16px;
  padding: 22px;
}

.detail-card h2 {
  margin: 0;
  color: var(--ck-text-strong);
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: 0;
}

.detail-card :deep(.q-item) {
  min-height: 36px;
  padding: 4px 0;
  color: var(--ck-text-secondary);
}

.detail-card :deep(.q-item__section--avatar) {
  min-width: 34px;
}
</style>
