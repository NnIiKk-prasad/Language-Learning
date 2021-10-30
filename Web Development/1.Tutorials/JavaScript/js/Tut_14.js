// Math Object in JavaScript

// Printing the math object
let m = Math;
console.log(m);

// Printing the constants from math object
console.log("The value of Math.E is: " + Math.E);
console.log("The value of Math.PI is: " + Math.PI);
console.log("The value of Math.LN2 is: " + Math.LN2);
console.log("The value of Math.SQRT1_2 is: " + Math.SQRT1_2);
console.log("The value of Math.LOG10E is: " + Math.LOG10E);

// Printing the functions from math object
let a = 23.547, b = 5;
console.log("The value of a and b is:", a, b);
console.log("The value of a and b rounded is:", Math.round(a), Math.round(b));

console.log("3 raised to power 2 is:", Math.pow(3, 2));
console.log("Square root of 36 is:", Math.sqrt(36));

console.log("5.8 rounded up to nearest integer is:", Math.ceil(5.8));
console.log("5.8 rounded down to nearest integer is:", Math.floor(5.8));

console.log("Absolute value of 5.66 is:", Math.abs(5.66));
console.log("Absolute value of -5.66 is:", Math.abs(-5.66));

console.log("The value of sin(PI) is:", Math.sin(Math.PI));
console.log("The value of cos(PI) is:", Math.cos(Math.PI));
console.log("The value of tan(PI) is:", Math.tan(Math.PI));

console.log("Minimum value of 14, 5, 16 is:", Math.min(14, 5, 16));
console.log("Maximum value of 14, 5, 16 is:", Math.max(14, 5, 16));

let r = Math.random();
console.log("Random number between 0 and 1 is:", r);
console.log("Random number between 0 and 100 is:", r * 100);

let x = 1, y = 50;
let r_xy = x + (y - x) * Math.random();
console.log(`Random number between ${x} and ${y} is: ${r_xy}`);