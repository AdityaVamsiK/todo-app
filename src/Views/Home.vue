<script setup>
    import { ref } from 'vue'

  import Navbar from '../components/Navbar.vue'
  import HomePendingTasks from '../components/HomePendingTasks.vue'
  import HomeCompletedTasks from '../components/HomeCompletedTasks.vue'

  var newTask = ref('')

  function addNewTask(){
    console.log("Adding New Task")
    newTask.value = ''
  }
</script>

<template>
    <div class="min-h-screen bg-gray-900">
        <!-- Navbar on top -->
        <Navbar />

        <!-- Two task components side-by-side -->
        <div class="flex justify-center gap-10 px-10 py-6">
            <HomePendingTasks />
            <HomeCompletedTasks />
        </div>
        <div class="flex justify-center items-center text-2xl text-cyan-200 mt-5">
            Add New Task:&nbsp;  
            <input type="text" v-model="newTask" class="justify-center border-2 items-center w-2xl" @keyup.enter="addNewTask">
        </div>
  </div>
</template> 