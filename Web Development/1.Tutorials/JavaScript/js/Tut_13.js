// Arrow function in JavaScript

// let greet = () => {
//     console.log("Good Morning");
// }
let greet = () => console.log("Good Morning");
greet();

setTimeout(() => {
    console.log("We are inside setTimeout");
}, 3000);

let sum = (a, b) => a + b;
let half = a => a / 2;

let obj1 = {
    greeting: "Good morning!",
    names: ["Suraj", "Satish", "Abhishek", "Piyush"],
    speak() {
        this.names.forEach((student) => {
            console.log(`${this.greeting} Welcome ${student}`);
        });
    }
}
obj1.speak();
