<template>
  <div class="container">
    <h2 style="font-size: 1.75rem; margin-bottom: 1rem;">Course Directory</h2>

    <!-- Search Input with v-model (Task 111) -->
    <div class="search-box">
      <input 
        type="text" 
        class="search-input" 
        placeholder="Search courses by name or code..."
        v-model="searchTerm"
      >
    </div>

    <!-- Course Cards Grid using v-for & v-bind shorthand (Task 110) -->
    <div class="course-grid">
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id"
        :id="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      >
        <template #actions>
          <div style="display: flex; gap: 0.5rem; margin-top: 1rem;">
            <RouterLink :to="`/courses/${course.id}`" class="btn-primary" style="background-color: transparent; color: #2563eb; border: 1px solid #bfdbfe;">
              Details
            </RouterLink>
            <button class="btn-primary" @click="handleEnroll(course)">
              Enroll
            </button>
          </div>
        </template>
      </CourseCard>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import CourseCard from '../components/CourseCard.vue';
import { useEnrollmentStore } from '../stores/enrollment';

// Tasks 109 & 111: Reactive state & Composition API
const courses = ref([]);
const searchTerm = ref('');
const enrollmentStore = useEnrollmentStore(); // Task 118: Pinia Store

onMounted(() => {
  // Initialize with 5 course objects (Task 109)
  courses.value = [
    { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4, grade: 'A' },
    { id: 2, name: 'Full Stack Web Development', code: 'CS202', credits: 4, grade: 'A-' },
    { id: 3, name: 'Database Management Systems', code: 'CS303', credits: 3, grade: 'B+' },
    { id: 4, name: 'Software Engineering', code: 'CS404', credits: 3, grade: 'A' },
    { id: 5, name: 'Computer Networks', code: 'CS505', credits: 4, grade: 'B' }
  ];
});

// Task 111: Computed property for filtering
const filteredCourses = computed(() => {
  if (!searchTerm.value.trim()) return courses.value;
  const term = searchTerm.value.toLowerCase();
  return courses.value.filter(c => 
    c.name.toLowerCase().includes(term) || 
    c.code.toLowerCase().includes(term)
  );
});

// Task 118: Call store.enroll on click
const handleEnroll = (course) => {
  enrollmentStore.enroll(course);
};
</script>
