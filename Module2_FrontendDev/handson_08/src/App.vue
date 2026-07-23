<template>
  <div class="app-container">
    <Header />
    <main>
      <!-- Task 113: RouterView Outlet -->
      <RouterView />
    </main>
    <footer class="site-footer">
      <p>&copy; 2026 Student Portal Vue 3 Application | Composition API, Vue Router & Pinia</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
import Header from './components/Header.vue';
</script>
