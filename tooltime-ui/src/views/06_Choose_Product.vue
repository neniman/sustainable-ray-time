<template>
  <div class="products">
    <button @click="takeProduct">Take Product</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Products',
    methods: {
        takeProduct() {
            this.$router.push('take-product');
        }
    }
}
</script>