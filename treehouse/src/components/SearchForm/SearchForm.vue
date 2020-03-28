<template>
    <v-card
            color="primary"
    >
        <v-card-title>
            Treehouse
        </v-card-title>
        <v-card-text>
            <v-form>
                <v-col cols="12" sm="6">
                    <v-date-picker v-model="dates" range color="blue" no-title></v-date-picker>
                </v-col>
            </v-form>
        </v-card-text>
    </v-card>

</template>

<script>
    export default {
        name: "SearchForm",
        data: () => ({
            picker: null,
            dates: [],

        }),
        computed: {
            dateRangeText() {
                return this.dates.join(' ~ ')
            },
        },

    }
</script>

<style scoped>

</style>
