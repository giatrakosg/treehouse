<template lang="html">
    <div class="">
        <UserList title="Users"/>
    </div>
</template>

<script>
import UserList from "../components/Admin/UserList"
export default {
    name : 'AdminPage' ,
    components : {
        UserList
    },
    created() {
        this.$store.dispatch('getUserList');
    }
}
</script>

<style lang="css" scoped>
</style>
