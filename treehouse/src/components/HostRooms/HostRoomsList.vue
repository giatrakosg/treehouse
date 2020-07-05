<template>

    <v-list height="800px" style="overflow: auto;border-radius: 8px;padding-top: 0" elevation="0" three-line
            id="#list"
    >

        <v-card-title style="position: sticky;top: 0;background-color: white;z-index: 1">

            <h3>Rooms</h3>
            <label style="margin-left: 20px;font-size: 13px;">({{rooms.length}})</label>
            <v-spacer/>
            <v-text-field v-model="search_title" label="Search Room" prepend-icon="mdi-magnify"/>
            <v-spacer/>
            <v-spacer/>
            <v-tooltip top color="primary">
                <template v-slot:activator="{ on }">
                    <v-btn color="primary" :ripple="false" v-on="on"
                           :to="{name:'HostRoomEdit',params:{room_id:-1}}">
                        <v-icon>mdi-plus</v-icon>

                    </v-btn>
                </template>
                Add New Room
            </v-tooltip>
        </v-card-title>
        <template v-for="(item,index) in rooms">

            <HostRoomsListItem :key="index" :room="item" :id="'#room'+'_'+index"/>


        </template>
    </v-list>

</template>

<script>
    import HostRoomsListItem from "./HostRoomsListItem";


    export default {
        name: "HostRoomsList",
        components: {HostRoomsListItem},
        data: () => ({
            display_rooms: [],
            search_title: ''
        }),
        computed: {
            rooms() {

                return this.$store.state.rooms.filter(room => room.title.toLowerCase().search(this.search_title.toLowerCase()) !== -1)
            }
        },

        mounted() {
            this.$root.$on('scroll-to-room', (index) => {
                document.getElementById("#list").scroll(0, index * 232)

            });
        }

    }
</script>

<style scoped>

</style>