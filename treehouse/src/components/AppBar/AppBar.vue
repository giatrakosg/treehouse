<template lang="html">
    <v-app-bar
            app
            color="white"
            dark
            hide-on-scroll
    >
        <!--     Temporary       -->
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
        <!--                      -->

        <div class="d-flex align-center">
            <v-img
                    alt="Vuetify Logo"
                    class="shrink mr-2"
                    contain
                    src="../../assets/treehouse.png"
                    transition="scale-transition"
                    width="40"
            />
        </div>
        <v-spacer></v-spacer>
        <div class="d-flex align-right mx-4">
          <v-dialog
            v-model="dialog"
            width="500"
          >
            <template v-slot:activator="{ on }">
              <v-btn
                color="primary"
                dark
                v-on="on"
              >
                Login
              </v-btn>
            </template>
            <LoginForm />
          </v-dialog>
        </div>
        <div class="d-flex align-right mx-4">
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
    }
}
</script>

<style lang="css" scoped>
</style>
