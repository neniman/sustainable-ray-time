<template>
  <div class="camera-container">
      <vue-web-cam
          ref="webcam"
          :device-id="deviceId"
          width="100%"
          @started="onStarted"
          @stopped="onStopped"
          @error="onError"
          @cameras="onCameras"
          @camera-change="onCameraChange"
      />
      <img :src="img" style="width: 50px; height: 50px;" class="img-responsive" />
    <button @click="goToPin">Go Pin</button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { WebCam } from "vue-web-cam";

export default Vue.extend({
    name: 'CameraContainer',
    components: {
      "vue-web-cam": WebCam
    },
     data() {
      return {
          img: null,
          camera: null,
          deviceId: null,
          devices: []
      };
    },
    computed: {
        device: function() {
            return this.devices.find(n => n.deviceId === this.deviceId);
        }
    },
    watch: {
        camera: function(id) {
            this.deviceId = id;
        },
        devices: function() {
            // Once we have a list select the first one
            const [first, ...tail] = this.devices;
            if (first) {
                this.camera = first.deviceId;
                this.deviceId = first.deviceId;
            }
        }
    },
    methods: {
        scan() {
            // TODO do facerecognition
        }, 
        goToPin() {
          this.img = this.$refs.webcam.capture();
            // console.log(WebCam.capture);
            // this.$router.push('pin');
        },
        onCapture() {
            this.img = this.$refs.webcam.capture();
        },
        onStarted(stream) {
            console.log("On Started Event", stream);
        },
        onStopped(stream) {
            console.log("On Stopped Event", stream);
        },
        onStop() {
            this.$refs.webcam.stop();
        },
        onStart() {
            this.$refs.webcam.start();
        },
        onError(error) {
            console.log("On Error Event", error);
        },
        onCameras(cameras) {
            this.devices = cameras;
            console.log("On Cameras Event", cameras);
        },
        onCameraChange(deviceId) {
            this.deviceId = deviceId;
            this.camera = deviceId;
            console.log("On Camera Change Event", deviceId);
        }
    }
});
</script>

<style scoped>
</style>