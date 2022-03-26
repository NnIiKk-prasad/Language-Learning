// Using mongoose in Node.js
const mongoose = require('mongoose');

main().catch(err => console.log(err));

async function main() {
    await mongoose.connect('mongodb://localhost:27017/harryKart');
    console.log("We are connected!");
}

const kittySchema = new mongoose.Schema({
    name: String
});

kittySchema.methods.speak = function speak() {
    const greeting = this.name
        ? "Meow name is " + this.name
        : "I don't have a name";
    console.log(greeting);
};

const Kitten = mongoose.model('Kitten', kittySchema);

const silence = new Kitten({ name: 'Silence' });
// console.log(silence.name);

const fluffy = new Kitten({ name: 'fluffy' });
// fluffy.speak();

fluffy.save(function (err, fluffy) {
    if (err) return console.error(err);
    // fluffy.speak();
});

silence.save(function (err, silence) {
    if (err) return console.error(err);
    // silence.speak();
});

Kitten.find(function (err, kittens) {
    if (err) return console.error(err);
    console.log(kittens);
});

Kitten.find({name: "Silence"}, function (err, kittens) {
    if (err) return console.error(err);
    console.log(kittens);
});
