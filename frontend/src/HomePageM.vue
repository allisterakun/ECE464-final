<template>
  <div id="HomePage">
    <h1>{{position}}</h1>
    <b-navbar id="bNavBar" toggleable="lg" type="light" variant="info">

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-if="!isManager" href="#/homepage/timesheet">Timesheet</b-nav-item>
        <b-nav-item v-if="isManager" href="#/homepage/timesheet">Check Timesheets</b-nav-item>
        <b-nav-item v-if="isManager" href="#/homepage/profit">Check Profit</b-nav-item>
        <b-nav-item v-if="!isManager" href="#/homepage/inventory">Check Inventory</b-nav-item>
        <b-nav-item v-if="!isManager" href="#/homepage/sell">Sell</b-nav-item>
        <b-nav-item v-if="!isManager" href="#/homepage/restock">Restock</b-nav-item>
        <b-nav-item v-if="!isManager" href="#/homepage/purchases">Check Purchases</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em>User</em>
          </template>
          <b-dropdown-item v-on:click="signOut">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

  <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios';
import backEndAddress from "./utili.js"
export default {
    name:"HomepageM",
    data:function(){
      return{
        position:"?",
        isManager: false
      }
    },
    methods:{
      checkLogin(){
        if(this.$cookie.get("employee_id") == null){
          this.$router.push('/');
          return false;
        }
        return true;
      },
      signOut(){
        this.$cookie.delete("employee_id");
        this.$router.push('/');

      },
      getPosition(){
        let self = this;
        let employee_id = this.$cookie.get('employee_id');
        axios.get(backEndAddress+"/home", {
          params: {
            employee_id: employee_id
          }
        }).then(function (response) {
          self.position = response.data.position;
          if(self.position == "Manager"){
            self.isManager = true;
          }

          self.$cookie.set("isManager", self.isManager);

          self.$router.push('/homepage/timesheet').catch(()=>{});

        })
        .catch(function (error) {
          console.log(error);
        });
      }
    },
    mounted(){
      if(this.checkLogin()){
        this.getPosition();
      }
    }
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