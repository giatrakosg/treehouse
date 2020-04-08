<template>
    <v-container>
        <v-row>
            <v-col>

            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider></v-divider>
        <v-row dense>
            <v-col md="auto" sm="12">
                <RoomImages/>
            </v-col>
            <v-col>
                <RoomEditDescription/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" lg="6">
                test
            </v-col>
            <v-col cols="12" lg="6">
                test
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import RoomEditDescription from "../components/HostRoomEdit/HostRoomEditDescription";
    import RoomImages from "../components/RoomInfo/RoomImages";

    export default {
        name: "HostRoomEdit",
        components: {RoomImages, RoomEditDescription}
    }
</script>

<style scoped>

</style>