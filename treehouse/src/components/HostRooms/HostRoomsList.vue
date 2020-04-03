<template>

        <v-list height="800px" style="overflow: auto;border-radius: 8px;padding-top: 0px" elevation="2" three-line>

            <v-card-title

                    style="position: sticky;top: 0;background-color: white;z-index: 1"
            >

                Rooms

                <label style="margin-left: 20px;font-size: 13px;">(1000)</label>
                <v-spacer/>
                <v-tooltip top color="primary">
                    <template v-slot:activator="{ on }">
                        <v-btn color="primary" :ripple="false" v-on="on" >
                            <v-icon small style="padding-right: 5px" class="fas fa-plus"></v-icon>

                        </v-btn>
                    </template>
                    Add New Room
                </v-tooltip>
            </v-card-title>
            <template v-for="(item,index) in rooms">
                <HostRoomsListItem v-bind:key="index" />
                <v-divider v-bind:key="index+rooms.length"/>

            </template>
        </v-list>

</template>

<script>
    import HostRoomsListItem from "./HostRoomsListItem";
    export default {
        name: "HostRoomsList",
        props:['rooms'],
        components: {HostRoomsListItem},
        data: () => ({


        }),
    }
</script>

<style scoped>

</style>