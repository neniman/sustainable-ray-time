<template>
  <div class="container-div">
      <div class="div-label"><label> {{ text }} </label></div>
      <div v-if="showImg" class="div-img"><img v-if="showImg" v-bind:src="getPath" alt="img"></div>
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
          if (this.imgPath.includes('png')) {
            let path = this.imgPath.replace('png','')
            return require(`@/assets/${path}.png`);
          } else if (this.imgPath.includes('gif')) {
            let path = this.imgPath.replace('gif','')
            return require(`@/assets/${path}.gif`);

          } else {
            return require(`@/assets/${this.imgPath}.svg`);
          }
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

.container-div .div-label label {
  color: #ffffff;
  font-family: 'Rubik', sans-serif;
  font-weight: bold;
  font-size: 30px;
  height: 100%;
}

.container-div .div-label {
  height: 10%;
}

.container-div .div-img img {
  height: 100%;
  width: 100%;
  object-fit: contain;
}

.container-div .div-img {
  height: 90%;
}
</style>
