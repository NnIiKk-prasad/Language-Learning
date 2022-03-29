// Asynchronous or non-blocking
// - line by line execution not guaranteed
// - callbacks will fire
const { readFile, writeFile } = require('fs')

console.log('start')
readFile(`${__dirname}/content/first.txt`, 'utf8', (err, result) => {
  if (err) {
    console.log(err)
    return
  }
  const first = result
  readFile(`${__dirname}/content/second.txt`, 'utf8', (err, result) => {
    if (err) {
      console.log(err)
      return
    }
    const second = result
    writeFile(
      `${__dirname}/content/result-async.txt`,
      `Here is the result : ${first}, ${second}`,
      (err, result) => {
        if (err) {
          console.log(err)
          return
        }
        console.log('done with this task')
      }
    )
  })
})
console.log('starting next task')
