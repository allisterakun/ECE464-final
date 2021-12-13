<template>
    <div id="Restock">
        <h3>
            Enter the Product and Quantity for Restocking:
        </h3>
        <b-form-select style="font-size:20px; padding:10px;margin:20px" v-model="product_name" :options="products"></b-form-select>
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
            quantity: 0 ,
            products:[]
        }
    }, mounted() {
        this.getProductNames();
    },
    methods:{
        getProductNames(){
            let self = this;
            axios.get(backEndAddress + "/getProducts", {
                params: {
                    store_id: this.$cookie.get("store_id")
                }
            })
            .then(res => {
                console.log(res)
                for(let i = 0; i < res.data.length; i++){
                    self.products.push( res.data[i].product_name);
                }

            })
            .catch(err => {
                console.error(err); 
            })
        },
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