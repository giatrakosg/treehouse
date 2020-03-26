<template>
     <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title >
                <h2>Awesome room</h2>
            </v-list-item-title>
            <v-list-item-subtitle>
                <v-rating style="display:inline-flex"
                  half-increments
                  v-model="rating"
                  readonly
                    dense
                > </v-rating>
                 <label style="margin-left: 20px;font-size: 13px;">(1000 reviews)</label>
            </v-list-item-subtitle>
          </v-list-item-content>
     </v-list-item>
</template>

<script>
    export default {
        name: "RoomTitle",
        data:function (){
            return {
                rating:3.5
            }
        }
    }
</script>

<style scoped>

</style>