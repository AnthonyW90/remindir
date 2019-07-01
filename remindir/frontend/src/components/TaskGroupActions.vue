<template>
  <div class="actions">
    <router-link class="no-decorate" :to="{name: 'group-editor', params: {slug: slug}}">
      <v-btn icon>
        <v-icon>edit</v-icon>
      </v-btn>
    </router-link>
    <v-btn icon @click="deleteTaskGroup">
      <v-icon>delete_forever</v-icon>
    </v-btn>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "TaskGroupActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deleteTaskGroup() {
      let endpoint = `/api/taskgroups/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style>
.no-decorate:hover {
  text-decoration: none;
}
</style>

