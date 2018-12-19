import Vue from 'vue'
import Vuex from 'vuex'
//import createPersistedState from 'vuex-persistedstate'
//import * as Cookies from 'js-cookie'

import Login from './modules/login'

Vue.use(Vuex);

export const store = new Vuex.Store({
  modules: {
    Auth: Login
  }
});