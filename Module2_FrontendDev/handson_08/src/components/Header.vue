<template>
  <header class="site-header">
    <RouterLink to="/" class="site-title">Student Portal (Vue 3)</RouterLink>
    <nav class="nav-links">
      <RouterLink to="/" class="nav-link">Home</RouterLink>
      <RouterLink to="/courses" class="nav-link">Courses</RouterLink>
      <RouterLink to="/profile" class="nav-link">Profile</RouterLink>
      <!-- Display enrolled count from Pinia Store (Task 120) -->
      <span class="badge">Enrolled: {{ enrollmentStore.enrolledCourses.length }}</span>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

const enrollmentStore = useEnrollmentStore();
</script>

<style scoped>
/* Component scoped styles */
</style>
