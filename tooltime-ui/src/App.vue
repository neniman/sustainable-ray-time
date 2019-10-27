<template>
   <!-- <fullscreen ref="fullscreen" @change="fullscreenChange"> -->
    <div id="app">
      <!-- <button id="toggle-button" @click="fullScreen" :class="{'invisible' : fullscreen}"></button> -->
      <Header class="header-bar"/>
      <div class="main-container">
        <router-view/>
      </div>
    </div>
  <!-- </fullscreen> -->
</template>

<script lang="ts">
import Vue from 'vue';
import Fullscreen from "vue-fullscreen/src/component.vue"
import Header from '@/components/Header.vue';

export default Vue.extend({
  name: 'App',
  components: {
    Header,
    // Fullscreen
  },
  data() {
    return {
      fullscreen: false
    };
  },
  methods: {
    fullScreen() {
        this.$refs['fullscreen'].toggle()
    },
    fullscreenChange (fullscreen) {
    this.fullscreen = fullscreen
    }
  }
});
</script>

<style>
    /* background:#2b2a2a; // dark grey
    background:#3b3838; // Middle gray
    background:#979797; // Light gray  */

html {
  height: 100%;
  padding: 0%;
  margin: 0%;
  overflow: hidden !important;
  box-sizing: border-box;
}

body {
  height: 100%;
  padding: 0%;
  margin: 0%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  height: 100%;
  padding: 0%;
  margin: 0%;
  background: #2b2a2a;
}

.header-bar {
  height: 8%;
  width: 100%;
}

.middle-container {
  width: 453px;
  height: 486px;
  /* width: 40%;
  height: 60%; */
  margin: 0 auto;
}

.main-container {
  height: 90% !important; 
}

.first-pages {
  height: 100%;
  display: flex;
  align-items: center;
}

.header-container {
  height: 10%;
  box-sizing: border-box;
}

#toggle-button {
  position: absolute;
  bottom: 0;
  left: 0;
  background: #2b2a2a;
  width: 100px;
  height: 100px;
  border:none;
}

.invisible {
  display: none;
}
</style>
