<template>
  <div class="header">
    <div class="content-box">
      <a-dropdown :trigger="['hover']" placement="bottomRight">
        <span class="header-theme">
          <IconFont type="icon-theme" style="font-size: 18px;" theme="filled" />
        </span>
        <a-menu slot="overlay">
          <a-menu-item key="0">
            <a href="javascript:;" @click="handleMenuTheme('dark')">
              <span>暗色菜单风格</span>
            </a>
          </a-menu-item>
          <a-menu-item key="1">
            <a href="javascript:;" @click="handleMenuTheme('light')">
              <span>亮色菜单风格</span>
            </a>
          </a-menu-item>
        </a-menu>
      </a-dropdown>

      <notice-icon class="action" />

      <a-dropdown>
        <span class="header-user">
          <a-avatar
            class="header-user-avatar"
            style="backgroundColor: #87d068; margin-right: 6px;"
            icon="user"
          />
          <span class="header-user-title">
            <strong>huoshaoy</strong>
            <span>免费用户</span>
          </span>
        </span>
        <a-menu slot="overlay" class="user-dropdown-menu-wrapper">
          <a-menu-item key="0">
            <a-icon type="user" />
            <span>个人中心</span>
          </a-menu-item>
          <a-menu-item key="1">
            <a-icon type="setting" />
            <span>账户设置</span>
          </a-menu-item>
          <a-menu-divider />
          <a-menu-item key="2">
            <a-icon type="logout" />
            <span>退出登录</span>
          </a-menu-item>
        </a-menu>
      </a-dropdown>
    </div>
  </div>
</template>

<script>
import NoticeIcon from "@/components/NoticeIcon/NoticeIcon.vue";
import { Icon } from "ant-design-vue";

const IconFont = Icon.createFromIconfontCN({
  scriptUrl: require("@/assets/font/iconfont")
});

export default {
  name: "Header",
  data() {
    return {
      avatar:
        "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
      theme: "dark"
    };
  },
  methods: {
    handleMenuTheme(theme) {
      this.$store.dispatch("ToggleTheme", theme);
    }
  },
  components: {
    NoticeIcon,
    IconFont
  }
};
</script>

<style lang="less" scoped>
@import "~@/assets/styles/global.less";

.header {
  float: right;

  .header-theme,
  .header-user {
    display: inline-block;
    padding: 0 6px;
    cursor: pointer;
  }

  .header-user-title {
    span {
      margin: 0 4px;
      background: @primary-color;
      padding: 2px 6px;
      border-radius: 3px;
      color: #fff;
      font-size: 12px;
    }
  }
}
</style>
