<template>
  <div @click="fullScreen" class="login first-pages" id="test">
    <Div 
        class="middle-container" 
       :text="getText('login')"
       :imgPath="'scangif'"
       />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue';
import { ApplicationState } from '@/util/enums';

export default Vue.extend({
    name: 'Login',
    components: {
        Div,
    },
    created() {
        this.$store.state.appState = ApplicationState.LOGGED_OUT;
    },
    data() {
        return {
            lang: this.$store.state.language
        };
    },
    methods: {
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