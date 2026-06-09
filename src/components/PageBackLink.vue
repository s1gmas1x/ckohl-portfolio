<template>
  <q-btn
    flat
    no-caps
    color="primary"
    icon="arrow_back"
    :label="label"
    :to="to"
    class="page-back-link"
  />
</template>

<script setup>
defineProps({
  label: {
    type: String,
    default: 'Back to portfolio',
  },
  to: {
    type: [String, Object],
    default: '/',
  },
})
</script>

<style lang="scss" scoped>
.page-back-link {
  margin-bottom: 32px;
  font-weight: 700;
}

@media (max-width: 640px) {
  .page-back-link {
    margin-bottom: 28px;
  }
}
</style>
