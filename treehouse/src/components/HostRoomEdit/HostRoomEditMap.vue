<template>
    <v-container>
        <v-row dense>
            <v-col>

                <l-map style="height: 470px;z-index: 0;border-radius: 8px;" :zoom="zoom" :center="center">
                    <l-tile-layer
                            :url="url"
                    />


                    <l-marker
                            :lat-lng="center"

                    >
                        <l-icon>
                            <img src="../../assets/treehouse.png" style="width: 45px">
                        </l-icon>

                    </l-marker>

                </l-map>
            </v-col>

        </v-row>


    </v-container>
</template>

<script>
    export default {
        name: "HostRoomEditMap",
        props: ['center'],
        data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 13,

            };
        },
        watch: {}
    }
</script>

<style scoped>

</style>