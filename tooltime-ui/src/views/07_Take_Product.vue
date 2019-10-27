<template>
  <div class="take first-pages">
      <div v-if="showIt" class="overlay"><img :src="getPath('inactivity')"></div>
      <div class="lel">
      <Div 
        class="middle-container" 
        :text="getText('take')"
        :imgPath="'take'"
      />
      </div>
    <div class="other-box"> 
      <div class="el"><label style="color: #ffffff;">{{ getText('value')}}</label></div>
      <div class="el"><label style="color: #ffca10;">{{ getText('valueNum')}}</label></div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue';
export default Vue.extend({
    name: 'Take',
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
            this.showLogout();
          }, 1000) 
        }
    }
});
</script>

<style scoped>
.overlay {
  position: absolute;
  margin: 0 auto;
}

.take {
  flex-wrap: wrap;
}

.other-box {
  width: 453px;
  margin: 0 auto;
  border-radius: 15px;
  background: #3b3838;
  border: 1px solid #979797;
  padding: 25px;
}

.other-box .el {
  height: 40%;
  width: 100%;
  color: #ffffff;
  font-family: 'Rubik', sans-serif;
  font-weight: bold;
  font-size: 30px;
}

.lel {
  width: 100%;
  height: 60% !important;
}
</style>