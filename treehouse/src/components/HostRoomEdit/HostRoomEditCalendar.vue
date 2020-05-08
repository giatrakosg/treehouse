<template>
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
                    label="Select Available Dates"
                    readonly
                    style="width: 220px"
                    color="blue"
                    v-on="on"
                    prepend-icon="mdi-calendar-range"
            >

            </v-text-field>
        </template>
        <v-card>
            <v-row dense>
                <v-col>
                    <v-date-picker v-model="dates" no-title scrollable range color="blue"
                                   style="-webkit-box-shadow: none!important;"
                                   event-color="primary"
                                   :events="availableDates"
                                   @close="make_available=false"
                                   :min="nowDate">


                        <v-spacer/>
                        <v-btn color="blue" style="color: white" @click="makeAvailable"
                               v-if="make_unavailable">
                            <span>Make Unavailable </span>
                        </v-btn>
                        <v-btn color="blue" style="color: white" @click="makeUnavailable(dates)"
                               v-if="make_available">
                            <span>Make Available </span>
                        </v-btn>
                        <v-spacer/>

                    </v-date-picker>
                </v-col>
                <v-col cols="auto">
                    <v-list dense height="326px" style="overflow: auto" min-width="200px" v-if="loaded">
                        <div style="position: sticky;top: -9px; background-color: white;z-index: 1" class="mt-0">
                            <h4 style="text-align: center;">Unavailable Dates</h4>
                            <v-divider/>
                        </div>

                        <v-list-item v-for="(i,index) in tmp_reservation_date_ranges" v-bind:key="index">

                            <v-list-item-content>
                                <label> {{showDate(i.date_from)}} ~ {{showDate(i.date_to)}}</label>
                                <v-divider/>
                            </v-list-item-content>
                            <v-list-item-action>
                                <v-btn color="blue" text @click="makeUnavailable([i.date_from,i.date_to])">
                                    <v-icon>mdi-minus</v-icon>
                                </v-btn>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-col>
            </v-row>
            <v-row dense>
                <v-spacer></v-spacer>

                <v-col cols="auto">
                    <v-btn style="color: white" color="blue" @click="saveDates">SAVE</v-btn>
                </v-col>
                <v-col cols="auto">
                    <v-btn text color="blue" @click="menu = false">Cancel</v-btn>
                </v-col>
                <v-spacer></v-spacer>

            </v-row>
        </v-card>


    </v-menu>
</template>

