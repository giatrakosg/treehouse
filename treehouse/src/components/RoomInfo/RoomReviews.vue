<template>
    <v-container>
        <v-list height="600px" style="overflow: auto;border-radius: 8px;padding-top: 0px" elevation="2" three-line>

            <v-card-title

                    style="position: sticky;top: 0;background-color: white;z-index: 1"
            >

                Reviews
                <v-rating style="display:inline-flex;margin-left: 20px;"
                          half-increments
                          v-model="room.rating"
                          readonly
                          dense
                ></v-rating>
                <label style="margin-left: 20px;font-size: 13px;">{{reviews.length}} reviews</label>
                <v-spacer/>
                <v-btn color="primary" @click="onOpenReviewForm">
                    <v-icon class="fas fa-edit"></v-icon>
                    Write a Review
                </v-btn>
            </v-card-title>
            <template v-for="(item,index) in reviews">
                <RoomReview v-bind:key="index"
                            avatar="https://cdn.vuetifyjs.com/images/lists/2.jpg"
                            v-bind:username="item.user_name"
                            v-bind:content="item.description"
                            v-bind:title="item.title"
                            v-bind:rating="item.rating"

                />
                <v-divider v-bind:key="index+reviews.length"/>

            </template>
        </v-list>
        <v-dialog v-model="show_review_form" width="500px"  >
            <RoomReviewForm
                    @close-review-form="onCloseReviewForm"/>
        </v-dialog>
    </v-container>

</template>

<script>
    import RoomReview from "./RoomReview";
    import RoomReviewForm from "./RoomReviewForm";

    export default {
        components: {RoomReviewForm, RoomReview},
        data: () => ({

            show_review_form: false,

        }),
        methods: {

            onCloseReviewForm() {
                this.show_review_form = false;
            },
            onOpenReviewForm() {
                if (this.$store.state.isLoggedIn) {
                    this.show_review_form = true
                } else {
                    //ok
                }
            }
        },
        computed: {
            reviews() {
                return this.$store.state.reviews
            },
            room() {
                return this.$store.state.room
            }
        },
        async created() {
            await this.$store.dispatch('getReviews')

        }

    }
</script>

<style scoped>

</style>