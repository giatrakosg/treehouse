<template>
    <v-container  >
        <v-row   >
            <v-col>
                <RoomTitle/>
            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider ></v-divider>
        <v-row dense  >
            <v-col md="auto" sm="12">
                <RoomImages />
            </v-col>
            <v-col  >
               <RoomDescription />

            </v-col>
        </v-row>
        <v-row  >
           <v-col  cols="12" lg="6" >
               <RoomReviews />
           </v-col>
            <v-col cols="12" lg="6" >
                <RoomLocation/>
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import RoomTitle from "../components/RoomInfo/RoomTitle";
    import RoomImages from "../components/RoomInfo/RoomImages";
    import RoomDescription from "../components/RoomInfo/RoomDescription";
    import RoomLocation from "../components/RoomInfo/RoomLocation";
    import RoomReviews from "../components/RoomInfo/RoomReviews";
    export default {
        name: "RoomInfo",
        components: {RoomReviews, RoomLocation, RoomDescription, RoomImages, RoomTitle},
        created() {

            
            console.log(this.$route.params.room_id)
        }
    }
</script>

<style scoped>

</style>