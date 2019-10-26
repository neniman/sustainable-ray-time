<template>
  <div class="face-recognition">
    <button @click="goToPin">Go Pin</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Login',
    methods: {
        scan() {
            // TODO do facerecognition
        }, 
        goToPin() {
            this.$router.push('pin');
        }
    }
}
</script>