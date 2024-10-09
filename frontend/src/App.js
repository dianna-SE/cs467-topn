// Source: https://dev.to/techcheck/creating-a-react-node-and-express-app-1ieg

import logo from './logo.svg';
import './App.css';
import axios from 'axios';

// function to make API call to backend
const testRequest = () => {
  axios.get('http://localhost:8080').then((data) => {
    console.log(data)
  })
}

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <button onClick={testRequest}>Click Me!</button>

        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
