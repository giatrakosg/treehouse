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
                               v-if="make_available || make_unavailable">
                            <span v-if="make_available">Make Available </span>
                            <span v-if="make_unavailable">Make Unavailable </span>

                        </v-btn>
                        <v-spacer/>

                    </v-date-picker>
                </v-col>
                <v-col>
                    <v-list dense height="326px" style="overflow: auto">
                        <h4 style="text-align: center">Available Dates</h4>
                        <v-divider/>
                        <v-list-item v-for="(i,index) in allowed_date_ranges" v-bind:key="index">

                            <v-list-item-content>
                                <label> {{ i[0]}} ~ {{i[1] }}</label>
                                <v-divider/>
                            </v-list-item-content>
                            <v-list-item-action>
                                <v-btn color="blue" text @click="removeDates(i)">
                                    <v-icon>mdi-minus</v-icon>
                                </v-btn>
                            </v-list-item-action>
                        </v-list-item>
                    </v-list>
                </v-col>
            </v-row>
            <v-row dense>
                <v-spacer></v-spacer>
                <v-col>
                    <v-btn text color="blue" @click="menu = false">Cancel</v-btn>
                </v-col>
                <v-col>
                    <v-btn style="color: white" color="blue" @click="$refs.menu.save(dates)">OK</v-btn>
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
        data: () => ({
            dates: [],
            menu: false,

            allowed_date_ranges: [
                ['2019-09-10', '2019-09-20']
            ],

            make_available: false,
            make_unavailable: false,
        }),
        watch: {
            dates: function () {
                if (this.dates.length !== 0) {
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
            addDates() {
                this.allowed_date_ranges.push(this.dates);

                this.make_available = false;


            },
            removeDates(date) {
                if (date !== null) {
                    let index = this.allowed_date_ranges.indexOf(date);
                    if (index > -1) {
                        this.allowed_date_ranges.splice(index, 1);

                    }
                }


            },
            allowedDates(val) {
                let d;
                let moment_date;

                moment_date = moment(val);

                for (d of this.allowed_date_ranges) {
                    let start_date = d[0];
                    let end_date = d[1];

                    if (start_date > end_date) {
                        start_date = d[1];
                        end_date = d[0]
                    }


                    if (moment_date.isBetween(start_date, end_date) || d[0] === val || d[1] === val) {

                        return true;
                    } else {

                        continue;
                    }

                }
                return false;

            }


        }
    }
</script>

<style scoped>

</style>