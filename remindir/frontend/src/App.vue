<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Navbar from "./components/Navbar.vue";
export default {
  name: "App",
  components: {
    Navbar
  },
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      const requestUser = data['username'];
      window.localStorage.setItem('username', requestUser)
    }
  },
  created() {
    this.setUserInfo()
  }
};
</script>

<style>
html,
body {
  font-family: "Roboto Condensed", sans-serif;
  height: 100%;
  margin: 0;
}
.btn:focus {
  box-shadow: none !important;
}
</style>
