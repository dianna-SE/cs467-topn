import React from 'react';
import { X } from 'lucide-react';

export const Dialog = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  const handleOutsideClick = (e) => {
    if (e.target.id === "dialog-overlay") onClose();
  };

  return (
    <div
      id="dialog-overlay"
      className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center z-20"
      onClick={handleOutsideClick}
    >
      <div
        className="bg-white p-10 rounded-lg w-full max-w-5xl h-[580px] min-w-[600px] flex flex-col relative bg-white dark:bg-gray-900 text-gray-800"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-1 text-gray-600 hover:text-gray-800 hover:bg-gray-200 transition duration-200 rounded-full"
          aria-label="Close"
        >
          <X size={24} />
        </button>

        {/* Content Container */}
        <div className="flex flex-col flex-1 justify-center items-center">
          {children}
        </div>
      </div>
    </div>
  );
};
