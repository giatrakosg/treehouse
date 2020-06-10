<template>
    <v-container>

        <v-row justify="center">
            <h1 style="text-align: center">My Rooms</h1>
        </v-row>

        <v-divider/>
        <v-row>
            <v-col cols="12" lg="6">
                <HostRoomsList v-bind:rooms="rooms"/>
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
        created() {

            let url = 'https://' + this.$hostname + ':5000/rooms/host';

            this.$http.get(url, {
                params: {
                    'host_id': 0
                }

            }).then((result) => {
                this.rooms = result.data;
                console.log(this.rooms);

                for (let r of result.data) {

                    this.rooms_loc.push({location: r.location, image: r.thumbnail})
                }
                console.log(this.rooms_loc)


            }).catch(error => console.log(error));


        }


    }
</script>

<style scoped>

</style>