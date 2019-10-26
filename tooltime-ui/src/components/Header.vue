<template>
  <div @click="goHome" class="header-container">
        <div class="icons-left">
            <img v-if="$route.name !== 'login'" src="@/assets/cart.svg" class="icon-back icons" alt="folder">
            <img src="@/assets/logo.svg" class="icon-logo icons" alt="logo">
            <img src="@/assets/tool-time.svg" class="icon-title icons" alt="Tool Time!">
        </div>
        <div class="icons-right">
            <img v-if="showAllIcons" src="@/assets/cart.svg" class="icon-cart icons" alt="cart">
            <img v-if="showAllIcons" src="@/assets/folder.svg" class="icon-folder icons" alt="folder">
            <img src="@/assets/language.svg" class="icon-language" alt="language">
            <img v-if="showAllIcons" src="@/assets/cart.svg" class="icon-logout" alt="logout">
        </div>
  </div>
</template>

<script lang="ts">

import { ApplicationState } from '@/util/enums'

export default {
  name: 'tooltime-header',
  data() {
      return {
      };
  },
  computed: {
      showAllIcons() {
          return this.$store.state.appState !== ApplicationState.LOGGED_OUT;
      }
  },
  methods: {
      goHome() {
          let path;
          switch(this.$store.state.appState) {
                case ApplicationState.LOGGED_OUT: 
                    path = '/';
                    break;
                case ApplicationState.LOGGED_IN_NORMAL: 
                    path = '/';
                    break;
                case ApplicationState.LOGGED_IN_SUPER: 
                    path = '/';
                    break;
                default: 
                    path = '/';
                    break;
          }
          this.$router.push(path);
      }
  }

}
</script>

<style scoped>
.header-container {
    background:#ffca10;
}
.icons {
    height: 100%;
    width: 10%;
}

.icons-left {
    float: left;
}

.icons-right {
    float: right;
}
</style>
