<template>

    <v-container class="pa-0 elevation-2" style="border-radius: 8px">
        <v-row dense>
            <v-col cols="5">
                <MessageThreads/>
            </v-col>
            <v-col cols="7">
                <Messages/>
            </v-col>
        </v-row>
    </v-container>

</template>

<script>
    import MessageThreads from "../Messages/MessageThreads";
    import Messages from "../Messages/Messages";


    export default {
        name: "HostRoomEditMessages",
        components: {Messages, MessageThreads},
        data: () => ({

            messages: [],
            loaded: false,
            user: '',
            thread_id: null


        }),
        created() {
            console.log(this.$store.state.room)
            if (this.$store.state.room.Id !== null) {
                this.$store.dispatch('getMessageThreadsRoom')
            }
        },

    }
</script>

<style scoped>

</style>