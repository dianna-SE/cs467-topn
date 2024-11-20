import React from 'react';
import { Upload } from 'lucide-react';

export const UploadButton = ({ onFileChange }) => (
  <label htmlFor="file-upload" className="cursor-pointer">
    <input
      id="file-upload"
      type="file"
      accept="audio/*"
      className="hidden"
      onChange={onFileChange}
    />
    <div className="flex items-center space-x-2 bg-blue-500 text-white px-6 py-3 rounded-full hover:bg-blue-600 transform transition-all duration-200 ease-out active:scale-95">
      <Upload className="w-5 h-5" />
      <span className="text-lg font-semibold">Upload Audio</span>
    </div>
  </label>
);
