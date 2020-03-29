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
                <v-btn color="primary">
                    <v-icon class="fas fa-edit"></v-icon>
                    Write a Review
                </v-btn>
            </v-card-title>
            <template v-for="(item) in items">
                <RoomReview v-bind:key="item"
                            v-bind:avatar="item.avatar"
                            v-bind:subtitle="item.subtitle"
                            v-bind:title="item.title"/>
                <v-divider v-bind:key="item"/>
            </template>
        </v-list>
    </v-container>
</template>

<script>
    import RoomReview from "./RoomReview";
    export default {
        components: {RoomReview},
        data: () => ({
            items: [

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
                },

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
                },

                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                },
            ],
            rating: 5
        }),
    }
</script>

<style scoped>

</style>