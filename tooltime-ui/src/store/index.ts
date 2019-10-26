import Vue from 'vue'
import Vuex from 'vuex'
import { ApplicationState } from '@/util/enums'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appState: ApplicationState.LOGGED_OUT as ApplicationState
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
