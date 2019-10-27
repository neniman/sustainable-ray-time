import Vue from 'vue'
import Vuex from 'vuex'
import { ApplicationState, Language } from '@/util/enums'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appState: ApplicationState.LOGGED_OUT as ApplicationState,
    language: Language.DE as Language,
    pinButtons: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '<', '0', 'OK'],
    pin: 1337,
    // pins: {
    //   id: pin
    // }
    texts: {
      de: {
        take: 'Produkt entnehmen!',
        reserve: 'Reservieren',
        rent: 'Ausleihen',
        login: 'ID oder Werkzeug scannen',
        success: 'Identifikation Erfolgreich',
        categoryPage: 'Kategorie wählen!',
        categoryProduct: 'Produkt wählen',
        pinField: 'PIN Eingeben',
        category: {
          safety: 'Schutzausrüstung',
          big: 'Großgeräte',
          toolBig: 'Handwerkszeug',
          small: 'Kleinteile',
          toolSmall: 'Kleingeräte',
          kits: 'Tool-Kits'
        },
        tools: {
          tool1: {
            voice: 'voice',
            imgMain: 'imgMain',
            mainText: 'TE-2000-AVR',
            smallText: 'Abbruchhammer',
            usage: 'usage',
            possibilities: 'possibilities',
            plus: 'plus',
            minus: 'minus'
          },
          tool2: {
            voice: 'voice',
            imgMain: 'imgMain',
            mainText: 'SD-5000',
            smallText: 'Magazin-Schrauben-Pistole',
            usage: 'usage',
            possibilities: 'possibilities',
            plus: 'plus',
            minus: 'minus'
          },
          tool3: {
            voice: 'voice',
            imgMain: 'imgMain',
            mainText: 'AG-230-20D',
            smallText: 'Winkelschleifer',
            usage: 'usage',
            possibilities: 'possibilities',
            plus: 'plus',
            minus: 'minus'
          }
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
