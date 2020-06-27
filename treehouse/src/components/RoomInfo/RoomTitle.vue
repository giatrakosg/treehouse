<template>
    <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title>
                <h2>{{room.title}}</h2>
            </v-list-item-title>
            <v-list-item-subtitle>
                <v-row dense align="center">
                    <v-col cols="auto">
                        <v-rating style="display:inline-flex;"
                                  half-increments
                                  v-model="room.rating"
                                  readonly
                                  dense
                                  size="20px"
                        ></v-rating>

                        <label style="margin-left: 20px;">({{room.reviews_num}})</label>
                    </v-col>
                    <v-col cols="auto">
                        <label style="padding-left: 20px">Host: </label>
                        <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">

                        <v-btn color="brown" text @click="sendMessage" v-ripple="false" class="text-capitalize"
                               v-on="on">
                            John
                            <i class="fas fa-external-link-square-alt "></i>
                        </v-btn>
                        </template>
                             Contact
                        </v-tooltip>

                    </v-col>
                </v-row>


            </v-list-item-subtitle>


        </v-list-item-content>
        <v-dialog max-width="60%" v-model="contact">
            <v-card class="pa-2">

                <Messages user="John" :room_title="room.title"/>
            </v-card>
        </v-dialog>

    </v-list-item>
</template>

<script>
    import Messages from "../Messages/Messages";
    export default {
        name: "RoomTitle",
        components: {Messages},
        data: function () {
            return {
                contact: false
            }
        },
        methods: {
            sendMessage() {

                this.contact = this.$store.state.isLoggedIn;

            }
        },
        computed: {
            room() {
                return this.$store.state.room
            }
        }
    }
</script>

<style scoped>

</style>