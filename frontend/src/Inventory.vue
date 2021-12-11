<template>
    <div>
    </div>
  
</template>

<script>
import axios from 'axios'
import backEndAddress from './utili.js'
export default {
    name:"Inventory",
    methods:{
        getInventory(){
            axios.get(backEndAddress + "/getInventory",params)
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.error(err); 
            })
        }
    }
}
</script>

<style>

</style>