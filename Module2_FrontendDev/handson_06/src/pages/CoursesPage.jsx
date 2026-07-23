import React from 'react';
import { useSelector } from 'react-redux';
import CourseCard from '../components/CourseCard';
import { courses } from '../data/courses';

const CoursesPage = () => {
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

  return (
    <div className="container">
      <h2 style={{ fontSize: '1.75rem', marginBottom: '1rem' }}>Course Directory</h2>
      <div className="course-grid">
        {courses.map(course => {
          const isEnrolled = enrolledCourses.some(item => item.id === course.id);
          return (
            <CourseCard 
              key={course.id} 
              course={course} 
              isEnrolled={isEnrolled} 
            />
          );
        })}
      </div>
    </div>
  );
};

export default CoursesPage;
