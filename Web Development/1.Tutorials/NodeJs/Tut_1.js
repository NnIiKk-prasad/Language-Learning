// Node.js HTTP Module 
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    // res.end('Hello, World!');
    res.end(`<!DOCTYPE html>
    <html>
    <head>
        <title>Quotations</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    </head>
    <body>
        <p><cite>Here is a quote from <abbr title="World Wild Life">WWF's</abbr> website:</cite></p>
        <p>WWF' goal is to: <q>Build a future whre people live in harmony with nature.</q></p>
        <blockquote cite="http://www.worldwildlife.org/who/index.html">
            For 50 years, WWF has been protecting the future of nature. The world's leading conservation organization, 
            WWF works in 100 countries and is supported by 1.2 million members in the United States and close to 5 
            million globally.
        </blockquote>
        <address>
            Written by John Doe.<br>
            Visit us at:<br>
            Example.com<br>
            Box 564, Disneyland<br>
            USA
        </address>
        <bdo dir="rtl">Nikhil Prasad</bdo>
    </body>
    </html>
    `);
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
