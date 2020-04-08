<template>
     <l-map style="height: 800px;z-index: 0;border-radius: 8px;" :zoom="zoom" :center="center">
            <l-tile-layer
                    :url="url"
            />
            <l-marker v-for="(item,index) in coordinates"
                      :lat-lng="item"
                      v-bind:key="index"


            >
                <l-icon>
                    <img src="../../assets/treehouse.png" class="highlight" style="width: 45px;" ref="image"/>
                </l-icon>

            </l-marker>
        </l-map>
</template>

<script>
    export default {
        name: "HostRoomsMap",
        props:['coordinates'],
         data() {
            return {
                url: 'http://mt.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}',
                zoom: 13,
                center: [37.984888, 23.730851],


            };
        },
        mounted(){
            this.$root.$on('highlight', (key) => {
                this.$refs.image[key].style.width = "62px";
            });
            this.$root.$on('default', (key) => {
                this.$refs.image[key].style.width = "45px";
            })

        }
    }
</script>

<style scoped>
    .highlight:hover {
        width: 62px!important;
        cursor: pointer;
    }

</style>