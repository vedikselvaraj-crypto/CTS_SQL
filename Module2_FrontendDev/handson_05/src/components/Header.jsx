import React from 'react';

/**
 * Functional Header component receiving props
 * Tasks 62, 64 & 70
 */
const Header = ({ siteName, enrolledCount }) => {
  return (
    <header class="site-header">
      <h1>{siteName}</h1>
      <nav class="nav-links">
        <a href="#home">Home</a>
        <a href="#courses">Courses</a>
        <a href="#profile">Profile</a>
        <span class="enrolled-badge">Enrolled: {enrolledCount}</span>
      </nav>
    </header>
  );
};

export default Header;
