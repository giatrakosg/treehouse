<template>
    <v-container>
        <v-row align="center" dense>
            <v-col>
                <RoomOptions v-on:apply-filters="applyFilters($event)"
                             v-on:order-by="orderBy($event)"
                             v-on:new-rooms="newRooms($event)"
                             v-bind:init_dates="dates"
                             v-bind:init_place="place"
                             v-bind:init_persons="persons"/>
            </v-col>
        </v-row>
        <v-divider></v-divider>

        <v-row>
            <v-col>
                <RoomsList v-bind:rooms="filtered_rooms"/>
            </v-col>
        </v-row>

    </v-container>
</template>

<script>
    import RoomsList from "../components/RoomListings/RoomsList";
    import RoomOptions from "../components/RoomListings/RoomOptions";

    export default {
        name: "RoomListings",
        components: {RoomOptions, RoomsList},
        props: ['date_from', 'date_to', 'place_label', 'place_lat', 'place_lng', 'persons'],
        data: () => ({

            rooms: [],
            filtered_rooms: [],

            dates: ["2020-1-2", "2020-10-30"],
            place: {
                label: 'Athens',
                latlng: [37.9754983, 23.7356671]
            },

            empty: false,
        }),
        created() {

            this.dates = [this.date_from, this.date_to]
            this.place.label = this.place_label
            this.place.latlng = [this.place_lat, this.place_lng]

            let filters = {
                type: null,
                wireless_internet: false,
                refrigerator: false,
                kitchen: false,
                tv: false,
                parking: false,
                elevator: false,
                dates_formatted: [],
                persons: this.persons,
                max_price: '',
                air_condition: false,
                apply_amen: false,
            }


            this.getRooms(this.dates, this.place.latlng, filters);
        },

        methods: {
            newRooms(event) {

                console.log(event)
                this.getRooms(event[0], [event[1].lat, event[1].lng], event[2]);
            },

            async getRooms(dates, loc, filters) {


                await this.$store.dispatch('getRooms', {dates, loc});
                this.rooms = this.$store.state.rooms
                this.applyFilters(filters);
                console.log(this.$store.state.user)


            },
            applyFilters: function (filters) {

                let filtered = this.rooms.filter(function (room) {

                        if (filters.persons !== room.persons_number) {
                            return false;
                        }


                        if (filters.max_price !== '' && room.cost_per_day > parseFloat(filters.max_price)) {
                            return false;
                        }

                        if (filters.type !== null && filters.type !== 'all') {
                            return room.type === filters.type
                        }

                        if (filters.apply_amen) {
                            if (room.air_condition === filters.air_condition && room.elevator === filters.elevator &&
                                room.kitchen === filters.kitchen && room.parking === filters.parking &&
                                room.refrigerator === filters.refrigerator && room.tv === filters.tv &&
                                room.wireless_internet === filters.wireless_internet) {

                                return true;
                            }
                        } else {
                            return true;
                        }


                    }
                );


                this.filtered_rooms = filtered;


            },
            orderBy(order) {
                if (order === 'Price-Low to High') {
                    this.filtered_rooms.sort((room1, room2) => room1.cost_per_day - room2.cost_per_day);
                } else if (order === 'Price-High to Low') {
                    this.filtered_rooms.sort((room1, room2) => room2.cost_per_day - room1.cost_per_day);
                } else if (order === 'Rating') {
                    this.filtered_rooms.sort((room1, room2) => room2.rating - room1.rating);
                }
            },


        }

    }
</script>

<style scoped>

</style>