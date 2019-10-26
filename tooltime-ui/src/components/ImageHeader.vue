<template>
  <div class="img-header-container">
      <img :src="getPath" alt="img">
      <label> {{ text }} </label>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    name: 'ImageHeader',
    props: {
        text: {
        type: String,
        required: true
        },
        imgPath: {
            type: String, 
            required: false,
            default: ''
        }
    },
    computed: {
        getPath(): any {
          return require(`@/assets/${this.imgPath}.svg`);
        }
    },
    methods: {
    }
});
</script>

<style scoped>
.img-header-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px 10px 20px 10px;
}
.img-header-container img {
    padding-top: 10px;
    padding-right: 10px;
    height: 150%;
}
.img-header-container label {
    padding-top: 10px;
    color: #ffffff;
    font-family: 'Rubik', sans-serif;
    font-weight: bold;
    font-size: 30px;
}
</style>