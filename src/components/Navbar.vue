<script setup>
  import { RouterLink } from 'vue-router';  
</script>

<template>
  <div class="flex justify-between items-center h-20 text-cyan-200 font-bold bg-gray-800 px-8 m-5 rounded-xl shadow-md">
    <!-- Left Title -->
     <div class="flex items-center space-x-4">
      <img src="../assets/circle-check-solid.svg" alt="Todo-icon" class="h-10 w-10">
      <RouterLink to="/" class="text-4xl text-left">My Todo App</RouterLink>
     </div>

    <!-- Right Nav Links -->
    <div class="flex space-x-6 text-2xl">
      <RouterLink to="/" class="hover:bg-gray-600 px-4 py-2 rounded cursor-pointer transition-colors duration-200">
        Home
      </RouterLink>
      <RouterLink to="/pendingtasks" class="hover:bg-gray-600 px-4 py-2 rounded cursor-pointer transition-colors duration-200">
        Pending Tasks
      </RouterLink>
      <RouterLink to="/finishedtasks" class="hover:bg-gray-600 px-4 py-2 rounded cursor-pointer transition-colors duration-200">
        Finished Tasks
      </RouterLink>
    </div>
  </div>
</template>
