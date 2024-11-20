import React, { useEffect, useState } from 'react';
import { Music, Github } from 'lucide-react';
import { Link } from 'react-router-dom';

export const Navbar = ({ darkMode, setDarkMode }) => {
  const [hasShadow, setHasShadow] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setHasShadow(window.scrollY > 0);
    };
    window.addEventListener('scroll', handleScroll);

    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
      <nav className={`fixed top-0 w-full bg-gray-100 border-b dark:border-gray-800 dark:bg-gray-900 px-12 z-10 transition-shadow ${hasShadow ? 'shadow-md' : ''}`}>

      <div className="mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-20">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Music className="h-8 w-8 text-blue-500" />
              <span className={`ml-2 text-xl font-bold ${darkMode ? 'text-gray-200' : 'text-gray-800'}`}>GenreAI</span>
            </div>
            <div className="ml-6 flex space-x-8">
              <Link to="/" className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-700 hover:text-black dark:text-gray-400 dark:hover:text-gray-100">
                Home
              </Link>
              <Link to="/about" className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-700 hover:text-black dark:text-gray-400 hover:text-gray-900 hover:dark:text-gray-100">
                About
              </Link>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            <a href="https://github.com" target="_blank" rel="noopener noreferrer" className={darkMode ? 'text-gray-400 hover:text-gray-200' : 'text-gray-500 hover:text-gray-900'}>
              <Github className="h-6 w-6" />
            </a>
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="px-4 py-2 rounded bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200 transition duration-150 transform active:scale-95 hover:opacity-90"
            >
              {darkMode ? 'Light Mode' : 'Dark Mode'}
            </button>

          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
