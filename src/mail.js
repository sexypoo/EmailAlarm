const nodemailer = require('nodemailer');

const mongoose = require('mongoose');
mongoose.connect('mongodb+srv://goeun:goeunrealpassword@cluster0.5xfl6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority');
const db = mongoose.connection;

db.on('error', () => {
    console.log('Failed');
  });
db.on('open', () => {
    console.log('Connected');
  });

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

 const EmailSchema = new mongoose.Schema({
     email: String
 })

PostSchema.set('collection', 'tests');
EmailSchema.set('collection', 'board');

const Post = mongoose.model('tests', PostSchema);
const Email = mongoose.model('board', EmailSchema);

let new_title = '';
let new_hompage = '';

let email;

Post.findOne({},(err,docs)=>{
    if(err){
        console.log(err);
    }
    console.log(docs.title);
    new_title = docs.title;
    new_hompage = docs.link;
})

Email.findOne({},(err,docs)=>{
    if(err){
        console.log(err)
    }
    console.log(docs.email)
    email = docs.email;
}).then(()=>{
    sendMail(email)
});

function sendMail(toEmail){
    let transporter = nodemailer.createTransport({
        service:'Naver',
        host: 'smtp.naver.com',
        post:587,
        secureConnection: false,
        auth:{
            user:'goeun_goeun_goeun_@naver.com',
            pass:'ro7429_mr_goeun'
        },
        tls: {
            ciphers:'SSLv3'
        }
    });

    let mailOptions = {
        from: 'goeun_goeun_goeun_@naver.com',
        to:toEmail,
        subject:'[틴 돋보기] 새로운 알림이 왔어요!',
        text:`${new_title}의 정보가 왔어요. 구경하러 가보세요. ${new_hompage}`
    };
    
    transporter.sendMail(mailOptions, (err,info)=>{
        if(err){
            console.log(err);
        }
        else{
            console.log("전송 완료: "+info);
            transporter.close();
        }
    
    })
}
