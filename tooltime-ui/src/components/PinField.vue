<template>
  <div class="field-container">
        <div class="input-field">
            <input type="password" v-model="inputField" disabled>
        </div>
        <div class="buttons">
            <PinButton class="pin-button" v-for="(element, index) in buttons" 
            :key="index"
            :text="element"
            v-on:pressed-input="buttonPressed"
            />
        </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import PinButton from '@/components/PinButton.vue';
import { ApplicationState } from '@/util/enums';

export default Vue.extend({
    name: 'PinField',
    components: {
        PinButton
    },
    data() {
      return {
          buttons: this.$store.state.pinButtons,
          pressedButtons: [] as string[],
          inputField: ''
      }
    },
    methods: {
        buttonPressed(input: string) {
            if (input === '<') {
                this.pressedButtons = [];
            } else if (input === 'OK') {
                if (this.inputField == this.$store.state.pin) {
                    this.$store.state.appState = ApplicationState.LOGGED_IN;
                    this.$router.push('success');
                } else {
                    this.pressedButtons = [];
                }
            } else {
                this.pressedButtons.push(input);
            }
            this.inputField = this.pressedButtons.join('');

            console.log('input field: ', this.inputField);
        }
    }
});
</script>

<style scoped>
.field-container {
    height: 90%;
}

.button-container {
    border-radius: 15px;
    background: #ffca10;
    border: 1px solid #979797;
    color: #000000;
}

.button-container:active {
    background: #d38100;
}

.input-field {
    height: 20%;
}

.input-field input {
    width: 100%;
    box-sizing: border-box;
    border-radius: 5px;
    margin: 0 0 10px 0;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 30px;
}

.buttons {
    display: inline-block;
    width: 100%;
    height: 80%;
}

.pin-button {
    float: left;
    display: block;
    width: 33.33%;
    height: 25%;
    box-sizing: border-box;
    position: relative;
}
</style>