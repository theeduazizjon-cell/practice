console.log("Web server starts")

const express = require('express')
const app = express()
const port = 3000

// Traditional API 
app.get('/', (req, res) => {
    console.log("/ get");
    res.send('<h1>Hello World!</h1>');
})

// Rest API 
app.get('/', (req, res) => {
    console.log("/ rest get");
    res.json({ name: "Marco", age: 21, group: "MIT" });
})

app.listen(port, () => {
    console.log(`BackEnd is running on port 3000`);
})