<template>
  <div class="return">
    <div class="upper">
      <img :src="getPath('zustand')" >
    </div>
    <div class="bottom">
      <img @click="$router.push('back')" :src="getPath('zubehoer')" >
      <img :src="getPath('kommentar')" >
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    methods: {
      getPath(key) {
        return require(`@/assets/${key}.svg`);
      },
      logout() {
          // this.$router. push('/');
      }
    }
});
</script>

<style scoped>
.return {
  height: 100%;
}
.upper, .bottom{
  width: 100%;
  height: 50%;
  box-sizing: border-box;
}

.upper img {
  height: 101%;
  width: 100%;
  padding: 0 20px 0 20px;
  box-sizing: border-box;
}

.bottom img {
  width: 50%;
  width: 50%;
  padding: 10px;
  box-sizing: border-box;
}
</style>