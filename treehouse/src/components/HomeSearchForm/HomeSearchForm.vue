<template>
    <v-card
            color="white"
            elevation="9"
            width="100%"

    >
        <v-card-text>
            <ValidationObserver ref="observer">
                <v-row align="center" justify-xl="space-around" justify="start">

                    <v-col cols="auto">


                        <v-menu
                                ref="menu"
                                v-model="menu"
                                :close-on-content-click="false"
                                :return-value.sync="dates"
                                transition="scale-transition"
                                offset-y


                        >
                            <template v-slot:activator="{ on }">
                                <ValidationProvider v-slot="{ errors }" rules="required">

                                    <v-text-field
                                            label="Select Dates"
                                            readonly
                                            :error-messages="errors"
                                            v-model="computedDateFormatted"
                                            v-on="on"
                                            prepend-icon="mdi-calendar-range"
                                    >

                                    </v-text-field>
                                </ValidationProvider>

                            </template>
                            <v-date-picker v-model="dates" :min="nowDate" no-title scrollable range color="primary">
                                <v-spacer></v-spacer>
                                <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                                <v-btn text color="primary" @click="this.$refs.menu.save(this.dates)">OK</v-btn>
                            </v-date-picker>
                        </v-menu>


                    </v-col>
                    <v-col cols="auto">


                        <places
                                placeholder="Location"
                                v-model="place.label"
                                @change=" updateLatLong($event)"
                                :options="places_options"
                                :class="place.label === '' ? 'ap-input1': 'ap-input2' "

                        >
                        </places>


                    </v-col>
                    <v-col cols="auto">
                        <ValidationProvider v-slot="{ errors }" rules="required">
                            <v-text-field
                                    v-model="persons"
                                    label="Persons"
                                    min="1"
                                    step="1"
                                    :error-messages="errors"

                                    prepend-icon="fas fa-male"
                                    type="number"/>
                        </ValidationProvider>
                    </v-col>

                    <v-col cols="auto" offset="20">
                        <v-btn color="primary" @click="getRooms">

                            Search
                        </v-btn>
                    </v-col>

                </v-row>
            </ValidationObserver>

        </v-card-text>
    </v-card>

</template>

<script>
    import Places from 'vue-places';
    import {extend} from 'vee-validate';
    import {required} from "vee-validate/dist/rules";
    import {ValidationProvider, ValidationObserver} from 'vee-validate';


    extend('required', {
        ...required,
        message: ' '
    });

    export default {
        name: "HomeSearchForm",
        components: {Places, ValidationObserver, ValidationProvider,},
        data: () => ({
            picker: null,

            menu: false,
            nowDate: new Date().toISOString().slice(0, 10),

            places_options: {
                appId: 'plBU33AXJV5Y',
                apiKey: '357dc78dcc889cdaecd7c7ad22d69b5d',
                countries: ['GR'],
            },

            dates: [],
            place: {
                label: '',
                latlng: []
            },
            persons: 1

        }),
        computed: {

            computedDateFormatted() {

                let formatted = this.formatDate(this.dates);
                if (formatted === null || formatted === undefined) return '';

                if (formatted[1] < formatted[0]) {
                    return `${formatted[1]} - ${formatted[0]}`
                } else {
                    return `${formatted[0]} - ${formatted[1]}`
                }
            }
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
            updateLatLong(suggestion) {


                if (this.place.latlng !== suggestion.latlng) {
                    this.place.latlng = suggestion.latlng
                }

            },
        }

    }
</script>

<style scoped>
    .ap-input1.ap-input {
        border-color: #ff0d47;

    }




</style>
