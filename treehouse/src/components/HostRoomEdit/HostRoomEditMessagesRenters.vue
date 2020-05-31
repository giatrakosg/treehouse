<template>
    <v-list three-line dense style="overflow: auto;height: 635px;border-right: groove">

        <h3 style="text-align: center;position: sticky;top: -10px;background-color: white;z-index: 1;"
        >Renters</h3>
        <v-divider/>
        <template v-for="(item, index) in threads">
            <div :key="index">
                <v-list-item @click="getMessages(item)" :ripple="false"


                >
                    <v-list-item-avatar>
                        <v-img src="https://cdn.vuetifyjs.com/images/lists/1.jpg"></v-img>
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
        name: "HostRoomEditMessagesRenters",
        props: ['threads'],
        methods: {
            getMessages(item) {
                item.last_message.is_read = true;
                this.$emit('get-messages', item.id)
            }
        }

    }
</script>

<style scoped>

</style>