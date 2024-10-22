const express = require('express')
const app = express()
const port = 3000

const mongoose = require('mongoose')

mongoose.connect('mongodb+srv://sol:password1234@boilerplate.3z7nd.mongodb.net/?retryWrites=true&w=majority&appName=boilerplate'
).then(() => console.log('Mongoose Connect...'))
    .catch(err => console.log(err))

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})