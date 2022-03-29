// Creating a Custom Backend Using NodeJs
const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

const home = fs.readFileSync(`${__dirname}/static/index.html`);
const about = fs.readFileSync(`${__dirname}/static/about.html`);
const services = fs.readFileSync(`${__dirname}/static/services.html`);
const contact = fs.readFileSync(`${__dirname}/static/contact.html`);

const server = http.createServer((req, res) => {
    // console.log(req.url);
    url = req.url;

    if (url == '/') {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.write(home)
        res.end();
    }
    else if (url == '/about.html') {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.write(about)
        res.end();
    }
    else if (url == '/services.html') {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.write(services)
        res.end();
    }
    else if (url == '/contact.html') {
        res.writeHead(200, { 'content-type': 'text/html' })
        res.write(contact)
        res.end();
    }
    else {
        res.writeHead(404, { 'content-type': 'text/html' })
        res.write('<h1>404 not found</h1>')
        res.end();
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});