import React from 'react';
import { MusicGenreClassifier } from '../components/MusicGenreClassifier';

const Home = () => (
    <div className="flex items-center justify-center bg-gray-100 dark:bg-gray-900">
    {/* Adjust calc value based on your Navbar height */}
    <MusicGenreClassifier />
  </div>
);

export default Home;
