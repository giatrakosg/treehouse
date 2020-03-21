<template >
    <v-container  >
        <v-row    align="center" dense>
            <v-col>
             <Options />
            </v-col>
        </v-row>
        <v-divider></v-divider>

        <v-row>
            <v-col >
                 <RoomsList />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import RoomsList from "../components/RoomListings/RoomsList";
    import Options from "../components/RoomListings/Options";
    export default {
        name: "RoomListings",
        components: {Options, RoomsList}
    }
</script>

<style scoped>
     .sticky {
        background: white;

        position: fixed;
         z-index: 2;
        }
</style>