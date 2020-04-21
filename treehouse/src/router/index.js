import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterPage from '../views/RegisterPage.vue'
import Home from '../views/Home.vue'
import RoomListings from "../views/RoomListings";
import RoomInfo from "../views/RoomInfo";
import HostRooms from "../views/HostRooms";
import HostRoomEdit from "../views/HostRoomEdit";

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
      path: '/room/:room_id',
      name: 'RoomInfo',
      component: RoomInfo
  },
  {
    path: '/hostrooms',
    name: 'HostRooms',
    component: HostRooms
  },
  {
    path: '/hostroomedit',
    name: 'HostRoomEdit',
    component: HostRoomEdit
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
