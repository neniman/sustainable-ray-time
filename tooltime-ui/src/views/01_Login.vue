<template>
  <div class="login">
    <Div 
        class="middle-container" 
       :text="getText('login')"
       :imgPath="'logo'"
       />
    <button @click="goToFaceRecognition">Go To Face Recoginition</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue'

export default Vue.extend({
    name: 'Login',
    components: {
        Div,
    },
    data() {
        return {
            lang: this.$store.state.language
        };
    },
    methods: {
        scan() {
            // TODO get id from store / get triggered from store
        }, 
        goToFaceRecognition() {
            this.$router.push('face-recognition');
        },
        getText(key) {
            return this.$store.state.texts[this.lang][key];
        }
    }
});
</script>

<style scoped>
</style>