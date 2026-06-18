<template>
  <q-btn
    flat
    dense
    round
    :icon="themeIcon"
    :aria-label="themeLabel"
    class="theme-toggle"
    @click="toggleTheme"
  />
</template>

<script setup>
import { computed } from 'vue'
import { useQuasar } from 'quasar'

const THEME_STORAGE_KEY = 'ckohl-portfolio-theme'

const $q = useQuasar()
const isDarkMode = computed(() => $q.dark.isActive)
const themeIcon = computed(() => (isDarkMode.value ? 'light_mode' : 'dark_mode'))
const themeLabel = computed(() => (isDarkMode.value ? 'Use light theme' : 'Use dark theme'))

restoreThemePreference()

function toggleTheme() {
  const nextIsDarkMode = !isDarkMode.value

  $q.dark.set(nextIsDarkMode)
  localStorage.setItem(THEME_STORAGE_KEY, nextIsDarkMode ? 'dark' : 'light')
}

function restoreThemePreference() {
  const storedTheme = localStorage.getItem(THEME_STORAGE_KEY)

  if (storedTheme === 'dark' || storedTheme === 'light') {
    $q.dark.set(storedTheme === 'dark')
  }
}
</script>

<style lang="scss" scoped>
.theme-toggle {
  color: var(--ck-link);
}

body.body--dark .theme-toggle {
  color: var(--ck-accent-orange);
}
</style>
