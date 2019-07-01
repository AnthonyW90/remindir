<template>
<nav>
  <v-toolbar app flat color="yellow">
    <v-toolbar-side-icon @click="drawer = !drawer" class="hidden-lg-and-up grey--text"></v-toolbar-side-icon>
    <v-toolbar-title class="headline">
      <router-link  class="no-decorate" :to="{ name: 'home' }">remindir</router-link>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-md-and-down">
      <!-- <v-btn flat><router-link  class="no-decorate" :to="{ name: 'home' }"> -->
        <!-- <span>Calendar</span> -->
        <!-- <v-icon >date_range</v-icon> -->
      <!-- </router-link></v-btn> -->
      <v-btn flat><router-link  class="no-decorate" :to="{ name: 'group-editor' }">
        <!-- <span>Add Group</span> -->
        <v-icon >add_to_queue</v-icon>
      </router-link></v-btn>
      <v-btn flat  class="no-decorate text--blue" href="/accounts/logout/">
        <span>Logout</span>
        <v-icon right>exit_to_app</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
  
  <v-navigation-drawer absolute temporary v-model="drawer" class="hidden-lg-and-up yellow lighten-1" color="yellow">
      <v-list class="pa-1">
        <v-list-tile class="ml-5 pl-3 mt-3">
          <h1 class="blue--text text--darken-1 text-xs-center">remindir</h1>
        </v-list-tile>
      </v-list>
      <v-list class="pt-0">
        <v-divider></v-divider>

        <router-link :to="{ name: 'home' }" class="no-decorate">
          <v-list-tile>
            <v-list-tile-content class="blue--text text--darken-1 text-xs-center">
              Home
            </v-list-tile-content>
          </v-list-tile>
        </router-link>
        <router-link :to="{ name: 'group-editor' }" class="no-decorate">
          <v-list-tile>
            <v-list-tile-content class="blue--text text--darken-1 text-xs-center">
              Add Group
            </v-list-tile-content>
          </v-list-tile>
        </router-link>
        <v-divider></v-divider>
          <v-list-tile href="/accounts/logout/">
            <v-list-tile-content prepend-icon="exit_to_app">
              <p class="no-decorate blue--text">Logout</p>
            </v-list-tile-content>
          </v-list-tile>
      </v-list>
  </v-navigation-drawer>
  
  </nav>
</template>
<script>
export default {
  name: "Navbar",
  data() {
    return {
      drawer: false
    }
  }
};
</script>
<style scoped>
.no-decorate:hover {
  text-decoration: none;
}
</style>

