const DEFAULT_TRACKING_ID = 'G-X565PQ44ZS'

export function initializeGA(trackingId = DEFAULT_TRACKING_ID) {
  if (typeof window === 'undefined' || window.gtag) {
    return
  }

  const script = document.createElement('script')
  script.async = true
  script.src = `https://www.googletagmanager.com/gtag/js?id=${trackingId}`
  document.head.appendChild(script)

  window.dataLayer = window.dataLayer || []
  window.gtag = function () {
    window.dataLayer.push(arguments)
  }

  window.gtag('js', new Date())
  window.gtag('config', trackingId)
}

export { DEFAULT_TRACKING_ID }
