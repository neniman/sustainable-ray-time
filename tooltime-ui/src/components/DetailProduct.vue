<template>
  <div @click="taken ? '' : $router.push('take-product')" :class="{ 'taken' : taken }" class="tool-detail">
        <img class="el icon-voice" v-bind:src="getPath('voice')" alt="voice">
        <img class="el icon-tool" v-bind:src="getPath('img-main')" alt="img-main">
        <label class="el label-main"> {{ getText('mainText') }} </label>
        <label class="el label-small"> {{ getText('smallText') }} </label>
        <img class="el icon-usage" v-bind:src="getPath('usage')" alt="usage">
        <img class="el icon-poss" v-bind:src="getPath('possibilities')" alt="possibilities">
        <div v-if="!taken" class="bottom-row">
            <img class="icon-plus" :src="getPath('plus')" alt="plus">
                <label> {{ count }} </label>
            <img class="icon-minus" :src="getPath('minus')" alt="minus">
        </div>
        <div v-else class="bottom-button">
            <button>
                {{ $store.state.texts[$store.state.language].reserve}}
            </button>
        </div>
      <slot></slot>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

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
          taken: true
      };
  },
  methods: {
        getPath(key): any {
        //   return require(`@/assets/${this.imgPath}-${key}.svg`);
          return require(`@/assets/safety.svg`);
        },
        getText(key): any {
            return 'Bla';
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
