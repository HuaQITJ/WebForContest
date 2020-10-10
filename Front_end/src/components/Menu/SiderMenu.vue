<template>
  <a-menu
    :selectedKeys="selectedKeys"
    :openKeys.sync="openKeys"
    mode="inline"
    :theme="navTheme"
  >
    <template v-for="item in menuData">
      <a-menu-item
        v-if="!item.children"
        :key="item.path"
        @click="() => $router.push({ path: item.path, query: $route.query })"
      >
        <IconFont v-if="item.meta.icon" :type="item.meta.icon" />
        <span>{{ item.meta.title }}</span>
      </a-menu-item>
      <sub-menu v-else :menu-info="item" :key="item.path" />
    </template>
  </a-menu>
</template>

<script>
import { mixin } from "@/utils/mixin";
import SubMenu from "./SubMenu";
import { Icon } from "ant-design-vue";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: require("@/assets/font/iconfont")
});

export default {
  name: "SiderMenu",
  mixins: [mixin],
  data() {
    this.selectedKeysMap = {};
    this.openKeysMap = {};
    const menuData = this.getMenuData(this.$router.options.routes);
    return {
      menuData,
      selectedKeys: this.selectedKeysMap[this.$route.path],
      openKeys: this.collapsed ? [] : this.openKeysMap[this.$route.path]
    };
  },
  methods: {
    getMenuData(routes = [], parentKeys = [], selectedKey) {
      const menuData = [];
      for (let item of routes) {
        if (item.name && !item.hideInMenu) {
          this.openKeysMap[item.path] = parentKeys;
          this.selectedKeysMap[item.path] = [selectedKey || item.path];
          const newItem = { ...item };
          delete newItem.children;
          if (item.children) {
            newItem.children = this.getMenuData(item.children, [
              ...parentKeys,
              item.path
            ]);
          } else {
            this.getMenuData(
              item.children,
              selectedKey ? parentKeys : [...parentKeys, item.path],
              selectedKey || item.path
            );
          }
          menuData.push(newItem);
        } else if (!item.hideInMenu && item.children) {
          menuData.push(
            ...this.getMenuData(item.children, [...parentKeys, item.path])
          );
        }
      }
      return menuData;
    }
  },
  props: {
    collapsed: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    "$route.path": function(val) {
      this.selectedKeys = this.selectedKeysMap[val];
      this.openKeys = this.collapsed ? [] : this.openKeysMap[val];
    },
    collapsed(val) {
      if (val) {
        this.cacheOpenKeys = this.openKeys;
        this.openKeys = [];
      } else {
        this.openKeys = this.cacheOpenKeys;
      }
    }
  },
  components: {
    SubMenu,
    IconFont
  }
};
</script>
