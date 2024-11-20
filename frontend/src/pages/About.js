import React from 'react';
import { Music } from 'lucide-react';

const About = () => (
  <div className="flex flex-col flex-1 items-center justify-start bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-gray-200 py-16 px-6 sm:px-8 lg:px-16">
    
    {/* Hero Section */}
    <div className="w-full max-w-5xl text-center mb-16">
      <h1 className="text-5xl font-bold mb-6 leading-tight">
        Welcome to <span className="text-blue-600">GenreAI</span>
      </h1>
      <p className="text-lg">
        Empowering artists, producers, and music enthusiasts with the power of AI to classify their music.
      </p>
    </div>

    {/* Our Goal Section */}
    <div className="flex flex-col lg:flex-row items-center lg:items-start w-full max-w-5xl gap-12 mb-16">
      <div className="flex-1">
        <img 
          src="/spotify_genres.jpg" 
          alt="Our Goal" 
          className="rounded-lg shadow-md object-cover w-full h-64 lg:h-80"
        />
      </div>
      <div className="flex-1 text-left">
        <h2 className="text-4xl font-semibold text-gray-800 dark:text-gray-100 mb-4">Our Goal</h2>
        <p className="text-lg text-gray-600 dark:text-gray-300 mb-4">
          We are looking to bridge the gap between technology and music by providing an intuitive tool for genre identification. Whether you're a professional in the industry or a music lover, GenreAI makes it simple to categorize, organize, and understand your music.
        </p>
        <div className="flex items-center space-x-4">
            <Music className="h-10 w-10 text-blue-600" />
            <span className="text-lg font-medium text-gray-700 dark:text-gray-200 ">
            Accuracy, Speed, and Ease of Use.
            </span>
        </div>
      </div>
    </div>

    {/* How It Works Section */}
    <div className="flex flex-col lg:flex-row-reverse items-center lg:items-start w-full max-w-5xl gap-12 mb-16">
      <div className="flex-1">
        <img 
          src="/record_store.jpg" 
          alt="How It Works" 
          className="rounded-lg shadow-md object-cover w-full h-64 lg:h-80"
        />
      </div>
      <div className="flex-1 text-left">
        <h2 className="text-4xl font-semibold text-gray-800 dark:text-gray-100 mb-4">How It Works</h2>
        <p className="text-lg text-gray-600 dark:text-gray-300 mb-4">
        Our system takes audio files and transforms them into Mel spectrograms—visual representations of sound frequencies—using the librosa library. These spectrograms serve as input for a Convolutional Neural Network (CNN) designed to classify music genres. The model is trained on the GTZAN dataset, which includes 10 distinct genres. By converting audio data into structured visual patterns, the system leverages deep learning to accurately identify genre characteristics. It ensures robust training by dynamically filtering out corrupted data and optimizing the model's accuracy through iterative learning, ultimately enabling efficient and reliable genre classification.        </p>
        <div className="flex items-center space-x-4">
            <Music className="h-10 w-10 text-blue-600" />
            <span className="text-lg font-medium text-gray-700 dark:text-gray-200 ">
            Advanced Machine Learning.
            </span>
        </div>
      </div>
    </div>

    {/* Call to Action Section
    <div className="w-full max-w-3xl bg-blue-600 text-white py-12 my-28 px-16 rounded-lg shadow-lg text-center">
      <h2 className="text-4xl font-bold mb-4">Get Started Today</h2>
      <p className="text-lg mb-8">
        Ready to experience the power of AI-driven genre classification? Upload a track and let GenreAI uncover the genre for you.
      </p>
      <button className="bg-white text-blue-600 px-6 py-3 font-semibold rounded-lg shadow-md hover:bg-gray-100 transition-colors">
        Upload Your Track
      </button>
    </div> */}
  </div>
);

export default About;
