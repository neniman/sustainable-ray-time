<template>
  <div class="face-recognition first-pages">
      <Div 
        class="middle-container" 
        :text="$store.state.texts[$store.state.language].pinField"
      > 
        <Camera /> 
      </Div>
    
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Camera from '@/components/Camera.vue';
import Div from '@/components/Div.vue';

export default Vue.extend({
    name: 'Login',
    components: {
      Camera,
      Div
    },    
   
});
</script>