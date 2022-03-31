const mongoose = require('mongoose')

const connectDB = (url) => {
  // return mongoose.connect('mongodb://localhost:27017/Store-API')
  return mongoose.connect(url)
}

module.exports = connectDB
