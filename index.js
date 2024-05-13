require('dotenv').config();
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send("Пиздец");
});

app.get('/dashboard', (req, res) => {
    res.json({
        msg: 'Good',
        status: 200
    });
});

app.listen(PORT, () => {
    console.log("Пупырнул ${PORT}");
});
