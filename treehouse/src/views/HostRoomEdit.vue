<template>
    <v-container>
        <v-row>
            <v-col>

            </v-col>
            <v-spacer/>
        </v-row>
        <v-divider></v-divider>
        <v-row dense align="center">
            <v-col cols="12" md="12" lg="6" xl="4" order-lg="1" order-xl="1">
                <HostRoomEditImages/>
            </v-col>

            <v-col cols="12" md="12" lg="12" xl="4" order-lg="3" order-xl="2">
                <HostRoomEditDescription/>
            </v-col>
            <v-col cols="12" md="12" lg="6" xl="4" order-lg="2" order-xl="3">
                <HostRoomEditMap/>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12" lg="6">
                <HostRoomEditReviews/>
            </v-col>
            <v-col cols="12" lg="6">
                test
            </v-col>

        </v-row>
    </v-container>
</template>

<script>
    import HostRoomEditDescription from "../components/HostRoomEdit/HostRoomEditDescription";
    import HostRoomEditImages from "../components/HostRoomEdit/HostRoomEditImages";
    import HostRoomEditMap from "../components/HostRoomEdit/HostRoomEditMap";
    import HostRoomEditReviews from "../components/HostRoomEdit/HostRoomEditReviews";

    export default {
        name: "HostRoomEdit",
        components: {HostRoomEditReviews, HostRoomEditMap, HostRoomEditImages, HostRoomEditDescription}
    }
</script>

<style scoped>

</style>