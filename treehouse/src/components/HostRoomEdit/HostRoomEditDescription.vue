<template>
    <ValidationObserver ref="observer">
        <v-list dense style="border-radius: 8px;border-color: #33af58;border-style: solid;border-width: thin">
            <v-list-item dense>
                <v-list-item-content>

                    <v-container>
                        <v-row>
                            <v-col>
                                <ValidationProvider v-slot="{ errors }" rules="required">

                                    <v-text-field name="alpha_field" label="Room Name" v-model="room.title"

                                                  :error-messages="errors"/>
                                </ValidationProvider>
                            </v-col>
                        </v-row>
                        <v-row dense align="center">
                            <v-col cols="6">


                                <places
                                        placeholder="Location"
                                        v-model="room.address"
                                        @change=" updateLatLong($event)"
                                        :options="places_options"
                                >
                                </places>


                            </v-col>
                            <v-col cols="6">

                                <v-text-field color="primary" label="Transport Info"
                                              v-model="room.transport_info">

                                </v-text-field>
                            </v-col>
                        </v-row>

                        <v-row dense align="center">
                            <v-col cols="auto">
                                <ValidationProvider v-slot="{ errors }" rules="required">
                                    <v-select :items="room_types"
                                              v-model="room.type"
                                              outlined
                                              :error-messages="errors"
                                              required
                                              dense
                                              label="Room Type"
                                              style="height: 40px;width: 180px"
                                              :prepend-icon="room.type === 'private room' ? 'mdi-account'
                                                    : room.type === 'shared room' ? 'mdi-account-multiple'
                                                    : room.type === 'house' ? 'mdi-home'
                                                    : '' "
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
                                                        <v-icon> {{room_types.item.value === 'private room' ?
                                                            'mdi-account'
                                                            : room_types.item.value === 'shared room' ?
                                                            'mdi-account-multiple'
                                                            : room_types.item.value === 'house' ? 'mdi-home'
                                                            : '' }}
                                                        </v-icon>
                                                    </v-col>
                                                </v-row>
                                            </v-container>
                                        </template>


                                    </v-select>
                                </ValidationProvider>
                            </v-col>
                            <v-col cols="auto">

                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <ValidationProvider v-slot="{ errors }" rules="required">
                                            <v-text-field color="primary" prepend-icon="mdi-shower" v-on="on"
                                                          type="number" style="width: 70px" min="0"
                                                          v-model="room.baths_number"
                                                          :error-messages="errors"
                                            />
                                        </ValidationProvider>
                                    </template>
                                    Bathrooms Number
                                </v-tooltip>

                            </v-col>

                            <v-col cols="auto">

                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <ValidationProvider v-slot="{ errors }" rules="required">
                                            <v-text-field color="primary" prepend-icon="mdi-bed-king" v-on="on"
                                                          type="number" style="width: 70px" min="0"
                                                          v-model="room.bedrooms_number"
                                                          :error-messages="errors"
                                            />
                                        </ValidationProvider>
                                    </template>
                                    Bedrooms Number
                                </v-tooltip>

                            </v-col>

                            <v-col cols="auto">

                                <v-tooltip top color="primary">

                                    <template v-slot:activator="{ on }">
                                        <ValidationProvider v-slot="{ errors }" rules="required">
                                            <v-text-field color="primary" prepend-icon="mdi-bed" v-on="on"
                                                          type="number" style="width: 70px" min="0"
                                                          v-model="room.beds_number"
                                                          :error-messages="errors"

                                            />
                                        </ValidationProvider>
                                    </template>
                                    Beds Number
                                </v-tooltip>

                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.lounge" prepend-icon="mdi-sofa" v-on="on"/>
                                    </template>
                                    Lounge
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <ValidationProvider v-slot="{ errors }" rules="required">
                                            <v-text-field color="primary" prepend-icon="mdi-fit-to-page" v-on="on"
                                                          type="number" style="width: 110px" min="0"
                                                          v-model="room.area"
                                                          :error-messages="errors">
                                                <template slot="append"><i><sub>m<sup>2</sup></sub></i></template>
                                            </v-text-field>
                                        </ValidationProvider>
                                    </template>
                                    Area
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.wireless_internet" prepend-icon="mdi-wifi"
                                                    v-on="on"/>
                                    </template>
                                    Wifi
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.air_condition" prepend-icon="mdi-air-conditioner"
                                                    v-on="on"/>
                                    </template>
                                    A/C
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.refrigerator" prepend-icon="mdi-fridge"
                                                    v-on="on"/>
                                    </template>
                                    Refrigerator
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.kitchen" prepend-icon="mdi-stove" v-on="on"/>
                                    </template>
                                    Kitchen
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox hint="ok" v-model="room.tv" prepend-icon="mdi-television"
                                                    v-on="on"/>
                                    </template>
                                    TV
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.parking" prepend-icon="mdi-garage-open-variant"
                                                    v-on="on"/>
                                    </template>
                                    Parking
                                </v-tooltip>
                            </v-col>

                            <v-col cols="auto">
                                <v-tooltip top color="primary">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox v-model="room.elevator" prepend-icon="mdi-elevator-passenger"
                                                    v-on="on"/>
                                    </template>
                                    Elevator
                                </v-tooltip>
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
                                        <v-checkbox color="brown" v-model="room.smoking_allowed"
                                                    prepend-icon="mdi-smoking" v-on="on"/>
                                    </template>
                                    Smocking Allowed
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="brown">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox color="brown" v-model="room.pets_allowed"
                                                    prepend-icon="mdi-paw"
                                                    v-on="on"/>
                                    </template>
                                    Pets Allowed
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <v-tooltip top color="brown">
                                    <template v-slot:activator="{ on }">
                                        <v-checkbox color="brown" v-model="room.events_allowed"
                                                    prepend-icon="mdi-party-popper"
                                                    v-on="on"/>
                                    </template>
                                    Events Allowed
                                </v-tooltip>
                            </v-col>
                            <v-col cols="auto">
                                <ValidationProvider v-slot="{ errors }" rules="required">

                                    <v-text-field color="brown" label="Minimum stay" suffix="days"
                                                  type="number" style="width: 140px" min="0"
                                                  v-model="room.min_stay"
                                                  :error-messages="errors">

                                    </v-text-field>
                                </ValidationProvider>
                            </v-col>
                            <v-col cols="auto">
                                <ValidationProvider v-slot="{ errors }" rules="required">
                                    <v-text-field color="brown" label="Persons number"
                                                  type="number" style="width: 100px" min="0"
                                                  v-model="room.persons_number"
                                                  :error-messages="errors">

                                    </v-text-field>
                                </ValidationProvider>
                            </v-col>

                        </v-row>
                        <v-row dense>
                            <v-col cols="auto">


                                <HostRoomEditCalendar/>

                            </v-col>
                            <v-col cols="auto">
                                <ValidationProvider v-slot="{ errors }" rules="required">

                                    <v-text-field color="blue" label="Cost per day" suffix="€"
                                                  type="number" style="width: 120px" min="0"
                                                  :value="room.cost_per_day | formatFloat"
                                                  v-model="room.cost_per_day"
                                                  :error-messages="errors">

                                    </v-text-field>
                                </ValidationProvider>
                            </v-col>
                            <v-col cols="auto">
                                <ValidationProvider v-slot="{ errors }" rules="required">

                                    <v-text-field color="blue" label="Extra person cost" suffix="€"
                                                  type="number" style="width: 140px" min="0"
                                                  :value="room.add_persons_cost | formatFloat"
                                                  v-model="room.add_persons_cost"
                                                  :error-messages="errors">

                                    </v-text-field>
                                </ValidationProvider>
                            </v-col>


                        </v-row>

                    </v-container>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <ValidationProvider v-slot="{ errors }" rules="required">
                        <v-textarea

                                auto-grow
                                v-model="room.description"
                                label="Description"
                                :error-messages="errors"

                        ></v-textarea>
                    </ValidationProvider>
                </v-list-item-content>
            </v-list-item>
            <v-list-item>
                <v-list-item-content>
                    <v-container>
                        <v-row>
                            <v-btn :disabled="room.Id===null" color="red darken-3" style="color: white"
                                   :loading="loading_delete" @click="dialog=true">
                                <div>Delete room</div>
                            </v-btn>
                            <v-spacer/>
                            <v-btn color="primary" :loading="loading_save" @click="saveChanges">
                                <v-icon v-if="show_tick"> mdi-check</v-icon>
                                <div v-if="!show_tick">Save</div>
                            </v-btn>

                        </v-row>


                    </v-container>

                </v-list-item-content>


            </v-list-item>
            <v-dialog width="30%" v-model="dialog">
                <v-card>
                    <v-card-title>
                        <v-spacer/>
                        <span>Are you sure you want to delete it?</span>
                        <v-spacer/>
                    </v-card-title>

                    <v-card-actions>
                        <v-spacer/>
                        <v-btn color="primary" @click="deleteRoom">YES</v-btn>
                        <v-btn color="red darken-3" style="color: white" @click="dialog=false">NO</v-btn>
                        <v-spacer/>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-list>
    </ValidationObserver>
