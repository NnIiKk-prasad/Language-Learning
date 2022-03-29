const express = require('express')
const people = require('./routes/people')
const auth = require('./routes/auth')

const app = express()

// static assets
app.use(express.static(`${__dirname}/public`))
// parse form data
app.use(express.urlencoded({ extended: false }))
// parse json
app.use(express.json())

app.use('/api/people', people)
app.use('/login', auth)

app.listen(5000, () => {
  console.log('Server is listening on port 5000....')
})
