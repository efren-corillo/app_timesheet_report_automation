/* eslint-env node */
import { defineConfig } from '@quasar/app-vite'
export default defineConfig(() => ({
  css: ['app.scss'],
  build: { target: { browser: ['es2022', 'edge90', 'firefox90', 'chrome90', 'safari15'] } },
  devServer: { open: false, port: 8080, host: '0.0.0.0' },
  framework: { plugins: [] }
}))
