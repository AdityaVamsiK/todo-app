  <!-- <script setup>
    import Navbar from './components/Navbar.vue'
    import HomePendingTasks from './components/HomePendingTasks.vue';
    import HomeCompletedTasks from './components/HomeCompletedTasks.vue';
  </script>

  <template>
    <Navbar />
    <div class="flex justify-around">
      <HomePendingTasks />
      <HomeCompletedTasks />
    </div>
  </template>

  <style scoped>

  </style> -->

<script setup>
  import { RouterView } from 'vue-router';
</script>

<template>
  <router-view />
</template>
