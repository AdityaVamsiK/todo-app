import { createRouter, createWebHistory } from "vue-router";

import Home from "../Views/Home.vue";
import FinishedTasks from "../Views/FinishedTasks.vue";
import PendingTasks from "../Views/PendingTasks.vue";

const routes = [
    {path: '/', name: "home", component: Home},
    {path: '/pendingtasks', name: "pendingtasks", component: PendingTasks},
    {path: '/finishedtasks',name: "finishedtasks", component: FinishedTasks}
]


const router = createRouter({
  history: createWebHistory(), // ✅ This enables real browser navigation
  routes
})

export default router