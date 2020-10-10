<template>
  <div class="logo">
    <router-link to="/">
      <img :src="logo" height="40" width="40" alt="logo" />
      <h1
        v-if="!showTitle"
        class="logo-title"
        :style="{
          color: navTheme === 'dark' ? '#FFF' : '#000'
        }"
      >
        {{ title }}
      </h1>
    </router-link>
  </div>
</template>

<script>
import { mixin } from "@/utils/mixin";

export default {
  name: "Logo",
  mixins: [mixin],
  data() {
    return {
      logo: require("@/assets/images/logo.png")
    };
  },
  props: {
    title: {
      type: String,
      required: false,
      default: "火烧云数据"
    },
    showTitle: {
      type: Boolean,
      required: true,
      default: false
    }
  },
  components: {}
};
</script>

<style lang="less" scoped>
.logo {
  height: 64px;
  position: relative;
  padding-left: 24px;
  overflow: hidden;
  line-height: 64px;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  img {
    display: inline-block;
    vertical-align: middle;
  }

  .logo-title {
    display: inline-block;
    color: #fff;
    font-size: 20px;
    margin: 0 0 0 12px;
    font-family: Avenir, Helvetica Neue, Arial, Helvetica, sans-serif;
    font-weight: 600;
    vertical-align: middle;
  }
}
</style>
