module.exports = {
  content: [
    './templates/**/*.html',
    './src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),        // ปลั๊กอินสำหรับฟอร์ม
    require('@tailwindcss/typography'),   // ปลั๊กอินสำหรับ typography
    require('@tailwindcss/aspect-ratio'), // ปลั๊กอินสำหรับ aspect-ratio
  ],
}
