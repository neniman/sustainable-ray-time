<template>
  <div class="logout">
    <button @click="logout">Logout</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Logout',
    methods: {
        logout() {
            this.$router.push('/');
        }
    }
}
</script>