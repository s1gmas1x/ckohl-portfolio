import gardenPlannerMapThumb from 'src/assets/images/garden-app/garden-planner-map-thumb.png'
import kitchenRatioOverviewThumb from 'src/assets/images/kitchenratio/kitchenratio-overview-thumb.png'
import weatherMapSatelliteRadar from 'src/assets/images/weather-map/weather-map-satellite-radar.png'

export const projects = [
  {
    title: 'Gardening App',
    description:
      'A database-driven garden planning app for mapping growing areas, tracking plants, and organizing seasonal work.',
    tags: ['Laravel', 'Vue 3', 'PostgreSQL'],
    url: 'https://garden.ckohl.com/',
    image: {
      src: gardenPlannerMapThumb,
      alt: 'Garden Planning App map layout screenshot',
    },
  },
  {
    title: "KitchenRatio: Baker's Math Calculator",
    description:
      "A Vue 3 baking calculator for scaling formulas, checking hydration, and working with baker's percentages.",
    tags: ['Vue 3', 'Pinia', 'Calculator'],
    url: 'https://kitchenratio.com/calculator',
    image: {
      src: kitchenRatioOverviewThumb,
      alt: 'KitchenRatio overview screenshot',
    },
  },
  {
    title: 'Weather map',
    description:
      'A Leaflet weather map that combines radar, alerts, hurricane tracking, and multiple map layers.',
    tags: ['Leaflet', 'Esri-Leaflet', 'Weather APIs'],
    url: 'https://weather.ckohl.com/',
    image: {
      src: weatherMapSatelliteRadar,
      alt: 'Weather Map satellite radar layer screenshot',
    },
  },
  {
    title: 'Previous landing page',
    description:
      'A responsive static landing page preserved from an earlier Laravel-based version of the site.',
    tags: ['SCSS', 'Responsive design', 'Static site'],
    url: 'https://oldsite.ckohl.com',
  },
]
