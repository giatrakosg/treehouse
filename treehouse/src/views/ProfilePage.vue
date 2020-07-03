<template lang="html">
    <v-layout row align-start>
        <v-flex sm1 md1 lg1>
            <v-spacer></v-spacer>
        </v-flex>
        <v-flex sm3 md3 lg3 class="ma-3">
            <ProfileInfoCard :user="profile"/>
        </v-flex>
        <v-flex sm7 md7 lg7 class="ma-3">
            <v-container class="pa-0 elevation-2" style="border-radius: 8px;">
                <v-row dense>
                    <v-col cols="5">
                        <MessageThreads/>
                    </v-col>
                    <v-col cols="7">
                        <Messages/>
                    </v-col>
                </v-row>
            </v-container>
        </v-flex>
    </v-layout>
</template>

<script>
    import ProfileInfoCard from "../components/Profile/ProfileInfoCard.vue"
    import Messages from "../components/Messages/Messages";
    import MessageThreads from "../components/Messages/MessageThreads";

    export default {
        name: 'ProfilePage',
        components: {
            ProfileInfoCard,
            Messages,
            MessageThreads
        },
        data: () => ({}),
        created() {
            console.log(this.$store.state.room);
            this.$store.dispatch('getMessageThreadsUser');
        },
        computed : {
            profile() {
                if (this.$route.params.id == 'me') {
                    return this.$store.state.user ;
                } else {
                    this.$store.dispatch('getUser',this.$route.params.id);
                    return this.$store.state.user_profile ;
                }
            }
        }
    }
</script>

<style lang="css" scoped>
</style>
