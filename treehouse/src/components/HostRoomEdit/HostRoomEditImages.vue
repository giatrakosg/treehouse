<template>
    <v-container>
        <v-row dense>
            <v-col class="d-inline-flex ">
                <v-img style="border-radius: 8px 8px 0 0" class="fade" @click="dialog=true" width="200px"
                       max-width="528px" height="350px"
                       src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-col>
        </v-row>
        <v-row justify="start" dense>
            <v-col class="hidden-sm-and-down" cols="auto">
                <v-img class="fade" @click="dialog=true" width="260px"
                       src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-col>

            <v-col class="hidden-sm-and-down">
                <v-img class="fade" @click="dialog=true" width="260px"
                       src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-col>

        </v-row>
        <v-row justify="start" dense>
            <v-col class="hidden-sm-and-down" cols="auto">
                <v-img class="fade" @click="dialog=true" width="260px" style="border-radius: 0 0 0 8px"
                       src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-col>

            <v-col class="hidden-sm-and-down">
                <v-img class="fade" @click="dialog=true" width="260px" style="border-radius: 0 0 8px 0"
                       src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-col>

        </v-row>


        <v-dialog v-model="dialog" max-width="70%">
            <v-card>

                <v-container style="overflow: auto;max-height: 500px">
                    <v-row align="center">
                        <v-col cols="12" sm="12" lg="4" v-for="(image,index) in items" v-bind:key="index">
                            <v-img :src="image" contain style="border-radius: 8px"
                                   @click="showImage(image)"
                                   draggable="true"
                                   @dragstart="startDrag($event,image)"
                                   @drop="onDrop($event,image)"
                                   @dragover.prevent
                                   @dragenter.prevent

                            >

                                <v-btn fab color="primary" x-small style="float: right" class="ma-1"
                                       @click.stop.prevent="removeImage(index)">
                                    <v-icon>mdi-minus</v-icon>
                                </v-btn>

                            </v-img>
                            <v-dialog v-model="show_image">
                                <v-img :src="image_to_show"></v-img>
                            </v-dialog>

                        </v-col>
                    </v-row>

                </v-container>

                <v-card-actions>
                    <v-spacer style="width: 14%"/>
                    <v-tooltip top color="primary">
                        <template v-slot:activator="{ on }">
                            <input type="file" ref="file" style="display: none">
                            <v-btn color="primary" v-on="on" @click="$refs.file.click()">
                                <v-icon>mdi-plus</v-icon>
                            </v-btn>
                        </template>
                        Add Image
                    </v-tooltip>
                    <v-spacer></v-spacer>

                    <v-btn color="primary" @click="dialog = false">Save</v-btn>
                    <v-btn color="green darken-1" text @click="dialog = false">Cancel</v-btn>

                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
    export default {
        name: "HostRoomEditImages",
        data: function () {
            return {
                dialog: false,
                first_image: 3,
                show_image: false,
                image_to_show: '',
                items: [
                    "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg",
                    "https://cdn.vuetifyjs.com/images/carousel/sky.jpg",
                    "https://cdn.vuetifyjs.com/images/carousel/bird.jpg",
                    "https://cdn.vuetifyjs.com/images/carousel/planet.jpg",
                ]
            }
        },
        methods: {
            showImage(img) {
                this.show_image = true;
                this.image_to_show = img;
            },
            removeImage(index) {
                this.items.splice(index, 1);
            },
            ShowAlert() {
                this.dialog = true;
            },
            startDrag: (evt, src) => {


                evt.dataTransfer.setData('src', src);


            },
            onDrop(evt, drop_src) {
                let src = evt.dataTransfer.getData('src');


                let index_to = this.items.indexOf(drop_src);

                let index_from = this.items.indexOf(src);

                this.items.splice(index_from, 1);
                this.items.splice(index_to, 0, src);


            }
        }
    }
</script>

<style scoped>
    .fade:hover {
        filter: brightness(85%);
        cursor: pointer;
    }
</style>