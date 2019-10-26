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
    padding: 20px 10px 20px 10px;
}
.img-header-container img {
    height: 90%;
    padding-right: 10px;
}
.img-header-container label {
    color: #ffffff;
    font-family: 'Rubik', sans-serif;
    font-weight: bold;
    font-size: 30px;
}
</style>