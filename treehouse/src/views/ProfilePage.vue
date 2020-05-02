<template lang="html">
    <v-layout row>
        <v-flex sm3 md3 lg3>
            <ProfileInfoCard />
        </v-flex>
        <v-flex sm1 md1 lg1>
            <v-spacer></v-spacer>
        </v-flex>
        <v-flex sm8 md8 lg8>
            <v-card>
                <v-card-title>
                    Hi , I am Ali Conners
                </v-card-title>
                <v-card-subtitle>
                    Member since 2018.
                </v-card-subtitle>
                <v-divider></v-divider>
                <v-card-title>
                    3 Reviews
                </v-card-title>
                <v-card-text>

                    <v-list three-line>
                      <template v-for="(item, index) in items">
                        <v-subheader
                          v-if="item.header"
                          :key="item.header"
                          v-text="item.header"
                        ></v-subheader>

                        <v-divider
                          v-else-if="item.divider"
                          :key="index"
                          :inset="item.inset"
                        ></v-divider>

                        <v-list-item
                          v-else
                          :key="item.title"

                        >
                          <v-list-item-avatar>
                            <v-img :src="item.avatar"></v-img>
                          </v-list-item-avatar>

                          <v-list-item-content>
                            <v-list-item-title v-html="item.title"></v-list-item-title>
                            <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                          </v-list-item-content>
                        </v-list-item>
                      </template>
                    </v-list>
                </v-card-text>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
import ProfileInfoCard from "../components/Profile/ProfileInfoCard.vue"
export default {
    name : 'ProfilePage' ,
    components : {
        ProfileInfoCard
    },
    data: () => ({
      items: [
        { header: 'Today' },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Brunch this weekend?',
          subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Birthday gift',
          subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Recipe to try',
          subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
        },
      ],
    }),
}
</script>

<style lang="css" scoped>
</style>
