<template>
  <v-app>
      <AppBar/>
      <v-content>
          <router-view/>
      </v-content>
      <v-footer color="brown"></v-footer>
  </v-app>
</template>

<script>
import AppBar from './components/AppBar/AppBar'
export default {
  name: 'App',

  components: {
    AppBar
  },

  data: () => ({
    //
  }),
};
</script>
