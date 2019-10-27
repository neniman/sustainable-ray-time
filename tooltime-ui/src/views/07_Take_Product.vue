<template>
  <div class="take">
      <Div 
        class="middle-container" 
        :text="getText('login')"
        :imgPath="'scangif'"
      />
    <button @click="takeProduct">Go To Logout</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Take',
    methods: {
        takeProduct() {
            this.$router.push('logout');
        }
    }
}
</script>