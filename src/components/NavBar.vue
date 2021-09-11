// Navigation Bar Content

<template>
  <!-- Create a navigation bar -->
  <b-navbar toggleable="md" type="dark" variant="info" class="nav-bar" sticky-top navbar-dark >
  <!-- <b-navbar toggleable="md" navbar-dark bg-dark> -->
    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    <b-navbar-brand href="#">Swift Chat</b-navbar-brand>
    <b-collapse is-nav id="nav_collapse">
      <b-navbar-nav class="ml-auto logged_user">
        Welcome back {{ logged_user }}
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    logged_user: String,
  },
};
</script>

<style scoped>
.nav-bar {
  border-bottom: 1px solid #17a2b8;
  width: 100% !important;
  margin: 0px auto;
  border-right: 0px;
}

.navbar {
  background-color: darkgray !important;
}
</style>
