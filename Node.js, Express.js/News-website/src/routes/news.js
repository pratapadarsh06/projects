const express = require('express')
const newsRouter = express.Router()
const axios = require('axios') //axios helps fetching data from blogs

newsRouter.get('', async(req, res)=>{
	
    try {
       const newsAPI = await axios.get('https://raddy.co.uk/wp-json/wp/v2/posts/')      
       //console.log(newsAPI.data)
       res.render('news',{articles: newsAPI.data}) 
    }catch(err){
    	if(err.response){
    		res.render('news',{articles: null})
         console.log(err.response.data)
    		console.log(err.response.status)
    		console.log(err.response.headers)
    	}else if (err.requiest){
         res.render('news',{articles: null})
    		console.log(err.requiest)
    	}else{
         res.render('news',{articles: null})
    		console.error('Error', err.message)
    	}
      
    }

})


newsRouter.get('/:id', async(req, res) => {
    let articleID = req.params.id

    try {
        const newsAPI = await axios.get(`https://raddy.co.uk/wp-json/wp/v2/posts/${articleID}`)
        res.render('newsSingle', { article : newsAPI.data })
    } catch (err) {
        if(err.response) {
            res.render('newsSingle', { article : null })
            console.log(err.response.data)
            console.log(err.response.status)
            console.log(err.response.headers)
        } else if(err.requiest) {
            res.render('newsSingle', { article : null })
            console.log(err.requiest)
        } else {
            res.render('newsSingle', { article : null })
            console.error('Error', err.message)
        }
    } 
})


newsRouter.post('', async(req, res) => {
    let search = req.body.search
    try {
        const newsAPI = await axios.get(`https://raddy.co.uk/wp-json/wp/v2/posts?search=search`)
        res.render('newsSearch', { articles : newsAPI.data })
    } catch (err) {
        if(err.response) {
            res.render('newsSearch', { articles : null })
            console.log(err.response.data)
            console.log(err.response.status)
            console.log(err.response.headers)
        } else if(err.requiest) {
            res.render('newsSearch', { articles : null })
            console.log(err.requiest)
        } else {
            res.render('newsSearch', { articles : null })
            console.error('Error', err.message)
        }
    } 
})


module.exports = newsRouter








//7169ea21ec1043c18ef41d94a166d805