</template>


<script>


    import HostRoomEditCalendar from "./HostRoomEditCalendar";
    import {extend} from 'vee-validate';
    import {required, max} from "vee-validate/dist/rules";
    import {ValidationProvider, ValidationObserver} from 'vee-validate';
    import Places from 'vue-places';


    extend('required', {
        ...required,
        message: ' '
    });
    extend('max', {
        ...max,
        message: '{_field_} may not be greater than {length} characters',
    });

    export default {

        name: "RoomEditDescription",
        components: {
            HostRoomEditCalendar, ValidationObserver, ValidationProvider, Places
        },

        data: () => ({

            menu: false,
            loading_delete: false,
            loading_save: false,
            show_tick: false,
            room_types: [
                {text: 'Private', value: 'private room'},
                {text: 'Shared', value: 'shared room'},
                {text: 'Home', value: 'house'},
            ],
            selected_type: null,
            icon: '',
            dialog: false,

            places_options: {
                appId: 'plBU33AXJV5Y',
                apiKey: '357dc78dcc889cdaecd7c7ad22d69b5d',
                countries: ['GR'],
            },

            reservations_changed: false


        }),
        computed: {
            room() {
                return this.$store.state.room
            }
        },
        methods: {


            updateLatLong(suggestion) {

                this.room.location[0] = suggestion.latlng.lat;
                this.room.location[1] = suggestion.latlng.lng;

            },

            deleteRoom() {

                this.loading_delete = true;

                this.$store.dispatch('delRoom', this.room.Id)

                this.loading_delete = false;
                this.show_tick = true;
                setTimeout(() => (this.show_tick = false), 4000);

                this.$router.go(-1);


            },

            async saveChanges() {


                if (await this.$refs.observer.validate() && (this.room.address !== '' || this.room.address !== null)) {

                    this.loading_save = true;
                    if (this.$store.state.room.Id === null) {
                        await this.$store.dispatch('newRoom')
                    } else {
                        await this.$store.dispatch('updateRoom')
                    }
                    console.log(this.$store.state.room)

                    let new_avail_days = {
                        'reservations': this.$store.state.room_reservations,
                        'public_user_id': this.$store.state.user.public_id
                    }

                    await this.$store.dispatch('updateRoomAvailableDates', new_avail_days)

                    this.loading_save = false;
                    this.show_tick = true;
                    setTimeout(() => (this.show_tick = false), 4000);
                }


            }
        },
        watch: {
            selected_type: function (new_value) {

                if (new_value === 'private room') {
                    this.icon = 'mdi-account';
                } else if (new_value === 'shared room') {
                    this.icon = 'mdi-account-multiple';
                } else if (new_value === 'house') {
                    this.icon = 'mdi-home';
                } else {
                    this.icon = '';
                }
                this.room.room_type = this.selected_type;
            }
        }
    }
</script>

<style scoped>
    .ap-dropdown-menu {
        position: relative !important;
    }
</style>