// Author: Andrew Gaynor
// Date Accessed: October 10, 2024
// Starter backend application with React and Express
// Adapted from source URL:
//      https://dev.to/techcheck/creating-a-react-node-and-express-app-1ieg

// server/server.js
const express = require('express');
const app = express();
const cors = require('cors');

app.use(cors())

app.get('/', (req, res) => {
    res.send('Hello from the backend server!');
  });

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`Backend server is running on port ${PORT}`);
});