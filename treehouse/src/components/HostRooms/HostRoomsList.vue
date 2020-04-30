<template>

    <v-list height="800px" style="overflow: auto;border-radius: 8px;padding-top: 0px" elevation="0" three-line
            ref="list">

        <v-card-title style="position: sticky;top: 0;background-color: white;z-index: 1">

            <h3>Rooms</h3>
            <label style="margin-left: 20px;font-size: 13px;">({{rooms.length}})</label>
            <v-spacer/>
            <v-text-field label="Search Room" prepend-icon="mdi-magnify" @input="searchRoom($event)"/>
            <v-spacer/>
            <v-spacer/>
            <v-tooltip top color="primary">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" :ripple="false" v-on="on"
                           :to="{name:'HostRoomEdit',params:{room_title:'New_Room'}}">
                        <v-icon>mdi-plus</v-icon>

                    </v-btn>
                </template>
                Add New Room
            </v-tooltip>
        </v-card-title>
        <template v-for="(item,index) in display_rooms">

            <HostRoomsListItem :key="index" :room="item"/>


        </template>
    </v-list>

</template>

<script>
    import HostRoomsListItem from "./HostRoomsListItem";

    export default {
        name: "HostRoomsList",
        props: ['rooms'],
        components: {HostRoomsListItem},
        data: () => ({
            display_rooms: []
        }),
        watch: {
            rooms() {
                console.log(this.rooms);
                this.display_rooms = this.rooms
            }
        },
        methods: {
            searchRoom(str) {
                console.log(str);
                this.display_rooms = [];
                for (let i of this.rooms) {
                    if (i.title.toLowerCase().search(str.toLowerCase()) !== -1) {
                        this.display_rooms.push(i)
                    }
                }

            }
        }

    }
</script>

<style scoped>

</style>