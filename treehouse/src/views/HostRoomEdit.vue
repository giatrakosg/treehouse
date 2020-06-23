<template>
    <v-container>

        <v-row dense align="center">


            <v-col>
                <HostRoomEditDescription v-if="loaded"/>
            </v-col>

        </v-row>
        <v-row align="center">
            <v-col cols="12" md="12" lg="12" xl="7" order-lg="1" order-xl="1">
                <HostRoomEditImages v-on:new-images="updateImages" v-if="loaded"/>
            </v-col>
            <v-col cols="12" md="12" lg="12" xl="5" order-lg="2" order-xl="3">
                <HostRoomEditMap :center="this.room.location" v-if="loaded"/>
            </v-col>

        </v-row>
        <v-row>
            <v-col cols="12" xl="5">
                <!--               // <HostRoomEditReviews />-->
            </v-col>
            <v-col cols="12" xl="7">
                <!--                <HostRoomEditMessages />-->
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import HostRoomEditDescription from "../components/HostRoomEdit/HostRoomEditDescription";
    import HostRoomEditImages from "../components/HostRoomEdit/HostRoomEditImages";
    import HostRoomEditMap from "../components/HostRoomEdit/HostRoomEditMap";
    // import HostRoomEditReviews from "../components/HostRoomEdit/HostRoomEditReviews";
    //
    //
    //
    // import HostRoomEditMessages from "../components/HostRoomEdit/HostRoomEditMessages";


    export default {
        name: "HostRoomEdit",
        components: {
            // HostRoomEditMessages,
            // HostRoomEditReviews,
            HostRoomEditMap,
            HostRoomEditImages,
            HostRoomEditDescription,

        },
        data: () => ({
            loaded: false,
        }),
        computed: {
            room() {
                return this.$store.state.room
            }
        },
        async created() {

            if (this.$route.params.room_id == -1) {
                this.$store.state.room = {
                    title: '',
                    air_condition: false,
                    elevator: false,
                    kitchen: false,
                    lounge: false,
                    parking: false,
                    refrigerator: false,
                    baths_num: 0,
                    beds_num: 0,
                    bedrooms_num: 0,
                    tv: false,
                    area: 0,
                    type: '',
                    description: '',
                    wireless_internet: false,
                    smoking_allowed: false,
                    pets_allowed: false,
                    events_allowed: false,
                    min_stay: 0,
                    persons_num: 0,
                    address: '',
                    transport_info: '',
                    cost_per_day: 0,
                    add_persons_cost: 0,
                    reservations: [{date_from: new Date().toISOString().slice(0, 10), date_to: null}],
                    images: [],
                    reviews_num: 0,
                    location: [37.983810, 23.727539]

                }


                this.loaded = true;
            } else {
                await this.$store.dispatch('getRoom', this.$route.params.room_id)
                console.log(this.$store.state.room)

                // let formatted_dates = [];
                //
                // for (let a of result.data.reservations) {
                //     if (a.status === 0) {
                //         if (a.date_to === null) {
                //             formatted_dates.push({
                //                 date_from: moment(a.date_from).format('YYYY-MM-DD'),
                //                 date_to: null
                //             });
                //         } else {
                //             formatted_dates.push({
                //                 date_from: moment(a.date_from).format('YYYY-MM-DD'),
                //                 date_to: moment(a.date_to).format('YYYY-MM-DD')
                //             });
                //         }
                //
                //     }
                //
                // }

                // this.room_desc.reservations = formatted_dates;
                //
                //
                // console.log(result.data);
                //
                // this.room_desc.location = result.data.location;
                // this.reviews = result.data.reviews;
                // this.message_threads = result.data.threads.sort(function (a, b) {
                //     if (new Date(a.last_message.timestamp) <= new Date(b.last_message.timestamp)) {
                //         return 1;
                //     } else {
                //         return -1;
                //     }
                // });
                // console.log(this.message_threads);
                //
                //
                // this.rating = result.data.rating;

                this.loaded = true;


            }

        },
        methods: {
            updateImages(updated_images) {
                this.images = updated_images;

                let url = 'https://127.0.0.1:5000/rooms/' + this.$route.params.room_title + '/update_images';

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