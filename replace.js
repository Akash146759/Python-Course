// Replace a single occurrence
let text = "Hello world, world is beautiful world!";
let newText = text.replace("world", "JavaScript");

console.log(newText); // Output: "Hello JavaScript, world is beautiful!"

// Using regular expression with global flag to replace all occurrences
let newTextAll = text.replace(/world/g, "JavaScript");

console.log(newTextAll); // Output: "Hello JavaScript, JavaScript is beautiful!"
