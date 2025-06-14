<!-- <script setup>
</script>

<template>
    <div class="flex m-5 h-20 text-cyan-200 items-center font-bold bg-gray-800 px-5 rounded-xl shadow-md" >
        <h1 class="flex text-5xl ml-5 ">My Todo App</h1>
        <div class="flex text-2xl ml-auto items-center justify-end">
            <div class="flex h-10 items-center justify-center hover:bg-gray-600 transition-colors duration-200 rounded cursor-pointer">
                <span class="mx-4">All Tasks</span>
            </div>
            <div class="flex h-10 items-center justify-center hover:bg-gray-600 transition-colors duration-200 rounded cursor-pointer">
                <span class="mx-4">Pending Tasks</span>
            </div>       
            <div class="flex h-10 items-center justify-center hover:bg-gray-600 transition-colors duration-200 rounded cursor-pointer">
                <span class="mx-4">Finished Tasks</span>
            </div>
        </div>
    </div>
</template>
 -->

<script setup>
  import { RouterLink } from 'vue-router';  
</script>

<template>
  <div class="flex justify-between items-center h-20 text-cyan-200 font-bold bg-gray-800 px-8 m-5 rounded-xl shadow-md">
    <!-- Left Title -->
    <RouterLink to="/" class="text-4xl">My Todo App</RouterLink>

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
