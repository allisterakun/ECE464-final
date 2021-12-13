<template>
    <div id="Purchases">
        <b-table striped hover :items="purchases"></b-table>
    </div>
  
</template>

<script>
import axios from 'axios'
import backEndAddress from './utili.js'

export default {
    name:"Purchases",
    data() {
        return {
            purchases:[]
        }
    },
    methods: {
        getPurchases(){
            let self = this;
            axios.get(backEndAddress + "/getPurchases", {
                params: {
                    store_id: self.$cookie.get("store_id")
                }
            })
            .then(res => {
                console.log(res);
                self.purchases = res.data;
            })
        }
    },
    mounted() {
        this.getPurchases();
    },

}
</script>

<style>

</style>