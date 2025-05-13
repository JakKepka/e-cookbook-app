/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'custom-light': '#F2F3AE',
        'custom-yellow': '#EDD382',
        'custom-orange': '#FC9E4F',
        'custom-red': '#F4442E',
        'custom-dark': '#020122',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
  safelist: [
    'bg-custom-light',
    'bg-custom-yellow',
    'bg-custom-orange',
    'bg-custom-red',
    'bg-custom-dark',
    'text-custom-light',
    'text-custom-yellow',
    'text-custom-orange',
    'text-custom-red',
    'text-custom-dark',
    'hover:bg-custom-yellow',
    'hover:bg-custom-orange',
    'hover:bg-custom-red',
    'hover:text-custom-light',
    'hover:text-custom-dark',
  ]
} 