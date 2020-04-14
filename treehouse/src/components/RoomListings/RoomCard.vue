<template>
    <v-card elevation="0"
            min-width="190px"
            max-width="400px"
            to="/room"
            v-ripple=false
    >
        <v-img
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >

        </v-img>
        <v-card-title style="height: 60px;font-size: 17px">

            <label>Awesome room </label>

        </v-card-title>
        <v-card-subtitle style="padding-bottom: 0px">
            <v-rating style="display:inline-flex"
                      half-increments
                      dense
                      v-model="rating"
                      readonly
                      small
            ></v-rating>
            <label style="margin-left: 20px;font-size: 13px">(1000 reviews)</label>
        </v-card-subtitle>

        <v-card-text>
            <v-chip-group column>
                <v-tooltip top color="blue">
                    <template v-slot:activator="{ on }">
                        <v-chip color="blue" style="color: white" v-ripple="false" v-on="on">
                            <i class="fas fa-euro-sign fa-lg"></i>
                            <label style="font-size: 16px"> /day:12</label>
                        </v-chip>
                    </template>
                    Cost per day
                </v-tooltip>
                <v-tooltip top color="brown">
                    <template v-slot:activator="{ on }">
                        <v-chip color="brown" style="color: white" v-ripple="false" v-on="on">
                            <v-icon>mdi-bed</v-icon>
                            <label style="font-size: 16px"> :2</label>
                        </v-chip>
                    </template>
                    Beds Number
                </v-tooltip>
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-chip color="primary" style="color: white" v-ripple="false" v-on="on">
                            <label style="font-size: 16px;margin-right: 5px">Room type: </label>
                            <v-icon>mdi-account</v-icon>
                        </v-chip>
                    </template>
                    Priavet Room
                </v-tooltip>
            </v-chip-group>


        </v-card-text>

    </v-card>
</template>

<script>
    export default {
        name: "RoomCard",
        data: function () {
            return {
                rating: 3
            }

        }
    }
</script>

<style scoped>

</style>