const express = require("express");
const path = require("path");

console.log("start the system");

const port = 8080;
const app = express();

//server static page
app.use(express.static(path.join(__dirname, '/Part3')))
app.use(express.json());
app.use(express.urlencoded({extended: true}));

// go to static page
app.get('/', (req, res) => {
    console.log("ddd")
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, () => console.log('port' + {port}));
module.exports = app;