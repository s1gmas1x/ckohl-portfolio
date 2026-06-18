<template>
  <div
    class="section-heading"
    :style="{ '--section-heading-max-width': maxWidth }"
    :class="[
      { 'section-heading--with-action': hasAction },
      size === 'compact' ? 'section-heading--compact' : '',
    ]"
  >
    <div v-if="hasAction" class="section-heading__top">
      <p v-if="eyebrow" class="eyebrow">{{ eyebrow }}</p>
      <slot name="action" />
    </div>
    <p v-else-if="eyebrow" class="eyebrow">{{ eyebrow }}</p>

    <component :is="titleTag" class="section-heading__title">
      {{ title }}
    </component>

    <p v-if="description" class="section-heading__description">
      {{ description }}
    </p>
  </div>
</template>

<script setup>
import { computed, useSlots } from 'vue'

defineProps({
  eyebrow: {
    type: String,
    default: '',
  },
  title: {
    type: String,
    required: true,
  },
  titleTag: {
    type: String,
    default: 'h2',
  },
  description: {
    type: String,
    default: '',
  },
  size: {
    type: String,
    default: 'default',
    validator: (value) => ['default', 'compact'].includes(value),
  },
  maxWidth: {
    type: String,
    default: '720px',
  },
})

const slots = useSlots()
const hasAction = computed(() => Boolean(slots.action))
</script>

<style lang="scss" scoped>
.section-heading {
  max-width: var(--section-heading-max-width);
  margin-bottom: 30px;
}

.section-heading--with-action {
  max-width: none;
  margin-bottom: 14px;
}

.section-heading--with-action > .section-heading__title,
.section-heading--with-action > .section-heading__description {
  max-width: 720px;
}

.section-heading__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
}

.section-heading__top :deep(.section-heading__link) {
  margin-top: -8px;
  min-height: 34px;
  padding: 0;
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

.section-heading__title {
  margin: 0;
  color: var(--ck-text-strong);
  font-weight: 800;
  letter-spacing: 0;
  line-height: 1.1;
}

h1.section-heading__title {
  font-size: 3.5rem;
  line-height: 1.05;
}

h2.section-heading__title {
  font-size: 2.85rem;
}

.section-heading--compact {
  margin-bottom: 28px;
}

.section-heading--compact h2.section-heading__title {
  font-size: 2.2rem;
  line-height: 1.15;
}

.section-heading__description {
  margin: 14px 0 0;
  color: var(--ck-text-secondary);
  font-size: 1.08rem;
  line-height: 1.68;
}

@media (max-width: 900px) {
  h1.section-heading__title {
    font-size: 2.8rem;
  }
}

@media (max-width: 640px) {
  h1.section-heading__title {
    font-size: 2.25rem;
  }

  h2.section-heading__title {
    font-size: 2.2rem;
    line-height: 1.15;
  }

  .section-heading--compact h2.section-heading__title {
    font-size: 1.85rem;
  }

  .section-heading--with-action {
    display: grid;
    gap: 12px;
  }

  .section-heading__top {
    display: grid;
    gap: 8px;
  }

  .section-heading__top :deep(.section-heading__link) {
    justify-self: start;
  }
}
</style>
