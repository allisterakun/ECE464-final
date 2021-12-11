<template>
  <div id="timeSheetRow">
    <b-card
    :title="date"
    style="max-width: 20rem;"
    class="mb-2"
  >
      <b-card-text>
      <p>Clock In : {{clockIn}}</p>
      <p>Clock Out: {{clockOut}}</p>
      <p>Item Sold: {{sold}}</p>
      </b-card-text>

    </b-card>
  </div>
</template>

<script>
export default {
    name: "timeSheetRow",
    props:["clockIn","clockOut","sold","date"]

}
</script>

<style>

</style>