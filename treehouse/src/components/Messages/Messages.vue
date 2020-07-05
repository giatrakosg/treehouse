<template>
    <v-container>

        <v-row>

            <v-list three-line dense style="overflow: auto;height: 450px;width: 100%;border-bottom: groove">
                <template v-for="(item,index) in messages">


                    <v-list-item
                            v-if="item.sender_public_id===user.public_id"
                            :key="index"
                            style="width: 340px;"
                            class="ma-1 mr-1 pa-0 ml-auto"


                    >

                        <v-list-item-action-text style="align-self: center">
                            <span>
                                 <v-icon size="17" @click="deleteMessage(item,index)">mdi-delete</v-icon>
                            </span>

                        </v-list-item-action-text>
                        <v-list-item-content class="pa-3"
                                             style="background-color: #33af58;font-size: 14px;border-radius: 12px;">


                                <span style="word-wrap:break-word;width: 100%;color: white ">
                                    {{item.text}}
                                </span>
                            <br/>
                            <span style="font-size:11px;text-align: end;color: white">

                                {{showDate(item.timestamp)}}
                            </span>

                        </v-list-item-content>


                    </v-list-item>
                    <v-list-item
                            class="pa-0 ma-1 ml-0"
                            v-else
                            :key="index"
                            style="width: 340px; "


                    >

                        <v-list-item-content class="pa-3"
                                             style="background-color: #e7eaed;font-size: 14px;border-radius: 12px;">


                                <span style="word-wrap:break-word;width: 100%; ">
                                    {{item.text}}
                                </span>
                            <br/>
                            <span style="font-size:11px;text-align: end">

                                {{showDate(item.timestamp)}}
                            </span>

                        </v-list-item-content>
                        <v-list-item-action-text style="align-self: center;">
                            <v-icon size="17" @click="deleteMessage(item,index)">mdi-delete</v-icon>

                        </v-list-item-action-text>

                    </v-list-item>
                </template>
            </v-list>


        </v-row>
        <v-row align="center">
            <v-col cols="10">
                <v-textarea hide-details dense no-resize outlined rows="3" v-model="message.text"></v-textarea>
            </v-col>
            <v-col cols="2">
                <v-icon v-on:click="pushMessage" color="#a1795a" size="50px">mdi-send</v-icon>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import moment from 'moment'

    export default {

        name: "Messages",
        data: () => ({
            message: {
                sender_public_id: '',
                receiver_public_id: '',
                text: '',
                timestamp: null,


            },
            username: "John"

        }),
        computed: {
            messages() {
                console.log(this.$store.state.thread_messages)
                return this.$store.state.thread_messages

            },
            user() {
                return this.$store.state.user
            },
            thread() {
                return this.$store.state.current_thread
            }
        },
        methods: {
            async pushMessage() {
                if (this.message.text !== '' && this.message.text !== null) {

                    this.message.sender_public_id = this.$store.state.user.public_id


                    if (this.$store.state.current_thread.user2_public_id === this.$store.state.user.public_id) {
                        this.message.receiver_public_id = this.$store.state.current_thread.user1_public_id
                    } else {
                        this.message.receiver_public_id = this.$store.state.current_thread.user2_public_id
                    }


                    this.message.timestamp = moment().format("DD/MM/YYYY HH:mm")
                    console.log(this.message)

                    let mess = this.message;
                    await this.$store.dispatch('newMessage', mess);

                    this.message.sender_public_id = ''
                    this.message.receiver_public_id = ''
                    this.message.text = ''
                    this.message.timestamp = null


                }
            },
            deleteMessage(item) {
                console.log(item)
                this.$store.dispatch('deleteMessage', item.id)


            },
            showDate: function (date) {
                console.log(date)
                if (date === this.message.timestamp) {
                    return date;
                } else {
                    return moment(date).format("DD/MM/YYYY HH:mm")
                }


            },
        },

    }
</script>

<style scoped>


</style>