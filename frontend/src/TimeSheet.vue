<template>
  <div id="TimeSheet">

    <b-card v-if="!isManager"
    title="Record Your Work"
    style="max-width: 50rem;"
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
      
      <p>Item Sold:</p>
      <b-form-input type="number" v-model="soldRecord"></b-form-input>
      <p></p>
       <b-button v-on:click="addNewTimeSheet">Submit</b-button>
      </b-card-text>

    </b-card>
    <ul v-if="!isManager" id="example-1" style="list-style: none">
        <li v-for="item in timeSheetRow" :key="item.message">
            <time-sheet-row id="sheets" :clockIn="item.clock_in_time" :clockOut="item.clock_out_time" :date="item.work_date" :sold="item.items_sold"/>
        </li>
    </ul>
    <div v-if="isManager">
      <h2>Start Date:</h2>
      <b-form-datepicker id="datePicker" v-model="start_Date" class="mb-2"></b-form-datepicker>
      <h2>End Date:</h2>
      <b-form-datepicker id="datePicker" v-model="end_Date" class="mb-2"></b-form-datepicker>
      <b-button v-on:click="getAllTimeSheets(start_Date, end_Date)"> Get Timesheets</b-button>
    </div>
    <b-table v-if="isManager" striped hover :items="timeSheetRow"></b-table>
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
      let self = this;
      let parameters = {
        work_date: this.checkInDate,
        clock_in_time:this.checkInTime,
        clock_out_time:this.checkOutTime,
        items_sold:this.soldRecord,
        employee_id: this.$cookie.get("employee_id")
      }
      axios.post(backEndAddress + "/newTimesheet", parameters)
      .then(res => {

        console.log(res);
        if(res.data.statusCode != "200"){
           self.$notify({ type: 'error', text: res.data.msg });
        }else{
          self.getMyTimeSheet(this.$cookie.get("employee_id"));
          self.checkInDate = "";
          self.checkInTime = "";
          self.checkOutTime = "";
          self.soldRecord = "";
        }
      })
      .catch(err => {
        self.$notify({ type: 'error', text: 'Please select a different day! You already submitted a timesheet for today.' + err });
      })
    },
    getAllTimeSheets(start_Date = "2000-1-1", end_Date = "2023-1-1"){
      let self = this;
      axios.get(backEndAddress +"/getAllTimesheet",{params: {
            employee_id: this.$cookie.get("employee_id"),
            store_id: this.$cookie.get("store_id"),
            start_date: start_Date,
            end_date: end_Date
          }
        })
      .then(res => {
        console.log(res);
        self.timeSheetRow = res.data
      })

    }
  },
  mounted(){
    this.isManager = this.$cookie.get("isManager");

    if(this.isManager == 'true'){
      this.isManager = true;
      this.getAllTimeSheets();
    }else{
      this.isManager = false;
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
      soldRecord: 0,
      start_Date:"",
      end_Date:""
      
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

<style>
#sheets{
  margin: auto;
}
</style>