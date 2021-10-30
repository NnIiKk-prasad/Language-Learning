// Set and clear Timeout & Interval in JavaScript

// setTimeout - Allows us to run the function once after a given interval of time
function greet(name, byeText){
    console.log(`Bye ${name}, ${byeText}.`);
}

let timeOut = setTimeout(greet, 5000, "Nikhil", "take care");
clearTimeout(timeOut);

// setInterval - Allows us to run the function repeatedely at a given interval of time
intervalId = setInterval(greet, 2000, "Nikhil", "take care");
clearInterval(intervalId);

function displayTime(){
    time = new Date();
    console.log(time);
    document.getElementById('time').innerHTML = time;
}

setInterval(displayTime, 1000);