import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { unenroll } from '../store/enrollmentSlice';

/**
 * ProfilePage Component displaying enrolled courses and allowing un-enrollment (Tasks 84, 88, 89)
 */
const ProfilePage = () => {
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);
  const dispatch = useDispatch();

  const handleUnenroll = (id) => {
    dispatch(unenroll(id));
  };

  return (
    <div className="container">
      <h2 style={{ fontSize: '1.75rem', marginBottom: '1.5rem' }}>Student Profile & Enrolled Courses</h2>
      
      <div style={{ backgroundColor: 'white', padding: '1.5rem', borderRadius: '10px', marginBottom: '2rem', border: '1px solid #e2e8f0' }}>
        <h3>Student Information</h3>
        <p><strong>Name:</strong> John Doe</p>
        <p><strong>Email:</strong> john.doe@university.edu</p>
        <p><strong>Program:</strong> Computer Science B.S.</p>
      </div>

      <h3>Enrolled Courses ({enrolledCourses.length})</h3>
      
      {enrolledCourses.length === 0 ? (
        <p style={{ color: '#64748b', marginTop: '1rem' }}>No courses currently enrolled. Visit the Courses tab to add courses.</p>
      ) : (
        <div className="course-grid">
          {enrolledCourses.map(course => (
            <div key={course.id} className="course-card">
              <div>
                <span className="code-badge">{course.code}</span>
                <h4 style={{ margin: '0.5rem 0' }}>{course.name}</h4>
                <p style={{ fontSize: '0.85rem', color: '#64748b' }}>{course.credits} Credits</p>
              </div>
              <button 
                className="btn-danger" 
                onClick={() => handleUnenroll(course.id)}
                style={{ marginTop: '1rem' }}
              >
                Un-enroll
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default ProfilePage;
