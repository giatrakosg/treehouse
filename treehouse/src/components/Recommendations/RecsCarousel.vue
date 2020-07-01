<template lang="html">
    <v-card>
        <v-card-text>
            <v-layout row>
                <v-flex col sm3 md3 lg3>
                    <v-spacer></v-spacer>
                </v-flex>
                <v-flex col sm6 md6 lg6>
                    <RoomsList />
                </v-flex>
                <v-flex col sm3 md3 lg3>
                    <v-spacer></v-spacer>
                </v-flex>
            </v-layout>
        </v-card-text>
    </v-card>
</template>

<script>
import RoomsList from "../RoomListings/RoomsList"
//import RoomCard from "../RoomListings/RoomCard"
export default {
    name : 'RecsCarousel',
    components : {
        //RoomCard,
        RoomsList
    }
}
</script>

<style lang="css" scoped>
</style>
