<template>
  <div @click="goToFaceRecognition" class="login first-pages" id="test">
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
    mounted() {
        this.$store.state.appState = ApplicationState.LOGGED_OUT;
        this.myInt = setInterval(this.checkNFC, 1000);
    },
    beforeDestroy() {
        clearInterval(this.myInt)
    },
    data() {
        return {
            lang: this.$store.state.language,
            myInt: null
        };
    },
    methods: {
        async checkNFC() {
            let id = '';
            let url = '/api/uid/1'

            fetch(url)
            .then(response => {
                // console.log('res:', response);
                // console.log('json', response.json());
                return response.json();
            })
            .then((res) => {
                // console.log('res:', res);
                if (res.uid === '0xabacaf1c' ) {
                    this.$router.push('pin');
                } else if (res.uid === '0x410f49aa56581') {
                    this.$router.push('return');
                }
                // console.log(res);
            })
            .catch((error) => { 
                // console.log('error:', error); 
                // console.error(error);
                });
        },
        goToFaceRecognition() {
            this.$router.push('pin');
        },
        getText(key) {
            return this.$store.state.texts[this.lang][key];
        }
    }
});
</script>

<style scoped>

</style>