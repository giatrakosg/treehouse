import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import https from 'https'

Vue.use(Vuex)

//https.globalAgent.options.rejectUnauthorized = false;

const agent = new https.Agent({
    rejectUnauthorized: false
});
const instance = axios.create({
    httpsAgent: agent,
    baseURL: 'https://localhost:5000'
});

Vue.filter('formatFloat', function (value) {

    return value.toFixed(2)
});


//const url = 'https://localhost:5000/'
export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user: {},
        users: [],
        isLoggedIn: false,
        room: null,
        rooms: [],
        reviews: [],

        message_threads: [],
        thread_messages: [],
        current_thread: '',

        room_reservations: []
    },
    mutations: {
        addUser(state, payload) {
            state.user = payload.user;
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
            state.isLoggedIn = false;
            localStorage.clear()
            state.message_threads = []
            state.thread_messages = []
            state.current_thread = []

        },
        addUsers(state, payload) {
            state.users = payload.users
        },
        removeUser(state, payload) {
            state.users.splice(payload.index, 1)
        },
        addRoom(state, payload) {
            state.room = payload;
        },
        addRooms(state, payload) {

            state.rooms = payload;
        },
        addReviews(state, payload) {
            state.reviews = payload
        },
        addReview(state, payload) {
            state.reviews.push(payload)

        },
        addThreads(state, payload) {
            state.message_threads = payload
        },
        addThread(state, payload) {
            state.current_thread = payload
        },
        addMessages(state, payload) {
            state.thread_messages = payload
        },
        addMessage(state, payload) {
            console.log(payload)

            state.thread_messages.push(JSON.parse(JSON.stringify(payload)))

        },
        removeMessage(state, payload) {
            console.log(payload)
            console.log("REMOVED MESSAGE")

            state.thread_messages = state.thread_messages.filter(function (m) {
                return m.id !== payload;
            });
        },
        addReservations(state, payload) {
            state.room_reservations = payload
        },
        addReservation(state, payload) {
            state.room_reservations.push(payload)
        },


    },
    actions: {
        login({commit}, user) {
            const tok = user.uname + ':' + user.password;
            const hash = btoa(tok);
            const Basic = 'Basic ' + hash;
            return new Promise((resolve, reject) => {
                commit('auth_request')
                instance({
                    url: '/login',
                    headers: {'Authorization': Basic}, method: 'GET'
                })
                    .then(resp => {
                        const token = resp.data.token
                        const user = resp.data.user
                        console.log(user)
                        //console.log(user)
                        localStorage.setItem('token', token)
                        // Add the following line:
                        axios.defaults.headers.common['x-access-token'] = token
                        commit('auth_success', {token})
                        commit('addUser', {user})
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('auth_error')
                        localStorage.removeItem('token')
                        reject(err)
                    })
            })
        },
        logout({commit}) {
            commit('logout');
        },
        register({commit}, user) {
            return new Promise((resolve, reject) => {
                commit('auth_request')
                instance({url: 'user', data: user, method: 'POST'})
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
                instance({
                    url: '/user/pending', headers: {
                        common: {
                            'x-access-token': token
                        }
                    }, method: 'GET'
                })
                    .then(resp => {
                        //console.log(resp.data)
                        const users = resp.data.users
                        commit('addUsers', {users})
                        //commit('decrease_routes')
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });
        },
        acceptUser({commit, state}, index) {
            var token = localStorage.getItem('token');
            var pid = state.users[index].public_id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/user/pending/' + pid, headers: {
                        common: {
                            'x-access-token': token
                        }
                    }, method: 'PUT'
                })
                    .then(resp => {
                        //console.log(resp.data)
                        commit('removeUser', {index})
                        //commit('decrease_routes')
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });
        },
        rejectUser({commit, state}, index) {
            var token = localStorage.getItem('token');
            var pid = state.users[index].public_id
            return new Promise((resolve, reject) => {
                instance({
                    url: 'user/pending/' + pid, headers: {
                        common: {
                            'x-access-token': token
                        }
                    }, method: 'DELETE'
                })
                    .then(resp => {
                        //console.log(resp.data)
                        commit('removeUser', {index})
                        //commit('decrease_routes')
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });
        },
        updateUser({state}, user) {
            var token = localStorage.getItem('token');
            var pid = state.user.public_id;
            return new Promise((resolve, reject) => {
                instance({
                    url: 'user/' + pid, headers: {
                        common: {
                            'x-access-token': token
                        }
                    }, data: user, method: 'PATCH'
                })
                    .then(resp => {
                        //console.log(resp.data)
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });
        },
        getRoom({commit}, room_id) {
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id, headers: {}, method: 'GET'
                })
                    .then(resp => {

                        commit('addRoom', resp.data)
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });

        },
        delRoom({commit}, room_id) {
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id, headers: {}, method: 'DELETE'
                })
                    .then(resp => {
                        commit('addRoom', null)
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });

        },
        updateRoom({state}) {

            return new Promise((resolve, reject) => {

                let room_id = state.room.Id
                let room = state.room

                instance({
                    url: '/rooms/' + room_id, headers: {}, method: 'PATCH', data: {
                        room
                    }
                })
                    .then(resp => {

                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });

        },

        updateRoomImages({state}) {
            return new Promise((resolve, reject) => {

                let room_id = state.room.Id
                let images = state.room.images

                instance({
                    url: '/rooms/' + room_id + '/update_images', headers: {}, method: 'POST', data: {
                        images
                    }
                })
                    .then(resp => {
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });

        },
        newRoom({state}) {
            return new Promise((resolve, reject) => {
                let room_id = null
                let room = state.room
                instance({
                    url: '/rooms/' + room_id, headers: {}, method: 'POST', data: {
                        room
                    }
                })
                    .then(resp => {
                        console.log(resp.data)
                        state.room.Id = resp.data.room_id
                        resolve(resp)
                    })
                    .catch(err => {
                        reject(err)
                    })
            });

        },
        getRooms({commit}, params) {
            return new Promise((resolve, reject) => {

                instance({
                    url: '/rooms',
                    params: {
                        'date_from': params.dates[0],
                        'date_to': params.dates[1],
                        'lat': params.loc[0],
                        'long': params.loc[1]

                    },
                    method: 'GET',
                }).then(resp => {
                    commit('addRooms', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getRoomReservations({commit, state}) {
            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/reservations',
                    method: 'GET',
                }).then(resp => {
                    commit('addReservations', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        newRoomReservation({state}, reservation) {
            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/reservations',
                    method: 'PUT', data: {
                        reservation
                    }
                }).then(resp => {
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        updateRoomAvailableDates({state, commit}, new_reservations) {

            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/reservations/unavailable_dates',
                    method: 'POST', data: {
                        new_reservations
                    }
                }).then(resp => {
                    commit('addReservations', new_reservations)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getRoomAvailableDates({state, commit}) {
            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/reservations/unavailable_dates',
                    method: 'GET'
                }).then(resp => {
                    commit('addReservations', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },

        getHostRooms({commit}, host_id) {
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/host/' + host_id,
                    method: 'GET',
                }).then(resp => {
                    commit('addRooms', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getReviews({commit, state}) {


            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/reviews',
                    method: 'GET',
                }).then(resp => {
                    commit('addReviews', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        saveReview({commit}, payload) {

            return new Promise((resolve, reject) => {
                let review = payload.new_review
                instance({
                    url: '/rooms/' + payload.room_id + '/new_review',
                    method: 'POST',
                    data: {
                        review
                    }
                }).then(resp => {
                    commit('addReview', review)

                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });
        },
        getMessageThreadsRoom({commit, state}) {
            let room_id = state.room.Id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/rooms/' + room_id + '/threads',
                    method: 'GET',
                }).then(resp => {
                    commit('addThreads', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getMessageThreadsUser({commit, state}) {
            let user_id = state.user.public_id
            return new Promise((resolve, reject) => {
                instance({
                    url: '/users/' + user_id + '/threads',
                    method: 'GET',
                }).then(resp => {
                    commit('addThreads', resp.data)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        newMessage({commit, state}, message) {
            console.log(message)
            console.log(state.current_thread)
            return new Promise((resolve, reject) => {
                instance({
                    url: '/threads/thread/new_message',
                    method: 'POST',
                    params: {
                        'sender_public_id': message.sender_public_id,
                        'receiver_public_id': message.receiver_public_id,
                        'room_id': state.room.Id
                    },
                    data: {
                        message
                    },

                }).then(resp => {
                    commit('addMessage', message)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        deleteMessage({commit, state}, message_id) {
            return new Promise((resolve, reject) => {
                instance({
                    url: '/threads/' + state.current_thread.Id + '/messages',
                    method: 'DELETE',
                    params: {
                        'message_id': message_id,
                    },

                }).then(resp => {
                    commit('removeMessage', message_id)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getThreadMessages({commit}, thread) {
            return new Promise((resolve, reject) => {
                instance({
                    url: '/threads/' + thread.Id + '/messages',
                    method: 'GET',
                }).then(resp => {
                    commit('addMessages', resp.data)
                    commit('addThread', thread)
                    resolve(resp)
                }).catch(err => {
                    reject(err)
                })
            });

        },
        getData(){
            var token = localStorage.getItem('token');
            return new Promise((resolve, reject) => {
                instance({
                    url: '/export/json', headers: {
                        common: {
                            'x-access-token': token
                        }
                    }, method: 'GET'
                })
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
    modules: {}
})
