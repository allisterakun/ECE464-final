<template>
    <div id="Sell">
        <h3>
            Enter the Product and Quantity for {{sellOrRestock}}:
        </h3>
        <b-form-input placeholder="Product Name">
        </b-form-input>
        <p></p>
        <b-form-input placeholder="Quantity" type="number" v-model="soldRecord">
        </b-form-input>
        <p></p>

        <b-button v-if="sellOrRestock == 'Selling'">Sell</b-button>

        <b-button v-if="sellOrRestock == 'Restocking'">Restock</b-button>
    </div>
  
</template>

<script>
export default {
    name:"Sell",
    data() {
        return {
            sellOrRestock:'Selling'
        }
    },

}
</script>

<style>

</style>