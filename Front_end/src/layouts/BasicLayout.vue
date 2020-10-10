<template>
  <div>
    <a-layout
      id="components-layout-demo-custom-trigger"
      style="min-height: 100vh;"
    >
      <a-layout-sider
        :class="['sider', `ant-layout-sider-${navTheme}`]"
        :trigger="null"
        collapsible
        v-model="collapsed"
      >
        <Logo :showTitle="collapsed" />
        <SiderMenu :collapsed="collapsed" />
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0 24px 0 16px;">
          <a-icon
            class="trigger"
            :type="collapsed ? 'menu-unfold' : 'menu-fold'"
            @click="() => (collapsed = !collapsed)"
          />
          <Header />
        </a-layout-header>
        <a-layout-content
          :style="{
            margin: '24px 24px 0',
            height: '100%',
            minHeight: '280px'
          }"
        >
          <MultiTab />

          <transition name="page-transition">
            <router-view />
          </transition>
        </a-layout-content>
        <a-layout-footer style="textAlign: center">
          <Footer />
        </a-layout-footer>
      </a-layout>
    </a-layout>
  </div>
</template>

<script>
import Header from "@/components/Header/Header.vue";
import Footer from "@/components/Footer/Footer.vue";
import SiderMenu from "@/components/Menu/SiderMenu.vue";
import Logo from "../components/Logo/Logo.vue";
import MultiTab from "../components/MultiTab/MultiTab.vue";
import { mixin } from "@/utils/mixin";

export default {
  name: "BasicLayout",
  mixins: [mixin],
  data() {
    return {
      collapsed: false
    };
  },
  mounted() {
    const userAgent = navigator.userAgent;
    if (userAgent.indexOf("Edge") > -1) {
      this.$nextTick(() => {
        this.collapsed = !this.collapsed;
        setTimeout(() => {
          this.collapsed = !this.collapsed;
        }, 16);
      });
    }
  },
  components: {
    Header,
    Footer,
    SiderMenu,
    MultiTab,
    Logo
  }
};
</script>

<style lang="less" scoped>
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #da5054;
}

.page-transition-enter {
  opacity: 0;
}

.page-transition-leave-active {
  opacity: 0;
}

.page-transition-enter .page-transition-container,
.page-transition-leave-active .page-transition-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
