<template>
  <article class="course-card">
    <div class="card-header">
      <span class="code-badge">{{ code }}</span>
      <span class="credits-badge">{{ credits }} Credits</span>
    </div>
    <h3 style="font-size: 1.15rem; color: #0f172a; margin-bottom: 0.5rem;">{{ name }}</h3>
    <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 1rem;">Target Grade: {{ grade }}</p>
    <slot name="actions"></slot>
  </article>
</template>

<script setup>
// Define component props (Task 108)
defineProps({
  id: Number,
  name: String,
  code: String,
  credits: Number,
  grade: String
});
</script>

<style scoped>
/* Component scoped styles */
</style>
