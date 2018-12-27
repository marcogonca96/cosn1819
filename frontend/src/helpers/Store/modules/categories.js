// import {
//     getCategories
// } from "@/helpers/Home/home.js";

const state = {
    categories: JSON.parse(localStorage.getItem('categories')),
    categoriesMapping: JSON.parse(localStorage.getItem('categoriesMapping'))
};

const getters = {
    categories: state => {
        return state.categories;
    },
    categoriesMapping: state => {
        return state.categoriesMapping;
    }
};

const mutations = {
    categories: (state, payload) => {
        state.categories = payload.categories;
        state.categoriesMapping = payload.categoriesMapping;

        localStorage.setItem("categories", JSON.stringify(state.categories));
        localStorage.setItem("categoriesMapping", JSON.stringify(state.categoriesMapping));
    }
};

const actions = {

    setCategories: ({commit}, payLoad) => {
        commit('categories', payLoad)
     }
};

export default {
    state,
    getters,
    mutations,
    actions
}