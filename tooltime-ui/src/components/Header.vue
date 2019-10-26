<template>
  <div @click="goHome" class="header-container">
      HEADER
      <div class="icons">
          <img src="" class="icon-language" alt="language">
          <img v-if="showAllIcons" src="" class="icon-cart" alt="cart">
          <img v-if="showAllIcons" src="" class="icon-folder" alt="folder">
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
</style>
