<template>
    <v-container fluid class="grid-list-lg "  >
        <v-layout   >
            <v-flex   class="d-inline-flex ">
                 <v-img  style="border-radius: 8px 0px 0px 8px" class="fade" @click="dialog=true"  width="500px" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                </v-img>
            </v-flex>
            <v-flex  >
                <v-layout  >
                    <v-flex  class="hidden-sm-and-down" >
                         <v-img class="fade" @click="dialog=true" width="270px"   src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                        </v-img>
                    </v-flex>
                </v-layout>
                <v-layout   >
                    <v-flex  class="hidden-sm-and-down">
                         <v-img  class="fade" @click="dialog=true" width="270px"    src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                        </v-img>
                    </v-flex>
                </v-layout>
            </v-flex>
            <v-flex  >
                <v-layout  >
                    <v-flex  class="hidden-sm-and-down" >
                         <v-img class="fade" @click="dialog=true" width="270px"  style="border-radius: 0px 8px 0px 0px" src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                        </v-img>
                    </v-flex>
                </v-layout>
                <v-layout   >
                    <v-flex  class="hidden-sm-and-down">
                         <v-img  class="fade" @click="dialog=true" width="270px"  style="border-radius: 0px 0px 8px 0px"  src="https://cdn.vuetifyjs.com/images/cards/docks.jpg">
                        </v-img>
                    </v-flex>
                </v-layout>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" max-width="50%" >
          <v-card>
               <v-carousel v-model="first_image">
                <v-carousel-item
                  v-for="(item,i) in items"
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
        data:function(){
            return {
                dialog:false,
                first_image:3,
                items:[
                    {
                        src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
                    },
                    {
                     src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
                    },
                    {
                     src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
                    },
                    {
                     src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
                    },
                ]
            }
        },
        methods:{
            ShowAlert(){
                this.dialog=true;
            }
        }
    }
</script>

<style scoped>

    .fade:hover {
           filter:brightness(85%);
            cursor: pointer;
    }

</style>