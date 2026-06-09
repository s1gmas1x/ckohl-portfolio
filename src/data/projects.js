import gardenPlannerMapThumb from 'src/assets/images/garden-app/garden-planner-map-thumb.png'
import kitchenRatioOverviewThumb from 'src/assets/images/kitchenratio/kitchenratio-overview-thumb.png'
import weatherMapSatelliteRadar from 'src/assets/images/weather-map/weather-map-satellite-radar.png'

export const projects = [
  {
    title: 'Gardening App',
    description:
      'Garden planning and plant tracking app for keeping seasonal work organized in one place.',
    tags: ['Garden planning', 'Product UI', 'Side project'],
    url: 'https://garden.ckohl.com/',
    image: {
      src: gardenPlannerMapThumb,
      alt: 'Garden Planning App map layout screenshot',
    },
  },
  {
    title: "KitchenRatio: Baker's Math Calculator",
    description:
      "Vue 3 calculator that helps bakers scale recipes and test dough formulas with baker's percentages.",
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
      'Interactive weather map built with Leaflet and Esri-Leaflet using live weather layers and map controls.',
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
      'Earlier static marketing landing page converted from a Laravel app with responsive layouts.',
    tags: ['SCSS', 'Responsive design', 'Static site'],
    url: 'https://oldsite.ckohl.com',
  },
]
