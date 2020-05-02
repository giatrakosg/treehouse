<template lang="html">
    <v-layout row>
        <v-flex sm1 md1 lg1>
            <v-spacer></v-spacer>
        </v-flex>
        <v-flex sm10 md10 lg10 >
            <ProfileInfoCard />
        </v-flex>
    </v-layout>

</template>

<script>
import ProfileInfoCard from "../components/Profile/ProfileInfoCard.vue"
export default {
    name : 'ProfilePage' ,
    components : {
        ProfileInfoCard
    }
}
</script>

<style lang="css" scoped>
</style>
