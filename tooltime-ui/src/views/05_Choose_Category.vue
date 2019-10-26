<template>
  <div class="main">
    <button @click="chooseTool">ChooseTool</button>
  </div>
</template>

<script lang="ts">
export default {
    name: 'Main',
    methods: {
        chooseTool() {
            this.$router.push('tool-detail');
        }
    }
}
</script>