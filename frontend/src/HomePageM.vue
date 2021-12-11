<template>
  <div id="HomePage">
    <h1>Homepage</h1>
    <b-navbar id="bNavBar" toggleable="lg" type="light" variant="info">

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Check Profit</b-nav-item>
        <b-nav-item href="#">Check Timesheets</b-nav-item>
        <b-nav-item href="#">Check Inventory</b-nav-item>
        <b-nav-item href="#">Timesheet</b-nav-item>
        <b-nav-item href="#">Sell</b-nav-item>
        <b-nav-item href="#">Check Purchase</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  </div>
</template>

<script>
export default {
    name:"HomepageM"
}
</script>

<style>

#bNavBar{
  background-color: transparent!important;
  border-top: black 3px solid!important;
}

h1{
  color: black;
  margin-bottom: 100px;
}

</style>