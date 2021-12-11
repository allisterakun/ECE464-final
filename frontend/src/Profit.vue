<template>
    <div id="profit">
        <h2>Start Date</h2>
        <b-form-datepicker id="datePicker" v-model="start_Date" class="mb-2"></b-form-datepicker>
        <h2>End Date</h2>
        <b-form-datepicker id="datePicker" v-model="end_Date" class="mb-2"></b-form-datepicker>
        <h2>Total Profit:</h2>
        <h2>{{h2rofit}}</h2>
    </div>
  
</template>

<script>
// import axios from 'axios';

export default {
    name:"Profit",
    data() {
        return {
            start_Date:"",
            end_Date:"",
            profit:0
        }
    },
}
</script>

<style>

</style>