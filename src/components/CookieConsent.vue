<script setup>
import { onMounted, ref } from 'vue'
import { initializeGA } from 'src/utils/initializeGA.js'
import { trackInternal } from 'src/utils/trackInternal.js'

const showBanner = ref(false)

onMounted(() => {
  const consent = localStorage.getItem('ga-consent')

  if (!consent) {
    showBanner.value = true
    return
  }

  if (consent === 'accepted') {
    initializeGA()
  }
})

function acceptCookies() {
  localStorage.setItem('ga-consent', 'accepted')
  showBanner.value = false
  initializeGA()
}

async function declineCookies() {
  localStorage.setItem('ga-consent', 'declined')
  showBanner.value = false

  try {
    await trackInternal('cookie_decline', 'banner')
  } catch (error) {
    console.error('Tracking failed', error)
  }
}
</script>

<template>
  <div v-if="showBanner" class="cookie-overlay" role="presentation">
    <q-card
      class="cookie-banner"
      role="dialog"
      aria-modal="true"
      aria-live="polite"
      aria-label="Cookie consent"
    >
      <q-card-section class="cookie-banner__content">
        <div class="cookie-banner__copy">
          <p class="cookie-banner__eyebrow">Privacy preferences</p>
          <p class="cookie-banner__message">
            This portfolio uses analytics cookies to understand how visitors use the site and improve the experience.
          </p>
        </div>

        <div class="cookie-banner__actions">
          <q-btn unelevated no-caps color="primary" label="Accept" @click="acceptCookies" />
          <q-btn outline no-caps color="primary" label="Decline" @click="declineCookies" />
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<style lang="scss" scoped>
.cookie-overlay {
  position: fixed;
  inset: 0;
  z-index: 9998;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 20px;
  background: rgba(8, 12, 17, 0.42);
  pointer-events: all;
}

.cookie-banner {
  width: min(920px, 100%);
  background: var(--ck-surface-bg);
  border: 1px solid var(--ck-border);
  border-radius: 8px;
  box-shadow: 0 22px 70px rgba(0, 0, 0, 0.28);
  color: var(--ck-text-primary);
}

.cookie-banner__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 18px 20px;
}

.cookie-banner__copy {
  min-width: 0;
}

.cookie-banner__eyebrow {
  margin: 0 0 6px;
  color: var(--ck-link);
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.cookie-banner__message {
  margin: 0;
  color: var(--ck-text-secondary);
  font-size: 0.95rem;
  line-height: 1.55;
}

.cookie-banner__actions {
  display: flex;
  flex: 0 0 auto;
  gap: 10px;
}

@media (max-width: 640px) {
  .cookie-overlay {
    padding: 12px;
  }

  .cookie-banner__content {
    align-items: stretch;
    flex-direction: column;
    gap: 16px;
    padding: 16px;
  }

  .cookie-banner__actions {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
</style>
