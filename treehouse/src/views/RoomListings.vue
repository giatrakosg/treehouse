<template>
    <v-container>
        <v-row align="center" dense>
            <v-col>
                <RoomOptions v-on:apply-filters="applyFilters($event)"/>
            </v-col>
        </v-row>
        <v-divider></v-divider>

        <v-row>
            <v-col>
                <RoomsList v-bind:rooms="filtered_rooms"/>
            </v-col>
        </v-row>
        <v-row v-if="empty" justify="center" align="center">
            <v-spacer/>
            <v-col cols="auto">
                <span style="color: #86989B;font-size: 40px">No Results</span>
            </v-col>
            <v-spacer/>
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

            list_key: 0,
            empty: false,
        }),
        created() {
            this.$http.get('http://127.0.0.1:5000/rooms')
                .then((result) => {

                    this.rooms = result.data;
                    this.filtered_rooms = this.rooms;

                })
                .catch(error => console.log(error));
        },
        methods: {
            applyFilters: function (filters) {
                console.log(filters);

                let filtered = this.rooms.filter(function (room) {

                        if (room.air_condition === filters.air_condition && room.elevator === filters.elevator &&
                            room.kitchen === filters.kitchen && room.parking === filters.parking &&
                            room.refrigerator === filters.refrigerator && room.tv === filters.tv &&
                            room.wireless_internet === filters.wireless_internet) {

                            if (filters.persons !== '' && filters.persons !== room.persons_number.toString()) {
                                return false;
                            }

                            if (filters.selected_type === null || filters.selected_type === 'all') {
                                return true;
                            } else {
                                return room.type === filters.selected_type
                            }


                        } else {
                            return false;
                        }

                    }
                );
                this.filtered_rooms = filtered;
                if (filtered.length === 0) {
                    this.empty = true;
                } else {

                    this.empty = false;
                }


            }

        }

    }
</script>

<style scoped>

</style>