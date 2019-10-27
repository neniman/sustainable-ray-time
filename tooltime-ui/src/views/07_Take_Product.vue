<template>
  <div class="take first pages">
      <Div 
        class="middle-container" 
        :text="getText('take')"
        :imgPath="'scangif'"
      />
    <button @click="takeProduct">Go To Logout</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue';
export default Vue.extend({
    name: 'Take',
    components: {
      Div
    },
    methods: {
        takeProduct() {
            this.$router.push('logout');
        },
        getText(key) {
            return this.$store.state.texts[this.$store.state.language][key];
        }
    }
});
</script>