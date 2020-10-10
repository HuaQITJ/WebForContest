import Vue from "vue";

const theme = {
  state: {
    theme: "",
    multiTab: true
  },
  mutations: {
    TOGGLE_THEME(state, theme) {
      Vue.ls.set("DEFAULT_THEME", theme);
      state.theme = theme;
    },
    TOGGLE_MULTI_TAB: (state, bool) => {
      Vue.ls.set("DEFAULT_MULTI_TAB", bool);
      state.multiTab = bool;
    }
  },
  actions: {
    ToggleTheme({ commit }, theme) {
      commit("TOGGLE_THEME", theme);
    },
    ToggleMultiTab({ commit }, bool) {
      commit("TOGGLE_MULTI_TAB", bool);
    }
  }
};

export default theme;
