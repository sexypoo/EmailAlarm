//mongoDB connect with mongoose
const mongoose = require('mongoose');
mongoose.connect('mongodb+srv://goeun:goeunrealpassword@cluster0.5xfl6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');
const db = mongoose.connection;

//import crawling module cheerio-httpcli
const client = require("cheerio-httpcli");

//base url in this file
let url = 'https://www.wevity.com/?c=find&s=1&gub=2&cidx=30&gp=2';

let list = []; //database list
let sub_url = []; //each url in this file

//check connection
db.on('error', () => {
  console.log('Failed');
});
db.on('open', () => {
  console.log('Connected');
});

//create Schema
const PostSchema = new mongoose.Schema({
  title: String,
  link: String,
  part: String,
  img : String,
  info : String,
  dday: String,
  host: String,
  reward: String,
  price: String,
  hompage: String,
  local:String
});

const Post = mongoose.model('Test', PostSchema);

//crawling start
client.fetch(url, (err, $, res)=>{

  if(err){ //error
    console.log(err);
    return;
  }

  $('.tit').each(function(post){ //select all doc which have '.tit'

    const nowData = {
      title : $(this).find("a").text(),
      link : url + $(this).find("a").attr('href'),
      part : $(this).find(".sub-tit").text()
    };

    sub_url.push(nowData['link']); //extract each post's link

    list.push(nowData); //save current data

  });

  for(let i = 0; i<sub_url.length; i++){
    client.fetch(sub_url[i],(err,$,res) => {

      if(err){ //error
        console.log(err);
        return
      }

      list[i].img = $('.thumb img').attr('src'); //extract every img
      list[i].info = $('.comm-desc').text(); //extract every infomation
      list[i].dday = $(".dday-area").text();
      list[i].host = $(".cd-info-list li:nth-child(3)").text();
      list[i].reward = $(".cd-info-list li:nth-child(6)").text();
      list[i].price = $(".cd-info-list li:nth-child(7)").text();
      list[i].hompage = $('.cd-info-list li:nth-child(8)').text();
      list[i].local = "기타";

      Post.create(list[i],(error, data)=>{ //create and save data

        if(error) //error
          console.log(error);

        else //succeed!
          console.log('Saved');
      
    })
  })
}
})