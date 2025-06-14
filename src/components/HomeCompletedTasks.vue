<script setup>
    import { ref, computed } from 'vue';
    import taskData from '../tasks.json'
    const tasks = ref(taskData.tasks)

    const filteredTasks = computed(() => {
      return tasks.value.filter((task) => task.Status === 'Complete')
    })


    function onSelect(id){
      for(var task of tasks.value){
        if(task.id === id){
          if(task.Status === 'Incomplete'){
            task.Status = 'Complete'
          }else{
            task.Status = 'Incomplete'
          }
        }
      }
      console.log('In the function')
      console.log(tasks.value)
    }
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <div class="flex flex-col bg-gray-800 rounded-xl w-[24rem] min-h-[400px] py-4">

      <!-- Fixed Header -->
      <div class="flex justify-center items-center bg-gray-700 h-20 mb-4 w-4/5 rounded-xl self-center">
        <span class="text-cyan-200 text-2xl font-bold">My Finished Tasks ...</span>
      </div>

      <!-- Scrollable or auto-expanding Task list -->
      <div class="flex flex-col items-center space-y-3">
        <div
          v-for="task in filteredTasks"
          :key="task.id"
          class="flex justify-between items-center bg-gray-700 min-h-[5rem] w-4/5 rounded-xl text-cyan-200 text-lg px-4 font-medium text-center"
        >
          <span class="text-left w-full">{{ task.Description }}</span>
          <input
            type="checkbox"
            checked
            name="status"
            :id="task.id"
            class="ml-3"
            @change="onSelect(task.id)"
          />
        </div>
      </div>

    </div>
  </div>
</template>
