<template>
    <v-container>
        <v-row align="center" dense>
            <v-col cols="auto">
                <v-menu
                        ref="menu"
                        v-model="menu"
                        :close-on-content-click="false"
                        :return-value.sync="dates"
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
                    <v-date-picker v-model="dates" no-title scrollable range color="primary">
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="$refs.menu.save(dates)">OK</v-btn>
                    </v-date-picker>
                </v-menu>

            </v-col>
            <v-text-field
                    v-model="persons"
                    label="Persons"
                    min="1"
                    step="1"
                    style="max-width: 90px"
                    prepend-icon="fas fa-male"
                    type="number"/>
            <v-col cols="auto">
                <v-btn color="primary">

                    Search
                </v-btn>
            </v-col>
            <v-spacer/>

            <v-col cols="2">
                <v-select :items="room_types"
                          v-model="selected_type"
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
                                    <v-icon> {{room_types.item.value === 0 ? 'mdi-account'
                                        : room_types.item.value === 1 ? 'mdi-account-multiple'
                                        : room_types.item.value === 2 ? 'mdi-home'
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
                        <v-checkbox v-model="wifi" prepend-icon="mdi-wifi" v-on="on"/>
                    </template>
                    Wifi
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="a_c" prepend-icon="mdi-air-conditioner" v-on="on"/>
                    </template>
                    A/C
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="refrigerator" prepend-icon="mdi-fridge" v-on="on"/>
                    </template>
                    Refrigerator
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="kitchen" prepend-icon="mdi-stove" v-on="on"/>
                    </template>
                    Kitchen
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox hint="ok" v-model="tv" prepend-icon="mdi-television" v-on="on"/>
                    </template>
                    TV
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="parking" prepend-icon="mdi-garage-open-variant" v-on="on"/>
                    </template>
                    Parking
                </v-tooltip>
            </v-col>

            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="elevator" prepend-icon="mdi-elevator-passenger" v-on="on"/>
                    </template>
                    Elevator
                </v-tooltip>
            </v-col>
            <v-col cols="2">
                <v-select :items="order"
                          outlined
                          dense
                          label="Order By"
                          style="height: 40px"
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
                    {text: 'Private', value: 0},
                    {text: 'Shared', value: 1},
                    {text: 'Home', value: 2},
                    {text: 'All', value: 3},
                ],
                selected_type: null,
                wifi: true,
                air_condition: true,
                refrigerator: true,
                kitchen: true,
                tv: true,
                parking: true,
                elevator: true,
                dates: [],
                persons: 0,
                order: ['Ascending price', 'Descending price'],
                icon: ''
            }

        },
        watch: {
            selected_type: function (new_value) {

                if (new_value === 0) {
                    this.icon = 'mdi-account';
                } else if (new_value === 1) {
                    this.icon = 'mdi-account-multiple';
                } else if (new_value === 2) {
                    this.icon = 'mdi-home';
                }
            }
        }


    }
</script>

<style scoped>

</style>