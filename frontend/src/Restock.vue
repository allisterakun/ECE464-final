<template>
    <div id="Restock">
        <h3>
            Enter the Product and Quantity for Restocking:
        </h3>
        <b-form-input v-model="product_name" placeholder="Product Name">
        </b-form-input>
        <p></p>
        <b-form-input v-model="quantity" placeholder="Quantity" type="number">
        </b-form-input>
        <p></p>

        <b-button v-on:click="restockProduct()">Restock</b-button>

    </div>
  
</template>

<script>
import axios from 'axios'
import backEndAddress from './utili.js'

export default {
    name:"Restock",
    data() {
        return {
            product_name :"",
            quantity: 0 
        }
    },
    methods:{
        restockProduct(){
            let params = {
                quantity : this.quantity,
                product_name : this.product_name,
                store_id : this.$cookie.get("store_id"),  

            }
            let self = this;
            axios.post(backEndAddress + "/restock",params)
            .then(res => {
                self.quantity = 0;
                self.product_name = "";
                console.log(res)
            })
            .catch(err => {
                self.$notify({ type: 'error', text: 'Cannot Restock Product!'+ err });
            })
        }
    }

}
</script>

<style>

</style>