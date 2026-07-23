import React, { useState } from 'react';

/**
 * StudentProfile Component with Local Form State
 * Task 74
 */
const StudentProfile = () => {
  const [profile, setProfile] = useState({
    name: 'John Doe',
    email: 'john.doe@university.edu',
    semester: 6
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <div className="profile-card">
      <h2>Student Profile</h2>
      <form onSubmit={(e) => e.preventDefault()}>
        <div className="form-group">
          <label htmlFor="name">Full Name</label>
          <input 
            type="text" 
            id="name" 
            name="name" 
            value={profile.name} 
            onChange={handleChange} 
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email Address</label>
          <input 
            type="email" 
            id="email" 
            name="email" 
            value={profile.email} 
            onChange={handleChange} 
          />
        </div>
        <div className="form-group">
          <label htmlFor="semester">Current Semester</label>
          <input 
            type="number" 
            id="semester" 
            name="semester" 
            value={profile.semester} 
            onChange={handleChange} 
          />
        </div>
      </form>
    </div>
  );
};

export default StudentProfile;
