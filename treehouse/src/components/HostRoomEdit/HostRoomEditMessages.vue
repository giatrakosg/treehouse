<template>

    <v-container class="pa-0 elevation-2" style="border-radius: 8px">
        <v-row dense align="top">
            <v-col cols="5">
                <HostRoomEditMessagesRenters/>
            </v-col>
            <v-col cols="7">
                <Messages/>
            </v-col>
        </v-row>
    </v-container>

</template>

<script>
    import HostRoomEditMessagesRenters from "./HostRoomEditMessagesRenters";
    import Messages from "../../views/Messages";

    export default {
        name: "HostRoomEditMessages",
        components: {Messages, HostRoomEditMessagesRenters},
    }
</script>

<style scoped>

</style>