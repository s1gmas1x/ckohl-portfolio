<template>
  <q-page class="not-found-page">
    <div class="not-found-page__content">
      <p class="not-found-page__code">404</p>
      <h1>Oops. Nothing here...</h1>

      <q-btn
        class="q-mt-xl"
        color="primary"
        unelevated
        icon="home"
        to="/"
        label="Go Home"
        no-caps
      />
    </div>
  </q-page>
</template>

<script setup>
import { useMeta } from 'quasar'

useMeta({
  title: 'Page Not Found | Chad Kohl',
  meta: {
    robots: {
      name: 'robots',
      content: 'noindex, follow',
    },
  },
})
</script>

<style lang="scss" scoped>
.not-found-page {
  display: grid;
  min-height: calc(100vh - 68px);
  place-items: center;
  padding: 48px 24px;
  background: var(--ck-page-bg);
  color: var(--ck-text-primary);
  text-align: center;
}

.not-found-page__content {
  display: grid;
  justify-items: center;
}

.not-found-page__code {
  margin: 0;
  color: var(--ck-link);
  font-family: var(--ck-font-heading);
  font-size: clamp(6rem, 24vw, 13rem);
  font-weight: 800;
  line-height: 0.9;
}

.not-found-page h1 {
  margin: 18px 0 0;
  color: var(--ck-text-strong);
  font-size: clamp(1.8rem, 5vw, 3rem);
  font-weight: 800;
  line-height: 1.1;
}
</style>
