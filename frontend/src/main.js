import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import {
  store
} from './helpers/Store/store'


Vue.config.productionTip = false

new Vue({
  iconfont: 'mdi',
  router,
  store,
  render: h => h(App)
}).$mount('#app')

