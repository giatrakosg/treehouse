<template>
    <v-list-item>
        <v-list-item-avatar>
            <v-img :src="avatar"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
            <v-list-item-title v-html="title"></v-list-item-title>
            <v-list-item-subtitle v-html="subtitle"></v-list-item-subtitle>
        </v-list-item-content>

    </v-list-item>
</template>

<script>
    export default {
        name: "RoomReview",
        props: ['title', 'avatar', 'subtitle']
    }
</script>

<style scoped>

</style>