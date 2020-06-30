<template lang="html">
    <v-container>
        <v-layout row>
            <UserList title="Users"/>
        </v-layout>
        <v-layout row>
            <v-btn @click="getDataJSON">Export to JSON</v-btn>
            <v-btn @click="getDataXML">Export to XML</v-btn>
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
        getDataJSON() {
            this.$store.dispatch('getDataJSON');
        },
        getDataXML() {
            this.$store.dispatch('getDataXML');
        }

    }
}
</script>

<style lang="css" scoped>
</style>
