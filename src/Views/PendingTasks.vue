<script setup>
    import HomePendingTasks from '../components/HomePendingTasks.vue'
    import Navbar from '../components/Navbar.vue';
</script>

<template>
    <div class="min-h-screen bg-gray-900">
        <!-- Navbar on top -->
        <Navbar />
        <HomePendingTasks />
    </div>
</template>