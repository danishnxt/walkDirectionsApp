const express = require('express');
const bodyParser = require('body-parser')
const path = require('path')


const app = express();


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/index.html'));
})


app.post('/', (req, res) => {

})

app.listen(3000, () => {
    console.log("Listening on port -> 3000")
})













