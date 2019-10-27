<template>
<div class="category-container">
  <div @click="$router.push('tool-detail')" class="inner-container">
      <img v-bind:src="getPath" alt="img">
      <label> {{ text }} </label>
      <slot></slot>
  </div>
</div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'scan',
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
  data() {
      return {
      };
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
.inner-container {
    border-radius: 8px;
    background: #3b3838;
    border: 1px solid #979797;
    padding: 20px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
    object-fit: contain;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
}

.category-container {
    padding: 15px;
    width: 33.33% !important;
    height: 50% !important;
    box-sizing: border-box;
}

.category-container:active {
    background: #2b2a2a;
}

.category-container img {
    width: 100%;
    height: 70%;
    object-fit: scale-down;
}

.category-container label {
    color: #ffffff;
    font-family: 'Rubik', sans-serif;
    font-weight: bold;
    font-size: 25px;
    width: 100%;
    height: 30%;
}
</style>
