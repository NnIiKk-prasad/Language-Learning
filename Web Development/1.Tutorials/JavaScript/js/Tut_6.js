// Functions in JavaScript

function greet(name, greet_Text = "Good Morning!") {
    console.log(greet_Text + " " + name);
    console.log(name + " is a good boy");
}

let names = ["Harry", "Carry", "Larry", "Garry"];
let greetText = "Good Afternoon!";
greet(names[0], greetText);
greet(names[1], greetText);
greet(names[2], greetText);
greet(names[3]);

function sum(a, b, c) {
    let res = a + b + c;
    return res;
}

let returnVal = sum(1, 2, 3);
console.log(returnVal);