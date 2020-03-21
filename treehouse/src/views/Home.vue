<template>
  <div class="home">
      <v-container>
          <v-img contain
           src="../assets/back-ground-image-3.jpg">
           <v-layout row class="mx-5 my-9">
               <v-flex sm4 md4 lg4 >
                   <SearchForm />
               </v-flex>
           </v-layout>
          </v-img>
      </v-container>
  </div>
</template>

<script>
import SearchForm from '../components/SearchForm/SearchForm'
export default {
  name: 'Home',
  components: {
      SearchForm
  }
}
</script>
