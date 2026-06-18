<template>
  <router-link :to="to" :aria-label="ariaLabel" class="logo-mark" :style="logoStyle">
    <img :src="siteLogo" alt="CK." class="logo-mark__image" />
  </router-link>
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'
import ckLogoDark from 'src/assets/svg/logo/ck-logo.svg'
import ckLogoLight from 'src/assets/svg/logo/ck-logo-light.svg'

const props = defineProps({
  to: {
    type: [String, Object],
    default: '/',
  },
  ariaLabel: {
    type: String,
    default: 'Chad Kohl home',
  },
  size: {
    type: Number,
    default: 82,
  },
  mobileSize: {
    type: Number,
    default: null,
  },
})

const $q = useQuasar()
const isDarkMode = computed(() => $q.dark.isActive)
const siteLogo = computed(() => (isDarkMode.value ? ckLogoDark : ckLogoLight))
const logoStyle = computed(() => ({
  '--logo-size': `${props.size}px`,
  '--logo-mobile-size': `${props.mobileSize ?? props.size}px`,
}))
</script>

<style lang="scss" scoped>
.logo-mark {
  display: inline-flex;
  align-items: center;
  width: fit-content;
}

.logo-mark__image {
  display: block;
  width: var(--logo-size);
  height: auto;
}

@media (max-width: 720px) {
  .logo-mark__image {
    width: var(--logo-mobile-size);
  }
}
</style>
