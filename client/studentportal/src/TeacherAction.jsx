import React, { useState } from 'react';
import axios from 'axios';

const TeacherActions = ({ userType }) => {
  const [studentId, setStudentId] = useState('');
  const [newGrade, setNewGrade] = useState('');

  const handleGradeChange = async () => {
    try {
      await axios.post('/api/change-grade', { studentId, newGrade });
      alert('Grade changed');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded-md shadow-md">
      <h1 className="text-xl font-bold mb-4">Teacher Actions</h1>
      {userType === 'teacher' && (
        <>
          <div className="mb-4">
            <input
              type="text"
              placeholder="Enter student's ID"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
              className="border p-2 w-full rounded-md"
            />
          </div>
          <div className="mb-4">
            <input
              type="text"
              placeholder="Enter new grade"
              value={newGrade}
              onChange={(e) => setNewGrade(e.target.value)}
              className="border p-2 w-full rounded-md"
            />
          </div>
          <button
            onClick={handleGradeChange}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Change Grade
          </button>
        </>
      )}
    </div>
  );
};

export default TeacherActions;

