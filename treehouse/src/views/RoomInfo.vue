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
    </v-container>
</template>

<script>
    import RoomTitle from "../components/RoomInfo/RoomTitle";
    import RoomImages from "../components/RoomInfo/RoomImages";
    import RoomDescription from "../components/RoomInfo/RoomDescription";
    export default {
        name: "RoomInfo",
        components: {RoomDescription, RoomImages, RoomTitle}
    }
</script>

<style scoped>

</style>