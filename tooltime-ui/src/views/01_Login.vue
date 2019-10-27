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
            lang: this.$store.state.language
        };
    },
    methods: {
        async checkNFC() {
            let id = '';
            let url = '192.168.4.1:5000/api/uid/1'

            fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.uid === '123' ) {
                    this.$router.push('pin');
                } else if (data.uid === '456') {
                    this.$router.push('return');
                }
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