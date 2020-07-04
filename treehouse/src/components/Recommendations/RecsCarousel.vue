<template lang="html">
<!--    <v-card>
        <v-card-text> -->
        <v-container>
            <v-row>
                <v-col cols="12" sm="3" md="3" lg="4" v-for="(room,index) in recs" :key="index">
                    <RoomCard v-bind:type="room.type"
                              v-bind:title="room.title"
                              v-bind:rating="room.rating"
                              v-bind:beds_number="room.beds_number"
                              v-bind:cost_per_day="room.cost_per_day"
                              v-bind:image_src="room.image_src"
                              v-bind:id="room.id"
                              v-bind:reviews_number="room.reviews_num"
                    />
                </v-col>
            </v-row>
        </v-container>
         <!-- </v-card-text> -->
<!--    </v-card> -->
</template>

<script>
import RoomCard from "../RoomListings/RoomCard"
export default {
    name : 'RecsCarousel',
    components : {
        RoomCard,
    },
    computed : {
        recs () {
            return this.$store.state.recs.recs;
        }
    }
}
</script>

<style lang="css" scoped>
</style>
