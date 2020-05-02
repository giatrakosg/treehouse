<template>

    <v-list dense>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    <span style="font-size: 20px;font-weight: 500;text-decoration-line: underline">Apartment:</span>
                </v-list-item-title>

                <v-chip-group column>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-shower</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;"> {{room_desc.baths_number}}</label>
                            </v-chip>
                        </template>
                        Bathrooms number
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-on="on" v-ripple="false">
                                <v-icon> mdi-bed-king</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;">{{room_desc.bedrooms_number}}</label>
                            </v-chip>
                        </template>
                        Bedrooms number
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <label style="font-size: 16px;">Room type</label>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <v-icon v-if="room_desc.room_type==='private room'">mdi-account</v-icon>
                                <v-icon v-if="room_desc.room_type==='shared room'">mdi-account-multiple</v-icon>
                                <v-icon v-if="room_desc.room_type==='house'">mdi-home</v-icon>
                            </v-chip>
                        </template>
                        Room type
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-bed</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">{{room_desc.beds_number}}</label>
                            </v-chip>
                        </template>
                        Beds number
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-sofa</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.lounge ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Lounge
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-fit-to-page</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">{{room_desc.area}} m<sup>2</sup> </label>
                            </v-chip>
                        </template>
                        Area
                    </v-tooltip>

                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-wifi</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.wireless_internet ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Wifi
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-air-conditioner</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.air_condition ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Air condition
                    </v-tooltip>

                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-fridge</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.refrigerator ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Fridge
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-stove</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.kitchen ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Kitchen
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-television</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.tv ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        TV
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-garage-open-variant</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.tv ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Parking
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-icon>mdi-elevator-passenger</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.tv ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Elevator
                    </v-tooltip>


                </v-chip-group>


            </v-list-item-content>
        </v-list-item>

        <v-list-item>
            <v-list-item-content>
                <v-list-item-title>
                    <span style="font-size: 20px;font-weight: 500;text-decoration-line: underline">Rules:</span>
                </v-list-item-title>
                <v-chip-group column>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-icon>mdi-smoking</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.smoking_allowed? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Smocking Allowed
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-on="on" v-ripple="false">
                                <v-icon>mdi-paw</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.pets_allowed ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Pets
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-icon>mdi-party-popper</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i :class="room_desc.events_allowed ? 'fas fa-check-circle fa-lg' : 'fas fa-times-circle fa-lg'"></i>
                            </v-chip>
                        </template>
                        Events
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-icon>mdi-human-male</v-icon>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">{{room_desc.persons_number}}</label>
                            </v-chip>
                        </template>
                        Persons number
                    </v-tooltip>


                    <v-chip top color="brown" style="color: white" v-ripple="false">
                        <label style="font-size: 16px">Minimum stay</label>
                        <span style="margin-left: 3px;margin-right: 3px">:</span>
                        <label style="font-size: 16px">{{room_desc.min_stay}} days</label>
                    </v-chip>


                </v-chip-group>
            </v-list-item-content>
        </v-list-item>
        <v-list-item>
            <v-list-item-content>
                <v-textarea

                        auto-grow
                        :value="room_desc.description"
                        label="Description"
                        readonly

                ></v-textarea>
            </v-list-item-content>
        </v-list-item>
    </v-list>
</template>

<script>


    export default {
        name: "RoomDescription",
        props: {
            room_desc: {
                air_condition: Boolean,
                elevator: Boolean,
                kitchen: Boolean,
                lounge: Boolean,
                parking: Boolean,
                refrigerator: Boolean,
                baths_number: Number,
                beds_number: Number,
                bedrooms_number: Number,
                tv: Boolean,
                area: Number,
                room_type: String,
                wireless_internet: Boolean,
                description: String,
                smoking_allowed: Boolean,
                pets_allowed: Boolean,
                events_allowed: Boolean,
                min_stay: Number,
                persons_number: Number
            }
        },
        data: () => ({
            loading: false
        })
    }
</script>

<style scoped>

</style>