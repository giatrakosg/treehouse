<template>
    <v-footer

            padless
    >
        <v-card
                flat
                tile
                width="100%"
                class="indigo lighten-1 white--text text-center"
                color="brown"
        >
            <v-card-text>
                <v-btn
                        v-for="item in items"
                        :key="item.link"
                        class="mx-4 white--text"
                        icon
                        :href="item.link"
                        target="_blank"
                >
                    <v-icon size="24px">{{ item.icon }}</v-icon>
                </v-btn>
            </v-card-text>

            <v-card-text class="white--text pt-0">
                I always wanted a treehouse
                somewhere to escape
                to a world that might someday be
                something like
                those fantasy books I'd read.

                A place where magical creatures might finally approach me
                and take to me on an adventure
                And my life would finally begin.
            </v-card-text>

            <v-divider></v-divider>

            <v-card-text class="white--text">
                {{ new Date().getFullYear() }} Ⓒ— <strong>Gregory George</strong>
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
    export default {
        name: "Footer",
        data: () => ({
            items: [
                {link: 'https://www.facebook.com/groups/di.uoa/', icon: 'mdi-facebook'},
                {link: 'https://github.com/giatrakosg/treehouse', icon: 'mdi-github'},
                {link: 'https://www.youtube.com/watch?v=9D05ej8u-gU', icon: 'mdi-instagram'},
                {link: 'https://www.youtube.com/watch?v=GDs_aOMkzM8', icon: 'mdi-youtube'}

            ],
        }),
    }
</script>

<style scoped>

</style>