<template>
    <v-container>
        <v-row align="center" dense>
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
                                style="width: 220px"
                                v-model="computedDateFormatted"
                                v-on="on"
                                prepend-icon="mdi-calendar-range"
                        >

                        </v-text-field>
                    </template>
                    <v-date-picker v-model="dates" :min="nowDate" no-title scrollable range color="primary">
                        <v-spacer></v-spacer>
                        <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                        <v-btn text color="primary" @click="newDates">OK</v-btn>
                    </v-date-picker>
                </v-menu>


            </v-col>
            <v-col cols="auto">


                <places
                        placeholder="Location"
                        v-model="place.label"
                        @change=" updateLatLong($event)"
                        :options="places_options"
                >
                </places>


            </v-col>
            <v-col cols="auto">
                <v-text-field
                        v-model="filters.persons"
                        label="Persons"
                        min="1"
                        step="1"
                        style="max-width: 100px"
                        prepend-icon="fas fa-male"
                        type="number"/>
            </v-col>

            <v-col cols="auto">
                <v-btn color="primary" @click="applyFilters">

                    Search
                </v-btn>
            </v-col>
            <v-spacer/>

            <v-col cols="auto">
                <v-select :items="room_types"
                          v-model="filters.type"
                          outlined
                          dense
                          label="Room Type"
                          style="height: 40px;width: 180px"
                          :prepend-icon="filters.type === 'private room' ? 'mdi-account'
                                        : filters.type === 'shared room' ? 'mdi-account-multiple'
                                        : filters.type === 'house' ? 'mdi-home'
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
                                    <v-icon> {{room_types.item.value === 'private room' ? 'mdi-account'
                                        : room_types.item.value === 'shared room' ? 'mdi-account-multiple'
                                        : room_types.item.value === 'house' ? 'mdi-home'
                                        : '' }}
                                    </v-icon>
                                </v-col>
                            </v-row>
                        </v-container>
                    </template>

                </v-select>
            </v-col>
            <v-col cols="auto">
                <v-switch v-model="filters.apply_amen" label="Filters"/>
            </v-col>

            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.wireless_internet" prepend-icon="mdi-wifi" v-on="on"
                                    :disabled="!filters.apply_amen"
                        />
                    </template>
                    Wifi
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.air_condition" prepend-icon="mdi-air-conditioner" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    A/C
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.refrigerator" prepend-icon="mdi-fridge" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    Refrigerator
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.kitchen" prepend-icon="mdi-stove" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    Kitchen
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox hint="ok" v-model="filters.tv" prepend-icon="mdi-television" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    TV
                </v-tooltip>
            </v-col>
            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.parking" prepend-icon="mdi-garage-open-variant" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    Parking
                </v-tooltip>
            </v-col>

            <v-col cols="auto">
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-checkbox v-model="filters.elevator" prepend-icon="mdi-elevator-passenger" v-on="on"
                                    :disabled="!filters.apply_amen"/>
                    </template>
                    Elevator
                </v-tooltip>
            </v-col>
            <v-spacer/>
            <v-col cols="auto">
                <v-text-field
                        v-model="filters.max_price"
                        label="Max cost"
                        style="width: 100px"
                        type="number"/>
            </v-col>
            <v-col cols="auto">
                <v-select :items="order"
                          outlined
                          dense
                          label="Order By"
                          style="height: 40px;width: 200px"
                          v-model="order_by"

                >
                </v-select>

            </v-col>

        </v-row>
        <v-row>

        </v-row>

    </v-container>

</template>

<script>
    import Places from 'vue-places';

    export default {
        name: "RoomOptions",
        components: {Places},
        props: ['init_dates', 'init_place'],
        data: function () {
            return {
                menu: false,
                room_types: [
                    {text: 'Private', value: 'private room'},
                    {text: 'Shared', value: 'shared room'},
                    {text: 'Home', value: 'house'},
                    {text: 'All', value: 'all'},
                ],

                filters: {
                    type: null,
                    wireless_internet: false,
                    refrigerator: false,
                    kitchen: false,
                    tv: false,
                    parking: false,
                    elevator: false,
                    dates_formatted: [],
                    persons: '',
                    max_price: '',
                    air_condition: false,

                    apply_amen: false,
                },
                order: ['Price-Low to High', 'Price-High to Low', 'Rating'],
                icon: '',
                order_by: '',
                dates: this.init_dates,


                dates_changed: false,
                location_changed: false,

                places_options: {
                    appId: 'plBU33AXJV5Y',
                    apiKey: '357dc78dcc889cdaecd7c7ad22d69b5d',
                    countries: ['GR'],
                },

                place: this.init_place,

                nowDate: new Date().toISOString().slice(0, 10),


            }

        },
        watch: {


            order_by: function (order) {
                this.$emit('order-by', order);
            },

        },
        computed: {
            computedDateFormatted() {

                let formatted = this.formatDate(this.dates);
                if (formatted === null || formatted === undefined) return '';

                if (formatted[1] < formatted[0]) {
                    return `${formatted[1]} - ${formatted[0]}`
                } else {
                    return `${formatted[0]} - ${formatted[1]}`
                }
            },
        },
        methods: {

            updateLatLong(suggestion) {

                console.log(this.place)

                if (this.place.latlng !== suggestion.latlng) {
                    this.place.latlng = suggestion.latlng
                    this.location_changed = true
                }

            },

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
            applyFilters() {
                if (this.dates_changed || this.location_changed) {
                    console.log(this.place.latlng.lng)

                    this.$emit('new-rooms', [this.dates, this.place.latlng, this.filters]);

                    this.dates_changed = false;
                    this.location_changed = false;
                    return;
                }

                this.$emit('apply-filters', this.filters);
            },
            newDates() {

                this.$refs.menu.save(this.dates);
                this.dates_changed = true;

            }
        },


    }
</script>

<style scoped>


</style>