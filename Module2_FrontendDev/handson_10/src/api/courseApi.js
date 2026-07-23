import apiClient from './apiClient';

/**
 * Course Service API Functions (Task 139)
 */

export const getAllCourses = async () => {
  // Fetch first 5 posts mapped to course entities
  const posts = await apiClient.get('/posts?_limit=5');
  return posts.map((post, index) => ({
    id: post.id,
    name: post.title,
    code: `CS${(index + 1) * 101}`,
    credits: (index % 2 === 0) ? 4 : 3,
    grade: 'A',
    description: post.body
  }));
};

export const getCourseById = async (id) => {
  const post = await apiClient.get(`/posts/${id}`);
  return {
    id: post.id,
    name: post.title,
    code: `CS${post.id * 101}`,
    credits: 4,
    grade: 'A',
    description: post.body
  };
};

export const enrollStudent = async (studentId, courseId) => {
  return await apiClient.post('/posts', {
    userId: studentId,
    courseId: courseId,
    enrolledAt: new Date().toISOString()
  });
};
