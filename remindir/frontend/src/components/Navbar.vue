<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-title">remindir</router-link>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link :to="{ name: 'home' }" class="btn btn-sm btn-primary">Home</router-link>
          </li>
          <li class="nav-item mx-1">
            <router-link :to="{ name: 'home' }" class="btn btn-sm btn-outline-secondary">Add Group</router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/">Logout</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "Navbar"
};
</script>
<style scoped>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-title {
  font-weight: bold;
  font-size: 150%;
}
.navbar-title:hover {
  color: cornflowerblue;
  text-decoration: none;
}
</style>

