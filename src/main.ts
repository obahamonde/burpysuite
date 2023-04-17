import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { createPinia } from 'pinia'
import { Icon } from '@iconify/vue'
import { createAuth0 } from "@auth0/auth0-vue";
import routes from 'virtual:generated-pages'
import App from './App.vue'

import '@unocss/reset/tailwind.css'
import 'uno.css'

const app = createApp(App)
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
app
.use(router)
.use(createPinia())
.use(
  createAuth0({
    domain: "dev-tvhqmk7a.us.auth0.com",
    clientId: "53p0EBRRWxSYA3mSywbxhEeIlIexYWbs",
    authorizationParams: {
      redirect_uri: window.location.origin,
    },
  })
)
.component('Icon', Icon)
.mount('#app')
