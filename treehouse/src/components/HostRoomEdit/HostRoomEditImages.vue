<template>
    <v-container>
        <v-row dense>
            <v-col class="d-inline-flex ">
                <v-img v-if="images[0]===undefined || images[0]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="dialog=true" width="200px"
                       max-width="528px" height="350px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>

                <v-img v-else style="border-radius: 8px 8px 0 0" class="fade" @click="dialog=true" width="200px"
                       max-width="528px" height="350px"
                       :src="images[0].src">
                </v-img>
            </v-col>
        </v-row>
        <v-row justify="start" dense>
            <v-col class="hidden-sm-and-down" cols="auto">
                <v-img v-if="images[1]===undefined || images[2]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="dialog=true" width="260px" height="200px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>
                <v-img v-else class="fade" @click="dialog=true" width="260px" height="200px"
                       :src="images[1].src">
                </v-img>
            </v-col>

            <v-col class="hidden-sm-and-down">
                <v-img v-if="images[2]===undefined || images[2]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="dialog=true" width="260px" height="200px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>
                <v-img v-else class="fade" @click="dialog=true" width="260px" height="200px"
                       :src="images[2].src">
                </v-img>
            </v-col>

        </v-row>
        <v-row justify="start" dense>
            <v-col class="hidden-sm-and-down" cols="auto">
                <v-img v-if="images[3]===undefined || images[3]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="dialog=true"
                       width="260px" height="200px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>
                <v-img v-else class="fade" @click="dialog=true" width="260px" height="200px"
                       style="border-radius: 0 0 0 8px"
                       :src="images[3].src">
                </v-img>
            </v-col>

            <v-col class="hidden-sm-and-down">
                <v-img v-if="images[4]===undefined || images[4]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="dialog=true"
                       width="260px" height="200px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>
                <v-img v-else class="fade" @click="dialog=true" width="260px" height="200px"
                       style="border-radius: 0 0 8px 0"
                       :src="images[4].src">
                </v-img>
            </v-col>

        </v-row>


        <v-dialog v-model="dialog" max-width="70%">
            <v-card>

                <v-container style="overflow: auto;height:600px;">
                    <v-row align="center">
                        <v-col cols="12" sm="12" lg="4" v-for="(image,index) in tmp_images" v-bind:key="index">
                            <v-img :src="image.src" contain style="border-radius: 8px"
                                   @click="showImage(image.src)"
                                   draggable="true"
                                   @dragstart="startDrag($event,image.src)"
                                   @drop="onDrop($event,image.src)"
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

                    <v-btn style="position: sticky;top: 2;z-index: 3" color="primary" @click="saveImages">Save</v-btn>
                    <v-btn style="position: sticky;top: 2;z-index: 3" color="green darken-1" text
                           @click="dialog = false">Cancel
                    </v-btn>

                </v-card-actions>
            </v-card>

        </v-dialog>
    </v-container>
</template>

<script>
    export default {
        name: "HostRoomEditImages",
        props: ['images'],
        data: function () {
            return {
                dialog: false,
                first_image: 3,
                show_image: false,
                image_to_show: '',

                tmp_images: []

            }
        },
        watch: {

            dialog() {

                for (let i = 0; i < this.images.length; i++) {
                    this.tmp_images[i] = this.images[i]

                }


            }
        },
        methods: {
            showImage(img) {
                this.show_image = true;
                this.image_to_show = img;
            },
            removeImage(index) {
                this.tmp_images.splice(index, 1);
            },
            saveImages() {


                this.$emit('new-images', this.tmp_images);

                this.dialog = false
            },
            startDrag: (evt, src) => {


                evt.dataTransfer.setData('drag_src', src);


            },
            onDrop(evt, drop_src) {
                let drag_src = evt.dataTransfer.getData('drag_src');

                let index_to = this.tmp_images.findIndex(image => image.src === drop_src);


                let index_from = this.tmp_images.findIndex(image => image.src === drag_src);

                let image_from = this.tmp_images[index_from];

                this.tmp_images.splice(index_from, 1);
                this.tmp_images.splice(index_to, 0, image_from);


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