<template>
    <v-list dense>
        <v-list-item dense>
            <v-list-item-content>

                <v-container>
                    <v-row dense align="center">
                        <v-col cols="auto">
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
                                    <v-text-field color="primary" prepend-icon="mdi-shower" v-on="on"
                                                  type="number" style="width: 70px" min="0" v-model="bathrooms_number"/>
                                </template>
                                Bathrooms Number
                            </v-tooltip>
                        </v-col>

                        <v-col cols="auto">
                            <v-tooltip top color="primary">
                                <template v-slot:activator="{ on }">
                                    <v-text-field color="primary" prepend-icon="mdi-bed-king" v-on="on"
                                                  type="number" style="width: 70px" min="0"
                                                  v-model="bedrooms_number"/>
                                </template>
                                Bedrooms Number
                            </v-tooltip>
                        </v-col>

                        <v-col cols="auto">
                            <v-tooltip top color="primary">
                                <template v-slot:activator="{ on }">
                                    <v-text-field color="primary" prepend-icon="mdi-bed" v-on="on"
                                                  type="number" style="width: 70px" min="0"
                                                  v-model="beds_number"/>
                                </template>
                                Beds Number
                            </v-tooltip>
                        </v-col>
                        <v-col cols="auto">
                            <v-tooltip top color="primary">
                                <template v-slot:activator="{ on }">
                                    <v-checkbox v-model="lounge" prepend-icon="mdi-sofa" v-on="on"/>
                                </template>
                                Lounge
                            </v-tooltip>
                        </v-col>
                        <v-col cols="auto">
                            <v-tooltip top color="primary">
                                <template v-slot:activator="{ on }">
                                    <v-text-field color="primary" prepend-icon="mdi-fit-to-page" v-on="on"
                                                  type="number" style="width: 110px" min="0"
                                                  v-model="area">
                                        <template slot="append"><i><sub>m<sup>2</sup></sub></i></template>
                                    </v-text-field>
                                </template>
                                Area
                            </v-tooltip>
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
                    </v-row>

                    <v-row dense>
                        <v-col cols="6">

                            <v-text-field color="primary" label="Address" prepend-icon="mdi-map-marker" v-on="on"
                                          v-model="min_stay">

                            </v-text-field>

                        </v-col>
                        <v-col cols="6">

                            <v-text-field color="primary" label="Transport Info" v-on="on"
                                          v-model="min_stay">

                            </v-text-field>
                        </v-col>
                    </v-row>


                </v-container>
            </v-list-item-content>
        </v-list-item>
        <v-list-item dense>
            <v-list-item-content>

                <v-container>
                    <v-row dense align="center">
                        <v-col cols="auto">
                            <v-tooltip top color="brown">
                                <template v-slot:activator="{ on }">
                                    <v-checkbox color="brown" v-model="smocking" prepend-icon="mdi-smoking" v-on="on"/>
                                </template>
                                Smocking Allowed
                            </v-tooltip>
                        </v-col>
                        <v-col cols="auto">
                            <v-tooltip top color="brown">
                                <template v-slot:activator="{ on }">
                                    <v-checkbox color="brown" v-model="elevator" prepend-icon="mdi-paw" v-on="on"/>
                                </template>
                                Pets Allowed
                            </v-tooltip>
                        </v-col>
                        <v-col cols="auto">
                            <v-tooltip top color="brown">
                                <template v-slot:activator="{ on }">
                                    <v-checkbox color="brown" v-model="elevator" prepend-icon="mdi-party-popper"
                                                v-on="on"/>
                                </template>
                                Events Allowed
                            </v-tooltip>
                        </v-col>
                        <v-col cols="auto">

                            <v-text-field color="brown" label="Minimum stay" v-on="on" suffix="days"
                                          type="number" style="width: 140px" min="0"
                                          v-model="min_stay">

                            </v-text-field>
                        </v-col>

                    </v-row>
                    <v-row dense>
                        <v-col cols="auto">
                            <HostRoomEditCalendar/>
                        </v-col>
                        <v-col cols="auto">

                            <v-text-field color="blue" label="Cost per day" suffix="€" v-on="on"
                                          type="number" style="width: 120px" min="0"
                                          v-model="min_stay">

                            </v-text-field>
                        </v-col>
                        <v-col cols="auto">

                            <v-text-field color="blue" label="Extra person cost" suffix="€" v-on="on"
                                          type="number" style="width: 140px" min="0"
                                          v-model="min_stay">

                            </v-text-field>
                        </v-col>


                    </v-row>

                </v-container>
            </v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-list-item-content>
                <v-textarea

                        auto-grow
                        value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
                        label="Description"
                        readonly

                ></v-textarea>
            </v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-list-item-content>
                <v-container>
                    <v-row>
                        <v-spacer/>
                        <v-btn color="primary" :loading="loading" @click="saveChanges">
                            <v-icon v-if="show_tick"> mdi-check</v-icon>
                            <div v-if="!show_tick">Save</div>
                        </v-btn>

                    </v-row>


                </v-container>

            </v-list-item-content>


        </v-list-item>
    </v-list>
</template>


<script>


    import HostRoomEditCalendar from "./HostRoomEditCalendar";

    export default {

        name: "RoomEditDescription",
        components: {HostRoomEditCalendar},
        data: () => ({
            bedrooms_number: 0,
            beds_number: 0,
            bathrooms_number: 0,
            lounge: false,
            menu: false,
            loading: false,
            show_tick: false,
            room_types: [
                {text: 'Private', value: 0},
                {text: 'Shared', value: 1},
                {text: 'Home', value: 2}
            ],
            selected_type: null,
            icon: ''
        }),
        methods: {
            saveChanges() {
                this.loading = true;
                setTimeout(() => (this.loading = false), 2000);
                this.show_tick = true;
                setTimeout(() => (this.show_tick = false), 4000);

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