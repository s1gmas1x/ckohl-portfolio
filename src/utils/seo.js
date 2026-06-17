export const SITE_NAME = 'Chad Kohl'
export const SITE_URL = 'https://ckohl.com'
export const DEFAULT_OG_IMAGE_PATH = '/portfolio-social-share.png'
export const DEFAULT_OG_IMAGE_WIDTH = '1024'
export const DEFAULT_OG_IMAGE_HEIGHT = '1536'

export function absoluteUrl(path = '/') {
  return new URL(path, SITE_URL).toString()
}

export function createPageMeta({
  title,
  description,
  path,
  type = 'website',
  socialTitle = title,
  socialDescription = description,
  imagePath = DEFAULT_OG_IMAGE_PATH,
  imageAlt = 'Portfolio preview showing CK branding and selected work from Chad Kohl',
  imageWidth = DEFAULT_OG_IMAGE_WIDTH,
  imageHeight = DEFAULT_OG_IMAGE_HEIGHT,
  imageType = 'image/png',
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
        content: socialTitle,
      },
      ogDescription: {
        property: 'og:description',
        content: socialDescription,
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
      ogImageUrl: {
        property: 'og:image:url',
        content: imageUrl,
      },
      ogImageSecureUrl: {
        property: 'og:image:secure_url',
        content: imageUrl,
      },
      ogImageType: {
        property: 'og:image:type',
        content: imageType,
      },
      ogImageAlt: {
        property: 'og:image:alt',
        content: imageAlt,
      },
      ogImageWidth: {
        property: 'og:image:width',
        content: imageWidth,
      },
      ogImageHeight: {
        property: 'og:image:height',
        content: imageHeight,
      },
      twitterCard: {
        name: 'twitter:card',
        content: 'summary_large_image',
      },
      twitterTitle: {
        name: 'twitter:title',
        content: socialTitle,
      },
      twitterDescription: {
        name: 'twitter:description',
        content: socialDescription,
      },
      twitterUrl: {
        name: 'twitter:url',
        content: canonicalUrl,
      },
      twitterImage: {
        name: 'twitter:image',
        content: imageUrl,
      },
      twitterImageSrc: {
        name: 'twitter:image:src',
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
