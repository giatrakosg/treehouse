<template>
    <v-container  >
        <v-row  >
            <v-col>
                <RoomTitle/>
            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider ></v-divider>
        <v-row dense   >
            <v-col cols="auto">
                <RoomImages />
            </v-col>
            <v-col  >
               <RoomDescription />
            </v-col>
        </v-row>
        <v-row  no-gutters>
           <v-col lg="7" xs="12">
               <RoomReviews style="width:100%"/>
           </v-col>
            <v-col xs="12">
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
        components: {RoomReviews, RoomLocation, RoomDescription, RoomImages, RoomTitle}
    }
</script>

<style scoped>

</style>