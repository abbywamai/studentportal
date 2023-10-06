import React, { useState } from 'react';
import axios from 'axios';

const StudentActions = () => {
  const [studentName, setStudentName] = useState('');
  const [myGrade, setMyGrade] = useState('');

  const checkGrade = async () => {
    try {
      const response = await axios.get(`/student/grades?studentName=${studentName}`);
      setMyGrade(response.data.grade);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="max-w-md mx-auto my-4 p-6 bg-white rounded shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Student Actions</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Enter student's full name"
          value={studentName}
          onChange={(e) => setStudentName(e.target.value)}
          className="w-full px-4 py-2 border rounded"
        />
      </div>
      <button onClick={checkGrade} className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Check My Grade
      </button>
      <p className="mt-4">{`Name: ${studentName} Grade: ${myGrade}`}</p>
    </div>
  );
};

export default StudentActions;

