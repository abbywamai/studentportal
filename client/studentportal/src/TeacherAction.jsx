import React, { useState } from 'react';
import axios from 'axios';

const TeacherActions = () => {
  const [studentId, setStudentId] = useState('');
  const [courseId, setCourseId] = useState('');
  const [gradeValue, setGradeValue] = useState('');

  const handlePostGrade = async () => {
    try {
      const response = await axios.post('http://localhost:5000/teacher/postgrades', {
        student_id: studentId,
        course_id: courseId,
        grade_value: gradeValue
      });
      alert('Grade posted successfully');
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="max-w-md mx-auto my-4 p-6 bg-white rounded shadow-lg">
      <h2 className="text-2xl font-bold mb-4">Teacher Actions</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Student ID"
          value={studentId}
          onChange={(e) => setStudentId(e.target.value)}
          className="w-full px-4 py-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Course ID"
          value={courseId}
          onChange={(e) => setCourseId(e.target.value)}
          className="w-full px-4 py-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <input
          type="text"
          placeholder="Grade Value"
          value={gradeValue}
          onChange={(e) => setGradeValue(e.target.value)}
          className="w-full px-4 py-2 border rounded"
        />
      </div>
      <button
        onClick={handlePostGrade}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Post Grade
      </button>
    </div>
  );
};

export default TeacherActions;
