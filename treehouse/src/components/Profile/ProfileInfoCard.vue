<template lang="html">
      <v-card
        class="mx-auto"
        max-width="200"
        tile
      >
        <v-row>
            <v-col>
                <v-avatar
                  class="profile"
                  color="grey"
                  size="164"
                  tile
                >
                    <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                </v-avatar>

            </v-col>
      </v-row>
      <v-divider></v-divider>
      <v-row>
          <v-card-text>

              <v-list>
                  <v-list-item>
                      3 κριτικες
                  </v-list-item>
                  <v-list-item>
                      Η ταυτοτητα επαληθευτηκε
                  </v-list-item>
              </v-list>
          </v-card-text>
      </v-row>
      <v-divider></v-divider>
      <v-row>
          <v-card-text>

          </v-card-text>
      </v-row>

    </v-card>
</template>

<script>
export default {
    name : 'ProfileInfoCard'
}
</script>

<style lang="css" scoped>
</style>
