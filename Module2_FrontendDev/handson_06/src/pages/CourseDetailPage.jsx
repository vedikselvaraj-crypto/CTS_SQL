import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { enroll } from '../store/enrollmentSlice';
import { courses } from '../data/courses';

/**
 * CourseDetailPage utilizing useParams hook (Task 79)
 */
const CourseDetailPage = () => {
  const { courseId } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

  const course = courses.find(c => c.id === parseInt(courseId, 10));

  if (!course) {
    return (
      <div className="container">
        <h2>Course Not Found</h2>
        <p>No course exists with ID: {courseId}</p>
        <button className="btn-primary" onClick={() => navigate('/courses')} style={{ marginTop: '1rem' }}>
          Back to Courses
        </button>
      </div>
    );
  }

  const isEnrolled = enrolledCourses.some(item => item.id === course.id);

  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate('/profile');
  };

  return (
    <div className="container">
      <div className="detail-card">
        <span className="code-badge">{course.code}</span>
        <h2 style={{ fontSize: '2rem', margin: '0.5rem 0' }}>{course.name}</h2>
        <p style={{ fontSize: '1.1rem', color: '#475569', marginBottom: '1.5rem' }}>{course.description}</p>
        <div style={{ marginBottom: '1.5rem' }}>
          <p><strong>Credits:</strong> {course.credits}</p>
          <p><strong>Expected Grade Target:</strong> {course.grade}</p>
        </div>

        <div style={{ display: 'flex', gap: '1rem' }}>
          <button className="btn-details" onClick={() => navigate('/courses')}>
            &larr; Back to Directory
          </button>
          {!isEnrolled ? (
            <button className="btn-primary" onClick={handleEnroll}>
              Enroll in Course
            </button>
          ) : (
            <span className="badge" style={{ padding: '0.6rem 1rem', fontSize: '1rem' }}>Already Enrolled</span>
          )}
        </div>
      </div>
    </div>
  );
};

export default CourseDetailPage;
