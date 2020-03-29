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
                                <i class="fas fa-bath fa-lg"></i>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;"> 12</label>
                            </v-chip>
                        </template>
                        Bathrooms number :12
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-on="on" v-ripple="false">
                                <v-img src="../../assets/icons8-room-24.png"/>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px;">2</label>
                            </v-chip>
                        </template>
                        Bedrooms number :2
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <label style="font-size: 16px;">Room type</label>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-male fa-lg"></i>
                            </v-chip>
                        </template>
                        Private Room
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <i class="fas fa-bed fa-lg"></i>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">2</label>
                            </v-chip>
                        </template>
                        Beds number :2
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <i class="fas fa-couch fa-lg"></i>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Lounge
                    </v-tooltip>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <v-chip color="primary" v-ripple="false" v-on="on">
                                <v-img src="../../assets/room_space.png"/>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <label style="font-size: 16px">12 m<sup>2</sup> </label>
                            </v-chip>
                        </template>
                        Area
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
                                <i class="fas fa-smoking fa-lg"></i>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Smocking Allowed
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-on="on" v-ripple="false">
                                <i class="fas fa-dog fa-lg"></i>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Pets
                    </v-tooltip>
                    <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">
                            <v-chip top color="brown" style="color: white" v-ripple="false" v-on="on">
                                <v-img src="../../assets/party.png"/>
                                <span style="margin-left: 3px;margin-right: 3px">:</span>
                                <i class="fas fa-check-circle fa-lg"></i>
                            </v-chip>
                        </template>
                        Events
                    </v-tooltip>

                    <v-chip top color="brown" style="color: white" v-ripple="false" v-on="on">
                        <label style="font-size: 16px">Minimum stay</label>
                        <span style="margin-left: 3px;margin-right: 3px">:</span>
                        <label style="font-size: 16px">2 days</label>
                    </v-chip>

                </v-chip-group>
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
        <v-list-item >
            <RoomReservation/>
        </v-list-item>
    </v-list>
</template>

<script>
    import RoomReservation from "./RoomReservation";
    export default {
        name: "RoomDescription",
        components: {RoomReservation},
    }
</script>

<style scoped>
    v-label {
        font-size: 23px !important;
    }
</style>