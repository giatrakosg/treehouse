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
import AdminPage from "../views/AdminPage"
import EditProfilePage from "../views/EditProfilePage"
import SentEmailPage from "../views/SentEmailPage"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home ,
    meta : {
        requiresAuth : false
    }
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage ,
    meta : {
        requiresAuth : false
    }
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage ,
    meta : {
        requiresAuth : false
    }
  },
  {
    path: '/roomlistings',
    name: 'RoomListings',
    component: RoomListings,
    meta : {
        requiresAuth : false
    }
  },
  {
      path: '/room/:room_title',
      name: 'RoomInfo',
      component: RoomInfo,
      meta : {
          requiresAuth : false
      }
  },
  {
      path: '/hostrooms',
      name: 'HostRooms',
      component: HostRooms,
      meta : {
          requiresAuth : false
      }
  },
  {
      path: '/hostrooms/:room_title',
      name: 'HostRoomEdit',
      component: HostRoomEdit,
      meta : {
          requiresAuth : false
      }

  } ,
  {
      path : '/success' ,
      name : 'Success Page' ,
      component : SuccessPage ,
      meta : {
          requiresAuth : false
      }
  },
  {
      path : '/profile' ,
      name : 'Profile Page' ,
      component : ProfilePage ,
      meta : {
          requiresAuth : true
      }
  } ,
  {
      path : '/admin' ,
      name : 'Admin Page' ,
      component : AdminPage,
      meta : {
          requiresAuth : true
      }

  } ,
  {
      path : '/editprofile',
      name : 'Edit Profile Page',
      component : EditProfilePage,
      meta : {
          requiresAuth : true
      }
  },
  {
      path : '/sentemail',
      name : 'Sent Email Page',
      component : SentEmailPage,
      meta : {
          requiresAuth : false
      }
  },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login','/login/admin','/register','/success','/sentemail','/hostrooms',
'/roomlistings','/'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('token');

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
})

export default router
