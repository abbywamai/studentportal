
import React from "react"; 
import{ BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from "./Homepage"
import LoginPage from "./Login";
import Main from "./Main";
import TeacherActions from "./TeacherAction";
import StudentActions from "./StudentAction";



function App() {
  
  return (
   <div>
     <HomePage />
     <LoginPage/>
     <Main/>
     <TeacherActions/>
     <StudentActions/>
   </div>
  )
}

export default App
