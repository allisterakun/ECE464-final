<template>
  <div id="app">
    <b-card title="Login to the Inventory">
      <input v-model="UserName" placeholder="Enter UserName">
  
      <input v-model="Password" placeholder="Enter Password">
      <b-button>Login</b-button>
    </b-card>
  </div>
</template>

<script>

export default {
  name: 'App',
  data:function(){
    return{
      UserName:"",
      Password:""
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
input{
  display: flex;
  justify-content: center;
  margin: 20px;
}
div{
  width: 50%;
  margin: auto;
}
b-card{
  width: 40px;
}
b-button{
  margin: 10px;
}
</style>
