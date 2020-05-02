<template lang="html">
    <v-row>
        <v-col>
            <ProfileInfoCard />
        </v-col>
    </v-row>

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
