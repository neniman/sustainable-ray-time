<template>
  <div class="login">
    <Scan />
    <button @click="goToFaceRecognition">Go To Face Recoginition</button>
  </div>
</template>

<script lang="ts">
import Scan from '@/components/Scan.vue'

export default {
    name: 'Login',
    components: {
        Scan
    },
    methods: {
        scan() {
            // TODO get id from store / get triggered from store
        }, 
        goToFaceRecognition() {
            this.$router.push('face-recognition');
        }
    }
}
</script>