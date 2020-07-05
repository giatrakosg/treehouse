<template lang="html">
    <v-app-bar

            app
            color="primary"
            dark
            hide-on-scroll
    >
        <div class="d-flex align-center">


            <router-link v-if="isHost" to="/hostrooms">
                <v-img
                        alt="Vuetify Logo"
                        class="shrink mr-2"
                        contain

                        src="../../assets/treehouse.png"
                        transition="scale-transition"
                        width="40"
                >
                </v-img>
            </router-link>
            <router-link v-else to="/">
                <v-img
                        alt="Vuetify Logo"
                        class="shrink mr-2"
                        contain

                        src="../../assets/treehouse.png"
                        transition="scale-transition"
                        width="40"
                >
                </v-img>
            </router-link>


        </div>
        <v-spacer></v-spacer>
        <div class="d-flex align-right mx-4" v-if="!isLoggedIn">
            <v-dialog
                    v-model="dialog"
                    width="500"
            >
                <v-btn
                        color="primary"
                        dark
                        slot="activator"
                        @click="dialog = true"
                        elevation="0"
                >
                    Login
                     <v-icon right>mdi-login</v-icon>
                </v-btn>
                <LoginForm v-on:close-dialog="closeDialog"/>
            </v-dialog>
        </div>
        <div class="d-flex align-right mx-4" v-if="!isLoggedIn">
            <v-btn
                    color="primary"
                    to="/register"
                    elevation="0"
            >

                Register
                <v-icon right>mdi-account-plus</v-icon>
            </v-btn>
        </div>
        <div class="d-flex align-right mx-4" v-if="isLoggedIn & !isAdmin">
            <v-btn
                    color="primary"
                    to="/user/me"
                    elevation="0"
            >
                Profile
                <v-icon right>mdi-account</v-icon>
            </v-btn>
        </div>
        <div class="d-flex align-right mx-4" v-if="isAdmin">
            <v-btn
                    color="primary"
                    to="/admin"
                    elevation="0"
            >
                Admin Dashboard
            </v-btn>
        </div>
        <div class="d-flex align-right mx-4" v-if="isLoggedIn">
            <v-btn
                    color="primary"
                    @click="doLogout"
                    elevation="0"
            >
                Logout
                <v-icon right>mdi-logout</v-icon>
            </v-btn>
        </div>


    </v-app-bar>

</template>

<script>
    import LoginForm from '../Login/LoginForm'
    import router from "../../router";

    export default {
        name: 'AppBar',
        components: {
            LoginForm
        },
        data() {
            return {
                dialog: false,
            }
        },
        methods: {
            closeDialog: function () {
                this.dialog = false
            },
            doLogout: function () {

                this.$store.dispatch('logout')
                router.push({name: 'Home'})

            }
        },
        computed: {
            isLoggedIn() {
                return this.$store.state.isLoggedIn;
            },
            isAdmin() {
                return this.$store.state.user.isAdmin;
            },
            isHost() {
                return this.$store.state.user.isHost;
            }

        }
    }
</script>

<style lang="css" scoped>
</style>
