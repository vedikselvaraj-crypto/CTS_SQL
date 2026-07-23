import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import CoursesView from '../views/CoursesView.vue';
import CourseDetailView from '../views/CourseDetailView.vue';
import ProfileView from '../views/ProfileView.vue';

/**
 * Vue Router Route Definitions (Task 112)
 */
const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/courses', name: 'courses', component: CoursesView },
  { path: '/courses/:id', name: 'course-detail', component: CourseDetailView },
  { path: '/profile', name: 'profile', component: ProfileView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Navigation Guard (Task 116)
router.beforeEach((to, from) => {
  console.log(`[Vue Router Guard] Navigating to: ${to.fullPath} (from ${from.fullPath})`);
});

export default router;
