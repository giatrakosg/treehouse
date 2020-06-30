<template>
  <v-app>
      <AppBar/>
      <v-content>
          <router-view/>
      </v-content>
      <Footer/>
  </v-app>
</template>

<script>
    import AppBar from './components/AppBar/AppBar'
    import Footer from "./views/Footer";
export default {
  name: 'App',

  components: {
      Footer,
      AppBar
  },

  data: () => ({
    //
  }),
};
</script>
