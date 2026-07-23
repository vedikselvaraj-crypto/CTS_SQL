import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { selectEnrolledCourses } from '../store/coursesSlice';

const Header = () => {
  const enrolledCourses = useSelector(selectEnrolledCourses);

  return (
    <header className="site-header">
      <Link to="/" className="site-title">Student Portal (Central API)</Link>
      <nav className="nav-links">
        <NavLink to="/" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
          Courses
        </NavLink>
        <NavLink to="/profile" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
          Profile ({enrolledCourses.length})
        </NavLink>
      </nav>
    </header>
  );
};

export default Header;
