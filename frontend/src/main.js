import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'



Vue.config.productionTip = false

new Vue({
  iconfont: 'mdi',
  router,
  render: h => h(App)
}).$mount('#app')

