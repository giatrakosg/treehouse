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
                                   :events="allowedDates"
                                   @close="make_available=false">

                        <v-spacer/>
                        <v-btn color="blue" style="color: white" @click="addDates"
                               v-if="make_available">
                            <span>Make Available </span>
                        </v-btn>
                        <v-btn color="blue" style="color: white" @click="removeDates(dates)"
                               v-if="make_unavailable">
                            <span v-if="make_unavailable">Make Unavailable </span>
                        </v-btn>
                        <v-spacer/>

                    </v-date-picker>
                </v-col>
                <v-col cols="auto">
                    <v-list dense height="326px" style="overflow: auto" min-width="200px" v-if="loaded">
                        <div style="position: sticky;top: -9px; background-color: white;z-index: 1" class="mt-0">
                            <h4 style="text-align: center;">Available Dates</h4>
                            <v-divider/>
                        </div>

                        <v-list-item v-for="(i,index) in tmp_available_date_ranges" v-bind:key="index">

                            <v-list-item-content>
                                <label> {{showDate(i.date_from)}} ~ {{showDate(i.date_to) }}</label>
                                <v-divider/>
                            </v-list-item-content>
                            <v-list-item-action>
                                <v-btn color="blue" text @click="removeDates([i.date_from,i.date_to])">
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
        props: ['available_date_ranges'],
        data: () => ({
            dates: [],
            menu: false,

            tmp_available_date_ranges: [],

            available_dates: [],
            tmp_available_dates: [],

            make_available: false,
            make_unavailable: false,

            loaded: false,
        }),
        mounted() {
            this.tmp_available_date_ranges = JSON.parse(JSON.stringify(this.available_date_ranges));
            this.tmp_available_date_ranges.sort((a, b) => a.date_from > b.date_from ? 1 : -1);
            this.loaded = true;

            this.available_dates = this.getAllDates(this.available_date_ranges);
            this.tmp_available_dates = JSON.parse(JSON.stringify(this.available_dates));

        },

        watch: {
            menu() {
                if (!this.menu) {
                    this.tmp_available_dates = JSON.parse(JSON.stringify(this.available_dates));
                    this.tmp_available_date_ranges = JSON.parse(JSON.stringify(this.available_date_ranges));
                }

            },
            dates: function () {
                if (this.dates.length === 2) {

                    if (!this.allowedDates(this.dates[0]) || !this.allowedDates(this.dates[1])) {

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
                return moment(date).format(("DD/MM/YYYY"));
            },
            saveDates() {
                this.menu = false;

                this.available_dates = this.tmp_available_dates;

                this.$emit('new-dates', this.available_date_ranges);
                this.menu = false;


            },
            getAllDates(date_ranges) {
                let dates = [];

                for (let d of date_ranges) {
                    let end_date = moment(d.date_to);
                    let current_date = moment(d.date_from);

                    while (current_date <= end_date) {
                        dates.push(current_date.format("YYYY-MM-DD"));
                        current_date = moment(current_date).add(1, 'days');
                    }
                }


                return dates


            },
            addDates() {

                let dates;
                let dates_range = this.orderDates(this.dates);

                dates_range = [{date_from: dates_range[0], date_to: dates_range[1]}];

                dates = this.getAllDates(dates_range);

                for (let d of dates) {
                    this.tmp_available_dates.push(d);
                }

                this.tmp_available_dates.sort((a, b) => a > b ? 1 : -1);

                this.tmp_available_dates = [...new Set(this.tmp_available_dates)];


                this.tmp_available_date_ranges = this.makeDateRanges();
                this.dates = []


            },

            removeDates(dates_r) {

                let dates;
                let dates_range = this.orderDates(dates_r);

                dates_range = [{date_from: dates_range[0], date_to: dates_range[1]}];

                dates = this.getAllDates(dates_range);

                for (let d of dates) {

                    let index = this.tmp_available_dates.indexOf(d);
                    if (index !== -1) {
                        this.tmp_available_dates.splice(index, 1);
                    }

                }

                this.tmp_available_date_ranges = this.makeDateRanges();
                this.dates = []


            },
            makeDateRanges() {

                let ranges = [];

                let next_date;


                let current_date = moment(this.tmp_available_dates[0]);
                let start_date = current_date;

                console.log(this.tmp_available_dates);


                for (let i = 1; i < this.tmp_available_dates.length; i++) {
                    next_date = moment(this.tmp_available_dates[i]);
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
            allowedDates(val) {


                return this.tmp_available_dates.indexOf(val) !== -1

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