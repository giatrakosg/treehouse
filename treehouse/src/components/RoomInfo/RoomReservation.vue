<template>
    <v-container class="pa-0" style="border-style: outset ;
                                        border-color: #0097EE;border-radius: 8px;
                                        border-width: thin">


        <v-row dense align="center" justify="center">
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
                                color="blue"
                                style="width: 220px"
                                v-model="computedDateFormatted"
                                v-on="on"
                                prepend-icon="mdi-calendar-range"
                        >

                        </v-text-field>
                    </template>
                    <v-date-picker v-model="dates" no-title scrollable range color="blue" :min="nowDate"
                                   :allowed-dates="allowedDates">
                        <v-spacer></v-spacer>
                        <v-btn text color="blue" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="blue" @click="$refs.menu.save(dates)">OK</v-btn>
                    </v-date-picker>
                </v-menu>
            </v-col>

            <v-col cols="auto">

                <v-text-field
                        v-model="extra_persons"
                        label="Extra Persons"
                        min="0"
                        step="1"
                        color="blue"
                        style="max-width: 108px"
                        prepend-icon="fas fa-male"
                        type="number"/>
            </v-col>


            <v-col cols="auto">
                    <span style="font-weight: 500">{{room.add_persons_cost | formatFloat}}&euro;/extra person + {{room.cost_per_day | formatFloat}}&euro;* {{dates_diff}} days=
                        <span style="font-size: 22px">{{(room.add_persons_cost *extra_persons + room.cost_per_day * dates_diff) | formatFloat }}&euro;</span></span>
            </v-col>
        </v-row>
        <v-row dense justify="center">

            <v-col cols="10">
                <v-btn elevation="0" style="color: white;" color="blue" width="100%" v-on:click="newReservation">
                    Book
                </v-btn>
            </v-col>
        </v-row>


    </v-container>
</template>

<script>
    import moment from 'moment'

    export default {
        name: "RoomReservation",

        data: function () {
            return {
                menu: false,
                dates_diff: 0,
                dates: [],
                extra_persons: 0,
                total_cost: 0,
                nowDate: new Date().toISOString().slice(0, 10),

            }

        },
        async created() {
            await this.$store.dispatch('getRoomReservations', this.room.Id)

            this.$store.state.room_reservations.sort((r1, r2) => r1.date_from < r2.date_from ? -1 : 1)

        },

        methods: {
            formatDate(dates) {
                let formatted = [];

                if (!dates[0] || !dates[1]) return null;

                let [year, month, day] = dates[0].split('-');
                let new_date = `${day}/${month}/${year}`;
                formatted.push(new_date);

                [year, month, day] = dates[1].split('-');
                new_date = `${day}/${month}/${year}`;
                formatted.push(new_date);

                return formatted;

            },
            newReservation() {
                if (this.dates[0] > this.dates[1]) {
                    let tmp = this.dates[0]
                    this.dates[0] = this.dates[1]
                    this.dates[1] = tmp
                }

                let reservation = {
                    date_from: this.dates[0],
                    date_to: this.dates[1],

                }

                this.$store.dispatch('newRoomReservation', reservation)
            },

            allowedDates(date) {
                let date_from, date_to;


                for (let a of this.reservations) {
                    if (a.status === 1) {
                        date_from = moment(a.date_from).format("YYYY-MM-DD")
                        date_to = moment(a.date_to).format("YYYY-MM-DD")
                        if (date >= date_from && date <= date_to) {
                            console.log(date)
                            return false
                        }
                    } else {
                        if (a.date_to === null) {
                            return date < a.date_from;
                        }
                    }
                }
                return true
            }
        },
        computed: {
            computedDateFormatted() {

                let formatted = this.formatDate(this.dates);
                if (formatted === null) return '';

                if (formatted[1] < formatted[0]) {
                    return `${formatted[1]} - ${formatted[0]}`
                } else {
                    return `${formatted[0]} - ${formatted[1]}`
                }
            },
            room() {
                return this.$store.state.room
            },
            reservations() {
                return this.$store.state.room_reservations
            }

        },
        watch: {
            dates() {

                if (this.dates.length > 1) {
                    let start_date = moment(this.dates[0]);
                    let end_date = moment(this.dates[1]);

                    this.dates_diff = Math.abs(end_date.diff(start_date, 'days')) + 1;

                }

            }
        }

    }
</script>

<style scoped>

</style>