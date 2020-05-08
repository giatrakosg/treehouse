<template>

    <v-card elevation="0"
            min-width="190px"
            max-width="400px"
            :to="{name:'RoomInfo',params:{room_title:title}}"
            v-ripple=false
    >
        <v-img v-if="image_src!==''"
               :src="image_src"
               height="300px"
               style="border-radius: 8px"

        />
        <v-img v-else
               :src="require('../../assets/empty_thumbnail.png')"
               height="300px"
               style="border-radius: 8px"

        />
        <v-card-title style="height: 60px;font-size: 17px">
            <label>{{title}} </label>
        </v-card-title>
        <v-card-subtitle style="padding-bottom: 0px">
            <v-rating style="display:inline-flex"
                      half-increments
                      dense
                      v-model="rating"
                      readonly
                      small
            ></v-rating>
            <label style="margin-left: 20px;font-size: 13px">({{reviews_number}})</label>
        </v-card-subtitle>

        <v-card-text>
            <v-chip-group column>
                <v-tooltip top color="blue">
                    <template v-slot:activator="{ on }">
                        <v-chip color="blue" style="color: white" v-ripple="false" v-on="on">
                            <label style="font-size: 16px"> €/day:{{cost_per_day}}</label>
                        </v-chip>
                    </template>
                    Cost per day
                </v-tooltip>
                <v-tooltip top color="brown">
                    <template v-slot:activator="{ on }">
                        <v-chip color="brown" style="color: white" v-ripple="false" v-on="on">
                            <v-icon>mdi-bed</v-icon>
                            <label style="font-size: 16px"> :{{beds_number}}</label>
                        </v-chip>
                    </template>
                    Beds Number
                </v-tooltip>
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-chip color="primary" style="color: white" v-ripple="false" v-on="on">
                            <label style="font-size: 16px;margin-right: 5px">Room type: </label>
                            <v-icon v-if="type==='private room'">mdi-account</v-icon>
                            <v-icon v-if="type==='shared room'">mdi-account-multiple</v-icon>
                            <v-icon v-if="type==='house'">mdi-home</v-icon>
                        </v-chip>
                    </template>
                    <span v-if="type==='private room'">Private Room  </span>
                    <span v-if="type==='shared room'">Shared Room  </span>
                    <span v-if="type==='house'">House  </span>
                </v-tooltip>
            </v-chip-group>


        </v-card-text>

    </v-card>

</template>

<script>
    export default {
        name: "RoomCard",
        props: {
            id: Number,
            type: String,
            beds_number: Number,
            cost_per_day: Number,
            image_src: String,
            title: String,
            rating: Number,
            reviews_number: Number
        },
        methods: {

        }


    }
</script>

<style scoped>

</style>