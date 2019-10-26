<template>
  <div class="success">
    <button @click="goToMain">Go To Main</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Success',
    methods: {
        goToMain() {
            this.$router.push('main');
        }
    }
}
</script>