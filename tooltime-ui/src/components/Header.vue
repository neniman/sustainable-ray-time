<template>
  <div class="header-container">
        <div class="icons-left">
            <img 
                v-if="$route.name !== 'login'" 
                @click="go('back')"
                src="@/assets/back.svg" 
                class="icon-back icons" 
                alt="folder">
            <!-- <div class="logo">  -->
                <img 
                    @click="go('/')" 
                    src="@/assets/logo.svg" 
                    class="icon-logo icons" 
                    alt="logo">
            <!-- </div> -->
            <img 
                @click="go('/')" 
                src="@/assets/logo.png" 
                class="icon-title icons" 
                alt="Tool Time!">
        </div>
        <div class="icons-right">
            <img v-if="showAllIcons" src="@/assets/cart.svg" class="icon-cart icons" alt="cart">
            <img v-if="showAllIcons" src="@/assets/folder.svg" class="icon-folder icons" alt="folder">
            <img :class="{'big' : !showAllIcons}" src="@/assets/language.svg" class="icon-language" alt="language">
            <img 
                @click="$router.push('/')"
                v-if="showAllIcons" 
                src="@/assets/logout.svg" 
                class="icon-logout" 
                alt="logout">
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
      go(path: string) {
          if (path === 'back') {
            this.$router.go(-1);
          } else {
            this.$router.push(path);
          }
      },
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

.icons-left, .logo {
    float: left;
    height: 100%;
}

.icons-left img {
    float: left;
}

.icons-right {
    float: right;
    height: 100%;
    object-fit: contain;
}

.icons-right img {
    padding: 0 10px 0 10px;
}

.icons-right img, .icons-left img, .logo {
    height: 100%;
    object-fit: scale-down;
    width: 15%;
}


.icon-logo {
    height: 200px;
}

.icon-title {
    width: 60% !important;
}

.big {
    width: 60% !important;
}
</style>
