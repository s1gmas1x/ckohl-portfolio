export const SITE_NAME = 'Chad Kohl'
export const SITE_URL = 'https://ckohl.com'
export const DEFAULT_OG_IMAGE_PATH = '/chad-kohl-social-share.png'
export const DEFAULT_OG_IMAGE_WIDTH = '1122'
export const DEFAULT_OG_IMAGE_HEIGHT = '1402'

export function absoluteUrl(path = '/') {
  return new URL(path, SITE_URL).toString()
}

export function createPageMeta({
  title,
  description,
  path,
  type = 'website',
  imagePath = DEFAULT_OG_IMAGE_PATH,
  imageAlt = 'Portrait of Chad Kohl',
}) {
  const canonicalUrl = absoluteUrl(path)
  const imageUrl = absoluteUrl(imagePath)

  return {
    title,
    meta: {
      description: {
        name: 'description',
        content: description,
      },
      robots: {
        name: 'robots',
        content: 'index, follow',
      },
      ogType: {
        property: 'og:type',
        content: type,
      },
      ogUrl: {
        property: 'og:url',
        content: canonicalUrl,
      },
      ogTitle: {
        property: 'og:title',
        content: title,
      },
      ogDescription: {
        property: 'og:description',
        content: description,
      },
      ogSiteName: {
        property: 'og:site_name',
        content: SITE_NAME,
      },
      ogLocale: {
        property: 'og:locale',
        content: 'en_US',
      },
      ogImage: {
        property: 'og:image',
        content: imageUrl,
      },
      ogImageSecureUrl: {
        property: 'og:image:secure_url',
        content: imageUrl,
      },
      ogImageAlt: {
        property: 'og:image:alt',
        content: imageAlt,
      },
      ogImageWidth: {
        property: 'og:image:width',
        content: DEFAULT_OG_IMAGE_WIDTH,
      },
      ogImageHeight: {
        property: 'og:image:height',
        content: DEFAULT_OG_IMAGE_HEIGHT,
      },
      twitterCard: {
        name: 'twitter:card',
        content: 'summary_large_image',
      },
      twitterTitle: {
        name: 'twitter:title',
        content: title,
      },
      twitterDescription: {
        name: 'twitter:description',
        content: description,
      },
      twitterImage: {
        name: 'twitter:image',
        content: imageUrl,
      },
      twitterImageAlt: {
        name: 'twitter:image:alt',
        content: imageAlt,
      },
    },
    link: {
      canonical: {
        rel: 'canonical',
        href: canonicalUrl,
      },
    },
  }
}
