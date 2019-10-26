<template>
  <div class="field-container">
        <div class="input-field">
            <input type="text">
        </div>
        <div class="buttons">
            <PinButton v-for="(element, index) in buttons" 
            :key="index"
            :text="element"
            />
        </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import PinButton from '@/components/PinButton.vue'

export default Vue.extend({
    name: 'PinField',
    components: {
        PinButton
    },
    data() {
      return {
          buttons: this.$store.state.pinButtons
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