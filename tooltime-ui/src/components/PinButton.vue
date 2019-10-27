<template>
    <div class="button-container-outer">
        <div @click="$emit('pressed-input', text)" class="button-container">
            <label>{{ text }}</label>
        </div>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    name: 'PinButton',
    props: {
        text: {
            type: String, 
            required: true
        }
    },
    data() {
      return {
      }
    },
    methods: {
    }
});
</script>

<style scoped>
.button-container-outer {
    padding: 15px;

}

.button-container {
    height: 100%;
    width: 100%;
    border-radius: 15px;
    background: #ffca10;
    color: #000000;
    border: none;
}

.button-container:focus {
    background: #d38100;
}

.button-container label {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    font-weight: bold;
    font-size: 30px;
    /* font-size: 50px; */
}
</style>