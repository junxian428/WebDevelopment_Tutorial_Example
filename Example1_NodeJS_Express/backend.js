const express = require('express');
const app = express();
const path = require('path');
const cors = require('cors');
const ejs = require('ejs'); // Add this line

app.use(cors());
app.use(express.static(path.join(__dirname, 'public')));

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Define an API endpoint that returns a message
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello, API!' });
});

// Define a route that renders an EJS template
app.get('/', (req, res) => {
  res.render('index'); // Renders 'views/index.ejs'
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
