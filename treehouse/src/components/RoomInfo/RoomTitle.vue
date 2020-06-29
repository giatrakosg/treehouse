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

                                <v-btn color="brown" text @click="openDialog" v-ripple="false" class="text-capitalize"
                                       v-on="on">
                                    {{room.owner_name}}
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

                <v-row align="center">
                    <v-col cols="10">
                        <v-textarea hide-details dense no-resize outlined rows="3" v-model="message.text"></v-textarea>
                    </v-col>
                    <v-col cols="2">
                        <v-icon v-on:click="pushMessage" color="#a1795a" size="50px">mdi-send</v-icon>
                    </v-col>
                </v-row>
            </v-card>
        </v-dialog>

    </v-list-item>
</template>

<script>


    import moment from "moment";

    export default {
        name: "RoomTitle",
        components: {},
        data: function () {
            return {
                contact: false,
                message: {
                    sender_public_id: '',
                    receiver_public_id: '',
                    text: '',
                    timestamp: null,


                },
            }
        },
        methods: {
            openDialog() {

                this.contact = this.$store.state.isLoggedIn;

            },
            async pushMessage() {
                if (this.message.text !== '' && this.message.text !== null) {

                    this.message.sender_public_id = this.$store.state.user.public_id
                    this.message.receiver_public_id = this.$store.state.room.public_owner_id


                    this.message.timestamp = moment().format("DD/MM/YYYY HH:mm")
                    console.log(this.message)

                    let mess = this.message;


                    await this.$store.dispatch('newMessage', mess);

                    this.message.sender_public_id = ''
                    this.message.receiver_public_id = ''
                    this.message.text = ''
                    this.message.timestamp = null

                }
            }
        },
        computed: {
            room() {
                return this.$store.state.room
            },
        }
    }
</script>

<style scoped>

</style>