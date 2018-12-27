import Vue from 'vue'
import Router from 'vue-router'
import BackendSupportApp from '../components/BackendSupportApp.vue'

Vue.use(Router)



export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'BackendSupportApp',
      component: BackendSupportApp
    }
  ],
})