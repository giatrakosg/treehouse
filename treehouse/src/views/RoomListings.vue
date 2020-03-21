<template>
    <v-container>
     <v-row >
           <v-col>
              <h2>Search Results</h2>
           </v-col>
       </v-row>
        <v-row>
            <RoomsList/>
        </v-row>
    </v-container>
</template>

<script>
    import RoomsList from "../components/RoomListings/RoomsList";
    export default {
        name: "RoomListings",
        components: {RoomsList}
    }
</script>

<style scoped>

</style>