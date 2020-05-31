<template>

    <v-container class="pa-0 elevation-2" style="border-radius: 8px">
        <v-row dense>
            <v-col cols="5">
                <HostRoomEditMessagesRenters v-on:get-messages="getMessages($event)" :threads="message_threads"/>
            </v-col>
            <v-col cols="7">
                <Messages :user="user" :thread_id="thread_id"
                />
            </v-col>
        </v-row>
    </v-container>

</template>

<script>
    import HostRoomEditMessagesRenters from "./HostRoomEditMessagesRenters";
    import Messages from "../../views/Messages";


    export default {
        name: "HostRoomEditMessages",
        props: ['message_threads'],
        components: {Messages, HostRoomEditMessagesRenters},
        data: () => ({

            messages: [],
            loaded: false,
            user: '',
            thread_id: null


        }),
        methods: {
            getMessages(thread_id) {

                this.thread_id = thread_id;
                alert("okokkok")


            },

        }
    }
</script>

<style scoped>

</style>