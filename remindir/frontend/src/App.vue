<template>
  <div id="app">
    <Navbar/>
    <router-view/>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
export default {
  name: "App",
  components: {
    Navbar
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
