<template>
    <v-list three-line dense style="overflow: auto;height: 635px;border-right: groove">

        <template v-for="(item, index) in threads">
            <div :key="index">
                <v-list-item @click="getMessages(item)" :ripple="false" style="align-items: center;display: -webkit-box"


                >
                    <v-list-item-avatar>
                        <v-img :src="item.profile"></v-img>
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>
                            <span style="font-size: 16px">{{item.username}}</span>
                        </v-list-item-title>
                        <v-list-item-subtitle>

                            <span>{{item.last_message.sender}}</span>
                            &mdash;
                            <span v-if="item.last_message.is_read" class='text--primary' style="font-weight: 400">
                           {{item.last_message.text}}
                            </span>
                            <span v-else class='text--primary' style="font-weight: 600">
                           {{item.last_message.text}}
                        </span>

                        </v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-action-text v-if="!item.last_message.is_read">
                            <span>
                                 <v-icon color="primary" size="22">mdi-circle-medium</v-icon>
                            </span>

                    </v-list-item-action-text>
                </v-list-item>
                <v-divider/>
            </div>


        </template>
    </v-list>

</template>

<script>
    export default {
        name: "MessageThreads",
        methods: {
            async getMessages(item) {
                item.last_message.is_read = true;

                await this.$store.dispatch('getThreadMessages', item)
                console.log(this.$store.state.current_thread)
            }
        },
        computed: {
            threads() {
                return this.$store.state.message_threads
            }
        }

    }
</script>

<style scoped>

</style>