<template>
    <v-container>
        <v-row>
            <v-col>
                <RoomTitle v-bind:rating="rating" v-bind:reviews_number="reviews_num" v-bind:title="room_desc.title"/>
            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider></v-divider>
        <v-row dense align="center">
            <v-col xl="7" sm="auto">
                <RoomImages v-bind:images="images"/>
            </v-col>
            <v-col xl="5" sm="auto">
                <RoomDescription v-bind:room_desc="room_desc"/>
                <RoomReservation v-bind:reservation="reservation" class="ml-3 mr-4"/>
            </v-col>

        </v-row>


        <v-row>
            <v-col cols="12" lg="6">
                <RoomReviews v-bind:reviews="reviews" v-bind:rating="rating" :room_title="room_desc.title"/>
            </v-col>
            <v-col cols="12" lg="6">
                <RoomLocation :address="address" v-bind:transport_info="transport_info" :location="location"/>
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
        data: () => ({
            images: null,
            room_desc: {
                air_condition: Boolean,
                elevator: Boolean,
                kitchen: Boolean,
                lounge: Boolean,
                parking: Boolean,
                refrigerator: Boolean,
                baths_number: Number,
                beds_number: Number,
                bedrooms_number: Number,
                tv: Boolean,
                area: Number,
                room_type: String,
                wireless_internet: Boolean,
                description: String,
                smoking_allowed: Boolean,
                pets_allowed: Boolean,
                events_allowed: Boolean,
                min_stay: Number,
                persons_number: Number,
                title: String

            },
            reservation: {
                min_stay: Number,
                add_persons_cost: Number,
                persons_number: Number,
                cost_per_day: Number,
                available_dates: Array
            },

            location: [],
            address: '',
            transport_info: '',

            reviews: [],
            rating: 0,
            reviews_num: 0

        }),
        created() {

            let url = 'http://127.0.0.1:5000/rooms/' + this.$route.params.room_title;

            this.$http.get(url)
                .then((result) => {
                    console.log(result.data);

                    this.images = result.data.images;

                    this.room_desc.air_condition = result.data.air_condition;
                    this.room_desc.elevator = result.data.elevator;
                    this.room_desc.kitchen = result.data.kitchen;
                    this.room_desc.lounge = result.data.lounge;
                    this.room_desc.parking = result.data.parking;
                    this.room_desc.refrigerator = result.data.refrigerator;
                    this.room_desc.baths_number = result.data.baths_number;
                    this.room_desc.beds_number = result.data.beds_number;
                    this.room_desc.bedrooms_number = result.data.bedrooms_number;
                    this.room_desc.tv = result.data.tv;
                    this.room_desc.area = result.data.area;
                    this.room_desc.room_type = result.data.type;
                    this.room_desc.description = result.data.description;
                    this.room_desc.wireless_internet = result.data.wireless_internet;
                    this.room_desc.smoking_allowed = result.data.smoking_allowed;
                    this.room_desc.pets_allowed = result.data.pets_allowed;
                    this.room_desc.events_allowed = result.data.events_allowed;
                    this.room_desc.min_stay = result.data.min_stay;
                    this.room_desc.persons_number = result.data.persons_number;
                    this.room_desc.title = result.data.title;

                    this.reservation.add_persons_cost = result.data.add_persons_cost.toFixed(2);
                    this.reservation.cost_per_day = result.data.cost_per_day.toFixed(2);
                    this.reservation.min_stay = result.data.min_stay;
                    this.reservation.persons_number = result.data.persons_number;
                    this.reservation.available_dates = result.data.availabilities;

                    this.address = result.data.address;
                    this.transport_info = result.data.transport_info;
                    this.location = result.data.location;
                    this.reviews = result.data.reviews;
                    this.rating = result.data.rating;
                    this.reviews_num = result.data.reviews_num;


                })
                .catch(error => console.log(error));

        }
    }
</script>

<style scoped>

</style>