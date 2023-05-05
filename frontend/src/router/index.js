import { createRouter, createWebHistory } from 'vue-router'
import FirstView from '../components/FirstView.vue'
import SecondView from '../components/SecondView.vue'
import ThirdView from '../components/ThirdView.vue'

const routes = [
    {
      path: '/view1',
      name: 'FirstView',
      component: FirstView
    },
    {
      path: '/view2',
      name: 'SecondView',
      component: SecondView
    },
    {
      path: '/view3',
      name: 'ThirdView',
      component: ThirdView
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

