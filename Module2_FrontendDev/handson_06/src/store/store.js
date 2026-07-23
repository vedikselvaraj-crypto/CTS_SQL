import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './enrollmentSlice';

/**
 * Central Redux Store Setup (Task 86, 90)
 * Redux DevTools support is enabled by default in RTK configureStore.
 */
export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer
  },
  devTools: process.env.NODE_ENV !== 'production'
});
