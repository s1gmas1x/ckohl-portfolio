<template>
  <q-layout view="lHh lpR fFf">
    <q-header class="site-header" :class="{ 'site-header--dark': isDarkMode }">
      <q-toolbar class="site-toolbar">
        <q-toolbar-title class="site-title"> Chad Kohl </q-toolbar-title>

        <nav class="desktop-nav" aria-label="Primary navigation">
          <q-btn
            v-for="item in navigationItems"
            :key="item.id"
            flat
            no-caps
            :label="item.label"
            class="nav-link"
            @click="scrollToSection(item.id)"
          />
        </nav>

        <q-btn
          flat
          dense
          round
          :icon="themeIcon"
          :aria-label="themeLabel"
          class="theme-toggle"
          @click="toggleTheme"
        />

        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Open navigation"
          class="mobile-menu-btn"
          @click="toggleRightDrawer"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="rightDrawerOpen" side="right" bordered overlay :width="260" :dark="isDarkMode">
      <q-list padding>
        <q-item-label header> Navigation </q-item-label>

        <q-item
          v-for="item in navigationItems"
          :key="item.id"
          v-close-popup
          clickable
          @click="scrollToSection(item.id)"
        >
          <q-item-section>{{ item.label }}</q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useQuasar } from 'quasar'

const THEME_STORAGE_KEY = 'ckohl-portfolio-theme'

const $q = useQuasar()

const navigationItems = [
  { label: 'Projects', id: 'projects' },
  { label: 'Case Studies', id: 'case-studies' },
  { label: 'Skills', id: 'skills' },
  { label: 'Contact', id: 'contact' },
]

const rightDrawerOpen = ref(false)
const isDarkMode = computed(() => $q.dark.isActive)
const themeIcon = computed(() => (isDarkMode.value ? 'light_mode' : 'dark_mode'))
const themeLabel = computed(() => (isDarkMode.value ? 'Use light theme' : 'Use dark theme'))

restoreThemePreference()

function toggleRightDrawer() {
  rightDrawerOpen.value = !rightDrawerOpen.value
}

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

function scrollToSection(sectionId) {
  rightDrawerOpen.value = false

  document.getElementById(sectionId)?.scrollIntoView({
    behavior: 'smooth',
    block: 'start',
  })
}
</script>

<style lang="scss" scoped>
.site-header {
  background: rgba(255, 255, 255, 0.94);
  border-bottom: 1px solid #e6e8eb;
  color: #161a1d;
  backdrop-filter: blur(14px);
}

.site-toolbar {
  min-height: 72px;
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
  padding: 0;
}

.site-title {
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0;
}

.desktop-nav {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-link {
  color: #3c454c;
  font-weight: 600;
}

.theme-toggle {
  color: #3c454c;
  margin-left: 4px;
}

.mobile-menu-btn {
  display: none;
}

.site-header--dark {
  background: rgba(18, 24, 30, 0.94);
  border-bottom-color: #26323d;
  color: #f3f7fa;
}

.site-header--dark .nav-link,
.site-header--dark .theme-toggle,
.site-header--dark .mobile-menu-btn {
  color: #d7e0e7;
}

@media (max-width: 720px) {
  .site-toolbar {
    min-height: 64px;
    width: min(100% - 24px, 1120px);
  }

  .desktop-nav {
    display: none;
  }

  .mobile-menu-btn {
    display: inline-flex;
  }
}
</style>
