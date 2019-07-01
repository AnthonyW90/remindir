<template>
  <div class="home mt-5">
    <v-container>
      <v-layout row wrap justify-start>
        <v-flex xs6 md4 l3 v-for="taskgroup in taskGroups" :key="taskgroup.pk" pa-2>
          <router-link
            :to="{ name: 'taskgroup', params: { slug: taskgroup.slug } }"
            class="group-link"
          >
            <v-hover>
              <v-card
                height="150"
                slot-scope="{ hover }"
                :class="`elevation-${hover ? 12 : 2}`"
                class="mx-auto"
                width="344"
              >
                <v-card-title class="justify-center align-center">
                  <h3>{{ taskgroup.label }}</h3>
                </v-card-title>
                <v-card-text mt-4>
                  <v-layout row>
                    <v-flex mt-4 pr-2 pt-3 text-xs-right xs12>{{ taskgroup.task_count }}</v-flex>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-hover>
          </router-link>
        </v-flex>
        <v-flex xs6 md4 l3 pa-2>
          <router-link :to="{ name: 'group-editor' }" class="group-link">
            <v-hover>
              <v-card
                height="150"
                slot-scope="{ hover }"
                :class="`elevation-${hover ? 12 : 2}`"
                class="mx-auto"
                width="344"
              >
                <v-card-title class="justify-center align-center">
                  <v-icon size="96">add</v-icon>
                </v-card-title>
              </v-card>
            </v-hover>
          </router-link>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
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
        this.taskGroups.push(...data);
      });
    }
  },
  created() {
    this.getTaskGroups();
    document.title = "remindir";
  }
};
</script>

<style scoped>
.group-link {
  font-weight: bold;
  color: black;
}
.group-link:hover {
  text-decoration: none;
  color: #343a40;
}
</style>
