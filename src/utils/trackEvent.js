export function trackEvent({ category, action, label = null, value = null }) {
  if (typeof window === 'undefined' || localStorage.getItem('ga-consent') !== 'accepted') {
    return
  }

  if (typeof window.gtag !== 'function') {
    console.warn('gtag() not found. Google Analytics script is not loaded yet.')
    return
  }

  const eventObj = {
    event_category: category,
    event_label: label,
  }

  if (value !== null) {
    eventObj.value = value
  }

  window.gtag('event', action, eventObj)
}
