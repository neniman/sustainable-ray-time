import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/01_Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/face-recognition',
    name: 'face-recognition',
    component: () => import('../views/02_Face_Recognition.vue')
  },
  {
    path: '/pin',
    name: 'pin',
    component: () => import('../views/03_Pin.vue')
  },
  {
    path: '/success',
    name: 'success',
    component: () => import('../views/04_Login_Success.vue')
  },
  {
    path: '/main',
    name: 'main',
    component: () => import('../views/05_Choose_Category.vue')
  },
  {
    path: '/tool-detail',
    name: 'tool-detail',
    component: () => import('../views/06_Choose_Product.vue')
  },
  {
    path: '/take-product',
    name: 'take-product',
    component: () => import('../views/07_Take_Product.vue')
  },
  {
    path: '/return',
    name: 'return',
    component: () => import('../views/08_Logout_Timer.vue')
  },
  {
    path: '/back',
    name: 'back',
    component: () => import('../views/09_Back.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
