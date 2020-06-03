<template>
    <v-container>
        <v-row>
            <v-list-item style="border-bottom:groove">
                <v-list-item-avatar size="55">
                    <img
                            src="https://cdn.vuetifyjs.com/images/john.jpg"
                            alt="John"

                    >
                </v-list-item-avatar>
                <v-list-item-title>
                    <span>John</span>
                </v-list-item-title>
            </v-list-item>

        </v-row>
        <v-row>

            <v-list three-line dense style="overflow: auto;height: 450px;width: 100%;border-bottom: groove">
                <template v-for="(item,index) in items">


                    <v-list-item
                            v-if="item.user===0"
                            :key="item.name"
                            style="width: 340px;"
                            class="ma-1 mr-0 pa-0 ml-auto"


                    >

                        <v-list-item-action-text style="align-self: center">
                            <span>
                                 <v-icon size="17" @click="deleteMessage(index)">mdi-delete</v-icon>
                            </span>

                        </v-list-item-action-text>
                        <v-list-item-content class="pa-3"
                                             style="background-color: #33af58;font-size: 14px;border-radius: 12px;">


                                <span style="word-wrap:break-word;width: 100%;color: white ">
                                    {{item.text}}
                                </span>
                            <br/>
                            <span style="font-size:11px;text-align: end;color: white">

                                {{item.time}}
                            </span>

                        </v-list-item-content>


                    </v-list-item>
                    <v-list-item
                            class="pa-0 "
                            v-else
                            :key="item.name"
                            style="width: 340px; "


                    >

                        <v-list-item-content class="pa-3"
                                             style="background-color: #e7eaed;font-size: 14px;border-radius: 12px;">


                                <span style="word-wrap:break-word;width: 100%; ">
                                    {{item.text}}
                                </span>
                            <br/>
                            <span style="font-size:11px;text-align: end">

                                {{item.time}}
                            </span>

                        </v-list-item-content>
                        <v-list-item-action-text style="align-self: center;">
                            <v-icon size="17" @click="deleteMessage(index)">mdi-delete</v-icon>

                        </v-list-item-action-text>

                    </v-list-item>
                </template>
            </v-list>


        </v-row>
        <v-row align="center">
            <v-col cols="10">
                <v-textarea hide-details dense no-resize outlined rows="3" v-model="message"></v-textarea>
            </v-col>
            <v-col cols="2">
                <v-icon v-on:click="pushMessage" color="#a1795a" size="50px">mdi-send</v-icon>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import moment from 'moment'

    export default {

        name: "Messages",
        data: () => ({
            message: '',
            items: [
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 1,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 1,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 1,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },
                {
                    text: 'Ill be in your neisdasdasdasdasdasdasdasdasdasdasdghborhood doing errands this weekend. Do you want to hang out?',
                    user: 0,
                    time: moment().format("DD/MM/YYYY - hh:mm")
                },


            ],
        }),
        methods: {
            pushMessage() {
                if (this.message !== '' && this.message !== null) {
                    this.items.push({text: this.message, user: 0, time: moment().format("DD/MM/YYYY - hh:mm")})
                }
            },
            deleteMessage(index) {

                this.items.splice(index, 1);
            }
        }
    }
</script>

<style scoped>


</style>