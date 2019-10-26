<template>
  <div class="products">
    <!-- <Div 
      class="middle-container" 
      :text="getText('product')"
      :imgPath="'check'"
    /> -->
    <button @click="takeProduct">Take Product</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    name: 'Products',
    methods: {
        takeProduct() {
            this.$router.push('take-product');
        }
    }
});
</script>