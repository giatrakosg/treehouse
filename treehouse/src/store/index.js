import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
      register({ state },user) {
        state.hello = 'hello'
        console.log(user)

        return new Promise((resolve, reject) => {
          axios({ url: 'http://localhost:5000/user', data: user.data, method: 'POST' })
            .then(resp => {
              console.log(resp.data)
              resolve(resp)
            })
            .catch(err => {
              reject(err)
            })
        })

      },
  },
  modules: {
  }
})
