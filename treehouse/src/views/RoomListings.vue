<template>
    <v-container>
        <v-row align="center" dense>
            <v-col>
                <RoomOptions v-on:apply-filters="applyFilters($event)"
                             v-on:order-by="orderBy($event)"
                             v-on:new-rooms="newRoom($event)"
                             v-bind:init_dates="dates"/>
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
        data: () => ({

            rooms: [],
            filtered_rooms: [],

            dates: ["2020-1-2", "2020-10-30"],
            location: [37.9754983, 23.7356671],

            empty: false,
        }),
        created() {
            this.getRooms(this.dates, this.location, null);
        },

        methods: {
            newRoom(event) {
                console.log(event)
                this.getRooms(event[0], event[1], event[2]);
            },

            getRooms(dates, location, filters) {


                this.$http.get('http://127.0.0.1:5000/rooms', {
                    params: {
                        'date_from': dates[0],
                        'date_to': dates[1],
                        'lat': location[0],
                        'long': location[1]
                    }
                })
                    .then((result) => {

                        console.log(result);


                        this.rooms = result.data;


                        if (filters === null) {
                            this.filtered_rooms = this.rooms;
                        } else {

                            this.applyFilters(filters);
                        }

                    })
                    .catch(error => console.log(error));
            },
            applyFilters: function (filters) {

                let filtered = this.rooms.filter(function (room) {


                        if (!filters.apply_amen
                            || (room.air_condition === filters.air_condition && room.elevator === filters.elevator &&
                                room.kitchen === filters.kitchen && room.parking === filters.parking &&
                                room.refrigerator === filters.refrigerator && room.tv === filters.tv &&
                                room.wireless_internet === filters.wireless_internet)) {

                            if (filters.persons !== '' && filters.persons !== room.persons_number.toString()) {
                                return false;
                            }

                            if (filters.max_price !== '' && room.cost_per_day > parseFloat(filters.max_price)) {
                                return false;
                            }

                            if (filters.type === null || filters.type === 'all') {
                                return true;
                            } else {
                                return room.type === filters.type
                            }


                        } else {
                            return false;
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