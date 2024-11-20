// Updated Footer Component
import React from 'react';
import { Github, Mail } from "lucide-react";

const Footer = () => {
  return (
< footer className="h-[10vh] bg-gray-100 dark:bg-gray-900 text-gray-700 dark:text-gray-400 border-t dark:border-gray-800 py-4 px-16">
    <div className="w-full px-4 h-full"> {/* Replace 'container mx-auto' */}
        <div className="flex justify-between items-center h-full">
          <div className="text-sm">
            © {new Date().getFullYear()} - CS467 Capstone Project - Oregon State University
          </div>
          <div className="flex items-center space-x-4">
            <a 
              href="https://github.com" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="flex items-center hover:text-black dark:hover:text-gray-300 transition-colors"
            >
              <Github className="h-5 w-5 mr-2" />
              GitHub
            </a>
            <a 
              href="mailto:example@example.com" 
              className="flex items-center hover:text-black dark:hover:text-gray-300 transition-colors"
            >
              <Mail className="h-5 w-5 mr-2" />
              Contact
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
