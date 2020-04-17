<template>
    <v-container>


        <v-pagination
                v-if="pages_number>1"
                v-model="page"
                :length="this.pages_number">

        </v-pagination>
        <v-row>
            <v-col cols="12" sm="4" md="3" lg="3" v-for="(item,index) in page_rooms[page-1]" :key="index">

                <RoomCard v-bind:type="rooms[(page-1)*12+item-1].type"
                          v-bind:title="rooms[(page-1)*12+item-1].title"
                          v-bind:rating="rooms[(page-1)*12+item-1].rating"
                          v-bind:beds_number="rooms[(page-1)*12+item-1].beds_number"
                          v-bind:cost_per_day="rooms[(page-1)*12+item-1].cost_per_day"
                          v-bind:image_src="rooms[(page-1)*12+item-1].image_src"
                />
            </v-col>
        </v-row>

        <v-pagination
                v-if="pages_number>1"
                v-model="page"
                :length="this.pages_number">

        </v-pagination>

    </v-container>
</template>

<script>
    import RoomCard from "./RoomCard";

    export default {
        name: "RoomsList",
        components: {RoomCard},
        props: ['rooms'],
        data: function () {
            return {
                page: 1,
                max_rooms_per_page: 12,
                page_rooms: [],
                pages_number: 0,
                room: "test",


            }

        },
        created() {

        },
        watch: {
            rooms: function () {
                this.page_rooms = [];


                console.log("----------");
                console.log(this.rooms);

                let rem;
                let total_rooms = this.rooms.length;

                this.pages_number = Math.floor(total_rooms / this.max_rooms_per_page);
                rem = total_rooms % this.max_rooms_per_page;
                let i;

                for (i = 0; i < this.pages_number; i++) {
                    this.page_rooms.push(12);
                }
                if (rem > 0) {
                    this.page_rooms.push(rem);

                }

            },

        }

    }
</script>

<style scoped>

</style>