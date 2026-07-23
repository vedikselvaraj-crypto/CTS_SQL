<template>
  <div class="container">
    <div style="background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%); padding: 3rem 2rem; border-radius: 12px; border: 1px solid #e2e8f0; text-align: center;">
      <h2 style="font-size: 2.2rem; color: #0f172a; margin-bottom: 1rem;">Welcome to Student Portal (Vue 3)</h2>
      <p style="color: #475569; max-width: 600px; margin: 0 auto 1.5rem auto;">
        Built using Vue 3 Composition API (`<script setup>`), Vue Router for SPA navigation, and Pinia for reactive global state management.
      </p>
      <RouterLink to="/courses" class="btn-primary">Browse Courses</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>
