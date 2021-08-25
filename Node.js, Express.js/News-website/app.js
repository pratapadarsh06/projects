const express = require('express')
const bodyParser = require('body-parser')
const ejs = require("ejs")

const app = express()
const port = 5000

//static Files
app.use(express.static('public'))

//templating Engine 
app.set('views', './src/views/partials')
app.set('view engine', 'ejs')

app.use(bodyParser.urlencoded({ extended : true }))

//Routes
const newsRouter = require('./src/routes/news')

app.use('/', newsRouter)
app.use('/article', newsRouter)


//Listen on port 
app.listen(port, () => console.log('listening on port',port))