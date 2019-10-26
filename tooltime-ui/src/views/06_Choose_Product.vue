<template>
  <div class="products">
    <ImageHeader class="header-container" :text="getText('categoryProduct')" :imgPath="'big'"/>
    <div class="container-products">
      <DetailProduct class="product-el" :imgPath="'safety'" :text="'hello'" />
      <!-- <button @click="takeProduct">Take Product</button> -->
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import ImageHeader from '@/components/ImageHeader.vue';
import DetailProduct from '@/components/DetailProduct.vue';

export default Vue.extend({
    name: 'Products',
    components: {
      ImageHeader,
      DetailProduct
    },
    methods: {
        takeProduct() {
            this.$router.push('take-product');
        },
        getText(key) {
          return this.$store.state.texts[this.$store.state.language][key];
        }
    }
});
</script>

<style scoped>
.products {
    width: 100% !important;
    height: 100% !important;
}

.container-products {
  width: 100%;
  height: 90%;
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 0 auto;
  padding: 15px;
  padding-bottom: 30px;
}

.product-el {
  box-sizing: border-box;
  height: 100%;
}
</style>