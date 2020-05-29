<template lang="html">
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
</template>

<script>
export default {
    name : 'ReviewCard',
    data: () => (
        {
            items: [
              {
                avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                title: '5/5',
                subtitle: "<span class='text--primary'>Atticus Finch</span> &mdash; Ali is an excellent host . We were guests in her apt , and everything was beautiful . We only got bitten by rats once . The apt is filled with cute cockroaches <3",
              },
              { divider: true, inset: true },
              {
                avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                title: '5/5 ',
                subtitle: "<span class='text--primary'>Rowan Atkinson</span> &mdash; The apt is very close to a cemetery , which is always convenient .",
              },
              { divider: true, inset: true },
              {
                avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                title: '5/5',
                subtitle: "<span class='text--primary'>Bill Kilgore</span> &mdash; I love the smell of fresh Napalm in the morning!",
              },
            ],            
        }
    )

}
</script>

<style lang="css" scoped>
</style>
