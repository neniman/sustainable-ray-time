<template>
  <div :class="{ 'taken' : taken }" class="tool-detail">
        <img class="el icon-voice" v-bind:src="getPath('voice')" alt="voice">
        <img class="el icon-tool" v-bind:src="getPathKey('imgMain')" alt="img-main">
        <div class="el">
            <label class="label-main"> {{ getText('mainText') }} </label>
        </div> 
        <div class="el">
            <label class="el label-small"> {{ getText('smallText') }} </label>
        </div> 
        <img class="el icon-usage" v-bind:src="getPathKey('usage')" alt="usage">
        <div v-if="!taken" class="bottom-row">
            <button @click="counter('-')" class="icon-minus">-</button>
            <label class="count-label"> {{ count }} </label>
            <button @click="counter('+')" class="icon-plus">+</button>
        </div>
        <div v-else class="bottom-button">
            <button>
                {{ $store.state.texts[$store.state.language].reserve}}
            </button>
        </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import store from '../store';

export default Vue.extend({
  name: 'scan',
  props: {
    keyId: {
        type: String, 
        required: true
    }
  },
  data() {
      return {
          count: 0,
          taken: false
      };
  },
  methods: {
        getPathKey(key): any {
            let storeKey = this.getText(key);
            return require(`@/assets/${this.keyId}-${storeKey}.svg`);
            // return require(`@/assets/safety.svg`);
        },
        getPath(key): any {
            return require(`@/assets/${key}.svg`);
        },
        getText(key): any {
            return this.$store.state.texts[this.$store.state.language].tools[this.keyId][key]; 
        },
        counter(key) {
            if (key === '+') {
                this.count ++;
            } else {
                if (this.count === 0) {
                    return;
                } 
                this.count --;
            }
        }
  }
});
</script>

<style scoped>
.el {
    width: 100%;
    box-sizing: border-box;
}
.icon-voice {
    height: 5%;
    box-sizing: border-box;
    padding: 10px
}

.icon-tool {
    height: 40%;
}

.label-main {
    height: 15%;
    font-weight: bold;
    color: #ffffff;
    font-size: 28px;
}

.label-small {
    height: 5%;
    color: #ffffff;
    font-size: 18px;
}

.icon-usage {
    height: 20%;
    box-sizing: border-box;
    padding: 15px;
}

.bottom-row {
    padding: 10px 0 10px 0;
    box-sizing: border-box;
    height: 20%;
}

.count-label {
    width: 30%;
    font-size: 38px;
    font-weight: bold;
    color: #ffffff;
    padding: 15px
}

.bottom-row button {
    height: 100%;
  width: 30%;
  border-radius: 7px;
  background: #ffca10;
  border: 1px solid #979797;
  color: #ffffff;
  font-weight: bold;
  font-size: 30px;
  border: none;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
}

.taken {
    opacity: 0.3;
}

.tool-detail{
    border-radius: 15px;
    background: #3b3838;
    border: 1px solid #979797;
    padding: 25px;
    height: 90%;
    box-sizing: border-box;
}

.bottom-button button{
    width: 100%;
    border: none;
    border-radius: 7px;
    background: #ffca10;
}


</style>
