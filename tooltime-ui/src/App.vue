<template>
  <div id="app">
    <Header class="header-bar"/>
    <div class="main-container">
      <router-view/>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Header from '@/components/Header.vue';

export default Vue.extend({
  name: 'App',
  components: {
    Header
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
  overflow: hidden;
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
  margin: 0 auto;
}

.main-container {
  height: 92% !important; 
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
</style>
