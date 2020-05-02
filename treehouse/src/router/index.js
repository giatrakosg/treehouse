import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterPage from '../views/RegisterPage.vue'
import Home from '../views/Home.vue'
import RoomListings from "../views/RoomListings";
import RoomInfo from "../views/RoomInfo";
import HostRooms from "../views/HostRooms";
import HostRoomEdit from "../views/HostRoomEdit";
import LoginPage from "../views/LoginPage"
import SuccessPage from "../views/SuccessPage"
import ProfilePage from "../views/ProfilePage"

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
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
  path: '/roomlistings',
  name: 'RoomListings',
  component: RoomListings
  },
  {
      path: '/room/:room_title',
      name: 'RoomInfo',
      component: RoomInfo
  },
  {
    path: '/hostrooms',
    name: 'HostRooms',
    component: HostRooms
  },
  {
      path: '/hostrooms/:room_title',
      name: 'HostRoomEdit',
      component: HostRoomEdit
  } ,
  {
      path : '/success' ,
      name : 'SuccessPage' ,
      component : SuccessPage
  },
  {
      path : '/profile' ,
      name : 'ProfilePage' ,
      component : ProfilePage
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
