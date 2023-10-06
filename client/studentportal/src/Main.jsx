
import React from 'react';

const Main = ({ setUserType }) => {
  const handleRoleSelect = (role) => {
    setUserType(role);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-3xl mb-6">Welcome to the School Management System</h1>
      <button
        onClick={() => handleRoleSelect('teacher')}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
      >
        Teacher
      </button>
      <button
        onClick={() => handleRoleSelect('student')}
        className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
      >
        Student
      </button>
    </div>
  );
};

export default Main;
