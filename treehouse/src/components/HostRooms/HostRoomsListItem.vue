<template>
    <v-list-item :to="{name:'HostRoomEdit',params:{room_id:room.id}}"
                 v-on:mouseover="$root.$emit('highlight',$vnode.key)"
                 v-on:mouseleave="$root.$emit('default',$vnode.key)">
        <v-list-item-avatar tile size="200px" width="300px">

            <v-img v-if="room.thumbnail===''" style="border-radius: 8px 8px 0 0"

                   :src="require('../../assets/empty_thumbnail.png')">
            </v-img>
            <v-img v-else style="border-radius: 8px" :src="room.thumbnail">

            </v-img>

        </v-list-item-avatar>

        <v-list-item-content>
            <v-list-item-title>
                <h3>{{room.title}}</h3>
            </v-list-item-title>

            <v-row align="center">
                <v-col cols="auto">
                    <v-rating style="display:inline-flex;"
                              half-increments
                              v-model="room.rating"
                              readonly
                              dense
                              size="30px"

                    ></v-rating>
                </v-col>
                <v-col cols="auto">
                    <label>({{room.reviews_number}})</label>
                </v-col>


            </v-row>
            <v-chip-group column>

                <v-tooltip top color="blue">
                    <template v-slot:activator="{ on }">
                        <v-chip color="blue" style="color: white" v-ripple="false" v-on="on">
                            <label style="font-size: 16px"> €/day:{{room.cost_per_day}}</label>
                        </v-chip>
                    </template>
                    Cost per day
                </v-tooltip>
            </v-chip-group>
            <div>
                <v-icon>mdi-map-marker</v-icon>
                <label style="font-size: 20px">{{room.address}}</label>
            </div>

        </v-list-item-content>

    </v-list-item>
</template>

<script>
    export default {
        name: "HostRoomsListItem",
        props: ['room'],
        data: () => ({}),
        created() {
            console.log(this.room)
        }


    }
</script>

<style scoped>
    .v-slide-group__next {
        width: 20px;
    }
</style>