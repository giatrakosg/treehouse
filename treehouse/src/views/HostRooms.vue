<template>
    <v-container>
        <v-row justify="center">
              <h1 style="text-align: center">My Rooms</h1>
        </v-row>

    <v-divider/>
        <v-row >
            <v-col  cols="12"  lg="6">
                <HostRoomsList v-bind:rooms="rooms"/>
            </v-col>
            <v-col  cols="12"  lg="6">
                <HostRoomsMap v-bind:coordinates="rooms"/>
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
        data:()=>({

            rooms:[
                    [37.942907, 23.740806],
                    [37.945411, 23.735581],
                    [37.947575, 23.736627],
                    [37.956644, 23.734336],
                    [37.968875, 23.732418],
                    [37.975760, 23.731731],
                    [38.024167, 23.691184]
                ],

        })
    }
</script>

<style scoped>

</style>