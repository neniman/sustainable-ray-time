<template>
  <div class="container-div">
      <label> {{ text }} </label>
      <img v-if="showImg" v-bind:src="getPath" alt="img">
      <slot></slot>
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
          showImg: this.imgPath !== ''
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
.container-div{
    border-radius: 15px;
    background: #3b3838;
    border: 1px solid #979797;
    padding: 25px;
}

.container-div label {
    color: #ffffff;
    font-family: 'Rubik', sans-serif;
    font-weight: bold;
    font-size: 30px;
}
</style>
