<template>
    <div>
        <b-dropdown style="width:fit-content" id="dropdown-1" text="Type" class="m-2">
            <b-dropdown-item>All</b-dropdown-item>
            <b-dropdown-item>Fruit</b-dropdown-item>
            <b-dropdown-item>Meat</b-dropdown-item>
            <b-dropdown-item>Drink</b-dropdown-item>
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
        getInventory(){
            let self = this;
            let parameters = {
                params:{
                    // item_type: type,
                    store_id: this.$cookie.get("store_id")
                }
            }
            axios.get(backEndAddress + "/getInventory",parameters)
            .then(res => {
                self.inventory = res.data;
                console.log(res)
            })
            .catch(err => {
                console.error(err); 
            })
        }
    },
    mounted(){
        this.getInventory();
    },
    data() {
        return {
            inventory:[]
        }
    },
}
</script>

<style>

</style>