import { createSlice } from '@reduxjs/toolkit';

/**
 * Redux Toolkit Enrollment Slice (Tasks 87, 88)
 * Eliminates boilerplate using Immer for immutable state mutations.
 */
const initialState = {
  enrolledCourses: []
};

const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState,
  reducers: {
    enroll: (state, action) => {
      const course = action.payload;
      const exists = state.enrolledCourses.some(item => item.id === course.id);
      if (!exists) {
        state.enrolledCourses.push(course);
      }
    },
    unenroll: (state, action) => {
      const courseId = action.payload;
      state.enrolledCourses = state.enrolledCourses.filter(course => course.id !== courseId);
    }
  }
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;
