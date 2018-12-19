import {
    signIn
  } from "../../login/login";
  
  import router from '../../../router/index'
    
  const state = {
    token: null,
    email: null,
    auth: false,
  };
  
  const getters = {
    isLoggedIn: state => {
      return state.token !== null;
    },
    getToken: state => {
      return state.token;
    },
    authResult: state => {
      return state.auth;
    },
    getAccountEmail: state => {
      return state.email;
    }
  }
  
  const mutations = {
    login: (state, payload) => {
      state.token = payload.token;
      state.user = payload.user;
      state.auth = true;
    },
    logout: (state) => {
      localStorage.removeItem("token");
      localStorage.removeItem("username");
      state.token = null;
      state.user = null;
      state.auth = false;
      router.replace('/');
    }
  }
  
  const actions = {
    authLogin: ({ commit, dispatch }, payload) => {
      return new Promise((resolve, reject) => {
        signIn(payload.email, payload.password)
          .then(suc => {
            localStorage.setItem("token", suc.data.jwt);
            localStorage.setItem("email", suc.data.email);
            commit('login', {
              'token': suc.data.jwt,
              'email': suc.data.email,
              'userLevel': suc.data.level_id
            });
            dispatch('setLogoutTime', 3600);
            router.replace('/homePage');
            resolve(true);
          })
          .catch(() => {
              commit('logout');
              reject(Error("An error has occurred! Please try again."));
            })
      })
    },
  
  }
  
  export default {
    state,
    getters,
    mutations,
    actions
  }