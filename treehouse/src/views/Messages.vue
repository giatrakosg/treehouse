<template>
    <v-container>
        <v-row>
            <v-list-item style="border-bottom:groove">
                <v-list-item-avatar size="55">
                    <img
                            src="https://cdn.vuetifyjs.com/images/john.jpg"
                            alt="John"

                    >
                </v-list-item-avatar>
                <v-list-item-title>
                    <span>{{user}}</span>
                </v-list-item-title>
            </v-list-item>

        </v-row>
        <v-row>

            <v-list three-line dense style="overflow: auto;height: 450px;width: 100%;border-bottom: groove">
                <template v-for="(item,index) in messages">


                    <v-list-item
                            v-if="index % 2===0"
                            :key="index"
                            style="width: 340px;"
                            class="ma-1 mr-0 pa-0 ml-auto"


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
        props: ['user', 'thread_id', 'room_title'],
        data: () => ({
            message: {
                sender: '',
                text: '',
                timestamp: null
            },
            user_is_renter: true,

            messages: []


        }),
        watch: {
            thread_id: function () {
                let url = 'http://' + this.$hostname + ':5000/threads/' + this.thread_id;

                this.$http.get(url, {}).then((result) => {
                    console.log(result)
                    this.messages = result.data.messages;


                }).catch(error => console.log(error));

                this.user = this.message_threads.filter(thread => thread.id === this.thread_id)[0].username;


            },

        },

        methods: {
            pushMessage() {
                if (this.message.text !== '' && this.message.text !== null) {

                    this.message.sender = this.user;
                    this.message.timestamp = moment().format("DD/MM/YYYY  HH:mm")


                    let url = 'http://' + this.$hostname + ':5000/threads/' + this.thread_id + '/message';

                    if (this.user_is_renter) { //user is renter
                        this.$http.put(url, {

                            'message': JSON.stringify(this.message),
                            'room_title': JSON.stringify(this.room_title)

                        }).catch(error => console.log(error));
                    } else {
                        this.$http.post(url, {

                            'message': JSON.stringify(this.message)

                        }).catch(error => console.log(error));


                    }

                    this.messages.push({text: this.message.text, timestamp: moment()})
                    console.log(this.messages)

                }
            },
            deleteMessage(item, index) {

                let url = 'http://' + this.$hostname + ':5000/threads/' + this.thread_id + '/message';

                this.$http.delete(url, {
                    data: {

                        'message_id': JSON.stringify(item.id)
                    }

                }).catch(error => console.log(error));


                this.messages.splice(index, 1);


            },
            showDate: function (date) {

                return moment(date).format(("DD/MM/YYYY - HH:mm"));
            },
        },

    }
</script>

<style scoped>


</style>