import React, { useState } from 'react';
import { UploadButton } from './UploadButton';
import { GenrePredictionChart } from './GenrePredictionChart';
import { Dialog } from './Dialog';
import ErrorMessage from './ErrorMessage';

export const MusicGenreClassifier = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);

  // Development URL - Use this when testing locally with npm start
  // const MUSIC_GENRE_CLASSIFICATION_API = "http://127.0.0.1:8000/"; 

  // Production URL - Use this when testing in deployment/production instance
  const MUSIC_GENRE_CLASSIFICATION_API = "https://top-n-music-genre-classification-backend.onrender.com"; 

  // Function to handle file selection and open modal
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file); // Store the file into state variable 
    setErrorMessage(''); // Clear any previous error messages
    setPredictions([]); // Clear previous predictions
    setIsModalOpen(true);
    handleFileUpload(file); // Start file upload
  };

  // Function to handle file upload to backend
  const handleFileUpload = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      // Use for development instance
      // const response = await fetch(`http://127.0.0.1:8000/predict`, {

      // Use for production instance
      const response = await fetch(`${MUSIC_GENRE_CLASSIFICATION_API}/predict`, {
        method: 'POST',
        headers: {
          Accept: 'application/json',
        },
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setPredictions(data.top_genres); // Update predictions from response
      } else {
        const errorData = await response.json();
        setErrorMessage(errorData.error || "There was an issue with the audio file.");
      }
    } catch (error) {
      setErrorMessage("Failed to upload the file. Please try again.");
      console.error("Error uploading file:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200 text-center py-12 px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col items-center justify-center flex-1 px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold mb-2 text-center">Upload a song to</h1>
        <h1 className="text-4xl font-bold mb-8 text-center">discover the genre...</h1>
        <UploadButton onFileChange={handleFileChange} />
        <h3 className="mt-5 text-center text-gray-800 dark:text-gray-400">*File must be in .wav or .mp3 format</h3>

        {/* Conditionally render "View Last Result" button if predictions are available */}
        {predictions.length > 0 && !isModalOpen && (
          <button
            onClick={() => setIsModalOpen(true)}
            className="mt-4 text-blue-500 dark:text-blue-300 hover:text-blue-700 dark:hover:text-blue-400"
          >
            View Last Result
          </button>
        )}
      </div>
      
      <Dialog isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        {loading ? (
          <div className="flex items-center justify-center h-full">
            <div className="loader animate-spin w-12 h-12 border-4 border-t-blue-500 border-gray-200 rounded-full"></div>
          </div>
        ) : errorMessage ? (
          <ErrorMessage message={errorMessage} />
        ) : predictions.length > 0 ? (
          <>
            {/* Display file name using state variable and property */}
            <h2 className="text-2xl dark:text-gray-200 font-bold mb-6">Genre Match Results: <p class="font-normal">{selectedFile.name.slice(0,-4)}</p></h2>
            <GenrePredictionChart predictions={predictions}/>
          </>
        ) : null}
      </Dialog>
    </div>
  );
};
