<template>
  <div @click="goToFaceRecognition" class="login first-pages" id="test">
    <Div 
        class="middle-container" 
       :text="getText('login')"
       :imgPath="'scangif'"
    />
    {{ data }}
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
        this.checkNFC();
    },
    data() {
        return {
            data: 'Yo',
            lang: this.$store.state.language
        };
    },
    methods: {
        async checkNFC() {
            let id = '';
            let url = '192.168.4.1:5000/api/uid/1'
            let url2 = 'https://appdividend.com/2018/08/20/javascript-fetch-api-example-tutorial/'

            fetch(url2)
            .then(response => response.json())
            .then(data => {
                this.data=data;
                console.log(data);
            })
            .catch((error) => { console.log('hi'); console.error(error);});
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