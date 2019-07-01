import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import TaskGroup from "./views/TaskGroup.vue"
import GroupEditor from "./views/GroupEditor.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  // base: process.env.BASE_URL,
  routes: [{
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/taskgroups/:slug",
    name: "taskgroup",
    component: TaskGroup,
    props: true
  },
  {
    path: "/create/:slug?",
    name: "group-editor",
    component: GroupEditor,
    props: true
  }
]
});