import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterPage from '../views/RegisterPage.vue'
import Home from '../views/Home.vue'
import RoomListings from "../views/RoomListings";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage
  },
  {
  path: '/roomlistings',
  name: 'RoomListings',
  component: RoomListings
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
