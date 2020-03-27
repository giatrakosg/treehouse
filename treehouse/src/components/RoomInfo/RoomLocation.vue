<template>
    <v-container>

   <l-map  style="height: 600px;z-index: 0;border-radius: 8px;" :zoom="zoom" :center="center" >
        <l-tile-layer
                :url="url"
        />
       <l-marker
                    :lat-lng="center"
       >
           <l-icon>
                    <img src="../../assets/treehouse.png" style="width: 45px" >
           </l-icon>

       </l-marker>
    </l-map>
          <v-row>
           <v-col cols="auto">
               <label style="font-size: 15px;font-weight: 300">
                   Addreess: ok
               </label>
           </v-col>
           <v-col cols="auto">
                <label style="font-size: 15px;font-weight: 300">
                   Transport info: ok
               </label>
           </v-col>
       </v-row>
        </v-container>
</template>

<script>
    export default {
        name: "RoomLocation",
         data () {
             return {
                 url: 'http://mt.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                 zoom: 13,
                 center: [37.984888, 23.730851],

             };
         }
    }

</script>

<style scoped>

</style>