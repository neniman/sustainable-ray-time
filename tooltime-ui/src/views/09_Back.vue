<template>
  <div class="first-pages">
      <div v-if="showIt" class="overlay"><img :src="getPath('inactivity')"></div>
      <Div 
        class="middle-container" 
        :text="getText('return')"
        :imgPath="'take'"
      />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue';
export default Vue.extend({
    name: 'Back',
    components: {
      Div
    },
    data(){
      return {
        showIt: false
      };
    },
    mounted() {
      this.goOn();
    },
    methods: {
      getPath(key) {
          return require(`@/assets/${key}.svg`);
      },
        getText(key) {
            return this.$store.state.texts[this.$store.state.language][key];
        },
        goOn() {
          setTimeout(() => {
            this.showIt = true;
            this.showLogout();
          }, 1000) 
        },
        showLogout() {
            setTimeout(() => {
            this.$router.push('/');
          }, 1000) 
        }
    }
});
</script>

<style scoped>
.overlay {
  position: absolute;
  margin: 0 auto;
  left: 0;
  right: 0;
}

.cunt {
    border-radius: 15px;
    background: #3b3838;
    border: 1px solid #979797;
    padding: 25px;
}
</style>