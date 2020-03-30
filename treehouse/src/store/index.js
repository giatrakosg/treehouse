import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      status: '',
      token: localStorage.getItem('token') || '',
  },
  mutations: {
      auth_request(state) {
        state.status = 'loading'
      },
      auth_success(state, payload) {
        state.status = 'success'
        state.token = payload.token
      },
      auth_registererror(state) {
        state.status = 'error'
      },
      logout(state) {
        state.status = ''
        state.token = ''
        state.user = {}
      },

  },
  actions: {
      login({ commit , dispatch}, user) {
        const tok = user.email + ':' + user.password;
        const hash = btoa(tok);
        const Basic = 'Basic ' + hash;
        return new Promise((resolve, reject) => {
          commit('auth_request')
          axios({ url: 'http://localhost:5000/login', headers : {'Authorization' : Basic}, method: 'GET' })
            .then(resp => {
              const token = resp.data.token
              const user = resp.data.user
              //console.log(user)
              localStorage.setItem('token', token)
              // Add the following line:
              axios.defaults.headers.common['x-access-token'] = token
              commit('auth_success', { token , user})
              resolve(resp)
              dispatch('getUser');
            })
            .catch(err => {
              //commit('auth_error')
              localStorage.removeItem('token')
              reject(err)
            })
        })
      },
      register({ state },user) {
          state.hello = 'hello' ;
          console.log(user) ;

          return new Promise((resolve, reject) => {
            axios({ url: 'http://localhost:5000/user', data: user.data, method: 'POST' })
              .then(resp => {
                console.log(resp.data)
                resolve(resp)
              })
              .catch(err => {
                reject(err)
              })
          });
      }
  },
  modules: {
  }
})
