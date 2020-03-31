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
                <label style="margin-left: 20px;font-size: 13px;">1000 reviews</label>
                <v-spacer/>
                <v-btn color="primary" @click="show_review_form=true">
                    <v-icon class="fas fa-edit"></v-icon>
                    Write a Review
                </v-btn>
            </v-card-title>
            <template v-for="(item,index) in reviews">
                <RoomReview v-bind:key="index"
                            v-bind:avatar="item.avatar"
                            v-bind:username="item.username"
                            v-bind:content="item.description"
                            v-bind:title="item.title"
                            v-bind:rating="item.rating"
                />
                <v-divider v-bind:key="index+reviews.length"/>

            </template>
        </v-list>
        <v-dialog v-model="show_review_form" max-width="30%">
            <RoomReviewForm
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
        data: () => ({
            reviews: [

                {
                    username: 'John',
                    avatar: require('../../assets/anonymous_user_96.png'),
                    rating: 4,
                    title: 'Brunch this weekend?',
                    description: " I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },

                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ',
                    description: "  Wish I could come, but I'm out of town this weekend.",
                },
                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    description: "I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },

                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ ',
                    description: " Wish I could come, but I'm out of town this weekend.",
                },

                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    description: "Do you have Paris recommendations? Have you ever been?",
                },

                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    description: "Have any ideas about what we should get Heidi for her birthday?",
                },

                {
                    username: 'John',
                    rating: 4,
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    description: " We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                },
            ],
            rating: 5,
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