<template>
  <div class="take first-pages">
      <div v-if="showIt" class="overlay"><img style="margin: 100px;" :src="getPath('inactivity')"></div>
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
      this.openDoor();
      this.goOn();
    },
    methods: {
      getPath(key) {
          return require(`@/assets/${key}.svg`);
      },
      openDoor() {
          let url = '/api/uid/2/1'

        fetch(url)
            .then(response => {
                // console.log('res:', response);
                // console.log('json', response.json());
                return response.json();
            })
            .then((res) => {
                // console.log('res:', res);
                // if (res.uid === '0xabacaf1c' ) {
                //     this.$router.push('success');
                // } else if (res.uid === '0x410f49aa56581') {
                //     this.$router.push('return');
                // }
                // console.log(res);
            })
            .catch((error) => { 
                // console.log('error:', error); 
                // console.error(error);
                });
      },
        getText(key) {
            return this.$store.state.texts[this.$store.state.language][key];
        },
        goOn() {
          setTimeout(() => {
            this.showIt = true;
            this.showLogout();
          }, 5000) 
        },
        showLogout() {
            setTimeout(() => {
            this.$router.push('/');
          }, 5000) 
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
  background: #3b3838;
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