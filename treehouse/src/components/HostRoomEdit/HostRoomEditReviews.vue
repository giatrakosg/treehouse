<template>

    <v-list height="669px" style="overflow: auto;border-radius: 8px;padding-top: 0px" elevation="2" three-line>

        <v-card-title

                style="position: sticky;top: 0;background-color: white;z-index: 1"
        >

            Reviews
            <v-rating style="display:inline-flex;margin-left: 20px;"
                      half-increments
                      v-model="rating"
                          readonly
                          dense
                ></v-rating>
                <label style="margin-left: 20px;font-size: 13px;">({{reviews.length}})</label>
                <v-spacer/>

            </v-card-title>
            <template v-for="(item,index) in reviews">
                <RoomReview v-bind:key="index"
                            avatar="https://cdn.vuetifyjs.com/images/lists/2.jpg"
                            username="John"
                            v-bind:content="item.description"
                            v-bind:title="item.title"
                            v-bind:rating="item.rating"
                />

                <v-divider v-bind:key="index+reviews.length"/>

            </template>
        </v-list>


</template>

<script>
    import RoomReview from "../RoomInfo/RoomReview";

    export default {
        name: "HostRoomEditReviews",
        components: {RoomReview},
        props: ['reviews', 'rating'],
        data: () => ({})
    }
</script>

<style scoped>

</style>