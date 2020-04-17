<template>
    <v-container class="fixedElement">
        <v-row align="center" dense>
            <v-col cols="auto">
                <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :return-value.sync="filters.dates"
                        transition="scale-transition"
                        offset-y
                        min-width="290px"
                >
                    <template v-slot:activator="{ on }">

                        <v-text-field
                                label="Select Dates"
                                readonly
                                style="width: 150px"
                                v-on="on"
                                prepend-icon="mdi-calendar-range"
                        >

                        </v-text-field>
                    </template>
                    <v-date-picker v-model="filters.dates" no-title scrollable range color="primary">
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu.save(dates)">OK</v-btn>
                    </v-date-picker>
                </v-menu>

            </v-col>
            <v-col cols="auto">
                <v-text-field
                        v-model="filters.persons"
                        label="Persons"
                        min="1"
                        step="1"
                        style="max-width: 90px"
                        prepend-icon="fas fa-male"
                        type="number"/>
            </v-col>

            <v-col cols="auto">
                <v-btn color="primary" @click="applyFilters">

                    Search
                </v-btn>
            </v-col>
            <v-spacer/>

            <v-col cols="auto">
                <v-select :items="room_types"
                          v-model="type"
                          outlined
                          dense
                          label="Room Type"
                          style="height: 40px;width: 180px"
                          :prepend-icon="icon"
                          item-value="value"
                          item-text="text"

                >
                    <template slot="item" slot-scope="room_types">
                        <v-container>
                            <v-row dense>
                                <v-col cols="9">
                                    <label>{{room_types.item.text}}</label>
                                </v-col>
                                <v-col cols="3">
                                    <v-icon> {{room_types.item.value === 'private room' ? 'mdi-account'
                                        : room_types.item.value === 'shared room' ? 'mdi-account-multiple'
                                        : room_types.item.value === 'house' ? 'mdi-home'
                                        : '' }}
                                    </v-icon>
                                </v-col>
                            </v-row>
                        </v-container>
                    </template>

                </v-select>
            </v-col>

            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.wireless_internet" prepend-icon="mdi-wifi" v-on="on"/>
                    </template>
                    Wifi
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.air_condition" prepend-icon="mdi-air-conditioner" v-on="on"/>
                    </template>
                    A/C
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.refrigerator" prepend-icon="mdi-fridge" v-on="on"/>
                    </template>
                    Refrigerator
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.kitchen" prepend-icon="mdi-stove" v-on="on"/>
                    </template>
                    Kitchen
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox hint="ok" v-model="filters.tv" prepend-icon="mdi-television" v-on="on"/>
                    </template>
                    TV
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.parking" prepend-icon="mdi-garage-open-variant" v-on="on"/>
                    </template>
                    Parking
                </v-tooltip>
            </v-col>

            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.elevator" prepend-icon="mdi-elevator-passenger" v-on="on"/>
                    </template>
                    Elevator
                </v-tooltip>
            </v-col>
            <v-spacer/>
            <v-col cols="auto">
                <v-text-field
                        v-model="filters.max_price"
                        label="Max cost"
                        style="width: 100px"

                        type="number"/>
            </v-col>
            <v-col cols="auto">
                <v-select :items="order"
                          outlined
                          dense
                          label="Order By"
                          style="height: 40px;"

                >
                </v-select>

            </v-col>

        </v-row>
        <v-row>

        </v-row>

    </v-container>

</template>

<script>
    export default {
        name: "RoomOptions",
        data: function () {
            return {
                menu: false,
                room_types: [
                    {text: 'Private', value: 'private room'},
                    {text: 'Shared', value: 'shared room'},
                    {text: 'Home', value: 'house'},
                    {text: 'All', value: 'all'},
                ],
                filters: {
                    selected_type: null,
                    wireless_internet: true,
                    refrigerator: true,
                    kitchen: true,
                    tv: true,
                    parking: true,
                    elevator: true,
                    dates: [],
                    persons: '',
                    max_price: null,
                    air_condition: true,
                },
                order: ['Ascending price', 'Descending price'],
                icon: '',
                type: ''


            }

        },
        watch: {
            type: function (new_value) {
                console.log(new_value);

                if (new_value === 'private room') {
                    this.icon = 'mdi-account';
                } else if (new_value === 'shared room') {
                    this.icon = 'mdi-account-multiple';
                } else if (new_value === 'house') {
                    this.icon = 'mdi-home';
                }
                this.filters.selected_type = this.type;
            }
        },
        methods: {
            applyFilters() {

                this.$emit('apply-filters', this.filters);
            }
        }


    }
</script>

<style scoped>
    .fixedElement {
        position: sticky;
        top: 0;


    }

</style>