// Author: Andrew Gaynor
// Date Accessed: October 10, 2024
// Starter frontend application with React and Express
// Adapted from source URL:
//      https://dev.to/techcheck/creating-a-react-node-and-express-app-1ieg

// App.js
import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';  // Import Navbar once
import Footer from './components/Footer';
import { MusicGenreClassifier } from './components/MusicGenreClassifier';
import Home from './pages/Home';
import About from './pages/About';

function App() {
  return (
    <Router>
      <Navbar/>
      <div className="App">
        <main className="">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
