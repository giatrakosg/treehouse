<template>
    <v-container>
        <v-list height="600px" style="overflow: auto;border-radius: 8px;padding-top: 0px" elevation="2" three-line>

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
                <label style="margin-left: 20px;font-size: 13px;">{{reviews.length}} reviews</label>
                <v-spacer/>
                <v-btn color="primary" @click="show_review_form=true">
                    <v-icon class="fas fa-edit"></v-icon>
                    Write a Review
                </v-btn>
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
        <v-dialog v-model="show_review_form" width="500px"  >
            <RoomReviewForm
                    :room_title="room_title"
                    @new-review="onNewReview"
                    @close-review-form="onCloseReviewForm"/>
        </v-dialog>
    </v-container>

</template>

<script>
    import RoomReview from "./RoomReview";
    import RoomReviewForm from "./RoomReviewForm";

    export default {
        components: {RoomReviewForm, RoomReview},
        props: ['reviews', 'rating', 'room_title'],
        data: () => ({

            show_review_form: false,

        }),
        methods: {
            onNewReview(review) {
                this.show_review_form = false;
                console.log(review);

                this.reviews.push(review);
            },
            onCloseReviewForm() {
                this.show_review_form = false;
            }
        }
    }
</script>

<style scoped>

</style>