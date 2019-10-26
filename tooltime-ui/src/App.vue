<template>
  <div id="app">
    <Header class="header-bar"/>
    <router-view />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Header from '@/components/Header.vue';
import Login from '@/views/01_Login.vue';

@Component({
  components: {
    Header,
    Login
  },
})
export default class App extends Vue {}
</script>

<style>

    /* background:#2b2a2a;  */
    /* background:#3b3838;  */
    /* background:#979797;  */
html {
  height: 100%;
  padding: 0%;
  margin: 0%;
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
</style>
