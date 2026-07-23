import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

/**
 * Pinia Store for Enrollment Management (Tasks 117, 149)
 * Setup Store syntax using Vue 3 Composition API refs and computed properties.
 */
export const useEnrollmentStore = defineStore('enrollment', () => {
  // State ref
  const enrolledCourses = ref([]);

  // Computed property: Sum of enrolled course credits
  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0);
  });

  // Action: Enroll course
  function enroll(course) {
    const exists = enrolledCourses.value.some(c => c.id === course.id);
    if (!exists) {
      enrolledCourses.value.push(course);
    }
  }

  // Action: Un-enroll course
  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId);
  }

  // Advanced Action: fetchAndEnroll (Task 149)
  async function fetchAndEnroll(courseId) {
    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${courseId}`);
      const data = await response.json();
      const course = {
        id: data.id,
        code: `CS${data.id * 101}`,
        name: data.title,
        credits: 4,
        grade: 'A'
      };
      enroll(course);
    } catch (err) {
      console.error('Failed to fetchAndEnroll:', err);
    }
  }

  // Action: Reset store
  function $reset() {
    enrolledCourses.value = [];
  }

  return {
    enrolledCourses,
    totalCredits,
    enroll,
    unenroll,
    fetchAndEnroll,
    $reset
  };
});
