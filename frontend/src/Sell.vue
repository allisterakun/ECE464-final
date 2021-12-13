<template>
    <div id="Sell">
        <h3>
            Enter the Product and Quantity for Selling:
        </h3>
        <b-form-input v-model="product_name" placeholder="Product Name">
        </b-form-input>
        <p></p>
        <b-form-input v-model="quantity" placeholder="Quantity" type="number">
        </b-form-input>
        <p></p>

        <b-button v-on:click="sellProduct()">Sell</b-button>

    </div>
  
</template>

<script>
import axios from 'axios'
import backEndAddress from './utili.js'
export default {
    name:"Sell",
    data() {
        return {
            product_name :"",
            quantity: 0
            
        }
    },
    methods:{
        getProductNames(){
            axios.get(backEndAddress + )
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.error(err); 
            })
        },
        sellProduct(){
            let params = {
                quantity : this.quantity,
                product_name : this.product_name,
                store_id : this.$cookie.get("store_id"),  
                employee_id : this.$cookie.get("employee_id")

            }
            let self = this;
            axios.post(backEndAddress + "/sell",params)
            .then(res => {
                if(res.data.statusCode != "200"){
                    self.$notify({ type: 'error', text: 'Cannot Sell Product! Check product name or quantity!' });
                }else{
                    self.quantity = 0;
                    self.product_name = "";
                    console.log(res)
                }
            })
            .catch(err => {
                self.$notify({ type: 'error', text: 'Cannot Sell Product!'+ err });
            })
        }
    }

}
</script>

<style>

</style>