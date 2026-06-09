<template>
  <q-layout view="lHh lpR fFf">
    <q-header class="site-header" :class="{ 'site-header--dark': isDarkMode }">
      <q-toolbar class="site-toolbar">
        <q-toolbar-title class="site-title">
          <router-link to="/" aria-label="Chad Kohl home" class="site-logo-link">
            <img :src="siteLogo" alt="CK." class="site-logo" />
          </router-link>
        </q-toolbar-title>

        <nav class="desktop-nav" aria-label="Primary navigation">
          <q-btn
            v-for="item in navigationItems"
            :key="item.label"
            flat
            no-caps
            :label="item.label"
            :icon="item.icon"
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
      class="site-drawer"
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
          <q-item-section v-if="item.icon" avatar>
            <q-icon :name="item.icon" />
          </q-item-section>
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
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useQuasar } from 'quasar'
import { useRoute, useRouter } from 'vue-router'
import ckLogoDark from 'src/assets/svg/logo/ck-logo.svg'
import ckLogoLight from 'src/assets/svg/logo/ck-logo-light.svg'

const THEME_STORAGE_KEY = 'ckohl-portfolio-theme'
const HEADER_SCROLL_OFFSET = 84

const $q = useQuasar()
const route = useRoute()
const router = useRouter()

const navigationItems = [
  { label: 'Projects', id: 'projects' },
  { label: 'Case Studies', id: 'case-studies' },
  { label: 'About', id: 'about' },
  { label: 'Skills', id: 'skills' },
  { label: 'Contact', id: 'contact', icon: 'mail_outline' },
]

const homeSectionIds = navigationItems.map((item) => item.id).filter(Boolean)

const rightDrawerOpen = ref(false)
const activeSectionId = ref('')
const isDarkMode = computed(() => $q.dark.isActive)
const siteLogo = computed(() => (isDarkMode.value ? ckLogoDark : ckLogoLight))
const themeIcon = computed(() => (isDarkMode.value ? 'light_mode' : 'dark_mode'))
const themeLabel = computed(() => (isDarkMode.value ? 'Use light theme' : 'Use dark theme'))

restoreThemePreference()

onMounted(() => {
  updateActiveSection()
  window.addEventListener('scroll', updateActiveSection, { passive: true })
  window.addEventListener('resize', updateActiveSection)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', updateActiveSection)
  window.removeEventListener('resize', updateActiveSection)
})

watch(
  () => route.fullPath,
  async () => {
    await nextTick()
    updateActiveSection()
  },
)

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
  if (item.path) {
    return route.path === item.path
  }

  return route.path === '/' && activeSectionId.value === item.id
}

async function scrollToSection(sectionId) {
  rightDrawerOpen.value = false

  if (route.path !== '/') {
    await router.push('/')
    await nextTick()
  }

  const section = document.getElementById(sectionId)

  if (!section) return

  const scrollTop = section.getBoundingClientRect().top + window.scrollY - HEADER_SCROLL_OFFSET

  window.scrollTo({
    top: Math.max(scrollTop, 0),
    behavior: 'smooth',
  })

  activeSectionId.value = sectionId
}

function updateActiveSection() {
  if (route.path !== '/') {
    activeSectionId.value = ''
    return
  }

  const sectionIds = homeSectionIds.filter((sectionId) => document.getElementById(sectionId))

  const activationOffset = HEADER_SCROLL_OFFSET + 56
  let currentSectionId = ''

  for (const sectionId of sectionIds) {
    const sectionTop = document.getElementById(sectionId)?.getBoundingClientRect().top

    if (sectionTop !== undefined && sectionTop <= activationOffset) {
      currentSectionId = sectionId
    }
  }

  activeSectionId.value = currentSectionId
}
</script>

<style lang="scss" scoped>
.site-header {
  background: var(--ck-header-bg);
  border-bottom: 1px solid var(--ck-header-border);
  color: var(--ck-text-primary);
  backdrop-filter: blur(14px);
  box-shadow: 0 8px 24px rgba(8, 12, 17, 0.04);
}

.site-toolbar {
  min-height: 68px;
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
  padding: 0;
}

.site-title {
  display: flex;
  align-items: center;
}

.site-logo-link {
  display: inline-flex;
  align-items: center;
}

.site-logo {
  display: block;
  width: 82px;
  height: auto;
}

.desktop-nav {
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-link {
  position: relative;
  min-height: 40px;
  padding: 0 10px;
  border-radius: 0;
  color: var(--ck-text-primary);
  font-size: 0.84rem;
  font-weight: 700;
}

.nav-link::after {
  content: '';
  position: absolute;
  right: 10px;
  bottom: 2px;
  left: 10px;
  height: 2px;
  background: var(--ck-link);
  border-radius: 999px;
  opacity: 0;
  transform: scaleX(0.72);
  transition:
    opacity 160ms ease,
    transform 160ms ease;
}

.desktop-nav .nav-link:last-child {
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid rgba(249, 156, 30, 0.5);
  border-radius: 8px;
  color: var(--ck-link);
}

.desktop-nav .nav-link:last-child::after {
  content: none;
}

.nav-link:hover,
.nav-link:focus,
.nav-link--active {
  background: transparent;
  color: var(--ck-link);
}

.nav-link:hover::after,
.nav-link:focus::after,
.nav-link--active::after {
  opacity: 1;
  transform: scaleX(1);
}

.desktop-nav .nav-link:last-child:hover,
.desktop-nav .nav-link:last-child:focus,
.desktop-nav .nav-link:last-child.nav-link--active {
  background: rgba(249, 156, 30, 0.08);
  border-color: var(--ck-link);
}

.theme-toggle {
  color: var(--ck-link);
  margin-left: 10px;
}

.mobile-menu-btn {
  color: var(--ck-link);
  display: none;
}

.site-header--dark {
  background: var(--ck-header-bg);
  border-bottom-color: var(--ck-header-border);
  color: var(--ck-text-primary);
  box-shadow: none;
}

.site-header--dark .nav-link,
.site-header--dark .theme-toggle,
.site-header--dark .mobile-menu-btn {
  color: var(--ck-text-primary);
}

.site-header--dark .desktop-nav .nav-link:last-child {
  color: var(--ck-accent-orange);
}

.site-header--dark .nav-link:hover,
.site-header--dark .nav-link:focus,
.site-header--dark .nav-link--active,
.site-header--dark .theme-toggle {
  color: var(--ck-accent-orange);
}

.drawer-link--active {
  background: rgba(249, 156, 30, 0.08);
  color: var(--ck-link);
  font-weight: 800;
  border-left: 3px solid var(--ck-link);
}

.site-drawer {
  background: var(--ck-surface-bg);
  border-color: var(--ck-header-border);
  color: var(--ck-text-primary);
}

@media (max-width: 720px) {
  .site-toolbar {
    min-height: 62px;
    width: min(100% - 48px, 1120px);
  }

  .site-logo {
    width: 72px;
  }

  .desktop-nav {
    display: none;
  }

  .mobile-menu-btn {
    display: inline-flex;
  }
}
</style>
