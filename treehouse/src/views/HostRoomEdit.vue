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
                <HostRoomEditReviews v-if="loaded"/>
            </v-col>
            <v-col cols="12" xl="7">
                <HostRoomEditMessages v-if="loaded"/>
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import HostRoomEditDescription from "../components/HostRoomEdit/HostRoomEditDescription";
    import HostRoomEditImages from "../components/HostRoomEdit/HostRoomEditImages";
    import HostRoomEditMap from "../components/HostRoomEdit/HostRoomEditMap";
    import HostRoomEditReviews from "../components/HostRoomEdit/HostRoomEditReviews";
    import HostRoomEditMessages from "../components/HostRoomEdit/HostRoomEditMessages";


    export default {
        name: "HostRoomEdit",
        components: {
            HostRoomEditMessages,
            HostRoomEditReviews,
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
                    Id: null,
                    title: '',
                    air_condition: false,
                    elevator: false,
                    kitchen: false,
                    lounge: false,
                    parking: false,
                    refrigerator: false,
                    baths_num: '',
                    beds_num: '',
                    bedrooms_num: '',
                    tv: false,
                    area: '',
                    type: '',
                    description: '',
                    wireless_internet: false,
                    smoking_allowed: false,
                    pets_allowed: false,
                    events_allowed: false,
                    min_stay: '',
                    persons_num: '',
                    address: '',
                    transport_info: '',
                    cost_per_day: '',
                    add_persons_cost: '',
                    images: [],
                    reviews_num: '',
                    location: [37.983810, 23.727539],
                    public_owner_id: this.$store.state.user.public_id

                }
                this.$store.state.room_reservations = [{
                    date_from: new Date().toISOString().slice(0, 10),
                    date_to: null
                }]


                this.loaded = true;
            } else {
                await this.$store.dispatch('getRoom', this.$route.params.room_id)




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