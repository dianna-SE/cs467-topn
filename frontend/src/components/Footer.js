import React from 'react';
import { Github, Mail } from "lucide-react";

const Footer = () => {
  return (
    <footer className="h-[10vh] bg-gray-100 border-t py-4">
      <div className="container mx-auto px-6 h-full">
        <div className="flex justify-between items-center h-full">
          <div className="text-sm text-gray-600">
            © {new Date().getFullYear()} CS467 Capstone Project - Oregon State University
          </div>
          <div className="flex items-center space-x-4">
            <a 
              href="https://github.com" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="flex items-center text-gray-600 hover:text-black transition-colors"
            >
              <Github className="h-5 w-5 mr-2" />
              GitHub
            </a>
            <a 
              href="mailto:example@example.com" 
              className="flex items-center text-gray-600 hover:text-black transition-colors"
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
