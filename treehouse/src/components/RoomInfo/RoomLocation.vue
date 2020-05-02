<template>
    <v-container>

        <l-map v-if="loaded" style="height: 600px;z-index: 0;border-radius: 8px;" :zoom="zoom" :center="location">
            <l-tile-layer
                    :url="url"
            />
            <l-marker
                    :lat-lng="location"
            >
                <l-icon>
                    <img src="../../assets/treehouse.png" style="width: 45px">
                </l-icon>

            </l-marker>
        </l-map>
        <v-row>
            <v-col cols="auto">
                <label style="font-size: 15px;font-weight: 300">
                    Address: {{address}}
                </label>
            </v-col>
            <v-col cols="auto">
                <label style="font-size: 15px;font-weight: 300">
                    Transport info: {{transport_info}}
                </label>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "RoomLocation",
        props: {

            address: String,
            transport_info: String,
            location: Array
        },
        data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 13,
                loaded: false

            };
        },
        watch: {
            location() {

                this.loaded = true;
            }
        }
    }

</script>

<style scoped>

</style>