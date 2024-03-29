// show dbs
// use harryKart
// show collections

// Inserting data in mongo db
db.item.insertOne({name: "Samsung 30s", price: 22000, rating: 4.5, qty: 233, sold: 98})

db.item.insertMany([{name: "Samsung 30s", price: 22000, rating: 4.5, qty: 233, sold: 98}, 
{name: "Moto 30s", price: 29000, rating: 3.5, qty: 133, sold: 598},
{name: "Realme 30s", price: 129000, rating: 2.5, qty: 633, sold: 98}])

// Searchind data in mongo db
db.item.find()  // returns all objects in collection 'item'
db.item.find({rating: 3.5})  // returns all objects with rating equal to 3.5
db.item.find({rating: {$gte: 3.5}})  // returns all objects with rating greater than or equal to 3.5
db.item.find({rating: {$gt: 3.5}})  // returns all objects with rating greater than 3.5

db.item.find({rating: {$gt: 3.5}, price: {$gt: 4000}})  // AND opration
db.item.find({rating: {$lt: 3.5}, price: {$gt: 100000}})  // AND opration

db.item.find({$or: [{rating: {$gt: 3.5}}, {price: {$gt: 100000}}]})  // OR opration

db.item.find({rating: {$gt: 3.5}}, {rating: 1})  // to show rating only

db.item.find({rating: {$gt: 3.5}}, {rating: 1, qty: 1})  // to show rating and qty only

// Deleting data from mongo db
db.item.deleteOne({price: 22000})

db.item.deleteMany({price: 129000})

// Updating data in mongo db
db.item.updateOne({name: "Moto 30s"}, {$set: {price: 25000}})

db.item.updateMany({name: "Moto 30s"}, {$set: {price: 5000, rating: 1.0}})
