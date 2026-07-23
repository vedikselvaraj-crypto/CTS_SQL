import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { selectEnrolledCourses, unenrollCourse } from '../store/coursesSlice';

const ProfilePage = () => {
  const enrolledCourses = useSelector(selectEnrolledCourses);
  const dispatch = useDispatch();

  return (
    <div className="container">
      <h2 style={{ marginBottom: '1.5rem' }}>Student Profile & Central API Registrations</h2>
      
      <div style={{ backgroundColor: 'white', padding: '1.5rem', borderRadius: '10px', border: '1px solid #e2e8f0', marginBottom: '2rem' }}>
        <h3>Active Student Session</h3>
        <p><strong>Authorization Token:</strong> Bearer mock-jwt-token-xyz-12345</p>
        <p><strong>API Base URL:</strong> https://jsonplaceholder.typicode.com</p>
        <p style={{ color: '#2563eb', fontWeight: '600', marginTop: '0.5rem' }}>
          Enrolled Count: {enrolledCourses.length}
        </p>
      </div>

      <h3>Enrolled Courses List</h3>
      {enrolledCourses.length === 0 ? (
        <p style={{ color: '#64748b', marginTop: '1rem' }}>No courses enrolled yet.</p>
      ) : (
        <div className="course-grid">
          {enrolledCourses.map(course => (
            <div key={course.id} className="course-card">
              <div>
                <span className="code-badge">{course.code}</span>
                <h4 style={{ margin: '0.5rem 0' }}>{course.name}</h4>
                <p style={{ fontSize: '0.85rem', color: '#64748b' }}>{course.credits} Credits</p>
              </div>
              <button className="btn-danger" onClick={() => dispatch(unenrollCourse(course.id))} style={{ marginTop: '1rem' }}>
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
