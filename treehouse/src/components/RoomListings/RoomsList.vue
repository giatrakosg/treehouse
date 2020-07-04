<template>
    <v-container>
        <v-row v-if="empty" justify="center" align="center">
            <v-spacer/>
            <v-col cols="auto">
                <span style="color: #86989B;font-size: 40px">No Results</span>
            </v-col>
            <v-spacer/>
        </v-row>
        <div v-else>
            <v-pagination
                    v-if="pages_number>1"
                    v-model="page"
                    :length="this.pages_number"
                    total-visible="5"
            >

            </v-pagination>
            <v-row>
                <v-col cols="12" sm="4" md="3" lg="3" v-for="(item,index) in page_rooms[page-1]" :key="index">

                    <RoomCard v-bind:type="rooms[(page-1)*12+item-1].type"
                              v-bind:title="rooms[(page-1)*12+item-1].title"
                              v-bind:rating="rooms[(page-1)*12+item-1].rating"
                              v-bind:beds_number="rooms[(page-1)*12+item-1].beds_number"
                              v-bind:cost_per_day="rooms[(page-1)*12+item-1].cost_per_day"
                              v-bind:image_src="rooms[(page-1)*12+item-1].image_src"
                              v-bind:id="rooms[(page-1)*12+item-1].id"
                              v-bind:reviews_number="rooms[(page-1)*12+item-1].reviews_num"
                    />
                </v-col>
            </v-row>

            <v-pagination
                    v-if="pages_number>1"
                    v-model="page"
                    :length="this.pages_number"
                    total-visible="5">

            </v-pagination>
        </div>


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
                empty: false,
            }

        },
        created() {

        },
        watch: {
            rooms: function () {

                if (this.rooms.length === 0) {
                    this.empty = true;
                    return;
                } else {
                    this.empty = false;
                }


                this.page_rooms = [];

                let rem;

                let total_rooms = this.rooms.length;


                rem = total_rooms % this.max_rooms_per_page;

                this.pages_number = Math.ceil(total_rooms / this.max_rooms_per_page);

                let i;


                for (i = 0; i < this.pages_number - 1; i++) {
                    this.page_rooms.push(12);
                }
                if (rem > 0) {
                    this.page_rooms.push(rem);

                } else if (rem === 0) {
                    this.page_rooms.push(12);
                }

            },

        }

    }
</script>

<style scoped>

</style>
