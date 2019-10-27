<template>
  <div class="products">
    <ImageHeader class="header-container" :text="getText('categoryProduct')" :imgPath="'big'"/>
    <div class="container-products">
      <DetailProduct v-for="(element, index) in tools" 
      :key="index" class="product-el" :keyId="element"  />
      <!-- <button @click="takeProduct">Take Product</button> -->
    </div>
    <div class="container-btn">
      <button @click="takeProduct" class="rent-btn">{{ $store.state.texts[$store.state.language].rent }}</button>
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
    data() {
      return {
        tools: ['tool1', 'tool2', 'tool3']
      };
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
.header-container {
  height: 10%;
}

.products {
    width: 100% !important;
    height: 100%;
    box-sizing: border-box;
    padding: 10px;
}

.container-products {
  width: 100%;
  height: 78%;
  box-sizing: border-box;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  margin: 0 auto;
  padding: 15px;
}

.product-el {
  box-sizing: border-box;
  height: 100%;
  width: 30%;
}

.rent-btn {
  height: 100%;
  width: 100%;
  border-radius: 7px;
  background: #ffca10;
  border: 1px solid #979797;
  color: #000000;
  font-weight: bold;
  font-size: 30px;
  border: none;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
}

.rent-btn:focus {
  background: #d38100;
}

.container-btn {
  height: 13%;
  padding: 10px 0 10px 0;
  box-sizing: border-box;
}
</style>