// Creating Custom Modules in Node Using NodeJs
console.log("This is module");

function average(arr) {
    let sum = 0;
    arr.forEach(element => {
        sum += element;
    });
    return sum / arr.length;
}

// module.exports = average;
module.exports = {
    avg: average,
    name: "Nikhil",
    repo: "GitHub"
}