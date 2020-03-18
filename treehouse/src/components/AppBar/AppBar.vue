<template lang="html">
    <v-app-bar
      app
      color="transparent"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="../../assets/treehouse.png"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-spacer></v-spacer>
      <div class="d-flex align-right">
          <v-btn
           color="primary"
          >
              Login
          </v-btn>
      </div>

    </v-app-bar>

</template>

<script>
export default {
    name : 'AppBar'
}
</script>

<style lang="css" scoped>
</style>
