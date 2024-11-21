import React, { useState } from 'react';
import { UploadButton } from './UploadButton';
import { GenrePredictionChart } from './GenrePredictionChart';
import { Dialog } from './Dialog';

export const MusicGenreClassifier = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [predictions, setPredictions] = useState([]);
  const [file, setFile] = useState(null);

  // Function to handle file selection and open modal
  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    setIsModalOpen(true);
    handleFileUpload(selectedFile); // Start file upload
  };

  // Function to handle file upload to backend
  const handleFileUpload = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setPredictions(data.top_genres); // Update predictions from response
      } else {
        console.error("Error:", await response.json());
      }
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div className="h-[85vh] pb-10 bg-gray-100 flex flex-col">
      <div className="flex-grow flex flex-col items-center justify-center px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold mb-2 text-center">Upload a song to</h1>
        <h1 className="text-4xl font-bold mb-8 text-center">discover the genre...</h1>
        <UploadButton onFileChange={handleFileChange} />
      </div>
      <Dialog isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        <h2 className="text-2xl font-bold mb-4">Genre Predictions</h2>
        <GenrePredictionChart predictions={predictions} file = {file}/>
      </Dialog>
    </div>
  );
};
