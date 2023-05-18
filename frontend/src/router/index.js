import { createRouter, createWebHistory } from 'vue-router'
import OverView from '../components/OverView.vue'
import HomePage from '../components/HomePage.vue'
import RegionView from '../components/RegionView.vue'
import TweetView from '../components/TweetView.vue'

const routes = [
    {
        path: '/Home',
        name: 'HomePage',
        component: HomePage
    },
    {
        path: '/view0',
        name: 'OverView',
        component: OverView
    },
    {
        path: '/RegionView',
        name: 'RegionView',
        component: RegionView
    },
    {
        path: '/TweetView',
        name: 'TweetView',
        component: TweetView
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

