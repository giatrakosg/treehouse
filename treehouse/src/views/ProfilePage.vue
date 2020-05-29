<template lang="html">
    <v-layout row>
        <v-flex sm3 md3 lg3>
            <ProfileInfoCard />
        </v-flex>
        <v-flex sm1 md1 lg1>
            <v-spacer></v-spacer>
        </v-flex>
        <v-flex sm8 md8 lg8>
            <ReviewCard />
        </v-flex>
    </v-layout>
</template>

<script>
import ProfileInfoCard from "../components/Profile/ProfileInfoCard.vue"
import ReviewCard from "../components/Profile/ReviewCard.vue"

export default {
    name : 'ProfilePage' ,
    components : {
        ProfileInfoCard ,
        ReviewCard
    },
    data: () => ({
    }),
}
</script>

<style lang="css" scoped>
</style>
