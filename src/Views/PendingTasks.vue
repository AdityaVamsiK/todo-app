<script setup>
    import PendingTasks from '../components/PendingTasks.vue'
    import Navbar from '../components/Navbar.vue';
</script>

<template>
    <div class="min-h-screen bg-gray-900">
        <!-- Navbar on top -->
        <Navbar />
        <PendingTasks />
    </div>
</template>