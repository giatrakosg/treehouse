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
        <div class="d-flex align-right">
            <v-btn
                    color="primary"
            >
                Login
            </v-btn>
        </div>
        <div class="d-flex align-right mx-4">
            <v-btn
                    color="primary"
                    to="/register"
            >
                Register
            </v-btn>
        </div>

    </v-app-bar>

</template>

<script>
    export default {
        name: 'AppBar',
        data() {
            return {
                dialog: false
            }
        }
    }
</script>

<style lang="css" scoped>
</style>
