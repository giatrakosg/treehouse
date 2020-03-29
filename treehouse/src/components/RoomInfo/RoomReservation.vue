<template>
    <v-row dense align="center"  style="border-style: outset ;
                                        border-color: forestgreen;border-radius: 8px;
                                        border-width: thin">
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
                                    style="width: 135px"
                                    v-on="on"
                                    prepend-icon="far fa-calendar-minus fa-2x"
                            >

                            </v-text-field>
                        </template>
                        <v-date-picker v-model="dates" no-title scrollable range color="brown">
                            <v-spacer></v-spacer>
                            <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                            <v-btn text color="primary" @click="$refs.menu.save(dates)">OK</v-btn>
                        </v-date-picker>
                    </v-menu>
                </v-col>
                <v-col cols="auto">
                    <v-text-field
                            v-model="persons"
                            label="Extra Persons"
                            min="1"
                            step="1"
                            style="max-width: 108px"
                            prepend-icon="fas fa-male"
                            type="number"/>
                </v-col>

                <v-col cols="auto">
                    <span style="font-weight: 500" >10&euro;/extra person + 13&euro;*5 days=
                        <span style="font-size: 22px">30&euro;</span></span>
                </v-col>
                <v-spacer></v-spacer>
                <v-col >
                    <v-btn elevation="0" color="primary" width="50%"  >
                        Book
                    </v-btn>
                </v-col>
            </v-row>
</template>

<script>
    export default {
        name: "RoomReservation",
         data: function () {
            return {
                menu: false,


                dates: [],
                persons: 0,

            }

        },
    }
</script>

<style scoped>

</style>