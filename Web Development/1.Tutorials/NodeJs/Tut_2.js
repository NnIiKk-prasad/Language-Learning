//  Node.js File System Module
const fs = require('fs');

// Synchronous or blocking
// - line by line execution 
let text = fs.readFileSync('abc.txt', 'utf-8');
text = text.replace('Nikhil Prasad', 'me');

console.log("Content of the file is:\n", text);

fs.writeFileSync('abc.txt', text);

// Asynchronous or non-blocking
// - line by line execution not guaranteed
// - callbacks will fire
fs.readFile('abc.txt', 'utf-8', (err, data) => {
    console.log(data);
});

console.log("This is a message");