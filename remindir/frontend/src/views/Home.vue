<template>
  <div class="home">
    <div class="container">
      <div>
        <p class="mb-0"></p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
  name: "home",
  data() {
    return {
      taskGroups: []
    };
  },
  methods: {
    getTaskGroups() {
      let endpoint = "/api/taskgroups/";
      apiService(endpoint).then(data => {
        this.taskGroups.push(...data.results);
      });
    }
  },
  created() {
    this.getTaskGroups();
    console.log(this.taskGroups);
  }
};
</script>
