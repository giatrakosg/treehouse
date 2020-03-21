<template>
    <v-card elevation="1"
    min-width="250px"
    max-width="400px"
    to="/roomlistings"
    v-ripple=false

  >
    <v-img
      class="white--text align-end"
      height="175px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >

    </v-img>
      <v-card-title>
        <v-container >
          <v-row  dense no-gutters align="center">
            <v-col cols="8">
               Awesome room
            </v-col>
            <v-col cols="4">
               <v-rating
              half-increments
              dense
              v-model="rating"
              readonly
              small
              ></v-rating>
            </v-col>
          </v-row>
        </v-container>


      </v-card-title>

    <v-card-text class="text--primary">


      <v-chip-group column >
        <v-chip color="primary" outlined v-ripple="false" >
          <v-icon>  </v-icon>
          /day:12
        </v-chip>
        <v-chip color="brown" outlined v-ripple="false">beds number:2</v-chip>
        <v-chip color="blue" outlined v-ripple="false">room:private</v-chip>
      </v-chip-group>

    </v-card-text>

  </v-card>
</template>

<script>
    export default {
        name: "RoomCard",
        data:function () {
          return{
            rating:3
          }

        }
    }
</script>

<style scoped>

</style>