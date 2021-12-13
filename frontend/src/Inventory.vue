<template>
    <div>
        <b-dropdown style="width:fit-content" id="dropdown-1" :text="currentType" class="m-2">
            <b-dropdown-item v-on:click="getInventory('all')" >All</b-dropdown-item>
            <b-dropdown-item v-on:click="getInventory('fruit')">Fruit</b-dropdown-item>
            <b-dropdown-item v-on:click="getInventory('meat')">Meat</b-dropdown-item>
            <b-dropdown-item v-on:click="getInventory('drink')">Drink</b-dropdown-item>
        </b-dropdown>
        <b-table striped hover :items="inventory"></b-table>
    </div>
  
</template>

<script>
import axios from 'axios'
import backEndAddress from './utili.js'
export default {
    name:"Inventory",
    methods:{
        getInventory(type){
            let self = this;
            let parameters;
            this.currentType = type;
            if(type == 'all'){
                parameters = {
                    params:{
                        // item_type: type,
                        store_id: this.$cookie.get("store_id")
                    }
                }
            }else{
                parameters = {
                    params:{
                        item_type: type,
                        store_id: this.$cookie.get("store_id")
                    }
                }
            }
            
            axios.get(backEndAddress + "/getInventory",parameters)
            .then(res => {
                self.inventory = res.data;
                console.log(res)
            })
            .catch(err => {
                self.inventory = [];
                console.error(err); 
            })
        }
    },
    mounted(){
        this.getInventory('all');
    },
    data() {
        return {
            currentType:"all",
            inventory:[]
        }
    },
}
</script>


<style scoped>
div{
  width: 80%;
  margin: auto;
}
</style>