<template>
  <footer class="site-footer">
    <div class="site-footer__inner">
      <div class="site-footer__brand">
        <router-link to="/" aria-label="Chad Kohl home" class="site-footer__logo-link">
          <img :src="siteLogo" alt="CK." class="site-footer__logo" />
        </router-link>
        <p>Building web applications that make practical workflows easier to manage.</p>
      </div>

      <nav class="site-footer__links" aria-label="Footer navigation">
        <span class="site-footer__heading">Navigation</span>
        <button
          v-for="item in navigationLinks"
          :key="item.label"
          type="button"
          class="site-footer__link"
          @click="handleNavigation(item)"
        >
          {{ item.label }}
        </button>
      </nav>

      <div class="site-footer__links">
        <span class="site-footer__heading">Contact</span>
        <a class="site-footer__link site-footer__icon-link" href="mailto:chad_kohl@ckohl.com">
          <q-icon :name="mdiEmailOutline" size="18px" />
          <span>chad_kohl@ckohl.com</span>
        </a>
        <a
          v-for="link in socialLinks"
          :key="link.label"
          class="site-footer__link site-footer__icon-link"
          :href="link.url"
          target="_blank"
          rel="noopener noreferrer"
        >
          <q-icon :name="link.icon" size="18px" />
          <span>{{ link.label }}</span>
        </a>
      </div>
    </div>

    <div class="site-footer__bottom">
      <span>&copy; 2019-{{ year }} ckohl.com. All rights reserved.</span>
      <span>ckohl.com</span>
    </div>
  </footer>
</template>

<script setup>
import { computed, nextTick } from 'vue'
import { useQuasar } from 'quasar'
import { useRoute, useRouter } from 'vue-router'
import { mdiEmailOutline, mdiGithub, mdiLinkedin } from '@quasar/extras/mdi-v7'
import ckLogoDark from 'src/assets/svg/logo/ck-logo.svg'
import ckLogoLight from 'src/assets/svg/logo/ck-logo-light.svg'

const $q = useQuasar()
const route = useRoute()
const router = useRouter()

const navigationLinks = [
  { label: 'Projects', id: 'projects' },
  { label: 'Case Studies', id: 'case-studies' },
  { label: 'About', path: '/about' },
  { label: 'Skills', id: 'skills' },
  { label: 'Contact', id: 'contact' },
]

const socialLinks = [
  { label: 'GitHub', url: 'https://github.com/s1gmas1x', icon: mdiGithub },
  { label: 'LinkedIn', url: 'https://www.linkedin.com/in/chad-kohl401', icon: mdiLinkedin },
]

const isDarkMode = computed(() => $q.dark.isActive)
const siteLogo = computed(() => (isDarkMode.value ? ckLogoDark : ckLogoLight))
const year = new Date().getFullYear()

async function handleNavigation(item) {
  if (item.path) {
    await router.push(item.path)
    return
  }

  await scrollToHomeSection(item.id)
}

async function scrollToHomeSection(sectionId) {
  if (route.path !== '/') {
    await router.push('/')
    await nextTick()
  }

  document.getElementById(sectionId)?.scrollIntoView({
    behavior: 'smooth',
    block: 'start',
  })
}
</script>

<style lang="scss" scoped>
.site-footer {
  padding: 30px 0 24px;
  background:
    linear-gradient(180deg, color-mix(in srgb, var(--ck-section-bg) 42%, transparent), transparent),
    var(--ck-page-bg);
  border-top: 1px solid var(--ck-border);
  color: var(--ck-text-primary);
}

.site-footer__inner {
  display: grid;
  grid-template-columns: minmax(260px, 1fr) auto auto;
  gap: 36px;
  align-items: start;
  width: min(1120px, calc(100% - 32px));
  margin: 0 auto;
}

.site-footer__brand {
  display: grid;
  gap: 10px;
}

.site-footer__logo-link {
  display: inline-flex;
  width: fit-content;
}

.site-footer__logo {
  display: block;
  width: 82px;
  height: auto;
}

.site-footer__brand p {
  max-width: 360px;
  margin: 0;
  color: var(--ck-text-secondary);
  line-height: 1.62;
}

.site-footer__links {
  display: grid;
  gap: 5px;
  min-width: 142px;
}

.site-footer__heading {
  margin-bottom: 2px;
  color: var(--ck-text-strong);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.site-footer__link {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  width: fit-content;
  min-height: 24px;
  padding: 0;
  background: transparent;
  border: 0;
  color: var(--ck-text-secondary);
  cursor: pointer;
  font: inherit;
  line-height: 1.35;
  text-align: left;
  text-decoration: none;
  transition:
    color 0.18s ease,
    transform 0.18s ease;
}

.site-footer__link:hover,
.site-footer__link:focus {
  color: var(--ck-link);
  transform: translateX(2px);
}

.site-footer__icon-link :deep(.q-icon) {
  color: currentColor;
}

.site-footer__bottom {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  width: 100%;
  margin-top: 22px;
  padding: 16px max(16px, calc((100% - 1120px) / 2)) 0;
  border-top: 1px solid color-mix(in srgb, var(--ck-border) 72%, transparent);
  box-sizing: border-box;
  color: var(--ck-text-muted);
  font-size: 0.86rem;
}

@media (max-width: 760px) {
  .site-footer {
    padding-top: 28px;
  }

  .site-footer__inner {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 28px;
  }

  .site-footer__link {
    min-height: 28px;
  }

  .site-footer__brand {
    grid-column: 1 / -1;
  }
}

@media (max-width: 480px) {
  .site-footer__inner {
    width: min(1120px, calc(100% - 32px));
  }

  .site-footer__inner {
    grid-template-columns: 1fr;
  }

  .site-footer__bottom {
    display: grid;
    gap: 6px;
    padding-right: 24px;
    padding-left: 24px;
  }
}
</style>
