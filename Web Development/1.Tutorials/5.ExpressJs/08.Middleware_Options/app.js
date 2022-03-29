const express = require('express')
const morgan = require('morgan')

const app = express()

// app.use(express.static('./public'))  // built-in middleware
// app.use([logger, authorize])  // custom middleware
app.use(morgan('tiny'))  // external middleware

app.get('/', (req, res) => {
  res.send('Home')
})

app.get('/about', (req, res) => {
  res.send('About')
})

app.get('/api/products', (req, res) => {
  res.send('Products')
})

app.get('/api/items', (req, res) => {
  res.send('Items')
})

app.listen(5000, () => {
  console.log('Server is listening on port 5000....')
})
