import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import CoursesPage from './pages/CoursesPage';
import ProfilePage from './pages/ProfilePage';

const App = () => {
  return (
    <div className="app">
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<CoursesPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </main>
      <footer className="site-footer">
        <p>&copy; 2026 Student Portal | Centralized Axios API & Advanced State Management</p>
      </footer>
    </div>
  );
};

export default App;
