import React from 'react';

/**
 * Functional CourseCard component receiving props
 * Tasks 65 & 69
 */
const CourseCard = ({ id, name, code, credits, grade, onEnroll }) => {
  return (
    <article className="course-card">
      <div className="card-header">
        <span className="course-code">{code}</span>
        <span className="course-credits">{credits} Credits</span>
      </div>
      <h3 className="course-name">{name}</h3>
      <div className="card-footer">
        <span className="grade">Grade: {grade}</span>
        <button 
          className="btn-enroll" 
          onClick={() => onEnroll({ id, name, code, credits, grade })}
        >
          Enroll
        </button>
      </div>
    </article>
  );
};

export default CourseCard;
