import Vue from 'vue'
import Vuex from 'vuex'
import { ApplicationState, Language } from '@/util/enums'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appState: ApplicationState.LOGGED_OUT as ApplicationState,
    language: Language.DE as Language,
    pinButtons: ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '0', 'OK'],
    pin: 1337,
    // pins: {
    //   id: pin
    // }
    texts: {
      de: {
        login: 'Bitte ID oder Werkzeug scannen',
        success: 'Identifikation Erfolgreich',
        categoryPage: 'Kategorie wählen!',
        category: {
          safety: 'Schutzausrüstung',
          big: 'Großgeräte',
          toolBig: 'Handwerkszeug',
          small: 'Kleinteile',
          toolSmall: 'Kleingeräte',
          kits: 'Tool-Kits'
        }  
      },
      en: {
        login: 'Please scan ID or tool',
        success: 'Identification successfull'
      },
      ser: {

      }, 
      rum: {

      },
      bos: {

      }
    }
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
