// Writing our first Express App
const express = require('express');
const path = require('path');
const app = express();
const port = 80;

// for serving static files
app.use('/static', express.static('static'));

// set the template engine as pug
app.set('view engine', 'pug');

// set the views directory
app.set('views', path.join(__dirname, 'views'));

// our pug demo end point
app.get("/demo", (req, res) => {
    res.status(200).render('demo', { title: 'Hey', message: 'Hello, there!'});
});


app.get("/", (req, res) => {
    res.send("This is home page of my first express app");
});

app.get("/about", (req, res) => {
    res.send("This is about page of my first express app");
});

app.post("/about", (req, res) => {
    res.send("This is post requested about page of my first express app");
});

app.get("/this", (req, res) => {
    res.status(404).send("This page is not found");
});

app.listen(port, () => {
    console.log(`App started sucessfully at port ${port}`);
});
