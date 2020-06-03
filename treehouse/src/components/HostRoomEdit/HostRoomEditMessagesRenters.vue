<template>
    <v-list three-line dense style="overflow: auto;height: 635px;border-right: groove">
        <template v-for="(item, index) in items">
            <h3
                    v-if="item.header"
                    :key="item.header"
                    style="text-align: center;position: sticky;top: -10px;background-color: white;z-index: 1;"

            >{{item.header}}</h3>

            <v-divider
                    v-else-if="item.divider"
                    :key="index"
                    :inset="item.inset"
            ></v-divider>

            <v-list-item
                    v-else
                    :key="item.name"

            >
                <v-list-item-avatar>
                    <v-img :src="item.avatar"></v-img>
                </v-list-item-avatar>

                <v-list-item-content>
                    <v-list-item-title v-html="item.name"></v-list-item-title>
                    <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
        </template>
    </v-list>

</template>

<script>
    export default {
        name: "HostRoomEditMessagesRenters",
        data: () => ({
            items: [
                {header: 'Renters'},
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {divider: true, inset: false},
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    name: 'Ali Connors',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },

            ],
        }),
    }
</script>

<style scoped>

</style>