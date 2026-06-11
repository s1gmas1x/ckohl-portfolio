import gardenBedPlanner from 'src/assets/images/garden-app/garden-bed-planner-16x9.jpg'
import kitchenRatioDoughReadout from 'src/assets/images/kitchenratio/kitchenratio-dough-readout-16x9.jpg'
import nfcSmartCardScreenshot from 'src/assets/images/ckohl-works-nfc/ckohl-works-full-800.png'
import weatherMapThumbnail from 'src/assets/images/weather-map/weather-map-thumbnail-16x9.jpg'

export const projects = [
  {
    title: 'KitchenRatio',
    description:
      "A Vue 3 baking calculator for scaling formulas, checking hydration, and working with baker's percentages.",
    tags: ['Vue 3', 'Pinia', 'Calculator'],
    url: 'https://kitchenratio.com/calculator',
    caseStudyPath: '/case-studies/kitchenratio',
    icon: 'bakery_dining',
    iconColor: '#f99c1e',
    status: 'In Production',
    featured: true,
    image: {
      src: kitchenRatioDoughReadout,
      alt: 'KitchenRatio dough readout screenshot',
    },
  },
  {
    title: 'Garden App',
    description:
      'A database-driven garden planning app for mapping growing areas, tracking plants, and organizing seasonal work.',
    tags: ['Laravel', 'Vue 3', 'PostgreSQL'],
    url: 'https://garden.ckohl.com/',
    caseStudyPath: '/case-studies/garden-planning',
    icon: 'eco',
    iconColor: '#63d44e',
    status: 'In Development',
    featured: true,
    image: {
      src: gardenBedPlanner,
      alt: 'Garden App bed planner screenshot',
    },
  },
  {
    title: 'Weather Map',
    description:
      'A Leaflet weather map that combines radar, alerts, hurricane tracking, and multiple map layers.',
    tags: ['Leaflet', 'Esri-Leaflet', 'Weather APIs'],
    url: 'https://weather.ckohl.com/',
    icon: 'cloud',
    iconColor: '#44b9f2',
    status: 'In Development',
    featured: true,
    image: {
      src: weatherMapThumbnail,
      alt: 'Weather Map thumbnail screenshot',
    },
  },
  {
    title: 'Previous landing page',
    description:
      'A responsive static landing page preserved from an earlier Laravel-based version of the site.',
    tags: ['SCSS', 'Responsive design', 'Static site'],
    url: 'https://oldsite.ckohl.com',
    icon: 'web',
    iconColor: '#9aa6b5',
    featured: false,
  },
  {
    title: 'NFC Smart Business Card',
    description:
      'NFC-enabled business cards and QR experiences with dynamic landing pages, analytics, and customizable profiles.',
    tags: ['NFC', 'QR Codes', 'Analytics'],
    url: '',
    icon: 'contactless',
    iconColor: '#f99c1e',
    status: 'In Development',
    featured: false,
    image: {
      src: nfcSmartCardScreenshot,
      alt: 'Ckohl Works NFC smart business card landing page screenshot',
    },
  },
]

export const featuredProjects = projects.filter((project) => project.featured)
