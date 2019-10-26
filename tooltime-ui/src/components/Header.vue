<template>
  <div class="header-container">
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
  }

}
</script>

<style scoped>
</style>
