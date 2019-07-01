<template>
  <v-dialog max-width="600px" v-model="dialog">
    <v-btn icon small slot="activator">
      <v-icon>edit</v-icon>
    </v-btn>
    <v-card>
      <v-card-title>
        <h2>Title</h2>
      </v-card-title>
      <v-card-text>
        <v-form class="px-3" @submit.prevent="onSubmit">
          <v-text-field v-model="taskTitle" label="*Required"></v-text-field>
          <v-textarea v-model="taskContent"></v-textarea>
          <v-btn type="submit" @click="dialog = false" flat class="green">Submit</v-btn>
        </v-form>
        <p v-if="error" class="red">{{error}}</p>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "TaskEditor",
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      dialog: false,
      taskTitle: this.task.title,
      taskContent: this.task.content,
      taskCompleted: this.task.completed,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.taskTitle) {
        let endpoint = `/api/task/${this.task.id}/`;
        apiService(endpoint, "PUT", {
          title: this.taskTitle,
          content: this.taskContent,
          completed: this.taskCompleted
        }).then(() => {
          this.$router.push({
            name: "taskgroup",
            params: { slug: this.task.group_slug }
          });
        });
      } else {
        this.error = "Please enter a title";
      }
    }
  }
};
</script>
