<template>
  <div class="pin">
    <button @click="goToSuccess">Go Login Success</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Login',
    methods: {
        goToSuccess() {
            this.$router.push('success');
        }
    }
}
</script>