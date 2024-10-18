import React, { useState } from 'react';
import { Navbar } from './Navbar';
import { UploadButton } from './UploadButton';
import { GenrePredictionChart } from './GenrePredictionChart';
import axios from 'axios';

const genrePredictions = [
  { genre: "Rock", confidence: 0.8 },
  { genre: "Pop", confidence: 0.6 },
  { genre: "Hip Hop", confidence: 0.4 },
  { genre: "Electronic", confidence: 0.3 },
  { genre: "Jazz", confidence: 0.2 },
];

const Dialog = ({ isOpen, onClose, children }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-6 rounded-lg max-w-4xl w-full">
        {children}
        <button 
          onClick={onClose}
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Close
        </button>
      </div>
    </div>
  );
};


export const MusicGenreClassifier = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setIsModalOpen(true);
  };

  return (
    <div className="h-[90vh] pb-10 bg-gray-100 flex flex-col">
      <Navbar />
      <div className="flex-grow flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold mb-2 text-center">Upload a song to</h1>
        <h1 className="text-4xl font-bold mb-8 text-center">discover the genre...</h1>
        <UploadButton onFileChange={handleFileChange} />
      </div>
      <Dialog isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        <h2 className="text-2xl font-bold mb-4">Genre Predictions</h2>
        <GenrePredictionChart predictions={genrePredictions} />
      </Dialog>
    </div>
  );
};