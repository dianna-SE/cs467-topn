import React from 'react';
import './App.css';
import axios from 'axios';
import { MusicGenreClassifier } from './components/MusicGenreClassifier';
import Footer from './components/Footer';

// function to make API call to backend
const testRequest = () => {
  axios.get('http://localhost:8080').then((data) => {
    console.log(data)
  })
}

function App() {
  return (
    <div className="App">
      <main>
        <MusicGenreClassifier />
        {/* <button onClick={testRequest}>Click Me!</button> */}
      </main>
      <Footer />

    </div>
  );
}

export default App;