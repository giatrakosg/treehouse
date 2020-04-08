<template>
    <v-container >
        <v-row align="center" dense >
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
                                prepend-icon="far fa-calendar-minus fa-2x"
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
                          style="height: 40px;"
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
                                    <i :class=" room_types.item.value === 0 ? 'fas fa-male'
                                                : room_types.item.value === 1 ? 'fas fa-user-friends'
                                                 : room_types.item.value === 2 ? 'fas fa-home'
                                                  : '' "/>
                                </v-col>
                            </v-row>
                        </v-container>
                    </template>

                </v-select>
            </v-col>

            <v-col>
                <v-switch v-model="wifi" label=" Wifi ">

                </v-switch>

            </v-col>
            <v-col>
                <v-switch v-model="air_condition" label="A/C">

                </v-switch>

            </v-col>
            <v-col>
                <v-switch v-model="refrigerator" label="Refrigerator">

                </v-switch>

            </v-col>
            <v-col>
                <v-switch v-model="kitchen" label="Kitchen">

                </v-switch>

            </v-col>
            <v-col>
                <v-switch v-model="tv" label="TV">

                </v-switch>

            </v-col>
            <v-col>
                <v-switch v-model="parking" label="Parking">

                </v-switch>

            </v-col>

            <v-col>
                <v-switch v-model="elevator" label="Elevator">

                </v-switch>
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
        name: "Options",
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
                console.log(new_value);
                if (new_value === 0) {
                    this.icon = 'fas fa-male';
                } else if (new_value === 1) {
                    this.icon = 'fas fa-user-friends';
                } else if (new_value === 2) {
                    this.icon = 'fas fa-home';
                } else {
                    this.icon = '';
                }
            }
        }


    }
</script>

<style scoped>

</style>