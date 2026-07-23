<template>
  <div class="container">
    <h2 style="font-size: 1.75rem; margin-bottom: 1.5rem;">Student Profile (Pinia State Management)</h2>

    <div style="background: white; padding: 1.5rem; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 2rem;">
      <h3>Student Info</h3>
      <p><strong>Name:</strong> Jane Smith</p>
      <p><strong>Program:</strong> Software Engineering B.S.</p>
      <!-- Task 119: Display total credits from store computed property -->
      <p style="margin-top: 0.5rem; font-weight: 700; color: #2563eb;">
        Total Enrolled Credits: {{ totalCredits }}
      </p>
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
      <h3>Enrolled Courses ({{ enrolledCourses.length }})</h3>
      <button v-if="enrolledCourses.length > 0" class="btn-danger" @click="enrollmentStore.$reset()">
        Clear All Enrollments ($reset)
      </button>
    </div>

    <!-- Task 119: Render enrolled courses using v-for -->
    <div v-if="enrolledCourses.length > 0" class="course-grid">
      <div v-for="course in enrolledCourses" :key="course.id" class="course-card">
        <div>
          <span class="code-badge">{{ course.code }}</span>
          <h4 style="margin: 0.5rem 0;">{{ course.name }}</h4>
          <p style="font-size: 0.85rem; color: #64748b;">{{ course.credits }} Credits</p>
        </div>
        <button class="btn-danger" @click="enrollmentStore.unenroll(course.id)" style="margin-top: 1rem;">
          Un-enroll
        </button>
      </div>
    </div>
    <div v-else style="color: #64748b; padding: 1rem 0;">
      No courses currently enrolled.
    </div>
  </div>
</template>

<script setup>
import { storeToRefs } from 'pinia'; // Task 149: storeToRefs helper
import { useEnrollmentStore } from '../stores/enrollment';

const enrollmentStore = useEnrollmentStore();

// Task 149: Use storeToRefs to destructure reactive state & computed properties without losing reactivity
const { enrolledCourses, totalCredits } = storeToRefs(enrollmentStore);
</script>
