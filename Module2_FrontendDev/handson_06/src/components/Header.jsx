import React from 'react';
import { Link, NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';

/**
 * Header Component with React Router Links and Redux State (Task 78, 89)
 */
const Header = () => {
  // Read state directly from Redux Store via useSelector selector
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

  return (
    <header className="site-header">
      <h1>
        <Link to="/">Student Portal</Link>
      </h1>
      <nav className="nav-links">
        <NavLink to="/" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
          Home
        </NavLink>
        <NavLink to="/courses" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
          Courses
        </NavLink>
        <NavLink to="/profile" className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}>
          Profile
        </NavLink>
        <span className="badge">Enrolled: {enrolledCourses.length}</span>
      </nav>
    </header>
  );
};

export default Header;
