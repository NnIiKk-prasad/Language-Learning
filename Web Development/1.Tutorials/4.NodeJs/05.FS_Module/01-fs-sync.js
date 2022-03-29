// Synchronous or blocking
// - line by line execution 
const { readFileSync, writeFileSync } = require('fs')

console.log('start')
const first = readFileSync(`${__dirname}/content/first.txt`, 'utf8')
const second = readFileSync(`${__dirname}/content/second.txt`, 'utf8')

writeFileSync(
  `${__dirname}/content/result-sync.txt`,
  `Here is the result : ${first}, ${second}\n`,
  { flag: 'a' }
)
console.log('done with this task')

console.log('starting the next one')
