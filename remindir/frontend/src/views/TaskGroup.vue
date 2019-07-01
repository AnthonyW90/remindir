<template>
  <v-container class="mt-5">
    <div class="mt-2">
      <h1 class="text-xs-center">{{ taskgroup.label }}</h1>
      <div v-if="showForm">
        <form @submit.prevent="onSubmit">
          <v-card flat>
            <v-card-title>Add a new task</v-card-title>
            <v-card-text>
              <v-text-field
                autofocus
                v-model="newTaskTitle"
                outline
                label="*Required"
                placeholder="Title"
              ></v-text-field>
              <v-text-field v-model="newTaskContent" outline placeholder="Description"></v-text-field>
            </v-card-text>
            <v-card-actions width="100%">
              <v-spacer></v-spacer>
              <v-btn color="red" @click="showForm = false">Cancel</v-btn>
              <v-btn color="green" type="submit">Submit</v-btn>
            </v-card-actions>
          </v-card>
        </form>
        <p class="red--text">{{error}}</p>
      </div>
      <div v-else right>
        <v-layout row>
          <v-spacer></v-spacer>
          <v-flex xs1 pa-0 ma-0>
            <v-btn icon @click="showForm = true">
              <v-icon>add</v-icon>
            </v-btn>
          </v-flex>
          <v-flex xs2 pa-0 ma-0>
            <TaskGroupActions :slug="taskgroup.slug" />
          </v-flex>
        </v-layout>
      </div>
    </div>
    <hr />
    <div>
      <TaskComponent
        v-for="(task, index) in tasks"
        :task="task"
        :requestUser="requestUser"
        :key="index"
        @delete-task="deleteTask"
      />
    </div>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import TaskComponent from "@/components/Task.vue";
import TaskGroupActions from "@/components/TaskGroupActions.vue";
export default {
  name: "TaskGroup",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    TaskComponent,
    TaskGroupActions
  },
  data() {
    return {
      taskgroup: {},
      tasks: [],
      newTaskTitle: null,
      newTaskContent: null,
      error: null,
      showForm: false,
      requestUser: null
    };
  },
  computed: {
    isGroupCreator() {
      return this.taskgroup.created_by === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    getTaskGroupData() {
      let endpoint = `/api/taskgroups/${this.slug}/`;
      apiService(endpoint).then(data => {
        this.taskgroup = data;
        this.setPageTitle(data.label);
      });
    },
    getTasks() {
      let endpoint = `/api/taskgroups/${this.slug}/tasks/`;
      apiService(endpoint).then(data => {
        this.tasks = data;
      });
    },
    onSubmit() {
      if (this.newTaskTitle) {
        let endpoint = `/api/taskgroups/${this.slug}/task/`;
        apiService(endpoint, "POST", {
          title: this.newTaskTitle,
          content: this.newTaskContent
        }).then(data => {
          this.tasks.unshift(data);
        });
        this.newTaskTitle = null;
        this.newTaskContent = null;
        this.showForm = false;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "Please input a title.";
      }
    },
    async deleteTask(task) {
      let endpoint = `/api/task/${task.id}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$delete(this.tasks, this.tasks.indexOf(task));
      } catch (e) {
        console.log(e);
      }
    }
  },
  created() {
    this.getTaskGroupData();
    this.getTasks();
    this.setRequestUser();
  }
};
</script>

<style>
</style>

