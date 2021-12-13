<template>
    <div id="profit">
        <h2>Start Date</h2>
        <b-form-datepicker id="datePicker" v-model="start_Date" class="mb-2"></b-form-datepicker>
        <h2>End Date</h2>
        <b-form-datepicker id="datePicker" v-model="end_Date" class="mb-2"></b-form-datepicker>
        <p></p>
        <b-button v-on:click="calculateProfit" > Calculate Profit</b-button>
        <p></p>
        <h2>Total Profit:</h2>
        <h2>{{profit}}</h2>
        <h5>Employee Cost:</h5>
        <h5>{{salary}}</h5>
    </div>
  
</template>

<script>
import axios from 'axios';
import backEndAddress from './utili.js'

export default {
    name:"Profit",
    data() {
        return {
            start_Date:"",
            end_Date:"",
            profit:0,
            salary:0
        }
    },
    methods: {
        calculateProfit(){
            let self = this;
            axios.get(backEndAddress + "/getProfit", {
                params: {
                    store_id: self.$cookie.get("store_id"),
                    start_Date: self.start_Date,
                    end_Date : self.end_Date
                }
            })
            .then(res => {
                console.log(res);
                self.profit = res.data.profit;
            })
            .catch(err => {
                self.$notify({ type: 'error', text: 'Wrong dates entered!' + err });
            });

            axios.get(backEndAddress + "/getAllPay", {
                params: {
                    store_id: self.$cookie.get("store_id"),
                    start_date: self.start_Date,
                    end_date : self.end_Date
                }
            })
            .then(res => {
                console.log(res);
                self.salary= res.data.total;
            })
            .catch(err => {
                self.$notify({ type: 'error', text: 'Wrong dates entered!' + err });
            })
        }
    },
}
</script>

<style>

</style>