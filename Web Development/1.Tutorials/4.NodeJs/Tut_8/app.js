// Using raw HTML in Pug template engine
const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();
const port = 80;

// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static'));  // for serving static files
app.use(express.urlencoded());  // middleware

// PUG SPECIFIC STUFF
app.set('view engine', 'pug');  // set the template engine as pug
app.set('views', path.join(__dirname, 'views'));  // set the views directory

// ENDPOINTS
app.get('/', (req, res) => {
    const content = "This is a plane html using Pug.";
    const params = {'title': 'Using plane html in Pug', 'content': content};
    res.status(200).render('index.pug', params);
});

app.post('/', (req, res) => {
    // console.log(req.body);
    let myJsonStr = JSON.stringify(req.body);
    fs.writeFileSync('output.txt', myJsonStr);
    const params = {'message': 'Your form has been submitted sucessfully'};
    res.status(200).render('index.pug', params);
});

// START THE SERVER
app.listen(port, () => {
    console.log(`App started sucessfully at port ${port}`);
});
