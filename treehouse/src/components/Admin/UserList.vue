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
              v-for="item in items"
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

              </v-list-item-content>

              <v-list-item-icon>
                <v-icon :color="green"> mdi-check </v-icon>
                <v-icon> mdi-delete </v-icon>
              </v-list-item-icon>
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
/*      items: [
        { active: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
        { active: true, title: 'Ranee Carlson', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
        { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
        { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' },
      ],
*/    }),
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
    }
  }
</script>
