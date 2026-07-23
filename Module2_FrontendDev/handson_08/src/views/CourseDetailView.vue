<template>
  <div class="container">
    <div v-if="course" style="background: white; padding: 2rem; border-radius: 10px; border: 1px solid #e2e8f0;">
      <span class="code-badge">{{ course.code }}</span>
      <h2 style="font-size: 2rem; margin: 0.5rem 0;">{{ course.name }}</h2>
      <p style="color: #475569; margin-bottom: 1.5rem;">
        Master key concepts and build real-world projects in {{ course.name }}.
      </p>
      <p style="margin-bottom: 0.5rem;"><strong>Credits:</strong> {{ course.credits }}</p>
      <p style="margin-bottom: 1.5rem;"><strong>Target Grade:</strong> {{ course.grade }}</p>

      <div style="display: flex; gap: 1rem;">
        <RouterLink to="/courses" class="btn-primary" style="background-color: transparent; color: #2563eb; border: 1px solid #bfdbfe;">
          &larr; Back to Courses
        </RouterLink>
        <button class="btn-primary" @click="handleEnrollAndRedirect">
          Enroll & View Profile
        </button>
      </div>
    </div>
    <div v-else style="padding: 2rem; text-align: center;">
      <p>Course not found.</p>
      <RouterLink to="/courses" class="btn-primary" style="margin-top: 1rem;">Back to Directory</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter, RouterLink } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

// Tasks 114 & 115: useRoute and useRouter
const route = useRoute();
const router = useRouter();
const enrollmentStore = useEnrollmentStore();
const course = ref(null);

const coursesData = [
  { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4, grade: 'A' },
  { id: 2, name: 'Full Stack Web Development', code: 'CS202', credits: 4, grade: 'A-' },
  { id: 3, name: 'Database Management Systems', code: 'CS303', credits: 3, grade: 'B+' },
  { id: 4, name: 'Software Engineering', code: 'CS404', credits: 3, grade: 'A' },
  { id: 5, name: 'Computer Networks', code: 'CS505', credits: 4, grade: 'B' }
];

onMounted(() => {
  const courseId = parseInt(route.params.id, 10); // Task 114
  course.value = coursesData.find(c => c.id === courseId);
});

const handleEnrollAndRedirect = () => {
  if (course.value) {
    enrollmentStore.enroll(course.value);
    router.push('/profile'); // Task 115: Programmatic navigation to /profile
  }
};
</script>
