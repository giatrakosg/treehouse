<template lang="html">
    <v-container>
        <v-layout row>
            <UserList title="Users"/>
        </v-layout>
        <v-layout row>
            <v-btn @click="getData">Export to JSON</v-btn>
        </v-layout>
    </v-container>
</template>

<script>
import UserList from "../components/Admin/UserList"
export default {
    name : 'AdminPage' ,
    components : {
        UserList
    },
    data() {
        return {
            'active' : false
        }
    },
    created() {
        this.$store.dispatch('getUserList');
    },
    methods : {
        getData() {
            this.$store.dispatch('getData');
        }
    }
}
</script>

<style lang="css" scoped>
</style>
