import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { getAllCourses } from '../api/courseApi';

/**
 * Async Thunk for API Call (Task 143)
 */
export const fetchAllCourses = createAsyncThunk(
  'courses/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      const data = await getAllCourses();
      return data;
    } catch (error) {
      return rejectWithValue(error.message || 'Failed to fetch courses from server');
    }
  }
);

/**
 * Advanced Redux Toolkit Slice (Tasks 143, 144)
 */
const coursesSlice = createSlice({
  name: 'courses',
  initialState: {
    coursesList: [],
    enrolledCourses: [],
    loading: false,
    error: null
  },
  reducers: {
    enrollCourse: (state, action) => {
      const course = action.payload;
      if (!state.enrolledCourses.some(c => c.id === course.id)) {
        state.enrolledCourses.push(course);
      }
    },
    unenrollCourse: (state, action) => {
      state.enrolledCourses = state.enrolledCourses.filter(c => c.id !== action.payload);
    }
  },
  // Task 144: Handle Async Thunk Lifecycles in extraReducers
  extraReducers: (builder) => {
    builder
      .addCase(fetchAllCourses.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchAllCourses.fulfilled, (state, action) => {
        state.coursesList = action.payload;
        state.loading = false;
      })
      .addCase(fetchAllCourses.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload || 'Failed to load courses';
      });
  }
});

export const { enrollCourse, unenrollCourse } = coursesSlice.actions;

// Task 146: Decoupled Selectors
export const selectCourses = (state) => state.courses.coursesList;
export const selectEnrolledCourses = (state) => state.courses.enrolledCourses;
export const selectCoursesLoading = (state) => state.courses.loading;
export const selectCoursesError = (state) => state.courses.error;

export default coursesSlice.reducer;
