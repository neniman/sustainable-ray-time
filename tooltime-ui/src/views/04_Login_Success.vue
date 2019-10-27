<template>
  <div class="success first-pages">
        <Div 
        class="middle-container" 
       :text="getText('success')"
       :imgPath="'successgif'"
       />
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
    mounted() {
      this.goOn();
    },
    data() {
      return {
        lang: this.$store.state.language
      }
    },
    methods: {
        goOn() {
          setTimeout(() => {
            this.$router.push('main');
          }, 2000) 
        },
        getText(key) {
          return this.$store.state.texts[this.lang][key];
        }
    }
});
</script>