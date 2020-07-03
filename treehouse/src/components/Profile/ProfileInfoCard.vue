<template>
  <v-card
  >
    <v-img
      :src="user.avatar"
      height="300px"
      width="200px"
      dark
    >
      <v-row class="fill-height">
        <v-card-title>

        <v-spacer></v-spacer>

          <v-btn dark icon class="mr-4" to="/editprofile">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>


        </v-card-title>

        <v-spacer></v-spacer>

        <v-card-title class="white--text pl-12 pt-12">
          <div class="display-1 pl-12 pt-12">{{user.fname + ' ' + user.surname}}</div>
        </v-card-title>
      </v-row>
    </v-img>

    <v-list two-line>

      <v-list-item >
        <v-list-item-icon>
          <v-icon color="indigo">mdi-email</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{user.email}}</v-list-item-title>
          <v-list-item-subtitle>Personal</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item >
        <v-list-item-icon>
          <v-icon color="indigo">mdi-cellphone</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>Phone</v-list-item-title>
          <v-list-item-subtitle>{{user.phone}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
export default {
    name : 'ProfileInfoCard' ,
    props : ['user'],
    computed : {
        avatar() {
            return this.user.avatar ;
        }
    }
}
</script>

<style lang="css" scoped>
</style>
