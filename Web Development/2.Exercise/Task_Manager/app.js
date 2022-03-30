const express = require('express');
const tasks = require('./routes/tasks');
const connectDB = require('./db/connect')
require('dotenv').config();
const notFound = require('./middleware/not-found');
const errorHandlerMiddleware = require('./middleware/error-handler');

const app = express();
const port = process.env.PORT || 3000;

// Express specific middleware
app.use(express.static(`${__dirname}/public`));
app.use(express.json());

// Routes
app.use('/api/v1/tasks', tasks);

// Custom middleware
app.use(notFound);
app.use(errorHandlerMiddleware);

// Starts the SERVER only if connected to MongoDB
const start = async () => {
    try {
        await connectDB(process.env.MONGO_URI);
        app.listen(port, () =>
            console.log(`Server is listening on port ${port}...`)
        );
    } catch (error) {
        console.log(error);
    }
};

start();
