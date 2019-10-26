import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

enum ApplicationState {
  LOGGED_IN_NORMAL = 'normal',
  LOGEED_IN_SUPER = 'super', 
  LOGGED_OUT = 'logout',
  RETURN_TOOL = 'return'
}

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
