// ErrorMessage.js
import React from 'react';
import { AlertOctagon } from 'lucide-react'; // Exclamation icon from lucide-react

const ErrorMessage = ({ message }) => {
  return (
    <div className="flex items-center justify-center h-full text-red-500 animate-shake">
      <AlertOctagon className="w-16 h-16 mr-4 animate-pulse" /> {/* Pulsing icon */}
      <div className="text-2xl font-semibold">{message}</div>
    </div>
  );
};

export default ErrorMessage;
