<template>
    <v-container>
        <v-row>
            <v-spacer/>
            <v-col cols="auto">
                <ValidationProvider v-slot="{ errors }" rules="required">

                    <v-text-field name="alpha_field" label="Title" v-model="room_desc.title" style="width: 400px"
                                  :error-messages="errors" v-if="loaded"/>
                </ValidationProvider>
            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider></v-divider>
        <v-row dense align="center">
            <v-col cols="12" md="12" lg="6" xl="4" order-lg="1" order-xl="1">
                <HostRoomEditImages v-bind:images="images" v-on:new-images="updateImages" v-if="loaded"/>
            </v-col>

            <v-col cols="12" md="12" lg="12" xl="4" order-lg="3" order-xl="2">
                <HostRoomEditDescription :room_desc="this.room_desc" v-if="loaded"/>
            </v-col>
            <v-col cols="12" md="12" lg="6" xl="4" order-lg="2" order-xl="3">
                <HostRoomEditMap :center="this.room_desc.location" v-if="loaded"/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" lg="6">
                <HostRoomEditReviews v-bind:reviews="reviews" v-bind:rating="rating"/>
            </v-col>
            <v-col cols="12" lg="6">
                MESSAGES
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import HostRoomEditDescription from "../components/HostRoomEdit/HostRoomEditDescription";
    import HostRoomEditImages from "../components/HostRoomEdit/HostRoomEditImages";
    import HostRoomEditMap from "../components/HostRoomEdit/HostRoomEditMap";
    import HostRoomEditReviews from "../components/HostRoomEdit/HostRoomEditReviews";
    import moment from 'moment'
    import {extend} from "vee-validate";
    import {required} from "vee-validate/dist/rules";
    import {ValidationProvider} from 'vee-validate';


    extend('required', {
        ...required,
        message: 'Title is required '
    });

    export default {
        name: "HostRoomEdit",
        components: {
            HostRoomEditReviews,
            HostRoomEditMap,
            HostRoomEditImages,
            HostRoomEditDescription,
            ValidationProvider
        },
        data: () => ({
            loaded: false,

            images: null,
            room_desc: {
                air_condition: Boolean,
                elevator: Boolean,
                kitchen: Boolean,
                lounge: Boolean,
                parking: Boolean,
                refrigerator: Boolean,
                baths_num: Number,
                beds_num: Number,
                bedrooms_num: Number,
                tv: Boolean,
                area: Number,
                type: String,
                wireless_internet: Boolean,
                description: String,
                smoking_allowed: Boolean,
                pets_allowed: Boolean,
                events_allowed: Boolean,
                min_stay: Number,
                persons_num: Number,
                title: String,
                address: String,
                transport_info: String,
                add_persons_cost: Number,
                cost_per_day: Number,
                availabilities: Array,
                location: []


            },


            reviews: [],
            rating: 0
        }),
        created() {

            if (this.$route.params.room_title === 'New_Room') {

                this.images = [];

                this.room_desc.title = '';
                this.room_desc.air_condition = false;
                this.room_desc.elevator = false;
                this.room_desc.kitchen = false;
                this.room_desc.lounge = false;
                this.room_desc.parking = false;
                this.room_desc.refrigerator = false;
                this.room_desc.baths_num = 0;
                this.room_desc.beds_num = 0;
                this.room_desc.bedrooms_num = 0;
                this.room_desc.tv = false;
                this.room_desc.area = 0;
                this.room_desc.type = '';
                this.room_desc.description = '';
                this.room_desc.wireless_internet = false;
                this.room_desc.smoking_allowed = false;
                this.room_desc.pets_allowed = false;
                this.room_desc.events_allowed = false;
                this.room_desc.min_stay = 0;
                this.room_desc.persons_num = 0;
                this.room_desc.title = '';
                this.room_desc.address = '';
                this.room_desc.transport_info = '';
                this.room_desc.cost_per_day = 0;
                this.room_desc.add_persons_cost = 0;

                this.room_desc.location = [];
                this.reviews = [];
                this.rating = 0;
                this.room_desc.availabilities = [];


                this.loaded = true;
            } else {

                let url = 'http://127.0.0.1:5000/rooms/' + this.$route.params.room_title;

                this.$http.get(url, {}).then((result) => {


                    this.images = result.data.images;

                    this.room_desc.air_condition = result.data.air_condition;
                    this.room_desc.elevator = result.data.elevator;
                    this.room_desc.kitchen = result.data.kitchen;
                    this.room_desc.lounge = result.data.lounge;
                    this.room_desc.parking = result.data.parking;
                    this.room_desc.refrigerator = result.data.refrigerator;
                    this.room_desc.baths_num = result.data.baths_number;
                    this.room_desc.beds_num = result.data.beds_number;
                    this.room_desc.bedrooms_num = result.data.bedrooms_number;
                    this.room_desc.tv = result.data.tv;
                    this.room_desc.area = result.data.area;
                    this.room_desc.type = result.data.type;
                    this.room_desc.description = result.data.description;
                    this.room_desc.wireless_internet = result.data.wireless_internet;
                    this.room_desc.smoking_allowed = result.data.smoking_allowed;
                    this.room_desc.pets_allowed = result.data.pets_allowed;
                    this.room_desc.events_allowed = result.data.events_allowed;
                    this.room_desc.min_stay = result.data.min_stay;
                    this.room_desc.persons_num = result.data.persons_number;
                    this.room_desc.title = result.data.title;
                    this.room_desc.address = result.data.address;
                    this.room_desc.transport_info = result.data.transport_info;
                    this.room_desc.cost_per_day = result.data.cost_per_day;
                    this.room_desc.add_persons_cost = result.data.add_persons_cost.toFixed(2);

                    let formatted_dates = [];

                    for (let a of result.data.availabilities) {
                        formatted_dates.push({
                            date_from: moment(a.date_from).format('YYYY-MM-DD'),
                            date_to: moment(a.date_to).format('YYYY-MM-DD')
                        });

                    }

                    this.room_desc.availabilities = formatted_dates;


                    console.log(result.data);

                    this.room_desc.location = result.data.location;
                    this.reviews = result.data.reviews;
                    this.rating = result.data.rating;

                    this.loaded = true;


                }).catch(error => console.log(error));
            }

        },
        methods: {
            updateImages(updated_images) {
                this.images = updated_images;

                let url = 'http://127.0.0.1:5000/rooms/' + this.$route.params.room_title + '/update_images';

                this.$http.post(url, {
                    'images': this.images

                }).then(() => {

                }).catch(error => console.log(error));


            },


        }
    }
</script>

<style scoped>

</style>