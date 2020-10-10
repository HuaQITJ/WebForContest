import Vue from "vue";
import store from "@/store/index";

import config from "../config/defaultSettings";

export default function Initializer() {
  store.commit("TOGGLE_THEME", Vue.ls.get("DEFAULT_THEME", config.navTheme));
  store.commit(
    "TOGGLE_MULTI_TAB",
    Vue.ls.get("DEFAULT_MULTI_TAB", config.multiTab)
  );
}
