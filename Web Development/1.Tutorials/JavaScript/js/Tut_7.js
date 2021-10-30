// Interaction using Alert, Prompt & Confirm

// Alert in in-browser JavaScript
alert("This is a message!");  // does not return anything

// Prompt in JS
let name = prompt("What is your name?", "Guest");
console.log(name);

// Confirm in JS
let deletePost = confirm("Do you really want to delete this post?");
// console.log(deletePost);

if (deletePost) {
    // code to delete the post
    console.log("Your post has been deleted sucessfully");
}
else {
    // code to cancel deletion of the post
    console.log("Your post has not been deleted");
}