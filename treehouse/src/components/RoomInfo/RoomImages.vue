<template>
    <v-container class="grid-list-lg">

        <v-layout>
            <v-flex class="d-inline-flex ">
                <v-img v-if="images[0]===undefined || images[0]===null" style="border-radius: 8px 8px 0 0" class="fade"
                       @click="openAllImages(0)"
                       width="490px"
                       height="450px"
                       :src="require('../../assets/empty_thumbnail.png')">
                </v-img>
                <v-img v-else style="border-radius: 8px 0 0 8px" class="fade" @click="openAllImages(0)" width="490px"
                       height="450px"
                       :src="images[0].src">
                </v-img>
            </v-flex>
            <v-flex>
                <v-layout>
                    <v-flex class="hidden-sm-and-down">
                        <v-img v-if="images[1]===undefined || images[1]===null" style="border-radius: 8px 8px 0 0"
                               class="fade" @click="openAllImages(0)"
                               width="245px" height="217px"
                               :src="require('../../assets/empty_thumbnail.png')">
                        </v-img>
                        <v-img v-else class="fade" @click="openAllImages(1)" width="245px" height="217px"
                               :src="images[1].src">
                        </v-img>
                    </v-flex>
                </v-layout>
                <v-layout>
                    <v-flex class="hidden-sm-and-down">
                        <v-img v-if="images[2]===undefined || images[2]===null" style="border-radius: 8px 8px 0 0"
                               class="fade" @click="openAllImages(0)"
                               width="245px" height="217px"
                               :src="require('../../assets/empty_thumbnail.png')">
                        </v-img>
                        <v-img v-else class="fade" @click="openAllImages(2)" width="245px" height="217px"
                               :src="images[2].src">
                        </v-img>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex>
                <v-layout>
                    <v-flex class="hidden-sm-and-down">
                        <v-img v-if="images[3]===undefined || images[3]===null" style="border-radius: 8px 8px 0 0"
                               class="fade" @click="openAllImages(0)"
                               width="245px" height="217px"
                               :src="require('../../assets/empty_thumbnail.png')">
                        </v-img>
                        <v-img v-else class="fade" @click="openAllImages(3)" width="245px" height="217px"
                               style="border-radius: 0 8px 0 0"
                               :src="images[3].src">
                        </v-img>
                    </v-flex>
                </v-layout>
                <v-layout>
                    <v-flex class="hidden-sm-and-down">
                        <v-img v-if="images[4]===undefined || images[4]===null" style="border-radius: 8px 8px 0 0"
                               class="fade" @click="openAllImages(0)"
                               width="245px" height="217px"
                               :src="require('../../assets/empty_thumbnail.png')">
                        </v-img>
                        <v-img v-else class="fade" @click="openAllImages(4)" width="245px" height="217px"
                               style="border-radius: 0 0 8px 0"
                               :src="images[4].src">
                        </v-img>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" max-width="50%">
            <v-card>
                <v-carousel v-model="first_image">
                    <v-carousel-item
                            v-for="(item,i) in images"
                            :key="i"
                            :src="item.src"

                    ></v-carousel-item>
                </v-carousel>

                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="green darken-1" text @click="dialog = false">Close</v-btn>

                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>

<script>
    export default {
        name: "RoomImages",
        data: function () {
            return {
                dialog: false,
                first_image: 3,
                loaded: false

            }
        },

        methods: {
            openAllImages(index) {
                this.dialog = true;
                this.first_image = index;
            }
        },
        computed: {
            images() {
                return this.$store.state.room.images
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