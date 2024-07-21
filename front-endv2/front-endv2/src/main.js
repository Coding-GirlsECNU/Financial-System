import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
//login
import store from './stores/counter' 
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import '../src/assets/main.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)
//login
app.use(store) 

app.use(createPinia())
app.use(router).use(ElementPlus)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }
app.mount('#app')
