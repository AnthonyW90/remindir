<template>
  <v-container pa-1>
    <v-expansion-panel>
      <v-expansion-panel-content v-if="task.content">
        <template v-slot:header>
          <div>{{ task.title }}</div>
          <v-layout row v-if="isTaskCreator" align-center class="mr-2">
            <v-spacer></v-spacer>
            <v-flex xs1>
              <!-- <v-switch v-model="isCompleted" @click="completeTask" color="green" hide-details></v-switch> -->
              <v-btn v-if="isCompleted" class="green" icon small v-bind="isCompleted" @click="completeTask"><v-icon>check</v-icon></v-btn>
              <v-btn v-else icon small v-bind="isCompleted" @click="completeTask"><v-icon>check</v-icon></v-btn>
            </v-flex>
            <v-flex xs1>
              <TaskEditor v-bind:task="task" />
            </v-flex>
            <v-flex xs1>
              <v-btn icon small @click="triggerDeleteTask">
                <v-icon>delete_forever</v-icon>
              </v-btn>
            </v-flex>
          </v-layout>
        </template>
        <v-card>
          <v-card-text>{{ task.content }}</v-card-text>
        </v-card>
      </v-expansion-panel-content>
      <v-expansion-panel-content v-else hide-actions>
        <template v-slot:header>
          <div>{{ task.title }}</div>
          <v-layout row v-if="isTaskCreator" align-center class="mr-4 pr-2">
            <v-spacer></v-spacer>
            <v-flex xs1>
              <!-- <v-switch v-model="isCompleted" @click="completeTask" color="green" hide-details></v-switch> -->
              <v-btn v-if="isCompleted" class="green" icon small v-bind="isCompleted" @click="completeTask"><v-icon>check</v-icon></v-btn>
              <v-btn v-else icon small v-bind="isCompleted" @click="completeTask"><v-icon>check</v-icon></v-btn>
            </v-flex>
            <v-flex xs1>
              <TaskEditor v-bind:task="task" />
            </v-flex>
            <v-flex xs1>
              <v-btn icon small @click="triggerDeleteTask">
                <v-icon>delete_forever</v-icon>
              </v-btn>
            </v-flex>
          </v-layout>
        </template>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import TaskEditor from "./TaskEditor.vue";
export default {
  name: "TaskComponent",
  components: {
    TaskEditor
  },
  data() {
    return {
      isCompleted: this.task.completed
    };
  },
  props: {
    task: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  computed: {
    isTaskCreator() {
      return this.task.created_by === this.requestUser;
    }
  },
  methods: {
    triggerDeleteTask() {
      this.$emit("delete-task", this.task);
    },
    completeTask() {
      this.isCompleted = !(this.isCompleted);
      let endpoint = `/api/task/${this.task.id}/`;
      try {
        apiService(endpoint, "PUT", {
          title: this.task.title,
          content: this.task.content,
          completed: this.isCompleted
        });
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
