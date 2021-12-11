<template>
  <div id="TimeSheet">
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
      timeSheetRow:[]
      
    }
  },

}
</script>

<style>

</style>