import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div className="container">
      <div className="hero-box">
        <h2>Welcome to the Student Portal (React SPA)</h2>
        <p style={{ color: '#475569', marginBottom: '1.5rem', maxWidth: '600px', margin: '0 auto 1.5rem auto' }}>
          Explore our modern curriculum, enroll in courses, view real-time state updates powered by Redux Toolkit and React Router v6.
        </p>
        <Link to="/courses" className="btn-primary">
          Browse Course Directory
        </Link>
      </div>
    </div>
  );
};

export default HomePage;
