<template>
  <v-container>
    <h1>Add a group</h1>
    <form @submit.prevent="onSubmit">
      <v-text-field v-model="group_label" rows="3" placeholder="Name your group"></v-text-field>
      <br />
      <v-btn type="submit">Submit</v-btn>
    </form>
    <p v-if="error" class="muted" mt2>{{ error }}</p>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "GroupEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      group_label: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.group_label) {
        this.error = "Please name your group";
      } else if (this.group_label.length > 60) {
        this.error = "Must be less than 60 characters";
      } else {
        let endpoint = "/api/taskgroups/";
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        apiService(endpoint, method, {
          label: this.group_label,
          recurrences: "RRULE:FREQ=WEEKLY"
        }).then(group_data => {
          this.$router.push({
            name: "taskgroup",
            params: { slug: group_data.slug }
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    if (to.params.slug !== undefined) {
      let endpoint = `/api/taskgroups/${to.params.slug}/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.group_label = data.label));
    } else {
      return next();
    }
  },
  created() {
    document.title = "Editor";
  }
};
</script>
