<template>
    <v-container>

        <v-row justify="center">
            <h1 style="text-align: center">My Rooms</h1>
        </v-row>

        <v-divider/>
        <v-row>
            <v-col cols="12" lg="6">
                <HostRoomsList/>
            </v-col>
            <v-col cols="12" lg="6">
                <HostRoomsMap v-bind:rooms="rooms_loc"/>
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import HostRoomsList from "../components/HostRooms/HostRoomsList";
    import HostRoomsMap from "../components/HostRooms/HostRoomsMap";


    export default {
        name: "HostRooms",
        components: {HostRoomsMap, HostRoomsList},
        data: () => ({

            rooms: [],
            rooms_loc: [],
            key: 0,


        }),
        async created() {
            let host_id = this.$store.state.user.public_id
            //host -id = user.id

            await this.$store.dispatch('getHostRooms', host_id);


        }


    }
</script>

<style scoped>

</style>