// Using raw HTML in Pug template engine
const express = require('express');
const path = require('path');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

main().catch(err => console.log(err));

async function main() {
    await mongoose.connect('mongodb://localhost:27017/carForm');
    console.log("We are connected!");
}

const app = express();
const port = 80;

// Define mongoose schema
const carSchema = new mongoose.Schema({
    fname: String,
    lname: String,
    gender: String,
    cars: String,
    browser: String,
    message: String
});

const Car = mongoose.model('Car', carSchema);

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
    var myData = new Car(req.body);
    myData.save().then(() => {
        res.send("Item Saved Sucessfully!");
    }).catch(() => {
        res.status(400).send("Item was not saved.");
    });
});

// START THE SERVER
app.listen(port, () => {
    console.log(`App started sucessfully at port ${port}`);
});
