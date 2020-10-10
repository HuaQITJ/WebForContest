import Vue from "vue";
import Vuex from "vuex";
import theme from "./modules/app";
import getters from "./getters";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    theme
  },
  getters
});
