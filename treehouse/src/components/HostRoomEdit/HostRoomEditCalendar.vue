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
                                   style="-webkit-box-shadow: none!important;">
                        <label> {{ dates[0]}} ~ {{dates[1] }}</label>
                        <v-spacer></v-spacer>

                        <v-btn text color="blue" @click="addDates">
                            <v-icon>
                                mdi-plus
                            </v-icon>
                        </v-btn>


                    </v-date-picker>
                </v-col>
                <v-col>
                    <v-list dense height="326px" style="overflow: auto">
                        <v-list-item v-for="(i,index) in date_ranges" v-bind:key="index">
                            <v-list-item-content>
                                <label> {{ i[0]}} ~ {{i[1] }}</label>
                                <v-divider/>
                            </v-list-item-content>
                            <v-list-item-action>
                                <v-btn color="blue" icon="mdi-minus" @click="removeDates(i)">
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
    export default {
        name: "HostRoomEditCalendar",
        data: () => ({
            dates: [],
            menu: false,
            date_ranges: [
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],
                ['2019-09-10', '2019-09-20'],

            ],
        }),
        methods: {
            addDates() {
                this.date_ranges.push(this.dates);
            },
            removeDates(date) {
                if (date !== null) {
                    let index = this.date_ranges.indexOf(date);
                    if (index > -1) {
                        this.date_ranges.splice(index, 1);

                    }
                }


            }


        }
    }
</script>

<style scoped>

</style>