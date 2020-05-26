<template lang="html">
  <div class="">
        <v-card
         class="ma-5"
        >
            <v-toolbar
              color="primary"
              dark
            >
              <v-app-bar-nav-icon></v-app-bar-nav-icon>
              <v-toolbar-title>{{this.title}}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
          <v-list subheader>
              <v-select
                v-model="ftype"
                :items="filters"
                filled
                chips
                multiple
              ></v-select>
            <v-list-item
              v-for="(item,index) in items"
              :key="item.title"

            >
              <v-list-item-avatar>
                <v-img :src="item.avatar"></v-img>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title v-text="item.title"></v-list-item-title>
                <v-list-item-subtitle v-text="item.fname + ' ' + item.surname">
                </v-list-item-subtitle>
                <v-list-item-subtitle v-text="item.email">
                </v-list-item-subtitle>

                <v-btn @click="accept(index)">
                    <v-icon :color="green"> mdi-check</v-icon>
                </v-btn>
                <v-btn @click="reject(index)">
                    <v-icon> mdi-delete </v-icon>
                </v-btn>
              </v-list-item-content>
            </v-list-item>

          </v-list>
        </v-card>
  </div>
</template>
<style lang="css" scoped>
</style>
<script>
  export default {
    name : 'UserList',
    props : ['title'],
    data: () => ({
      filters : ['approved','pending'] ,
      values : ['approved','pending'],
    }),
    computed : {
        users() {
            return this.$store.state.users
        },
        items() {
            var list = []
            for (var i = 0; i < this.users.length; i++) {
                list.push({active:true,title:this.users[i].name,avatar:'https://cdn.vuetifyjs.com/images/lists/3.jpg',fname:this.users[i].first_name ,surname:this.users[i].last_name,email:this.users[i].email})
            }
            return list;
        }
    } ,
    methods : {
        accept(idx) {
            this.$store.dispatch('acceptUser',idx)
            return console.log(idx)
        },
        reject(idx) {
            this.$store.dispatch('rejectUser',idx)
            return console.log(idx)
        }
    }
  }
</script>
