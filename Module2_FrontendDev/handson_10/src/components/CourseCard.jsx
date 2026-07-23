import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { enrollCourse, selectEnrolledCourses } from '../store/coursesSlice';
import { enrollStudent } from '../api/courseApi';

/**
 * CourseCard Component consuming Centralized API & Redux Store (Task 142)
 */
const CourseCard = ({ course }) => {
  const dispatch = useDispatch();
  const enrolledCourses = useSelector(selectEnrolledCourses);

  const isEnrolled = enrolledCourses.some(c => c.id === course.id);

  const handleEnroll = async () => {
    try {
      // Call Central API function (Task 142)
      await enrollStudent(101, course.id);
      // Dispatch Redux Action
      dispatch(enrollCourse(course));
    } catch (err) {
      console.error('Failed to enroll student via API:', err);
    }
  };

  return (
    <article className="course-card">
      <div>
        <div className="card-header">
          <span className="code-badge">{course.code}</span>
          <span className="credits-badge">{course.credits} Credits</span>
        </div>
        <h3 style="font-size: 1.15rem; color: #0f172a; margin-bottom: 0.5rem;">{course.name}</h3>
        <p style={{ color: '#64748b', fontSize: '0.9rem', marginBottom: '1rem' }}>{course.description}</p>
      </div>

      <div>
        {!isEnrolled ? (
          <button className="btn-primary" onClick={handleEnroll} style={{ width: '100%' }}>
            Enroll via Central API
          </button>
        ) : (
          <button className="btn-primary" disabled style={{ width: '100%', backgroundColor: '#94a3b8' }}>
            Enrolled
          </button>
        )}
      </div>
    </article>
  );
};

export default CourseCard;
