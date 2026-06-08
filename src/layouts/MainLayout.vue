<template>
  <q-layout view="lHh lpR fFf">
    <q-header class="site-header" :class="{ 'site-header--dark': isDarkMode }">
      <q-toolbar class="site-toolbar">
        <q-toolbar-title class="site-title"> Chad Kohl </q-toolbar-title>

        <nav class="desktop-nav" aria-label="Primary navigation">
          <q-btn
            v-for="item in navigationItems"
            :key="item.label"
            flat
            no-caps
            :label="item.label"
            class="nav-link"
            :class="{ 'nav-link--active': isNavigationItemActive(item) }"
            @click="handleNavigation(item)"
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

    <q-drawer
      v-model="rightDrawerOpen"
      side="right"
      bordered
      overlay
      :width="260"
      :dark="isDarkMode"
    >
      <q-list padding>
        <q-item-label header> Navigation </q-item-label>

        <q-item
          v-for="item in navigationItems"
          :key="item.label"
          v-close-popup
          clickable
          :active="isNavigationItemActive(item)"
          active-class="drawer-link--active"
          @click="handleNavigation(item)"
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
import { computed, nextTick, ref } from 'vue'
import { useQuasar } from 'quasar'
import { useRoute, useRouter } from 'vue-router'

const THEME_STORAGE_KEY = 'ckohl-portfolio-theme'

const $q = useQuasar()
const route = useRoute()
const router = useRouter()

const navigationItems = [
  { label: 'About', path: '/about' },
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

async function handleNavigation(item) {
  rightDrawerOpen.value = false

  if (item.path) {
    await router.push(item.path)
    return
  }

  await scrollToSection(item.id)
}

function isNavigationItemActive(item) {
  return Boolean(item.path && route.path === item.path)
}

async function scrollToSection(sectionId) {
  rightDrawerOpen.value = false

  if (route.path !== '/') {
    await router.push({ path: '/', hash: `#${sectionId}` })
    await nextTick()
  }

  document.getElementById(sectionId)?.scrollIntoView({
    behavior: 'smooth',
    block: 'start',
  })
}
</script>

<style lang="scss" scoped>
.site-header {
  background: var(--ck-header-bg);
  border-bottom: 1px solid var(--ck-header-border);
  color: var(--ck-text-primary);
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
  color: var(--ck-text-strong);
}

.desktop-nav {
  display: flex;
  align-items: center;
  gap: 4px;
}

.nav-link {
  color: var(--ck-text-primary);
  font-weight: 600;
}

.nav-link:hover,
.nav-link:focus,
.nav-link--active {
  color: var(--ck-link);
}

.theme-toggle {
  color: var(--ck-link);
  margin-left: 4px;
}

.mobile-menu-btn {
  color: var(--ck-link);
  display: none;
}

.site-header--dark {
  background: var(--ck-header-bg);
  border-bottom-color: var(--ck-header-border);
  color: var(--ck-text-primary);
}

.site-header--dark .nav-link,
.site-header--dark .theme-toggle,
.site-header--dark .mobile-menu-btn {
  color: var(--ck-text-primary);
}

.site-header--dark .nav-link:hover,
.site-header--dark .nav-link:focus,
.site-header--dark .nav-link--active,
.site-header--dark .theme-toggle {
  color: var(--ck-accent-orange);
}

.drawer-link--active {
  color: var(--ck-link);
  font-weight: 800;
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
