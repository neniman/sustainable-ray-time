<template>
  <div @click="$emit('pressed-input', text)" class="button-container">
      <label>{{ text }}</label>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    name: 'PinButton',
    props: {
        text: {
            type: String, 
            required: true
        }
    },
    data() {
      return {
      }
    },
    methods: {
    }
});
</script>

<style scoped>
.button-container {
    border-radius: 15px;
    background: #ffca10;
    border: 1px solid #979797;
    color: #000000;
}

.button-container:focus {
    background: #d38100;
}
</style>