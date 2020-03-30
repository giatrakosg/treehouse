import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterPage from '../views/RegisterPage.vue'
import Home from '../views/Home.vue'
import RoomListings from "../views/RoomListings";
import RoomInfo from "../views/RoomInfo";
import LoginPage from "../views/LoginPage"

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
  {
  path: '/room',
  name: 'RoomInfo',
  component: RoomInfo
  },
  {
  path: '/login',
  name: 'Login',
  component: LoginPage
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
