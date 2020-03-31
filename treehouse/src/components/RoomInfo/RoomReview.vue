<template>
    <v-list-item>
        <v-list-item-avatar>


            <v-img :src="avatar">

            </v-img>

        </v-list-item-avatar>

        <v-list-item-content>
            <v-list-item-title>
                {{username}}
                <v-rating :value="rating"
                          readonly
                          half-increments
                          small
                          dense
                          style="display: inline-block"></v-rating>

            </v-list-item-title>
            <h4>{{title}}</h4>
            <v-list-item-subtitle v-html="content">

            </v-list-item-subtitle>
        </v-list-item-content>

    </v-list-item>
</template>

<script>
    export default {
        name: "RoomReview",
        props: ['username', 'title', 'rating', 'content', 'avatar'],

    }
</script>

<style scoped>

</style>