<script>
    import moment from 'moment'

    export default {
        name: "HostRoomEditCalendar",
        props: ['reservation_date_ranges'],
        data: () => ({
            dates: [],
            menu: false,

            tmp_reservation_date_ranges: [],

            reserved_dates: [],
            tmp_reserved_dates: [],

            make_available: false,
            make_unavailable: false,

            loaded: false,

            nowDate: new Date().toISOString().slice(0, 10),
        }),
        mounted() {
            console.log(this.reservation_date_ranges)
            this.tmp_reservation_date_ranges = JSON.parse(JSON.stringify(this.reservation_date_ranges));
            this.tmp_reservation_date_ranges.sort((a, b) => a.date_from > b.date_from ? 1 : -1);
            this.loaded = true;

            this.reserved_dates = this.getAllDates(this.reservation_date_ranges);
            this.tmp_reserved_dates = JSON.parse(JSON.stringify(this.reserved_dates));

        },

        watch: {
            menu() {
                if (!this.menu) {
                    this.tmp_reserved_dates = JSON.parse(JSON.stringify(this.reserved_dates));
                    this.tmp_reservation_date_ranges = JSON.parse(JSON.stringify(this.reservation_date_ranges));
                }

            },
            dates: function () {
                if (this.dates.length === 2) {

                    if (!this.availableDates(this.dates[0]) || !this.availableDates(this.dates[1])) {

                        this.make_available = true;
                        this.make_unavailable = false;


                    } else {

                        this.make_available = false;
                        this.make_unavailable = true;

                    }

                } else {
                    this.make_available = false;
                    this.make_unavailable = false;

                }


            }
        },

        methods: {
            showDate: function (date) {
                if (date === null) {
                    return "∞"
                }
                return moment(date).format(("DD/MM/YYYY"));
            },
            saveDates() {


                this.reserved_dates = this.tmp_reserved_dates;

                this.$emit('new-dates', this.tmp_reservation_date_ranges);
                this.menu = false;


            },
            getAllDates(date_ranges) {
                let dates = [];

                for (let d of date_ranges) {
                    let current_date = moment(d.date_from);
                    if (d.date_to === null) {
                        dates.push(current_date.format("YYYY-MM-DD"));
                        dates.push(null);
                    }
                    let end_date = moment(d.date_to);


                    while (current_date <= end_date) {
                        dates.push(current_date.format("YYYY-MM-DD"));
                        current_date = moment(current_date).add(1, 'days');
                    }
                }


                return dates


            },
            makeAvailable() {

                let dates;
                let dates_range = this.orderDates(this.dates);

                dates_range = [{date_from: dates_range[0], date_to: dates_range[1]}];

                dates = this.getAllDates(dates_range);

                for (let d of dates) {
                    this.tmp_reserved_dates.push(d);
                }

                this.tmp_reserved_dates.sort(function (a, b) {
                    if (a === null) {
                        return 1;
                    } else if (b === null) {
                        return -1;
                    } else {
                        return a > b ? 1 : -1;
                    }

                });

                this.tmp_reserved_dates = [...new Set(this.tmp_reserved_dates)];


                this.tmp_reservation_date_ranges = this.makeDateRanges();
                this.dates = []


            },

            makeUnavailable(dates_r) {

                let dates, flag = false;
                let i;
                let dates_range = this.orderDates(dates_r);

                dates_range = [{date_from: dates_range[0], date_to: dates_range[1]}];

                dates = this.getAllDates(dates_range);

                for (i = 0; i < dates.length; i++) {

                    let index = this.tmp_reserved_dates.indexOf(dates[i]);
                    if (index !== -1) {
                        this.tmp_reserved_dates.splice(index, 1);
                    } else if (dates[i] >= this.tmp_reserved_dates[this.tmp_reserved_dates.length - 2]) {
                        flag = true;
                        break;
                    }

                }
                if (flag) {
                    let add_dates = this.getAllDates([{
                        date_from: this.tmp_reserved_dates[this.tmp_reserved_dates.length - 2],
                        date_to: moment(dates[i]).subtract(1, 'days').format("YYYY-MM-DD")
                    }])

                    for (let i = 1; i < add_dates.length; i++) {
                        this.tmp_reserved_dates.splice(this.tmp_reserved_dates.length - 1, 0, add_dates[i])
                    }

                    let last_day = moment(dates[dates.length - 1]).add(1, 'days').format("YYYY-MM-DD");
                    this.tmp_reserved_dates.splice(this.tmp_reserved_dates.length - 1, 0, last_day)

                }

                this.tmp_reservation_date_ranges = this.makeDateRanges();
                this.dates = []


            },
            makeDateRanges() {

                let ranges = [];

                let next_date;


                let current_date = moment(this.tmp_reserved_dates[0]);
                let start_date = current_date;

                console.log(this.tmp_reserved_dates);


                for (let i = 1; i < this.tmp_reserved_dates.length; i++) {
                    if (this.tmp_reserved_dates[i] == null) {
                        ranges.push({
                            date_from: start_date.format("YYYY-MM-DD"),
                            date_to: null
                        });
                        return ranges
                    }
                    next_date = moment(this.tmp_reserved_dates[i]);

                    if (next_date.diff(current_date, 'days') !== 1) {
                        ranges.push({
                            date_from: start_date.format("YYYY-MM-DD"),
                            date_to: current_date.format("YYYY-MM-DD")
                        });
                        start_date = next_date;

                    }
                    current_date = next_date;

                }
                ranges.push({
                    date_from: start_date.format("YYYY-MM-DD"),
                    date_to: current_date.format("YYYY-MM-DD")
                });

                console.log(ranges);
                return ranges


            },
            availableDates(val) {

                for (let i = 0; i < this.tmp_reserved_dates.length; i++) {
                    if (this.tmp_reserved_dates[i] == null) {
                        return val <= this.tmp_reserved_dates[i - 1]
                    } else if (this.tmp_reserved_dates[i] === val) {
                        return false
                    }
                }
                return true

            },
            orderDates(dates) {
                let start_date = dates[0];
                let end_date = dates[1];

                if (start_date > end_date) {
                    start_date = dates[1];
                    end_date = dates[0]
                }
                return [start_date, end_date]
            }


        }
    }
</script>

<style scoped>


</style>