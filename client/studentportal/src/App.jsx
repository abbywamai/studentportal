
import React from "react"; 
import{ BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from "./Homepage"
import LoginPage from "./Login";



function App() {
  
  return (
   <div>
     <HomePage />
     <LoginPage/>
   </div>
  )
}

export default App
