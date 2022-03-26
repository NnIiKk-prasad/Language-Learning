// Date & Time in JavaScript

let now = new Date();
console.log(now);

let dt = new Date(0);
console.log(dt);

let newDate = new Date("2050-04-20");
console.log(newDate);

newDate = new Date(2050, 3, 20, 9, 3, 25, 2);
console.log(newDate);

let year = newDate.getFullYear();
console.log("The year is: " + year);

let month = newDate.getMonth();
console.log("The month is: " + month);

let date = newDate.getDate();
console.log("The date is: " + date);

let hours = newDate.getHours();
console.log("The hours is: " + hours);

newDate.setDate(39);
console.log(newDate);

function displayTime(){
    time = new Date();
    document.getElementById('time').innerHTML = time;
}

setInterval(displayTime, 1000);
