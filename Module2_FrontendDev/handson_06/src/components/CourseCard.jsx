import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { enroll } from '../store/enrollmentSlice';

/**
 * CourseCard Component utilizing useNavigate & Redux useDispatch (Tasks 80, 88)
 */
const CourseCard = ({ course, isEnrolled }) => {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleEnrollClick = () => {
    // Task 88: Dispatch Redux enroll action
    dispatch(enroll(course));
    
    // Task 80: Programmatic navigation to /profile after enrollment
    navigate('/profile');
  };

  return (
    <article className="course-card">
      <div className="card-header">
        <span className="code-badge">{course.code}</span>
        <span className="credits-badge">{course.credits} Credits</span>
      </div>
      <h3>{course.name}</h3>
      <p style={{ color: '#64748b', fontSize: '0.9rem', margin: '0.5rem 0' }}>{course.description}</p>
      
      <div className="card-actions">
        <button 
          className="btn-details" 
          onClick={() => navigate(`/courses/${course.id}`)}
        >
          View Details
        </button>
        
        {!isEnrolled && (
          <button className="btn-primary" onClick={handleEnrollClick}>
            Enroll Now
          </button>
        )}
      </div>
    </article>
  );
};

export default CourseCard;
