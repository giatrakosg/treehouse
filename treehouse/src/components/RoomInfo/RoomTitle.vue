<template>
    <v-list-item three-line>
        <v-list-item-content>
            <v-list-item-title>
                <h2>{{title}}</h2>
            </v-list-item-title>
            <v-list-item-subtitle>
                <v-row dense align="center">
                    <v-col cols="auto">
                        <v-rating style="display:inline-flex;"
                                  half-increments
                                  v-model="rating"
                                  readonly
                                  dense
                                  size="20px"
                        ></v-rating>

                        <label style="margin-left: 20px;">({{reviews_number}})</label>
                    </v-col>
                    <v-col cols="auto">
                        <label style="padding-left: 20px">Host: </label>
                        <v-tooltip top color="brown">
                        <template v-slot:activator="{ on }">

                        <v-btn color="brown" text to="/"  v-ripple="false" class="text-capitalize" v-on="on">
                            John
                            <i class="fas fa-external-link-square-alt "></i>
                        </v-btn>
                        </template>
                             Contact
                        </v-tooltip>

                    </v-col>
                </v-row>


            </v-list-item-subtitle>


        </v-list-item-content>

    </v-list-item>
</template>

<script>
    export default {
        name: "RoomTitle",
        props: ['title', 'rating', 'reviews_number'],
        data: function () {
            return {}
        }
    }
</script>

<style scoped>

</style>