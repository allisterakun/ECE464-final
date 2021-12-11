<template>
  <div id="TimeSheet">
    <b-card
    title="Record Your Work"
    style="max-width: 150rem;"
    class="mb-2"
    >
      <b-card-text>
      <p>Date:</p>
      <b-form-datepicker id="example-datepicker" v-model="checkInDate" class="mb-2"></b-form-datepicker>
      <!-- <p>Value: '{{ checkInDate }}'</p> -->

      <p>Clock In:</p>
      <b-form-timepicker v-model="checkInTime" locale="en"></b-form-timepicker>
      <!-- <div class="mt-2">checkInTime: '{{ checkInTime }}'</div> -->


      <p>Clock Out:</p>
      <b-form-timepicker v-model="checkOutTime" locale="en"></b-form-timepicker>
      
      <p>Item Sold: {{sold}}</p>
      <b-form-input type="number" v-model="soldRecord"></b-form-input>
      <p></p>
       <b-button v-on:click="addNewTimeSheet">Submit</b-button>
      </b-card-text>

    </b-card>
    <ul id="example-1" style="list-style: none">
        <li v-for="item in timeSheetRow" :key="item.message">
            <time-sheet-row :clockIn="item.clock_in_time" :clockOut="item.clock_out_time" :date="item.work_date" :sold="item.items_sold"/>
        </li>
    </ul>
  </div>
</template>

<script>
import backEndAddress from "./utili.js"
import axios from 'axios'
import timeSheetRow from './components/timeSheetRow.vue'
export default {
  name:"TimeSheet",
  components:{timeSheetRow},
  methods:{
    getMyTimeSheet(){
      let self = this;
      axios.get(backEndAddress + "/getTimesheet", {params: {
            employee_id: self.$cookie.get("employee_id")}
          })
      .then(res => {

        console.log(res);
        self.timeSheetRow = res.data;
      })
      .catch(err => {
        console.error(err); 
      })
    },
    addNewTimeSheet(){

    }
  },
  mounted(){
    this.isManager = this.$cookie.get("isManager");
      

    if(this.isManager == true){
        console.log(this.isManager);
        console.log("hi");
    }else{
      this.getMyTimeSheet(this.$cookie.get("employee_id"));
    }

  },
  data() {
    return {
      isManager: false,
      timeSheetRow:[],
      checkInDate: "",
      checkInTime: "",
      checkOutTime: "",
      soldRecord: 0
      
    }
  },

}
</script>

<style>

</style>