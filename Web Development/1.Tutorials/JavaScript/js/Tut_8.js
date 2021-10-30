// Loops in JavaScript

// for loop in JS
let i;
for (i = 0; i < 3; i++) {
    console.log(i);
}


let friends = ["Suraj", "Abhishek", "Satish", "Piyush"];
for (let index = 0; index < friends.length; index++) {
    console.log("Hello friend, " + friends[index]);
}

// forEach loop in JS
friends.forEach(function f(element) {
    console.log("Hello friend, " + element + " to modern JS");
});

// forof loop in JS
for (element of friends) {
    console.log("Hello friend, " + element + " to modern JS again");
}


let employee = {
    name: "Nikhil",
    salary: 36000,
    role: "Developer"
}

// forin loop in JS
for (key in employee) {
    console.log(`The ${key} of employee is ${employee[key]}`);
}


// while loop in JS
let j = 0;
while (j < 4) {
    console.log(`${j} is less than 4`);
    j++;
}

// do-while loop in JS
let k = 34;
do {
    console.log(`${k} is less than 4 and we are inside do-while loop`);
} while (k < 4);
