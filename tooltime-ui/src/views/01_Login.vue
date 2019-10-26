<template>
  <div class="Login">
    <Header />
    <Scan />
  </div>
</template>

<script lang="ts">
import Header from '@/components/Header.vue'
import Scan from '@/components/Scan.vue'

export default {
  name: 'Login',
  components: {
    Header,
    Scan
  }
}
</script>