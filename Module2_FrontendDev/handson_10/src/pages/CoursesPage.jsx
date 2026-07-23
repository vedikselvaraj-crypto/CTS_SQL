import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { 
  fetchAllCourses, 
  selectCourses, 
  selectCoursesLoading, 
  selectCoursesError 
} from '../store/coursesSlice';
import CourseCard from '../components/CourseCard';

/**
 * CoursesPage Component using Redux createAsyncThunk & Selectors (Tasks 145, 146, 148, 149, 151)
 * 
 * ===================================================================================
 * TASK 148: NgRx CONCEPT (ANGULAR STATE MANAGEMENT ARCHITECTURE)
 * ===================================================================================
 * NgRx follows the Redux Pattern adapted for RxJS Observables in Angular:
 * Components -> dispatch Action -> Effect listens & calls API -> API returns Observable ->
 * Effect dispatches Success Action -> Reducer updates State immutably -> Selectors project State ->
 * Component receives updated State via Async Pipe.
 * 
 * Data Flow Architecture:
 * Component -> Action -> Effect -> Service (HttpClient) -> Reducer -> Store -> Selector -> Component
 * 
 * ===================================================================================
 * TASK 149: PINIA ADVANCED PATTERNS (VUE 3 STATE MANAGEMENT)
 * ===================================================================================
 * Pinia provides a direct, low-boilerplate state solution for Vue 3 using Composition API:
 * 1. Setup Store syntax (ref, computed, function actions).
 * 2. storeToRefs(store) extracts reactive state refs while preserving reactivity.
 * 3. store.$reset() resets store state to initial state.
 * 4. Async actions execute API calls directly inside store actions without extra thunks.
 * ===================================================================================
 */
const CoursesPage = () => {
  const dispatch = useDispatch();
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  // Task 145: Dispatch async thunk on component mount
  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  return (
    <div className="container">
      <h2>Course Directory (Centralized API & Async Thunk)</h2>
      <p style={{ color: '#64748b', marginBottom: '1.5rem' }}>
        Data fetched using <code>apiClient.js</code> instance with Axios request/response interceptors.
      </p>

      {/* Loading Indicator */}
      {loading && <div className="loading-spinner">Loading courses via Redux Async Thunk...</div>}

      {/* Task 147: Error Handling UI */}
      {error && (
        <div className="error-banner">
          <h3>API Request Rejected</h3>
          <p>{error}</p>
          <button className="btn-primary" onClick={() => dispatch(fetchAllCourses())} style={{ marginTop: '0.75rem' }}>
            Retry Fetching Courses
          </button>
        </div>
      )}

      {/* Course Grid */}
      {!loading && !error && (
        <div className="course-grid">
          {courses.map(course => (
            <CourseCard key={course.id} course={course} />
          ))}
        </div>
      )}

      {/* Task 151: Framework State Management Comparison Section */}
      <section className="comparison-box">
        <h3 style={{ color: '#0f172a', marginBottom: '0.5rem' }}>
          Framework State Management Comparison (Task 151)
        </h3>
        <p style={{ color: '#475569', fontSize: '0.95rem' }}>
          Analysis of state management patterns across React (Redux Toolkit), Angular (NgRx), and Vue 3 (Pinia).
        </p>

        <table className="comparison-table">
          <thead>
            <tr>
              <th>Feature / Metric</th>
              <th>React (Redux Toolkit)</th>
              <th>Angular (NgRx)</th>
              <th>Vue 3 (Pinia)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Architecture</strong></td>
              <td>Slice, Reducer, Thunk, Selector</td>
              <td>Actions, Reducers, Effects, Selectors</td>
              <td>Setup Store (ref, computed, actions)</td>
            </tr>
            <tr>
              <td><strong>Boilerplate Level</strong></td>
              <td>Moderate (significantly simplified via RTK)</td>
              <td>High (requires action types & effects)</td>
              <td>Very Low (native Composition API style)</td>
            </tr>
            <tr>
              <td><strong>Reactivity Model</strong></td>
              <td>Immutable draft state via Immer</td>
              <td>RxJS Observables & Immutable state</td>
              <td>Direct Vue Reactivity (`ref`, `reactive`)</td>
            </tr>
            <tr>
              <td><strong>Async Handling</strong></td>
              <td>`createAsyncThunk` middleware</td>
              <td>NgRx Effects (`Actions.pipe(...)`)</td>
              <td>Async action functions directly in store</td>
            </tr>
            <tr>
              <td><strong>Learning Curve</strong></td>
              <td>Moderate</td>
              <td>Steep (Requires deep RxJS knowledge)</td>
              <td>Gentle</td>
            </tr>
          </tbody>
        </table>
      </section>
    </div>
  );
};

export default CoursesPage;
