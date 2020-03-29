<template>
    <v-container>
        <v-pagination
                v-model="page"
                :length="this.page_rows.length">

        </v-pagination>
        <v-row align-center justify="center" v-for="index in page_rows[page-1]" :key="index" wrap>
            <v-col cols="auto" v-for="index in page_cols[page-1]" :key="index">
                <RoomCard/>
            </v-col>
        </v-row>
        <v-pagination
                v-model="page"
                :length="this.page_rows.length">

        </v-pagination>
    </v-container>
</template>

<script>
    import RoomCard from "./RoomCard";

    export default {
        name: "RoomsList",
        components: {RoomCard},
        data: function () {
            return {
                page: 1,
                max_rooms_per_page: 12,
                total_rooms: 40,
                page_rows: [],
                page_cols: []
            }

        },
        created() {
            let pages_number, rem;

            pages_number = Math.floor(this.total_rooms / this.max_rooms_per_page);
            rem = this.total_rooms % this.max_rooms_per_page;
            let i;

            for (i = 0; i < pages_number; i++) {
                this.page_rows.push(3);
                this.page_cols.push(4);
            }
            if (rem > 0) {

                let rem_rows = Math.floor(rem / 4) + (rem % 4 != 0 ? 1 : 0);
                this.page_cols.push(4);
                this.page_rows.push(rem_rows);

            }

        }

    }
</script>

<style scoped>

</style>