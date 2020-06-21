import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import https from 'https'

Vue.use(Vuex)

//https.globalAgent.options.rejectUnauthorized = false;

const agent = new https.Agent({
  rejectUnauthorized: false
}) ;
const instance = axios.create({
  httpsAgent: agent ,
  baseURL : 'https://localhost:5000'
});

//const url = 'https://localhost:5000/'
export default new Vuex.Store({
  state: {
      status: '',
      token: localStorage.getItem('token') || '',
      user: {} ,
      users : [],
      isLoggedIn : false,
      room : ''
  },
  mutations: {
      addUser(state,payload) {
        state.user = payload.user ;
      },
      auth_request(state) {
        state.status = 'loading'
      },
      auth_success(state, payload) {
        state.status = 'success'
        state.token = payload.token
        state.isLoggedIn = true
      },
      auth_registererror(state) {
        state.status = 'error'
      },
      logout(state) {
        state.status = '';
        state.token = '';
        state.user = {};
        state.isLoggedIn = false ;
        localStorage.clear()
      },
      addUsers(state,payload) {
          state.users = payload.users
      },
      removeUser(state,payload) {
          state.users.splice(payload.index,1)
      } ,
      addRoom(state,payload) {
          state.room = payload.room;
      }

  },
  actions: {
    login({ commit }, user) {
        const tok = user.uname + ':' + user.password;
        const hash = btoa(tok);
        const Basic = 'Basic ' + hash;
        return new Promise((resolve, reject) => {
          commit('auth_request')
          instance({ url: '/login',
           headers : {'Authorization' : Basic}, method: 'GET' })
            .then(resp => {
              const token = resp.data.token
              const user = resp.data.user
              console.log(user)
              //console.log(user)
              localStorage.setItem('token', token)
              // Add the following line:
              axios.defaults.headers.common['x-access-token'] = token
              commit('auth_success', { token })
              commit('addUser',{user})
              resolve(resp)
            })
            .catch(err => {
              commit('auth_error')
              localStorage.removeItem('token')
              reject(err)
            })
        })
    },
    logout({commit}){
        commit('logout');
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        instance({ url: 'user', data: user, method: 'POST' })
          .then(resp => {
            console.log(resp.data)
            resolve(resp)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    getUserList({commit}) {
        var token = localStorage.getItem('token');
        return new Promise((resolve, reject) => {
          instance({ url: '/user/pending', headers : {
              common : {
                  'x-access-token' : token
              }
          } , method: 'GET' })
            .then(resp => {
              //console.log(resp.data)
              const users = resp.data.users
              commit('addUsers',{users})
              //commit('decrease_routes')
              resolve(resp)
            })
            .catch(err => {
                reject(err)
            })
      }) ;
    },
    acceptUser({commit,state},index) {
        var token = localStorage.getItem('token');
        var pid = state.users[index].public_id
        return new Promise((resolve, reject) => {
          instance({ url: '/user/pending/' + pid, headers : {
              common : {
                  'x-access-token' : token
              }
          } , method: 'PUT' })
            .then(resp => {
              //console.log(resp.data)
              commit('removeUser',{index})
              //commit('decrease_routes')
              resolve(resp)
            })
            .catch(err => {
                reject(err)
            })
      }) ;
    },
    rejectUser({commit,state},index) {
        var token = localStorage.getItem('token');
        var pid = state.users[index].public_id
        return new Promise((resolve, reject) => {
          instance({ url: 'user/pending/' + pid, headers : {
              common : {
                  'x-access-token' : token
              }
          } , method: 'DELETE' })
            .then(resp => {
              //console.log(resp.data)
              commit('removeUser',{index})
              //commit('decrease_routes')
              resolve(resp)
            })
            .catch(err => {
                reject(err)
            })
      }) ;
    } ,
    updateUser({state},user) {
        var token = localStorage.getItem('token');
        var pid = state.user.public_id ;
        return new Promise((resolve, reject) => {
          instance({ url: 'user/' + pid, headers : {
              common : {
                  'x-access-token' : token
              }
          } , data : user , method: 'PATCH' })
            .then(resp => {
              //console.log(resp.data)
              resolve(resp)
            })
            .catch(err => {
                reject(err)
            })
      }) ;
    },
    getRoom({commit},roomid) {
        var token = localStorage.getItem('token');
        var pid = state.user.public_id ;
        return new Promise((resolve, reject) => {
          instance({ url: 'user/' + roomid, headers : {
          } , method: 'GET' })
            .then(resp => {
                var room = resp.data.room ;
                commit('addRoom',room)
              resolve(resp)
            })
            .catch(err => {
                reject(err)
            })
      }) ;

    }

  },
  modules: {
  }
})
