// pages/About.js
import React from 'react';
import Navbar from '../components/Navbar';

const About = () => (
    
  <div className="h-[85vh] bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    {/* <Navbar /> */}
    <div className="max-w-3xl mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
      <div className="px-6 py-8">
        <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">About GenreAI</h1>
        
        <p className="text-gray-700 text-lg mb-6">
          Welcome to GenreAI. Our platform leverages advanced machine learning algorithms to analyze audio files and accurately predict genres, making it easier for artists, producers, and music enthusiasts to categorize and organize their music.
        </p>

        <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">Our Mission</h2>
        <p className="text-gray-700 mb-6">
          At GenreAI, our mission is to bridge the gap between technology and music by providing an intuitive, powerful tool for genre identification. We strive to make music classification accessible, empowering users to gain insights into musical trends, preferences, and influences.
        </p>

        <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">How It Works</h2>
        <p className="text-gray-700 mb-6">
          Using advanced neural networks, GenreAI analyzes the key attributes of each track, such as tempo, rhythm, and tonal quality, to determine its genre. Whether you're classifying a single track or an entire library, our tool offers accuracy, speed, and ease of use.
        </p>
      </div>
      <div className="bg-gray-100 px-6 py-4 text-center">
        <p className="text-gray-600">Ready to get started? Upload a track and discover its genre with GenreAI.</p>
      </div>
    </div>
  </div>
);

export default About;
