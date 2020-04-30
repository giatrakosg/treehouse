<template>
    <l-map style="height: 800px;z-index: 0;border-radius: 8px;" :zoom="zoom" v-bind:center="center">
        <l-tile-layer
                :url="url"
        />
        <l-marker v-for="(item,index) in coordinates"
                  :lat-lng="item"
                  v-bind:key="index"
                  v-show="loaded"

        >
            <l-icon>
                <img src="../../assets/treehouse.png" class="highlight" style="width: 45px;" ref="img"/>
            </l-icon>

        </l-marker>

    </l-map>

</template>

<script>
    import L from 'leaflet'

    export default {
        name: "HostRoomsMap",
        props: ['coordinates'],
        data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 10,
                center: [37.984888, 23.730851],
                loaded: false


            };
        },
        watch: {
            coordinates() {
                let sum = [0, 0];

                for (let c of this.coordinates) {
                    sum[0] = sum[0] + c[0];
                    sum[1] = sum[1] + c[1]
                }
                this.center = L.latLng(sum[0] / this.coordinates.length, sum[1] / this.coordinates.length)

            }
        },
        mounted() {

            this.$root.$on('highlight', (key) => {


                this.$refs.img[key].style.width = "65px";
                console.log(key)

            });
            this.$root.$on('default', (key) => {
                this.$refs.img[key].style.width = "45px";
            })


        }
    }
</script>

<style scoped>
    .highlight:hover {
        width: 62px !important;
        cursor: pointer;
    }

</style>