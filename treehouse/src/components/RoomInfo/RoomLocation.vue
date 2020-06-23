<template>
    <v-container>

        <l-map style="height: 600px;z-index: 0;border-radius: 8px;" :zoom="zoom" :center="room.location">
            <l-tile-layer
                    :url="url"
            />
            <l-marker
                    :lat-lng="room.location"
            >
                <l-icon>
                    <img src="../../assets/treehouse.png" style="width: 45px">
                </l-icon>

            </l-marker>
        </l-map>
        <v-row>
            <v-col cols="auto">
                <label style="font-size: 15px;font-weight: 300">
                    Address: {{room.address}}
                </label>
            </v-col>
            <v-col cols="auto">
                <label style="font-size: 15px;font-weight: 300">
                    Transport info: {{room.transport_info}}
                </label>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "RoomLocation",


        data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 13,


            };
        },
        computed: {
            room() {
                return this.$store.state.room
            }
        },
        watch: {}
    }

</script>

<style scoped>

</style>