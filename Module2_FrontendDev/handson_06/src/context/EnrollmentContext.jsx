import React, { createContext, useState } from 'react';

/**
 * Global Enrollment Context (Task 81, 84)
 * Demonstrated as an alternative to Redux Toolkit to showcase Context API patterns.
 */
export const EnrollmentContext = createContext();

export const EnrollmentProvider = ({ children }) => {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enrollCourse = (course) => {
    if (!enrolledCourses.some(item => item.id === course.id)) {
      setEnrolledCourses(prev => [...prev, course]);
    }
  };

  const unenrollCourse = (courseId) => {
    setEnrolledCourses(prev => prev.filter(c => c.id !== courseId));
  };

  return (
    <EnrollmentContext.Provider value={{ enrolledCourses, enrollCourse, unenrollCourse }}>
      {children}
    </EnrollmentContext.Provider>
  );
};
