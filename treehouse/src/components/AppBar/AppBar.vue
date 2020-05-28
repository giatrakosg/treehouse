<template lang="html">
    <v-app-bar
            app
            color="primary"
            dark
            hide-on-scroll
    >
        <div class="d-flex align-center">
            <v-btn to="/" text color="transparent">
                <v-img
                        alt="Vuetify Logo"
                        class="shrink mr-2"
                        contain
                        src="../../assets/treehouse.png"
                        transition="scale-transition"
                        width="40"
                />
            </v-btn>
        </div>
        <v-btn
                color="primary"
                to="/roomlistings"
        >
            TMP Button for LIstings
        </v-btn>
         <v-btn
                color="primary"
                to="/hostrooms"
        >
            TMP Button for HostRooms
        </v-btn>
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
                  >
                    Login
                  </v-btn>
                <LoginForm v-on:close-dialog="closeDialog" />
              </v-dialog>
            </div>
            <div class="d-flex align-right mx-4" v-if="!isLoggedIn">
                <v-btn
                        color="primary"
                        to="/register"
                >
                    Register
                </v-btn>
                <!-- <LoginForm /> -->
            </div>
    </v-app-bar>

</template>

<script>
import LoginForm from '../Login/LoginForm'
export default {
    name: 'AppBar',
    components:{
        LoginForm
    },
    data() {
        return {
            dialog: false ,
        }
    } ,
    methods : {
        closeDialog : function() {
            this.dialog = false
        }
    },
    computed : {
        isLoggedIn() {
            return this.$store.state.isLoggedIn
        }
    }
}
</script>

<style lang="css" scoped>
</style>
