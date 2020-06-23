<template>
    <l-map style="height: 800px;z-index: 0;border-radius: 8px;" :zoom="zoom" v-bind:center="center">
        <l-tile-layer
                :url="url"
        />
        <l-marker v-for="(item,index) in rooms"
                  :lat-lng="item.location"
                  v-bind:key="index"
                  v-on:click="$root.$emit('scroll-to-room',index)"

        >
            <l-icon>
                <img :src="item.thumbnail" class="highlight" style="width: 85px;height:85px;border-radius: 30px"
                     ref="img"/>
            </l-icon>

        </l-marker>

    </l-map>

</template>

<script>
    import L from 'leaflet'

    export default {
        name: "HostRoomsMap",
        data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 7,
                center: [37.984888, 23.730851],


            };
        },
        computed: {
            rooms() {
                return this.$store.state.rooms
            }
        },
        watch: {
            rooms() {
                let sum = [0, 0];

                for (let c of this.rooms) {
                    sum[0] = sum[0] + c.location[0];
                    sum[1] = sum[1] + c.location[1];
                }
                this.center = L.latLng(sum[0] / this.rooms.length, sum[1] / this.rooms.length)

            }
        },
        mounted() {


            this.$root.$on('highlight', (key) => {


                this.$refs.img[key].style.width = "95px";
                this.$refs.img[key].style.height = "95px";
                console.log(key)

            });
            this.$root.$on('default', (key) => {
                this.$refs.img[key].style.width = "85px";
                this.$refs.img[key].style.height = "85px";
            })


        }
    }
</script>

<style scoped>
    .highlight:hover {
        width: 90px !important;
        height: 90px !important;
        cursor: pointer;
    }

</style>