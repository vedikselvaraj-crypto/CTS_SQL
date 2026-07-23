import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import { initialCourses } from './data/courses';

const App = () => {
  // Task 66: Component State setup with useState
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Task 71, 72, 73: useEffect API Fetching with loading and error states
  useEffect(() => {
    const fetchCoursesFromAPI = async () => {
      try {
        setLoading(true);
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
        if (!response.ok) {
          throw new Error('Failed to fetch courses data');
        }
        const data = await response.json();
        
        // Map posts data into course-like objects
        const mappedCourses = data.map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS${(index + 1) * 101}`,
          credits: (index % 2 === 0) ? 4 : 3,
          grade: 'A'
        }));
        
        setCourses(mappedCourses);
        setLoading(false);
      } catch (err) {
        console.error('API Fetch Error:', err);
        // Fallback to local data on API error
        setCourses(initialCourses);
        setError(err.message);
        setLoading(false);
      }
    };

    fetchCoursesFromAPI();
  }, []); // Empty dependency array [] ensures this effect runs ONCE on component mount (componentDidMount)

  // Task 75: useEffect logging course changes with dependency array explanation comment
  /**
   * DEPENDENCY ARRAY EXPLANATION:
   * The dependency array [courses] instructs React to re-run this effect ONLY when the 'courses' state reference changes.
   * If the dependency array is omitted, the effect will execute after EVERY single render, which can lead to infinite loops if the effect modifies state.
   * If an empty array [] is passed, it executes only once after the initial render.
   */
  useEffect(() => {
    if (courses.length > 0) {
      console.log('Courses updated in state:', courses);
    }
  }, [courses]);

  // Task 69: State lifting - Enroll handler passed to CourseCard
  const handleEnroll = (course) => {
    if (!enrolledCourses.some(item => item.id === course.id)) {
      setEnrolledCourses(prev => [...prev, course]);
    }
  };

  // Task 68: Real-time search filter logic
  const filteredCourses = courses.filter(course =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    course.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-wrapper">
      {/* Header receiving props (Task 64 & 70) */}
      <Header siteName="Student Portal" enrolledCount={enrolledCourses.length} />

      <main className="app-container">
        {/* Search Input (Task 68) */}
        <div className="search-container">
          <input
            type="text"
            className="search-input"
            placeholder="Search courses by name or code..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>

        {/* Conditional Rendering for Loading & Error States (Tasks 72 & 73) */}
        {loading && <div className="loading-state">Loading courses...</div>}
        {error && <div className="error-state">Notice: Using cached course data. ({error})</div>}

        {/* Dynamic Course Grid (Task 67) */}
        {!loading && (
          <div className="course-grid">
            {filteredCourses.map(course => (
              <CourseCard
                key={course.id}
                {...course}
                onEnroll={handleEnroll}
              />
            ))}
          </div>
        )}

        {/* Student Profile Form (Task 74) */}
        <StudentProfile />
      </main>

      {/* Footer (Task 63) */}
      <Footer />
    </div>
  );
};

export default App;
