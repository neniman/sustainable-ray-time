<template>
  <div class="pin first-pages">
      <Div 
        class="middle-container" 
        :text="$store.state.texts[$store.state.language].pinField"
      > 
        <PinField/> 
      </Div>
    <button @click="goToSuccess">Go Login Success</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Div from '@/components/Div.vue';
import PinField from '@/components/PinField.vue';
import { ApplicationState } from '@/util/enums';

export default Vue.extend({
    name: 'Login',
    components: {
      Div,
      PinField
    },
    methods: {
        goToSuccess() {
                              this.$store.state.appState = ApplicationState.LOGGED_IN;

            this.$router.push('success');
        }
    }
});
</script>