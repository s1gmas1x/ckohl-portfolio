export async function trackInternal(eventType, eventLabel = null) {
  return fetch('https://api.ckohl.com/api/page-visits', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'X-Tenant': 'portfolio',
    },
    body: JSON.stringify({
      page: window.location.pathname,
      referrer: document.referrer,
      user_agent: navigator.userAgent,
      type: eventType,
      label: eventLabel,
    }),
  })
}
