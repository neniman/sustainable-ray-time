<template>
  <div @click="goToFaceRecognition" class="login">
    <Div 
        class="middle-container" 
       :text="getText('login')"
       :imgPath="'placeholderpng'"
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
.login {
    height: 100%;
    display: flex;
    align-items: center;
}
</style>