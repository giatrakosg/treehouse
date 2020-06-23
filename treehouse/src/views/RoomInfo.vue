<template>
    <v-container>
        <v-row>
            <v-col>
                <RoomTitle v-if="loaded"/>
            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider></v-divider>
        <v-row dense align="center">
            <v-col xl="7" sm="auto">
                <RoomImages v-if="loaded"/>
            </v-col>
            <v-col xl="5" sm="auto">
                <RoomDescription v-if="loaded"/>
                <RoomReservation v-if="loaded" class="ml-3 mr-4"/>
            </v-col>

        </v-row>


        <v-row>
            <v-col cols="12" lg="6">
                <RoomReviews v-if="loaded"/>
            </v-col>
            <v-col cols="12" lg="6">
                <RoomLocation v-if="loaded"/>
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
    import RoomReservation from "../components/RoomInfo/RoomReservation";

    export default {
        name: "RoomInfo",
        components: {RoomReservation, RoomReviews, RoomLocation, RoomDescription, RoomImages, RoomTitle},
        contact: false,
        data: () => ({

            loaded: false,


        }),
        async created() {

            await this.$store.dispatch('getRoom', this.$route.params.room_id);

            console.log(this.$store.state.room)

            this.loaded = true;

        }
    }
</script>

<style scoped>

</style>
