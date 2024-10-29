// Navbar.js
import React from 'react';
import { Music, Github } from 'lucide-react';
import { Link } from 'react-router-dom';
import axios from 'axios';

// function to make API call to backend
const testRequest = () => {
  axios.get('http://localhost:8080').then((data) => {
    console.log(data);
  });
};

export const Navbar = () => (
  <nav className="bg-white shadow-md px-16">
    <div className="mx-auto px-4 sm:px-6 lg:px-8">
      <div className="flex justify-between h-16">
        <div className="flex">
          <div className="flex-shrink-0 flex items-center">
            <Music className="h-8 w-8 text-blue-500" />
            <span className="ml-2 text-xl font-bold text-gray-800">GenreAI</span>
          </div>
          <div className="ml-6 flex space-x-8">
            <Link to="/" className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900">
              Home
            </Link>
            <Link to="/about" className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 hover:text-gray-900">
              About
            </Link>
            <button onClick={testRequest}>LOCAL API TEST!</button>
          </div>
        </div>
        <div className="flex items-center">
          <a href="https://github.com" target="_blank" rel="noopener noreferrer" className="text-gray-500 hover:text-gray-900">
            <Github className="h-6 w-6" />
          </a>
        </div>
      </div>
    </div>
  </nav>
);

export default Navbar;  // Change this line to use default export
