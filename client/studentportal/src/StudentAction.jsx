import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentActions = ({ userType }) => {
  const [studentName, setStudentName] = useState('');
  const [myGrade, setMyGrade] = useState('');

  const checkGrade = async () => {
    try {
      const response = await axios.get(`/api/get-grade?studentName=${studentName}`);
      setMyGrade(response.data.grade);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    if (userType === 'student') {
      checkGrade();
    }
  }, [userType]);

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded-md shadow-md">
      <h1 className="text-xl font-bold mb-4">Student Actions</h1>
      {userType === 'student' && (
        <>
          <div className="mb-4">
            <input
              type="text"
              placeholder="Enter student's full name"
              value={studentName}
              onChange={(e) => setStudentName(e.target.value)}
              className="border p-2 w-full rounded-md"
            />
          </div>
          <button
            onClick={checkGrade}
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Check My Grade
          </button>
          <p className="mt-4">{`Name: ${studentName} Grade: ${myGrade}`}</p>
        </>
      )}
    </div>
  );
};

export default StudentActions;

