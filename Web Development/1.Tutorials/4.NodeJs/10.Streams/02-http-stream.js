var http = require('http')
var fs = require('fs')

http
  .createServer((req, res) => {
    // const text = fs.readFileSync(`${__dirname}/content/big.txt`, 'utf8')
    // res.end(text)
    const fileStream = fs.createReadStream(`${__dirname}/content/big.txt`, 'utf8')
    fileStream.on('open', () => {
      fileStream.pipe(res)
    })
    fileStream.on('error', (err) => {
      res.end(err)
    })
  })
  .listen(5000)
