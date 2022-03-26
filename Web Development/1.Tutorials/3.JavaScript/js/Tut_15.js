// Working with JSON in JavaScript

let jsonObj = {
    name: "Nikhil",
    salary: 45000,
    role: "Developer"
}
console.log(jsonObj);

let myJsonStr = JSON.stringify(jsonObj);
console.log(myJsonStr);

myJsonStr = myJsonStr.replace('Nikhil', 'Prasad');
console.log(myJsonStr);

let newJsonObj = JSON.parse(myJsonStr);
console.log(newJsonObj);