/**
 * 项目默认配置项
 * navTheme - sidebar theme ['dark', 'light'] 两种主题
 *
 * storageOptions: {} - Vue-ls 插件配置项 (localStorage/sessionStorage)
 *
 */

export default {
  navTheme: "dark", // theme for nav menu
  multiTab: false,

  // vue-ls options
  storageOptions: {
    namespace: "hsy__", // key prefix
    name: "ls", // name variable Vue.[ls] or this.[$ls],
    storage: "local" // storage name session, local, memory
  }
};
