<template>
  <q-layout view="lHh lpR fFf">
    <q-header class="site-header">
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
          icon="menu"
          aria-label="Open navigation"
          class="mobile-menu-btn"
          @click="toggleRightDrawer"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="rightDrawerOpen" side="right" bordered overlay :width="260">
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
import { ref } from 'vue'

const navigationItems = [
  { label: 'Projects', id: 'projects' },
  { label: 'Case Studies', id: 'case-studies' },
  { label: 'Skills', id: 'skills' },
  { label: 'Contact', id: 'contact' },
]

const rightDrawerOpen = ref(false)

function toggleRightDrawer() {
  rightDrawerOpen.value = !rightDrawerOpen.value
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

.mobile-menu-btn {
  display: none;
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
