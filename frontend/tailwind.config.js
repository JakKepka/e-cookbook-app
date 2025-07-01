/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        'cookbook': {
          'light': '#F2F3AE',    // Jasny żółty
          'beige': '#EDD382',    // Beżowy
          'orange': '#FC9E4F',   // Pomarańczowy
          'red': '#F4442E',      // Czerwony
          'navy': '#020122',     // Ciemny granat
        }
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui'],
        serif: ['Playfair Display', 'ui-serif', 'Georgia'],
      },
    },
  },
  plugins: [],
} 