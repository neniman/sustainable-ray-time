<template>
  <div :class="{ 'taken' : taken }" class="tool-detail">
        <img class="el icon-voice" v-bind:src="getPath('voice')" alt="voice">
        <img class="el icon-tool" v-bind:src="getPathKey('imgMain')" alt="img-main">
        <div class="el">
            <label class="label-main"> {{ getPath('mainText') }} </label>
        </div> 
        <div class="el">
            <label class="el label-small"> {{ getPath('smallText') }} </label>
        </div> 
        <img class="el icon-usage" v-bind:src="getPathKey('usage')" alt="usage">
        <img class="el icon-poss" v-bind:src="getPathKey('possibilities')" alt="possibilities">
        <div v-if="!taken" class="bottom-row">
            <button class="icon-plus">+</button>
                <label> {{ count }} </label>
            <button class="icon-minus">-</button>
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
            // let storeKey = this.getText(key);
            // console.log(this.keyId + '-' + storeKey);
            // return require(`@/assets/${this.keyId}-${storeKey}.svg`);
            return require(`@/assets/safety.svg`);
        },
        getPath(key): any {
            return require(`@/assets/safety.svg`);
            // return require(`@/assets/${key}.svg`);
        },
        getText(key): any {
            return this.$store.state.texts[this.$store.state.language].tools[this.keyId][key]; 
        }
  }
});
</script>

<style scoped>
.el {
    width: 100%;
}
.icon-voice {
    height: 10%;
}

.icon-tool {
    height: 40%;
}

.label-main {
    height: 15%
}

.label-small {
    height: 5%;
}

.icon-usage, .icon-poss {
    height: 10%;
}

.bottom-row {
    height: 20%;
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
