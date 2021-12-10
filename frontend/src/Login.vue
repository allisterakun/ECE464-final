<template>
  <div id="Login">
    <b-card title="Login to the Inventory">
      <section>
        <h3 class="loginSubtitle">UserName:</h3>
        <input class="loginInput" v-model="UserName" placeholder="Enter UserName">
      </section>

      <section>
        <h3 class="loginSubtitle">Password:</h3>
        <input class="loginInput" v-model="Password" type="password" placeholder="Enter Password">
      </section>

      <b-button v-on:click="login">Login</b-button>
    </b-card>
  </div>
  
</template>

<script>
import post from './utili.js'
export default {
  name: 'Login',
  data:function(){
    return{
      UserName:"",
      Password:""
    }
  },
  methods:{
    login(){
      post(
        {
          inputName:this.UserName,
          inputPassword:this.Password
        }
      )

      this.$cookie.set('test', 'Hello world!', 1);
      console.log(this.$cookie.get('test'));
      this.$router.push('/homepageM')
    }
  }
}


</script>

<style>
section{
  display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 20px;
}
div{
  width: 80%;
  margin: auto;
}
b-card{
  width: 40px;
}
b-button{
  margin: 10px;
}

b-card{
  background: #2c3e50;
}
.loginSubtitle{
  font-size: 20px;
  margin-right: 10px;
}
</style>
