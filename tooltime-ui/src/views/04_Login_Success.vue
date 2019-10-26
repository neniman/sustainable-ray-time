<template>
  <div class="success">
        <Div 
        class="middle-container" 
       :text="getText('success')"
       :imgPath="'check'"
       />
    <button @click="goToMain">Go To Main</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue'

export default Vue.extend({
    name: 'Success',
    components: {
      Div,
    },
    data() {
      return {
        lang: this.$store.state.language
      }
    },
    methods: {
        goToMain() {
            this.$router.push('main');
        },
        getText(key) {
          return this.$store.state.texts[this.lang][key];
        }
    }
});
</script>