import { mapState } from "vuex";

const mixin = {
  computed: {
    ...mapState({
      navTheme: state => state.theme.theme
    })
  }
};

export { mixin };
